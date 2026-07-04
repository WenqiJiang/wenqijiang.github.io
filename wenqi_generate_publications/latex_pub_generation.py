import argparse
import re

import yaml

# load "publications.yaml"
with open('publications.yaml', 'r') as f:
	all_pubs = yaml.load(f, Loader=yaml.FullLoader)
tag_order = ['conference', 'journal', 'workshop', 'tutorial', 'preprint']


def tag_to_header(tag):
	tail = '\n' + '\\begin{enumerate}[label={[\\arabic*]}]'
	if tag == 'preprint':
		return '\\begin{rSection}{Preprint}' + tail
	elif tag == 'conference':
		return '\\begin{rSection}{Conference Papers}' + tail
	elif tag == 'journal':
		return '\\begin{rSection}{Journal Papers}' + tail
	elif tag == 'workshop':
		return '\\begin{rSection}{Workshop Papers}' + tail
	elif tag == 'tutorial':
		return '\\begin{rSection}{Tutorials}' + '\n' + tail
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
	for tag in tag_order:
		if len(classified_pubs[tag]) == 0:
			del classified_pubs[tag]
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
	An example used in resume:
	\item 
	\begin{Pub}{Co-design Hardware and Algorithm for Vector Search} {\\textbf{Wenqi Jiang}, Shigang Li, Yu Zhu, Johannes de Fine Licht, Zhenhao He, Runbin Shi, Cedric Renggli, Shuai Zhang, Theodoros Rekatsinas, Torsten Hoefler, and Gustavo Alonso} {The International Conference for High Performance Computing, Networking, Storage and Analysis \\textbf{(SC 2023)}, Denver, USA, Nov 12–17, 2023}
	\end{Pub}
	"""

	pub_str = '\n\n'
	pub_str += '\\item\n'
	title = pub['title']
	if 'paper' in pub:
		title = '\\href{' + pub['paper'] + '}{' + title + '}'
	pub_str += '\\begin{Pub}{' + title + '}' + '\n'
	pub_str += '{' + pub['authors'].replace('Wenqi Jiang', '\\textbf{Wenqi Jiang}') + '}' + '\n'
	if 'venue' in pub:
		pub_str += '{' + pub['venue'] 
		if 'short_venue' in pub:
			pub_str += ' '
			if 'black_short_venue' in pub and pub['black_short_venue']:
				pub_str += '(\\textbf{' + pub['short_venue'] + '})}'
			else:
				pub_str += '(' + pub['short_venue'] + ')}'
		else:
			pub_str += ', ' + str(pub['year']) + ' }'
	else:
		# pub_str += '{' + str(pub['year']) + ' }'
		pub_str += '{}'
	pub_str += '\n' + '\end{Pub}'

	# optional award
	if 'award' in pub:
		pub_str += '\n\\vspace{-.5em}\n\\raisebox{-0.2em}{\\includegraphics[height=1.2em]{figures/trophy.png}}~{\\color{red}\\textbf{' + pub['award'] + '}}'

	return pub_str

def parse_args():
	parser = argparse.ArgumentParser(description='Generate publication LaTeX.')
	parser.add_argument('--mode', choices=['split', 'mixed'], default='split',
		help='split groups publications by type; mixed emits one chronological list')
	parser.add_argument('--output', default=None,
		help='output file path; defaults to publications.tex for split and publications_mixed.tex for mixed')
	parser.add_argument('--verbose', action='store_true',
		help='print parsed publication data')
	return parser.parse_args()

if __name__ == '__main__':
	args = parse_args()
	if args.verbose:
		print(all_pubs)

	out_str = ''

	if args.mode == 'split':
		classified_pubs = classify_publications(all_pubs)
		for tag in tag_order:
			if tag in classified_pubs:
				out_str += '\n\n' + tag_to_header(tag)
				for pub in classified_pubs[tag]:
					out_str += get_pub_str(pub)
				out_str += '\end{enumerate}' + '\n' + '\end{rSection}' + '\n\n'
	else:
		out_str += '\n\n\\begin{rSection}{Publications}'
		out_str += '\n\\begin{enumerate}[label={[\\arabic*]}]'
		for pub in get_publications_by_time(all_pubs):
			out_str += get_pub_str(pub)
		out_str += '\end{enumerate}' + '\n' + '\end{rSection}' + '\n\n'

	output = args.output
	if output is None:
		output = 'publications.tex' if args.mode == 'split' else 'publications_mixed.tex'

	with open(output, 'w') as f:
		f.write(out_str)

	print("Wrote %s" % output)
