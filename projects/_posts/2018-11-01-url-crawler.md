---
layout: posts
title:  "URL Crawler"
date:   2018-07-03 10:38:51 +0200
author: "Lucien Baumgartner"
categories: [ projects ]
permalink: /projects/2018/07/03/url-crawler
redirect_to: 'https://htmlpreview.github.io/?https://github.com/lucienbaumgartner/r-helpers/blob/master/readme/text-extraction-url-crawling.html'
---
The following procedure has been developed to provide a stable URL collection method than can be coupled with text extraction and text burning features. The method was used for this research proposal for SocialScienceOne. The main goal of the workflow is to generate a corpus of URLs related to online media content for all Swiss referanda from June, 2017 to March, 2018, including their text body. The starting point for the URL collection is a list of the top Google searches for each initiative prior to the respective ballots. From there, the algorithm accesses all URLs and extracts all potential links to other informational content on the referendum, this is hyperreferences indluded on those pages. To avoid including links to web-ads or other unrelated content we applied a keyword filter to the newly scraped URLs. The new URLs are then matched to the ones from the initial collection. Only the new entries are then accessed in turn, to extract all possible references, and so on, until there is no new reference or a time limit has been reached.
