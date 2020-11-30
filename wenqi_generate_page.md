# TODO

* Add contact email to side bar
  * seems in _includes/author-profile.html
* Update Talks
* Update CV  
  * add PDF file in CV sub-page, and about-me
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



