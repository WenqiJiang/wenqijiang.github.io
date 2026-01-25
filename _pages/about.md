---
permalink: /
title: ""
excerpt: "Home"
author_profile: true
redirect_from: 
  - /home/
  - /home.html
  - /about/
  - /about.html
---

<!-- Hi! My name is Wenqi Jiang.  -->

I am an incoming Assistant Professor at the National University of Singapore, starting from Fall 2026. 
I recently received my PhD at [ETH Zurich](https://ethz.ch/), where I was fortunate to be advised by [Gustavo Alonso](https://people.inf.ethz.ch/alonso/) and [Torsten Hoefler](https://htor.inf.ethz.ch/). 
Before joining the [Systems Group @ ETHz](https://systems.ethz.ch/), I earned my Master's degree from Columbia University and my Bachelor's degree from Huazhong University of Science and Technology, both with honors. My work has been recognized with a VLDB Best Paper Award (as the first-author), the ML and Systems Rising Star Award, and the AMD HACC Outstanding Researcher Award.

<!-- TODO: add links to those awards -->
<!-- https://mlcommons.org/2024/06/2024-mlc-rising-stars/ -->
<!-- https://www.amd-haccs.io/awards.html -->


<!-- My research centers around developing efficient <b>vector data systems on modern hardware</b>, an essential topic in today's <b>systems for machine learning</b>. -->

I work on **systems for machine learning**, with research spanning the boundaries of data management, computer systems, and computer architecture. Rather than focusing on a single layer of the stack, I work across algorithms, systems, and hardware, because the increasing complexity of future machine learning (ML) systems necessitates cross-stack efforts. My research has pioneered several important topics in machine learning systems, including retrieval-augmented generation (RAG), vector search, and recommender systems.

*Fun fact*: one of my hobbies is to publishing broadly across various systems-related venues. So far, I have published first-author papers in databases (SIGMOD, VLDB), high-performance computing (SC), computer architecture (ISCA), ML systems (MLSys), and data mining (KDD). OSDI/SOSP is one box I didn't check during my PhD, but it is very much on my agenda as a faculty member! Pro tip: I wouldn't recommend doing this as a new PhD student though, as you will have a hard time to find and settle into a research community.


<!-- However, as Moore's Law fades, we can no longer rely on automatic performance gains from technology scaling.  -->
<!-- Consequently,  -->


<!-- In an era when Moore's Law no longer exists, improving data system efficiency often relies the development of cross-stack solutions that integrate algorithms, software systems, and underlying hardware.
<!-- Recently, I have built Post-Moore data systems for vector search, recommender systems, and spatial data processing. -->
<!-- Recently, I have built post-Moore data systems for large language models, vector databases, recommender systems, and spatial data processing. -->


<!-- [![CV](/Users/wenqi/home/wenqi.github.io/images/cv-icon.png)](https://wenqijiang.github.io/files/2024.7.6_Wenqi_Jiang_CV.pdf) [![Google Scholar](https://wenqijiang.github.io/images/wenqi.png)](https://scholar.google.com/citations?user=0gT0jzkAAAAJ&hl=en&oi=ao) -->


<!-- [<img src="https://wenqijiang.github.io/images/cv-icon.png" alt="CV" style="width: 30px; height: 30px;">](https://wenqijiang.github.io/files/2024.7.6_Wenqi_Jiang_CV.pdf) -->
<!-- [<img src="https://wenqijiang.github.io/images/google-scholar-icon.png" alt="Google Scholar" style="width: 30px; height: 30px;">](https://scholar.google.com/citations?user=0gT0jzkAAAAJ&hl=en&oi=ao) -->

<a href="https://wenqijiang.github.io/files/2025.8.30_Wenqi_Jiang_CV.pdf" title="Download CV" style="margin-right: 10px;">
    <img src="https://wenqijiang.github.io/images/cv-icon.png" alt="CV Icon" style="vertical-align: middle; width: 25px; height: 25px;">
    CV
</a>
<a href="https://scholar.google.com/citations?user=0gT0jzkAAAAJ&hl=en&oi=ao" title="scholar link">
    <img src="https://wenqijiang.github.io/images/google-scholar-icon.png" alt="scholar Icon" style="vertical-align: middle; width: 25px; height: 25px;">
    Scholar
</a>


<p style="color: red; font-weight: bold;">
    I will join NUS as an assistant professor in Fall 2026, and I am looking for multiple PhD students to join our lab. Please check out the <a href="https://wenqijiang.github.io/recruiting" style="color: red; text-decoration: underline;">recruiting page</a> for more info.
</p>

<!-- Postdoc and intern positions may be available to outstanding candidates. -->


<!-- Feel free to check out my [CV](https://wenqijiang.github.io/files/2023.6.17_Wenqi_Jiang_CV.pdf) to know more about me. -->

<!-- 

======
Like many other Jekyll-based GitHub Pages templates, academicpages makes you separate the website's content from its form. The content & metadata of your website are in structured markdown files, while various other files constitute the theme, specifying how to transform that content & metadata into HTML pages. You keep these various markdown (.md), YAML (.yml), HTML, and CSS files in a public GitHub repository. Each time you commit and push an update to the repository, the [GitHub pages](https://pages.github.com/) service creates static HTML pages based on these files, which are hosted on GitHub's servers free of charge.

Many of the features of dynamic content management systems (like Wordpress) can be achieved in this fashion, using a fraction of the computational resources and with far less vulnerability to hacking and DDoSing. You can also modify the theme to your heart's content without touching the content of your site. If you get to a point where you've broken something in Jekyll/HTML/CSS beyond repair, your markdown files describing your talks, publications, etc. are safe. You can rollback the changes or even delete the repository and start over -- just be sure to save the markdown files! Finally, you can also write scripts that process the structured data on the site, such as [this one](https://github.com/academicpages/academicpages.github.io/blob/master/talkmap.ipynb) that analyzes metadata in pages about talks to display [a map of every location you've given a talk](https://academicpages.github.io/talkmap.html).

Getting started
======
1. Register a GitHub account if you don't have one and confirm your e-mail (required!)
1. Fork [this repository](https://github.com/academicpages/academicpages.github.io) by clicking the "fork" button in the top right. 
1. Go to the repository's settings (rightmost item in the tabs that start with "Code", should be below "Unwatch"). Rename the repository "[your GitHub username].github.io", which will also be your website's URL.
1. Set site-wide configuration and create content & metadata (see below -- also see [this set of diffs](http://archive.is/3TPas) showing what files were changed to set up [an example site](https://getorg-testacct.github.io) for a user with the username "getorg-testacct")
1. Upload any files (like PDFs, .zip files, etc.) to the files/ directory. They will appear at https://[your GitHub username].github.io/files/example.pdf.  
1. Check status by going to the repository settings, in the "GitHub pages" section

Site-wide configuration
------
The main configuration file for the site is in the base directory in [_config.yml](https://github.com/academicpages/academicpages.github.io/blob/master/_config.yml), which defines the content in the sidebars and other site-wide features. You will need to replace the default variables with ones about yourself and your site's github repository. The configuration file for the top menu is in [_data/navigation.yml](https://github.com/academicpages/academicpages.github.io/blob/master/_data/navigation.yml). For example, if you don't have a portfolio or blog posts, you can remove those items from that navigation.yml file to remove them from the header. 

Create content & metadata
------
For site content, there is one markdown file for each type of content, which are stored in directories like _publications, _talks, _posts, _teaching, or _pages. For example, each talk is a markdown file in the [_talks directory](https://github.com/academicpages/academicpages.github.io/tree/master/_talks). At the top of each markdown file is structured data in YAML about the talk, which the theme will parse to do lots of cool stuff. The same structured data about a talk is used to generate the list of talks on the [Talks page](https://academicpages.github.io/talks), each [individual page](https://academicpages.github.io/talks/2012-03-01-talk-1) for specific talks, the talks section for the [CV page](https://academicpages.github.io/cv), and the [map of places you've given a talk](https://academicpages.github.io/talkmap.html) (if you run this [python file](https://github.com/academicpages/academicpages.github.io/blob/master/talkmap.py) or [Jupyter notebook](https://github.com/academicpages/academicpages.github.io/blob/master/talkmap.ipynb), which creates the HTML for the map based on the contents of the _talks directory).

**Markdown generator**

I have also created [a set of Jupyter notebooks](https://github.com/academicpages/academicpages.github.io/tree/master/markdown_generator
) that converts a CSV containing structured data about talks or presentations into individual markdown files that will be properly formatted for the academicpages template. The sample CSVs in that directory are the ones I used to create my own personal website at stuartgeiger.com. My usual workflow is that I keep a spreadsheet of my publications and talks, then run the code in these notebooks to generate the markdown files, then commit and push them to the GitHub repository.

How to edit your site's GitHub repository
------
Many people use a git client to create files on their local computer and then push them to GitHub's servers. If you are not familiar with git, you can directly edit these configuration and markdown files directly in the github.com interface. Navigate to a file (like [this one](https://github.com/academicpages/academicpages.github.io/blob/master/_talks/2012-03-01-talk-1.md) and click the pencil icon in the top right of the content preview (to the right of the "Raw | Blame | History" buttons). You can delete a file by clicking the trashcan icon to the right of the pencil icon. You can also create new files or upload files by navigating to a directory and clicking the "Create new file" or "Upload files" buttons. 

Example: editing a markdown file for a talk
![Editing a markdown file for a talk](/images/editing-talk.png)

For more info
------
More info about configuring academicpages can be found in [the guide](https://academicpages.github.io/markdown/). The [guides for the Minimal Mistakes theme](https://mmistakes.github.io/minimal-mistakes/docs/configuration/) (which this theme was forked from) might also be helpful.
 -->
