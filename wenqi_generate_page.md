# TODO

* Add contact email to side bar
  * seems in _includes/author-profile.html
* Update Talks
* Update CV  
  * in the CV page, remove the "CV" title
* Conference Format 
  * **WSDM 2021** [core A*]. *The 14th ACM International Conference on Web Search and Data Mining*.
  * https://shuaizhang.tech/publications/

# Intro

### Generate HTML

Follow the instructions on https://github.com/academicpages/academicpages.github.io

Run bundle clean to clean up the directory (no need to run --force)

Run bundle install to install ruby dependencies. If you get errors, delete Gemfile.lock and try again.

Run bundle exec jekyll liveserve to generate the HTML and serve it from localhost:4000 the local server will automatically rebuild and refresh the pages on change.

```bash
# everytime generate HTML
bundle clean

# jekyll will automatically apply changes when you change .md files
bundle exec jekyll liveserve

# localhost:4000 in browser
```



### Apply Changes from Orignal Template to your own

http://archive.is/3TPas



### Markdown style in this repo

_pages/markdown.md



### Top Bar

_data/navigation.yml



### Manual of this Repo

https://mmistakes.github.io/minimal-mistakes/docs/configuration/



### Add images

must commit and push, before localhost can recognize it: they search from the git repo instead of local machine.

https://github.com/academicpages/academicpages.github.io/issues/91



### Empty Entry for Yaml

For example, in _publications/2020-3-21-Dynamic-Sampling-and-Selective-Masking-for-Communication-Efficient-Federated-Learning.md , maybe there's some field I do not want to fill, but the entry still need to be there.

In this case, use "~" or null as dummy info in that entry.

https://stackoverflow.com/questions/34089496/empty-field-in-yaml

```
title: "Dynamic Sampling and Selective Masking for Communication-Efficient Federated Learning"
collection: publications
permalink: /publication/2020-3-21-Dynamic-Sampling-and-Selective-Masking-for-Communication-Efficient-Federated-Learning
excerpt: ~
date: 2020-3-21
venue: 'arXiv preprint'
paperurl: ~ 
citation:  ~ 
```

### Adding author to publications

#### My changes to the YML entries

For publications, I have three fields, author before me, myself, and after me. I applied **bold** text for my own name while keeping others normal, by changing "_includes/archive-single.html" and "_layouts/single.html".



```
authors_before_me: ~
author_me: "Wenqi Jiang"
authors_after_me: ", Zhenhao He, Shuai Zhang, Thomas B. Preußer, Kai Zeng, Liang Feng, Jiansong Zhang, Tongxuan Liu, Yong Li, Jingren Zhou, Ce Zhang, Gustavo Alonso"
```



#### _includes/archive-single.html


This file is used as template for overall publication list.

I added one line to it.

```html
<p> <i>{{ post.authors_before_me }}</i> <i><b>{{ post.author_me }}</b></i> <i>{{ post.authors_after_me }}</i> </p>
```



#### _layouts/single.html

This file is used as template after people click one of your publications.

I added one line to it.

```html
<p> <i>{{ page.authors_before_me }}</i> <i><b>{{ page.author_me }}</b></i> <i>{{ page.authors_after_me }}</i> </p>
```



#### Shuai's Solution: Editing publications.md

_pages/publications.md

```
---
title: "Selected Publications"
permalink: /publications/
author_profile: true
---
[(Google Scholar Profile)](https://scholar.google.com.au/citations?user=PPjdxlcAAAAJ&hl=en) [(Full List at DBLP)](https://dblp.uni-trier.de/pers/hd/z/Zhang_0007:Shuai)

## Work in Progress
<b>[xFraud: Explainable Fraud Transaction Detection on Heterogeneous Graphs](https://arxiv.org/pdf/2011.12193.pdf)</b><br>
Co-author, under review.<br>

<b>[MicroRec: Accelerating Deep Recommendation Systems to Microseconds by Hardware and Data Structure Solutions](https://arxiv.org/abs/2010.05894)</b><br>
Co-author, under review.<br>
 
<b>[DeGNN: Characterizing and Improving Graph Neural Networks with Graph Decomposition]()</b><br>
Co-author, under review.<br>

<b>[R2D2: Reuse & Reduce via Dynamic Weight Diffusion for Training Efficient NLP Models]()</b><br>
Co-author, under review.<br>

## Book Chapters

<b>[Deep Neural Networks based Recommender Systems](), 2020, to appear</b><br>
<b>Shuai Zhang</b>, Yi Tay, Lina Yao, Aixin Sun, Ce Zhang. <br>
<i>Book Title: [the 3rd edition of the recommender systems handbook](https://link.springer.com/book/10.1007/978-0-387-85820-3). </i> <br>
<i>Book Authors: Francesco Ricci, Lior Rokach, Bracha Shapira, Paul B. Kantor. </i> <br>
<i> Publisher: Springer. </i>

<b>[Recommender Systems](https://d2l.ai/chapter_recommender-systems/index.html), 2019</b><br>
<b>Shuai Zhang</b>, Aston Zhang, Yi Tay. <br>
<i>Book Title: [Dive into Deep Learning](https://d2l.ai/). </i> <br>
<i>Book Authors: Aston Zhang, Zack C. Lipton, Mu Li, Alex J. Smola. </i>


<b>[Deep Neural Networks meet Recommender Systems](https://digital-library.theiet.org/content/books/10.1049/pbpc035g_ch2), 2019</b><br>
<b>Shuai Zhang</b>, Lina Yao, Aixin Sun, Guibing Guo, Xiwei Xu, Liming Zhu. <br>
<i>Book Title: Big Data Recommender Systems: Recent Trends and Advances. </i> <br>
<i>Book Editors: Osman Khalid, Samee U. Khan,  Albert Y. Zomaya . </i> <br>
<i> Publisher: Institution of Engineering and Technology. </i>

## Conference Papers
<b>[Learning User Representations with Hypercuboids for Recommender Systems](https://arxiv.org/abs/2011.05742)</b><br>
<b>Shuai Zhang</b>, Huoyu Liu, Aston Zhang, Yue Hu, Ce Zhang, Yumeng Li, Tanchao Zhu, Shaojian He and Wenwu Ou. <br>
<b>WSDM 2021</b> [core A*]. <i>The 14th ACM International Conference on Web Search and Data Mining</i>. <br>
```



# File Structure

## _pages

**Most .md files are stored here. **

For example, "about.md", "cv.md"

**Some templates of HTML.**

For example, talk.html, teaching.html, give the title of that page.

```
---
layout: archive
title: "Talks and presentations"
permalink: /talks/
author_profile: true
---

{% if site.talkmap_link == true %}

<p style="text-decoration:underline;"><a href="/talkmap.html">See a map of all the places I've given a talk!</a></p>

{% endif %}

{% for post in site.talks reversed %}
  {% include archive-single-talk.html %}
{% endfor %}
```



## _site

Generated HTML files by jekyll.