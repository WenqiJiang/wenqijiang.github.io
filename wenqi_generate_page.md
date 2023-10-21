# TODO

* Modify the Talk format
  * in a similar manner to my CV
* Transfer it to my own site?
* Add contact email to side bar
  * seems in _includes/author-profile.html

# Install Environment

Refer to: https://github.com/academicpages/academicpages.github.io

```
brew update-reset
brew install ruby-build

gem install bundler
gem install jekyll
# install nodejs: https://nodejs.org/en/download
```



use rbenv to create env: https://antran.app/2021/m1_mac_part2/ 

User the command from here that could actually install ruby on M1/M2 (although sad x86 in the command): https://github.com/rbenv/ruby-build/discussions/2125 

```
CFLAGS="-Wno-error=implicit-function-declaration" RUBY_CONFIGURE_OPTS='--with-readline-dir=/usr/local/opt/readline/' arch -x86_64 rbenv install 2.7.6
rbenv global 2.7.6
```

in bash.rc:

```
export PATH="$HOME/.rbenv/bin:$PATH"                                            eval "$(rbenv init -)"  
```

check version:

```
ruby -v
```

(Don't use) I tried to use docker for all these build, used rvm but it seems I cannot install that on MacOS

```sh
# install rvm: https://rvm.io/rvm/install

# install ruby
rvm install ruby-2.7.5

# How to use it: https://stackoverflow.com/questions/53270401/why-is-my-jekyll-command-not-working-anymore
rvm --default use ruby-2.7.5
```



# ETH Webpage

ETH CS系的挂载主页：

https://www.isg.inf.ethz.ch/Main/ServicesWeb



在compile了本地文件以后（见intro - generate HTML），

```
./compress_cp.sh
# which did the following
# tar czvf _site.tar.gz _site/
# scp _site.tar.gz wejiang@web-login.inf.ethz.ch:~/
```

For github page to update, push the changes, and wait a few minutes for github to update your page on github.io

在eth server上解压，

ssh wejiang@web-login.inf.ethz.ch

```
./cp_website.sh
# which did the following
# tar xzvf _site.tar.gz 
# rm -r public_html/*
# mv _site/* public_html/
```



For the eth host, I redirect to github.io by adding this line in index.html

```
<meta http-equiv="refresh" content="0; URL=https://wenqijiang.github.io/" />
```





# Intro

### Generate HTML

Follow the instructions on https://github.com/academicpages/academicpages.github.io

Run bundle clean to clean up the directory (no need to run --force)

Run bundle install to install ruby dependencies. If you get errors, delete Gemfile.lock and try again.

Run bundle exec jekyll liveserve to generate the HTML and serve it from localhost:4000 the local server will automatically rebuild and refresh the pages on change.

```bash
# everytime generate HTML
bundle clean --force
# rm _site/*html
# rm -r _site/talkmap _site/redirects.json _site/feed.xml _site/sitemap.xml _site/robots.txt _site/files _site/images _site/markdown_generator _site/talkmap 
# rm -r .DS_Store

# jekyll will automatically apply changes when you change .md files
bundle exec jekyll liveserve

# localhost:4000 in browser
```



## Latest way to update publication page

```
cd wenqi_generate_publications
### Update publications.yaml ###
python generate_publications.py 
cp publications.md ../_pages/
```



### Apply Changes from Orignal Template to your own

http://archive.is/3TPas



### Markdown style in this repo

_pages/markdown.md



The configuration file for the top menu is in [_data/navigation.yml](https://github.com/academicpages/academicpages.github.io/blob/master/_data/navigation.yml).



### Top Bar

_data/navigation.yml



### Manual of this Repo

https://mmistakes.github.io/minimal-mistakes/docs/configuration/



### Add images

**must commit and push, before localhost can recognize it**: they search from the git repo instead of local machine.

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



### Add new pages to navigation bar

in _data/navigation.yaml, add the new page you want, e.g., contact

```yml
  - title: "Contact"
    url: /contact/
```

in _pages, creat a file named contact.md

```
---
title: ""
permalink: /contact/
author_profile: true
---

## Address

STF G222<br>
Stampfenbachstrasse 114<br>
8092 Zurich<br>
Switzerland<br>

## Email

wenqi [dot] jiang [at] inf.ethz.ch

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

## _config.yaml

website, photos, links, website organizations, etc.

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



### _data

navigation.yaml decides what bars appear on top of the website, e.g., talks, cv

# Deploy on Amazon S3

Change the config.yml, so that the redirect base address is wenqij.com

```
#url                      : https://wenqijiang.github.io 
url                      : https://wenqij.com
```

In S3 console, https://s3.console.aws.amazon.com/s3/home?region=us-east-2#

select wenqij.com

delete all existed file.

in this folder, generate HTML first

```
# everytime generate HTML
bundle clean

# jekyll will automatically apply changes when you change .md files
bundle exec jekyll liveserve
```

Then shut down this process, to provide read permission to S3

drag all the files in _site/ to upload panel in S3

** Problem using S3 **

After doing this, the index page is not response (neither localhost:4000 nor wenqij.com)