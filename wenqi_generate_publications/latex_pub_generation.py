

import yaml

# load "publications.yaml"
with open('publications.yaml', 'r') as f:
	all_pubs = yaml.load(f, Loader=yaml.FullLoader)
tag_order = ['submission', 'conference', 'journal', 'workshop', 'tutorial']

print(all_pubs)


def tag_to_header(tag):
	tail = '\n' + '\\begin{enumerate}[label={[\\arabic*]}]'
	if tag == 'submission':
		return '\\begin{rSection}{Under Submission}' + tail
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

def get_pub_str(pub):
	"""
	An example used in resume:
	\item 
	\begin{Pub}{Co-design Hardware and Algorithm for Vector Search} {\\textbf{Wenqi Jiang}, Shigang Li, Yu Zhu, Johannes de Fine Licht, Zhenhao He, Runbin Shi, Cedric Renggli, Shuai Zhang, Theodoros Rekatsinas, Torsten Hoefler, and Gustavo Alonso} {The International Conference for High Performance Computing, Networking, Storage and Analysis \\textbf{(SC 2023)}, Denver, USA, Nov 12–17, 2023}
	\end{Pub}
	"""

	pub_str = '\n\n'
	pub_str += '\item \n'
	pub_str += '\\begin{Pub}{' + pub['title'] + '}' + '\n'
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

	return pub_str

if __name__ == '__main__':

	classified_pubs = classify_publications(all_pubs)

	out_str = ''

	for tag in tag_order:
		if tag in classified_pubs:
			out_str += '\n\n' + tag_to_header(tag)
			for pub in classified_pubs[tag]:
				out_str += get_pub_str(pub)
			out_str += '\end{enumerate}' + '\n' + '\end{rSection}' + '\n\n'

	with open('publications.tex', 'w') as f:
		f.write(out_str)