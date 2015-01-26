Course schedule
===

This schedule is still a work in progress, as I'm always finding new readings that are relevant. The assignment dates will be no earlier than as posted here. There are a few different categories of reading:

- **Reading**: This is required.
- **Supplemental reading**: Optional. These are usually research papers that relate to the topic of the class, and may be discussed in class. Look here for final project ideas.
- **Catch-up reading**: Optional. This is tutorial/survey material to help students catch up with the technical concepts in the class.
- **Also see**: Optional, non-peer-reviewed material. This includes blogposts and popular press articles.

# Part 1: Data science #

In this section, we will use contemporary research papers to get up to speed on statistical methods. If you have trouble keeping up with these readings, you may consult [Think Stats](http://greenteapress.com/thinkstats/thinkstats.pdf), a free online textbook.

## 1/5: Computational social science ##

- **Reading**: [Computational social science](http://gking.harvard.edu/files/LazPenAda09.pdf) by Lazer et al; [Six provocations for Big Data](http://papers.ssrn.com/sol3/papers.cfm?abstract_id=1926431) by boyd and Crawford.
- **Supplemental reading**:
[No silver bullet: De-identification still doesn't work](http://randomwalker.info/publications/no-silver-bullet-de-identification.pdf) by Narayanan and Felten.
- **Also see**: The view from the other side: [perspectives on computational sociology](http://orgtheory.wordpress.com/2015/01/02/building-computational-sociology-from-the-academic-side/#comments) from Fabio Rojas. Good comments, too;
[Sticky data: Why even 'anonymized' information can still identify you](http://www.theglobeandmail.com/technology/digital-culture/sticky-data-why-even-anonymized-information-can-still-identify-you/article19918717/).

## 1/7: Provocations; counting random events ##

We will cover basic probability and statistics, including random events, probability mass functions, cumulative distribution functions, and hypothesis testing.

- **Reading**: [Six provocations for Big Data](http://papers.ssrn.com/sol3/papers.cfm?abstract_id=1926431) by boyd and Crawford; [Think Stats](http://greenteapress.com/thinkstats/thinkstats.pdf) chapters 1-3.

Here is a [stats refresher iPython notebook](class-notes/stats-refresher.ipynb), focusing on tests of statistical significance. You may find this useful to look at before doing problem set 1.

## 1/12: Multiple comparisons; randomized tests; correlation ##

Further discussion of hypothesis testing, with emphasis on corrections for multiple comparisons, randomized tests, and measures of correlation.

- **Reading**: [Censorship and deletion practices in Chinese social media](http://journals.uic.edu/ojs/index.php/fm/article/view/3943/3169), by Bamman, O'Connor, and Smith, sections 1-4;
- **Catch-up reading**: [Think Stats](http://greenteapress.com/thinkstats/thinkstats.pdf), chapters 5 and 7.
- **Also see**: [Ages and names](https://fivethirtyeight.com/features/how-to-tell-someones-age-when-all-you-know-is-her-name/); [XKCD](http://xkcd.com/882/) on multiple comparisons; [Spurious correlations](http://www.tylervigen.com/)

## 1/14: Regression ##

- **Reading**: *Wasserman chapter on linear regression* (available on T-square, ask me if you can't access it);
[More tweets, more votes](http://www.plosone.org/article/info%3Adoi%2F10.1371%2Fjournal.pone.0079449) by Joseph DiGrazia et al, 2013; [How (not) to predict elections](http://cs.wellesley.edu/~pmetaxas/How-Not-To-Predict-Elections.pdf) by Metaxas et al, 2011 (skim).
- **Supplemental reading**: [The cost of racial animus on a Black presidential candidate: Using Google search data to find what surveys miss](http://static.squarespace.com/static/51d894bee4b01caf88ccb4f3/t/51d89ab3e4b05a25fc1f39d4/1373149875469/RacialAnimusAndVotingSethStephensDavidowitz.pdf); [Understanding the political representativeness of Twitter users](https://files.nyu.edu/pba220/public/barbera-rivero-2014.pdf); [Online and social media data as a flawed continuous panel survey](http://research.microsoft.com/en-us/um/redmond/projects/flawedsurvey/flawedsurvey.pdf) by Diaz et al 2014.
- **Catch-up reading**: [Think stats](http://greenteapress.com/thinkstats/thinkstats.pdf), chapters 4 and 8; [Notes on regression](http://cs229.stanford.edu/notes/cs229-notes1.pdf) by Andrew Ng, sections 0, 3, and 5.
- **Also see**: [this Vox piece](http://www.vox.com/2014/12/1/7311417/race-law-controls)  by Ezra Klein on the use of controls in studies of racial and gender discrimination.
- **[Problem set 1](psets/ps1.md)** out. Due January 23 at 5pm.

## 1/19: No class ##

Celebrate [Martin Luther King Day](http://www.ajc.com/news/events/events-and-things-do-around-atlanta-mlk-day/njgYC/)

## 1/21: Classification and clustering ##

- **Reading**: [A few useful things to know about machine learning](http://homes.cs.washington.edu/~pedrod/papers/cacm12.pdf) by Domingos, 2012.
[A computational approach to politeness](http://www.stanford.edu/~jurafsky/pubs/politeness-acl13.pdf) by Cristian Danescu-Nicolescu-Mizil et al, 2013.
[Data carpentry](http://www.mimno.org/articles/carpentry/) (very short!)
- **[Problem set 1](psets/ps1.md)** due on January 23 at 5pm.

# Part 2: Network Analysis #

In this section of the course, monday readings will be drawn from the textbook [Networks, Crowds, and Markets](http://www.cs.cornell.edu/home/kleinber/networks-book/) by Easley and Kleinberg (abbreviated E&K). Free PDFs of each chapter are available by following the link.

## 1/26 and 1/28: Networks ##

- **Monday reading**: E&K chapters 1 and 2
- **Wednesday reading**: [Structural diversity in social contagion](http://www.pnas.org/content/109/16/5962.full)
- **Supplemental reading**:  Chapter 6 of [Newman](http://www.amazon.com/Networks-An-Introduction-Mark-Newman/dp/0199206651) is more rigorous and more detailed.

## 2/2 and 2/4: Strong and weak ties ##

- **Monday reading**: E&K chapter 3
- **Wednesday reading**: [The Role of Social Networks in Information Diffusion](http://arxiv.org/pdf/1201.4145) by Bakshy et al, 2012;

## 2/9 and 2/11: Homophily ##

- **Monday reading**: E&K chapter 4
- **Wednesday reading**: [Inferring social ties from geographic coincidences](http://www.pnas.org/content/107/52/22436.full.pdf+html);
[Find me if you can](http://www.cameronmarlow.com/media/backstrom-geographical-prediction_0.pdf)
- **Supplemental reading**: [Homophily and Contagion Are Generically Confounded in Observational Social Network Studies](http://arxiv.org/pdf/1004.4704v3) by Shalizi and Thomas, 2011; 

## 2/16: No class ##

- **[Problem set 2](psets/ps2.md)** out. Due Feb 27 at 5pm.

## 2/18: Signed social networks ##

- **Reading**: E&K chapter 5

## 2/23: Signed social networks in social media and literature ##

- **Reading**: [Signed networks in social media](http://cs.stanford.edu/~jure/pubs/triads-chi10.pdf);
- **Supplemental reading**:
["You’re Mr. Lebowski, I’m the Dude": Inducing Address Term Formality in Signed Social Networks](http://arxiv.org/abs/1411.4351)

## 2/25: Statistical models of networks ##

- **Reading**: [A survey of statistical network models](arxiv.org/pdf/0912.5410), sections 2-3.8.
- **[Problem set 2](psets/ps2.md)** due on Feb 27 at 5pm.

# Part 3: Text #

## 3/2 and 3/4: Word counting ##

- **Monday reading** [The psychological meaning of words: LIWC and computerized text analysis methods](http://homepage.psy.utexas.edu/HomePage/Faculty/Pennebaker/Reprints/Tausczik&Pennebaker2010.pdf) by Tausczik and Pennebaker (2010);  [Text as data](http://stanford.edu/~jgrimmer/tad2.pdf) sections 2-4
- **Wednesday reading**: [Echoes of power: Language effects and power differences in social interaction](http://www.mpi-sws.org/~cristian/Echoes_of_power.html) by Danescu-Niculescu-Mizil, Lee, Pang, Kleinberg, 2012
- **Supplemental reading**:
[Linguistic Models for Analyzing and Detecting Biased Language](http://www.mpi-sws.org/~cristian/Biased_language_files/neutrality.pdf) by Recasens et al; [Shedding (a thousand points of) light on biased language](http://mlt.sv.cmu.edu/mlt/research/conferences/naacl2010/MTURK/pdf/MTURK23.pdf) by Yano et al; [Detecting and modeling local text reuse](http://www.ccs.neu.edu/home/dasmith/infect-dl-2014.pdf).

- **Also see**: [Fairness versus freedom](https://fivethirtyeight.com/datalab/fairness-vs-freedom-is-politics-going-back-to-the-1970s/)

## 3/9 and 3/11: Text classification and regression ##

- **Monday reading**: [Fighting words](http://www.law.berkeley.edu/files/MonroeColaresiQuinn.pdf) by Monroe, Colaresi, and Quinn
- **Wednesday reading**: [Narrative framing of consumer sentiment in online restaurant reviews](http://firstmonday.org/ojs/index.php/fm/article/view/4944/3863)
- **Supplemental reading**: [Phrases that signal workplace hierarchy](http://dl.acm.org/citation.cfm?id=2145359) by Gilbert; [Identifying regional dialects in online social media](http://www.cc.gatech.edu/~jeisenst/papers/dialectology-chapter.pdf) by Eisenstein;  [Sparse additive generative models of text](http://www.cc.gatech.edu/~jeisenst/papers/icml2011.pdf) by Eisenstein et al;  [Political ideology detection using recursive neural networks](http://www.cs.colorado.edu/~jbg/docs/2014_acl_rnn_ideology.pdf) by Iyyer et al; [More than Words: Syntactic Packaging and Implicit Sentiment](http://ftp.cfar.umd.edu/users/resnik/pubs/greene_resnik_naacl2009.pdf) by Greene and Resnick.
- **[Problem set 3](psets/ps3.md)** out on Monday 3/9, due 3/27.

## 3/16 and 3/18: No class, spring break ##

## 3/23 and 3/25: Topic models ##

- **Monday reading**:
[Statistical models](http://www.cs.columbia.edu/~blei/fogm/lectures/modeling.pdf);
[Probabilistic topic models](http://www.cs.princeton.edu/~blei/papers/Blei2012.pdf) by Blei, 2012.
- **Wednesday reading**: [Probabilistic topic models](http://www.jaist.ac.jp/~bao/VIASM-SML/SMLreading/TopicModel-Steyvers.pdf) by Steyvers and Griffiths
- **Supplemental reading**:  [Personality, Gender, and Age in the Language of Social Media: The Open-Vocabulary Approach](http://www.plosone.org/article/info%3Adoi%2F10.1371%2Fjournal.pone.0073791) by Schwartz et al; [Care and feeding of topic models](http://www.cs.colorado.edu/~jbg/docs/2014_book_chapter_care_and_feeding.pdf) by Boyd-Graber, Mimno, and Newman.
- **[Problem set 3](psets/ps3.md)** due 3/27 at 5pm.

## 3/30 and 4/1: Topic models and metadata ##

- **Monday reading**: [Topic and Role Discovery in Social Networks...](http://www.aaai.org/Papers/JAIR/Vol30/JAIR-3007.pdf)
- **Wednesday reading**:
- **Supplemental reading**: [Learning to extract international relations from political context](http://www.cs.cmu.edu/~nasmith/papers/oconnor+stewart+smith.acl13.pdf) by O'Connor et al, 2013.
- [Final project](psets/indie.md) proposal due Friday 4/3 at 5pm.

## 4/6 and 4/8: Joint models of networks and text ##

- **Monday reading**:
[Hierarchical relational models for document networks](https://www.cs.princeton.edu/~blei/papers/ChangBlei2009.pdf) 
- **Wednesday reading**: 
[Exploiting social network structure for person-to-person sentiment analysis](http://infolab.stanford.edu/~west1/TACL2014/)
[Unsupervised Induction of Signed Social Networks from Content and Structure](http://arxiv.org/pdf/1411.4351)

# Part 4: Final projects #

## 4/13 and 4/15: Final project check-ins ##

I will use a Google doc to schedule meetings with each group.

## 4/20: Final project presentations ##
## 4/22: Contemporary topics in computational social science ##
## 4/24: Final project writeups due at 5pm ##
