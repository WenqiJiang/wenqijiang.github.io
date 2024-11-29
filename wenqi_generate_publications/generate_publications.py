import yaml

# load "publications.yaml"
with open('publications.yaml', 'r') as f:
	all_pubs = yaml.load(f, Loader=yaml.FullLoader)
tag_order = ['submission', 'conference', 'journal', 'workshop', 'tutorial']

print(all_pubs)
header = '''---
title: ""
permalink: /publications/
author_profile: true
---
'''

def tag_to_header(tag):
	if tag == 'submission':
		return '## Under Submission'
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

def get_pub_str(pub):
	"""
	Pub: a single entry (dict) containing publicatoin information
	Mandatory: 
   		title, authors, venue, year, tag (submission, conference, journal, workshop, poster, demo, talk, tutorial, book)
	Optional:
		short_venue, black_short_venue, paper, code, talk, addtional
	"""

	color_short_venue = 'green' # green, blue
	color_paper_title = 'black' # blue, black

	pub_str = '\n\n'

	# first line: title
	if 'short_venue' in pub:
		if 'black_short_venue' in pub and pub['black_short_venue']:
			if color_short_venue == 'green':
				pub_str += '<span style="color:#009051"> [<b>' + pub['short_venue'] + '</b>]</span> '
			elif color_short_venue == 'blue':
				pub_str += '<span style="color:#071BA0"> [<b>' + pub['short_venue'] + '</b>]</span> '
			else:
				pub_str += '<span style="color:black"> [<b>' + pub['short_venue'] + '</b>]</span> '
		else:
			# no color
			pub_str += '<span style="color:black"> [' + pub['short_venue'] + ']</span> '
			# with color
			# pub_str += '<span style="color:#009051"> [' + pub['short_venue'] + ']</span> '

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
		pub_str += '<br>\n'

	return pub_str

if __name__ == '__main__':

	classified_pubs = classify_publications(all_pubs)

	out_str = ''
	out_str += header

	for tag in tag_order:
		if len(classified_pubs[tag]) > 0:
			out_str += tag_to_header(tag) + '\n'
			for pub in classified_pubs[tag]:
				out_str += get_pub_str(pub) + '\n\n'
	
	with open('publications.md', 'w') as f:
		f.write(out_str)

	print("Move to _pages/publications.md: cp publications.md ../_pages/")