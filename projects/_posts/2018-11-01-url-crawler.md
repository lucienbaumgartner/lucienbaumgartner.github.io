---
layout: posts
title:  "Text Similarity for Press Releases of Major Swiss Parties and Interest Organizations"
date:   2018-07-03 10:38:51 +0200
author: "Lucien Baumgartner & Maël Kubli"
categories: [ projects ]
---

This short contribution shall be an example for what one can expect form following articles in this project. The goal of this paper is to visualize the similarity between the five biggest parties within the swiss parliament and six well known and influential organizations. The underlying question to this article is: "Do we see similarities between actors which are commonly known as political close to each other or not?" Each actors’ official press release statements from their homepage were used to build a text corpus containing around 7'400 press releases from 2010 to April 2018. The results are quite interesting as they show some surprising similarities.

### Data

But first let us look at the data. To see how similar parties and organizations are to each other one needs suitable data. This data is publicly available from webpages and social media accounts for most actors of importance to the political live in Switzerland. The only thing that needs to be done is to collect all the data in a database. This is done in this very project. Hence, it is easy to build a data set containing only all the press releases of a specific set of actors already accessible in our database.

In this work we settle for the five biggest parties in the parliament which are the people's party of Switzerland (SVP), the social democratic party of Switzerland (SPS), the FDP the liberals (FDP), the Christian democratic people's party of Switzerland (CVP) and the green party of Switzerland (GPS). Additionally, we select six organizations we believe to be of great importance to the political process in Switzerland. These are the Economie Suisse, the swiss framers union (SBV), the swiss trade union confederation (SGB), the swiss business association (SGV), the swiss bankers association, and Travail Suisse. For our analysis we use all press releases published by them on their official webpage from 2010 to April 2018. This includes 7'421 published press releases, which results in a text corpus of over 1.5 million n-grams after stemming without stop words.

### Analysis

To get similarity values between all different actors there are several different formulas which could be used to obtain his. We settle for the Jaccard similarity coefficient.

The formula for this is

<p style="text-align:center;">`J(A,B) = (|A \cap B|)/(|A \cup B|)`</p>


The index is also known simply as the Jaccard index. The Jaccard coefficient measures nothing else than the similarity between different sample sets.
Unfortunately, if we apply this Jaccard similarity to all actors on the whole set of texts we get results which are not very useful. The issue here is that not all samples have the same size. Some have much more text published than others, which results in different similarity values when comparing the smaller actor with the bigger actor and vice versa.

Therefore, we extract the 500 most frequent adjectives, nouns and keywords from each actors’ corpus and produce a similarity matrix for each of these types. This results in useful similarity values which are quite similar for each type between each actor. To display the results nicely in one plot the similarity matrices are pooled with the arithmetic mean of the similarity of all three matrices.

The keywords were extracted with the rapid automatic keyword extraction algorithm (RAKE). This algorithm looks for keywords by looking at contiguous sequence of words which do not contain irrelevant words. The process behind calculates a score for each word which is part of any candidate keyword (in our case adjectives and nouns). This is achieved through the algorithms counting how many times each word is occurring and how many times it co-occurs with other words. From this a score is calculated for each word. This is the ratio of how many times it co-occurs with other words to the word frequency. Then the RAKE score for the full candidate keyword is calculated by summing up the scores from each of the words which define the candidate keywords. This particular step ensures that the results we have are to some degree topics that are used frequently by each actor. Hence, we are to some degree able to see which actors share topics with each other and which do not.

### Results

![sim](/img/txt_sim_webdev.png)


### References
<ul class="references">
<li>Niwattanakul, Suphakit, Jatsada Singthongchai, Ekkachai Naenudorn, and Supachanun Wanapu. 2013. “Using of Jaccard Coefficient for Keywords Similarity.” International MultiConference of Engineers and Computer Scientists I(March): 380–84.</li>


<li>Rose, Stuart, Dave Engel, Nick Cramer, and Wendy Cowley. 2010. “Automatic Keyword Extraction from Individual Documents.” Text Mining: Applications and Theory (March): 1–20.</li>
</ul>
