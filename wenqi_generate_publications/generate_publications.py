import argparse
import re
import yaml

# load "publications.yaml"
with open('publications.yaml', 'r') as f:
	all_pubs = yaml.load(f, Loader=yaml.FullLoader)
tag_order = ['conference', 'journal', 'workshop', 'tutorial', 'preprint']

def get_header(permalink):
	return '''---
title: ""
permalink: %s
author_profile: true
---
''' % permalink

def tag_to_header(tag):
	if tag == 'preprint':
		return '## Preprint'
	elif tag == 'conference':
		return '## Conference Papers'
	elif tag == 'journal':
		return '## Journal Papers'
	elif tag == 'workshop':
		return '## Workshop Papers'
	elif tag == 'tutorial':
		return '## Tutorials'
	else:
		raise ValueError('Unknown tag: %s' % tag)

def classify_publications(all_pubs):
	classified_pubs = {}
	for tag in tag_order:
		classified_pubs[tag] = []
	for key in all_pubs:
		pub = all_pubs[key]
		assert pub['tag'] in tag_order, 'Unknown tag:'
		if pub['tag'] not in classified_pubs:
			classified_pubs[pub['tag']] = []
		classified_pubs[pub['tag']].append(pub)
	return classified_pubs

def publication_time_key(pub):
	"""
	Sort by optional date first, then year. Supported date formats:
	YYYY, YYYY-MM, YYYY-MM-DD, YYYY.MM, and YYYY.MM.DD.
	"""
	raw_date = str(pub.get('date', pub.get('year', '0')))
	parts = [int(part) for part in re.findall(r'\d+', raw_date)]
	parts = (parts + [0, 0, 0])[:3]
	return tuple(parts)

def get_publications_by_time(all_pubs):
	indexed_pubs = list(enumerate(all_pubs.values()))
	indexed_pubs.sort(key=lambda item: (publication_time_key(item[1]), -item[0]), reverse=True)
	return [pub for _, pub in indexed_pubs]

def get_pub_str(pub):
	"""
	Pub: a single entry (dict) containing publicatoin information
	Mandatory: 
   		title, authors, venue, year, tag (preprint, conference, journal, workshop, poster, demo, talk, tutorial, book)
	Optional:
		short_venue, black_short_venue, paper, code, talk, addtional
	"""

	color_short_venue = 'green' # green, blue
	color_paper_title = 'black' # blue, black

	pub_str = '\n\n'

	# first line: title
	show_short_venue_in_title = 'short_venue' in pub and 'black_short_venue' in pub and pub['black_short_venue']
	if show_short_venue_in_title:
		if color_short_venue == 'green':
			pub_str += '<span style="color:#009051"> [<b>' + pub['short_venue'] + '</b>]</span> '
		elif color_short_venue == 'blue':
			pub_str += '<span style="color:#071BA0"> [<b>' + pub['short_venue'] + '</b>]</span> '
		else:
			pub_str += '<span style="color:black"> [<b>' + pub['short_venue'] + '</b>]</span> '

	if color_paper_title == 'blue':
		# blue + bold
		pub_str += '<span style="color:#071BA0"><b>' + pub['title'] + '</b></span> '
	elif color_paper_title == 'black':
		# black, normal font
		pub_str += '<span style="color:black">' + pub['title'] + '</span>'
	else:
		# grey + bold
		pub_str += '<span style="color:#555555"><b>' + pub['title'] + '</b></span> '
	if 'paper' in pub:
		pub_str += ' [[Paper]](%s)' % pub['paper']
	if 'talk' in pub:
		pub_str += ' [[Talk]](%s)' % pub['talk']
	if 'code' in pub:
		pub_str += ' [[Code]](%s)' % pub['code']
	if 'website' in pub:
		pub_str += ' [[Website]](%s)' % pub['website']
	pub_str += '<br>\n'

	# second line: author
	pub_str += '<span style="color:grey">'
	authors = pub['authors']
	# green 
	# authors = authors.replace('Wenqi Jiang', '<span style="color:#005493">Wenqi Jiang</span>')
	# grey
	authors = authors.replace('Wenqi Jiang', '<span style="color:rgb(50,50,50)">Wenqi Jiang</span>')
	authors = authors.replace('Wenqi Jiang', '<b>Wenqi Jiang</b>')
	authors = authors.replace('*', '\*')
	pub_str += authors
	pub_str += '</span><br>\n'

	# third line: optional venue
	if 'venue' in pub:
		# if 'short_venue' in pub:
		# 	if 'black_short_venue' in pub and pub['black_short_venue']:
		# 		pub_str += '<b>' + pub['short_venue'] + '</b>: '
		# 	else:
		# 		pub_str += pub['short_venue'] + ': '
		pub_str += pub['venue']
		if 'short_venue' in pub and not show_short_venue_in_title:
			pub_str += ' (' + pub['short_venue'] + ')'
		pub_str += '<br>\n'

	# optional award line
	if 'award' in pub:
		pub_str += '<span style="color:red">🏆 <b>%s</b></span><br>\n' % pub['award']


	return pub_str

def parse_args():
	parser = argparse.ArgumentParser(description='Generate publication markdown.')
	parser.add_argument('--mode', choices=['split', 'mixed'], default='mixed',
		help='split groups publications by type; mixed emits one chronological list')
	parser.add_argument('--output', default=None,
		help='output file path; defaults to publications.md for mixed and publications_by_type.md for split')
	parser.add_argument('--permalink', default=None,
		help='Jekyll permalink; defaults to /publications/ for mixed and /publications_by_type/ for split')
	parser.add_argument('--verbose', action='store_true',
		help='print parsed publication data')
	return parser.parse_args()

if __name__ == '__main__':
	args = parse_args()
	if args.verbose:
		print(all_pubs)

	out_str = ''
	permalink = args.permalink
	if permalink is None:
		permalink = '/publications/' if args.mode == 'mixed' else '/publications_by_type/'
	out_str += get_header(permalink)

	if args.mode == 'split':
		classified_pubs = classify_publications(all_pubs)
		for tag in tag_order:
			if len(classified_pubs[tag]) > 0:
				out_str += tag_to_header(tag) + '\n'
				for pub in classified_pubs[tag]:
					out_str += get_pub_str(pub) + '\n\n'
	else:
		out_str += '## Publications\n'
		for pub in get_publications_by_time(all_pubs):
			out_str += get_pub_str(pub) + '\n\n'

	output = args.output
	if output is None:
		output = 'publications.md' if args.mode == 'mixed' else 'publications_by_type.md'
	
	with open(output, 'w') as f:
		f.write(out_str)

	print("Wrote %s" % output)
	if args.mode == 'mixed':
		print("Move to _pages/publications.md: cp %s ../_pages/publications.md" % output)
	else:
		print("Move to _pages/publications_by_type.md: cp %s ../_pages/publications_by_type.md" % output)
	print("Serve locally:\nsource ~/.bashrc\ncd ..\nbundle exec jekyll serve")
