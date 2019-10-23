# [biasWord]-Task
## Summary
This task should be a starting point for you before you contributing to an ag-gipp project. We are using several techniques and tools to organize our development process. To keep it well structured and organized, every developer must be familiar with those tools before he/she is contributing new code. Please note that successfully finishing this task does not replace project specific contributing guidelines.

This project aims for two goals. One is to solve a problem programmatically, while the other one is to give you the understanding of our workflow and the tools we are using. The task description explains the task you have to solve. Please follow each point of the detailed instructions and at get a little familiar with the tools in the optional features section. Note that the linked guides are comprehensive and way too big for your purposes. It's up to you to find the right dose of information you need.

## Task Description

Word Embedding is a language modeling technique used for mapping words to vectors of real numbers. It represents words or phrases in vector space with several dimensions. Word embeddings can be generated using various methods like neural networks, co-occurrence matrix, probabilistic models, etc.

Word2Vec consists of models for generating word embedding. These models are shallow two layer neural networks having one input layer, one hidden layer and one output layer.

<b>First, scrape a dataset from any english newspaper you like. Your dataset should at least contain a 1000 articles and should be no older than 2017. Then, write a program in Python which takes your dataset and calculates the 1000 most likely bias words for any 10 bias words of your choice. So you will choose 10 words that you think are good examples for bias in your dataset (See a short description of what bias is on https://www.thoughtco.com/what-is-biased-language-1689168), and then use word embeddings to calculate the 100 most
 similar words to each of those words. Print out the cosine distances of each word to all its most similar words. You will need to use tokenization and charakter replacements, but are free in any model choice. An example of the process on how to calculate the bias words is given in this paper: https://bit.ly/2BCugKE. 
Helpful python modules can be genism and nltk. To enhance your creativity, you are free of choice in the selection of a newspaper and any type of scraping.</b>



## Detailed Instructions 

<a href="https://github.com"><img align="right" src="https://image.flaticon.com/icons/svg/25/25231.svg" height="28"></a><a href="https://git-scm.com/"><img align="right" src="https://git-scm.com/images/logos/downloads/Git-Logo-2Color.png" height="28"></a>
### Git & GitHub

1. Create a GitHub account and send your supervisor your username.
2. Get familiar with the basics of [Git](https://git-scm.com/book/en/v2/) and [GitHub](https://guides.github.com/activities/hello-world) to achieve the following steps
    1. `Checkout` your project template on your local machine (do not make any changes directly on the GitHub page! Use your terminal or your IDE to work with Git, i.e., pull, commit, push changes.)
    2. Create a file called `README.md` and explain what your project will do, what you need to achieve and how to use the program when finished your task. Put this file in your project parent directory so that it will show up in your GitHub-project start page.
    3. Create a `.gitignore` File and put it into your parent directory.
    4. __Optional:__ in bigger projects, we usually work on multiple branches. To get familiar with this technique, push your first changes to another branch (please use your terminal and not your IDE to see how it works most natively). However, in your task, you are the only developer and the project is small so it is not necessary to work with multiple branches furthermore. Thus, merge the second branch back to `master` and just work on the `master` branch. Don't forget to delete the temporary branch you just created. This keeps your repository clean.

_From now on, push every change to GitHub!_ 

### (Optional) Coding guidelines

1.    use Properties und setter (instead of getter und setter), public attributes if necessary and useful.
2.    use "class XYZ:" instead of  "class XYZ(object):"
3.    use Type Hints (consider this stackoverflow question and first answer.)
4.    use PyCharm or IntelliJ with Python plugin
5.    "Reformat code" before pushing anything to the repo (https://www.jetbrains.com/help/pycharm/reformat-and-rearrange-code.html)
6.    write comments
7.    avoid long functions
8.    use variable names that speak for themselves! bad: "tmp", good: "named_entity_counter"
9.    For more information on how to write good Python code and documentation, see https://www.python.org/dev/peps/pep-0008/

Code must be executable on Python 3.6!


### Final Statement

Please note that this task is not a tutorial to guide you through each tool. You have to figure out each part on your own. We do not claim to become an expert in every mentioned tool, but we expect a basic knowledge from you once you finished this task. Thus, don't lose yourself in hundreds of manual pages but get familiar with the basics that are necessary.

Also, if you have any comments for us, for example how we could improve this task, what was too difficult or too easy, let us know your opinion. We highly appreciate your feedback.

Good luck!
