Graded components
================

- 10%: [class participation](#class-participation), demonstrating knowledge of the assigned reading and original thinking
- 10%: [in-class paper presentation](#paper-presentations)
- 10%: [reading responses](#reading-responses)
- 30%: three [extended labs](#labs)
- 40%: [replication project](#replication-project)
  - 10%: proposal
  - 10%: replication paper presentation
  - 10%: final project poster presentation
  - 10%: final project report

All assignment submissions are due at 5pm. A penalty of 10% will be assessed for each day late (from 5:01pm until 5:00pm on the next day). Late assignments will not be accepted after four days.

# Class participation

This is a seminar class, and active participation in class discussions is mandatory. Students should attend each class ready to give informed reflections on the assigned reading.

# Paper presentations

Each wednesday, a team of two students will lead the discussion of an the day's assigned paper. This includes the following tasks:
- Prepare a presentation that highlights key claims of the paper, describes all figures and tables (using slides), and explain all methods in the paper. Note that this may necessitate additional reading or research. 
- Email two open-ended reading comprehension questions to the professor by 3pm on the preceding tuesday, which will be posed to the class.
- Lead the class discussion of the paper, soliciting comments from and posing questions to the other students.

# Reading responses

Reading responses will be due on wednesday, and will relate to wednesday's reading. They are worth one point each, up to a maximum of ten points. This means you may skip a few and still get full credit. However, they are due at the start of class, and will not be accepted late.

# Labs

Students will choose three of the ten labs, and perform a significant extension of the lab material, e.g. 
- acquiring and analyzing additional data
- applying and comparing more analytical techniques
- visualizing the results in a new way, etc. 

The extension should tackle a coherent research question. For ideas and feedback, please contact the professor in advance!

The lab report should be submitted on T-square as a well-organized Jupyter notebook, including both the .ipynb format and a PDF. The notebook should be runnable and readable top-to-bottom. If for some reason it is not possible to produce a runnable notebook (e.g., large or unshareable data), please check with the professor beforehand.

# Replication project

The final project in the class involves replicating and extending a published paper in computational social science. This project is to be performed in teams of 2-3 students, and the paper must be approved by the professor before the submission of the formal proposal. A list of recommended papers can be found [here](https://docs.google.com/spreadsheets/d/1O9pofBgcqhAE7Oz9cw5XoSMu18jrR49e9O-I0xfu7OU/edit?usp=sharing).

The project has several checkpoints:

- **November 10**: Declare team intentions
- **November 13-15**: Check-in with professor about project ideas. Come to this meeting with a few papers already in mind, and information about what will be needed to replicate them.
- **November 17** Written [project proposal](#project-proposal) due
- **November 20** Give a short (5-6 minutes) presentation of the paper to be replicated in class. This presentation should highlight the main findings, and explain the planned replication and extension. All team members should attend.
- **November 27-29**: Check-in with professor about ongoing progress of replication and extension effort.
- **December 4**: [Poster presentations](#poster-presentation) in class
- **December 6**: [Final project reports](#project-report) due

"Replication" is interpreted broadly, but students are encouraged to reuse the original authors' data and algorithms where possible. The balance between replication and extension depends on the difficulty of replication, and the size of the team. For example, if the original authors provide well-curated data and a runnable software implementation, then a more significant extension is expected; if the student team must re-implement a significant amount of software or gather a large dataset of their own, then the extension component can be more limited.

## Project Proposal
Each member of your team should submit a single, two-page proposal describing what you plan to do. The same proposal should be submitted by all team members. The proposal should indicate:

- Who is on the team
- What paper you plan to replicate (full citation) and why
	- Summarize the main findings of this paper
	- A sentence or two about why you think this paper is important
- How you will do it
	- **Data**: what you need, and where you can get it?
	- **Methods**: what computational techniques do you plan to employ, and how will you do it? Will you write your own code? Is there a software library you can use?
	- **Metrics**: how will you know if you have succeeded in replicating the paper? Be as specific as possible. If the paper has multiple findings, indicate how you will test that you have replicated each one.
	- **Risks**: What might go wrong that would cause this project to fail? What can you do to ameliorate these risks, and what will you do in this worst-case scenario?
	- **Limits**: are there findings that you will not be able to replicate? If so, explain why the parts that you *can* replicate are interesting enough on their own.
- When you will do what
	- How long will it take to replicate each finding? How do you plan to divide up the work?
	- **Stretch goals**: **If** the main findings of the paper are relatively easy to replicate given the data and resources that are available to you, how do you plan to go further, making an original contribution of your own?
	
## In-class Presentation
On December 4, you will give a short in-class presentation on the results of your replication effort. Please allot six minutes for your presentation, and two minutes for questions. You should have a total of six slides, including the title slide. Please include the following slides:

- One slide reviewing main findings of the original paper
- One or two slides describing the details of replication, such as data and software libraries
- One or two slides describing the results of your replication, which should be complete or very nearly complete by the day of the presentation. Include graphs and tables when possible.
- Final slide:
	- If the replication has not yet succeeded, describe the obstacles, and whether/how you can overcome them in the remaining two days.
	- If the replication has succeeded, you may describe any extensions that you are undertaking or envision for the future.

Please submit PDF slides by noon on December 4, so I can aggregate them into a single presentation.

## Project Report

Your final report should be a narrative of **at most** ten pages, submitted as a PDF. You can include an appendix for supplemental figures, tables, or code, but the 10 page report should be self-contained. You may find [this overleaf template](https://www.overleaf.com/latex/templates/template-for-2-columns-acl-proceedings-style/bdxxrbqzsmpv#.WhxkWRZOk5k) to be a useful format, if you want to use LaTeX. 

Your report should provide a complete description of what you did in your project, including all the points that you covered in your proposal and presentation:

- **What is your project's objective?** For example, Jurafsky et al wanted to identify the narrative structures that correlate with various types of restaurant reviews.
- **Why is it important?** Draw connections to theory and/or practical applications. For example, Bamman et al showed how it was possible to better understand internet censorship, which affects the way millions of people get information and express themselves.
- **What is your data source**? Explain how it was acquired, what are its limitations (if any), what preprocessing you did (and why). Explain how your use of data relates to that of the paper that you are replicating.
- **How did you analyze the data? What was your null model, and why is it justified?** For example, Stephens-Davidowitz compared against several competitive models, which included many strong predictors. He showed that the rate of racially-charged search terms added predictive power even above these competitive alternatives. Again, explain how your analysis relates to that of the paper that you are replicating.
- If the replication did not succeed, try to explain why not. Were you lacking key information from the original authors? Were you unable to obtain the same data? 
- If the replication did succeed, try to explain the limitations of your replication: would it work on other data? Does it rely on the method being implemented in exactly the same way as the original authors did? 
- If you had time to do an extension of the original paper, explain all of the points above with regard to your extension: the objective of your extension, why it is important, how you did it, and how the reader should understand the results.

### Writing advice:

- **Use specific examples to bolster high-level conclusions**: for example, if you find that unigram text features predict retweets, then show some of the words which are the strongest predictors (like Tan et al); if you find network centrality correlates with microfinance participation, give some examples of highly-central individuals and non-central individuals, and describe their outcomes. *This is especially important if you use unsupervised techniques such as clustering*, since the output of these techniques is otherwise opaque to the reader.
- Well-designed graphs and tables are more helpful than lots of text. Use the papers that we have read in class for guidance on how to write and structure your report, but keep in mind that each paper has its own idiosyncrasies, so think critically about what does and doesn't work in these papers.
- Similar to Wikipedia, citations should be provided for all factual statements, such as "Twitter language is noisy and ungrammatical" and "neural networks are the most powerful classification algorithm", to pick two examples completely at random. If text is taken verbatim from another source, it should be presented in quotations, with a citation; if the text is paraphrased from another source, a citation should also be included. I'm not picky about citation formats, but be sure to include all authors names, the full title, the year, and an unambiguous description of where the paper was published. 
