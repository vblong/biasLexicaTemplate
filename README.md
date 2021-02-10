# This project consists of source code and results by working on the tasks from the project 'biasLexicaTemplate'
### Original Link: https://github.com/ag-gipp/biasLexicaTemplate

## 0. Project Summary
Choose any 10 seed words manually that you consider as biased words. Scrape 1000 articles on the internet, build a Word2Vec model from them, then get out 100 most similar words for each of the 10 chosen seed words. Results should consist of the similar words and its cosine distance with the seed word.

## 1. How it's done
### 1.1 Scrapping data
I use a scrapper called 'newspaper' to scrape the articles, link: https://github.com/codelucas/newspaper. 

First I list out 50 online news websites, then browse all of them, on each websites I use jQuery to list out several articles links on the homepage, then store all of them inside the `articleUrls.txt` file.

The 50 news websites are taken from here: https://libguides.wlu.edu/c.php?g=357505&p=2412837

A total of 1154 links are retrieved, however only 1009 of them are scrape-able, as some returns 404 or some strange errors, or maybe it's the scraper problem.

As I get only the urls that are presented on the homepage, the scrapped articles are then only the newest ones, however their topics are very broad and this may not be a good training data set.

Finally I extracted some info that I consider important and store them in my own article class.

### 1.2 Clean data and train a Word2Vec model
All articles are then tokenized and stored into arrays, and build a collection of all of them.

As the data set is pure, having it cleaned is necessary. 

For that I removed all punctuations, and make them all lowercase.

At first I also removed stop words, however, some stop words are also considered as biased words, so I decided to not remove them anymore, instead I removed any tokens that consist less than 3 characters.

Any tokens that represent numbers are also removed.

After that the training session begins, here the Gensim library is used as stated from the task description, and the training takes one function call with default hyperparameters.

## 2. Result 
The 10 seed words are: 

`["housewife", "old", "policeman", "maid", "homosexual", "aliens", "slave", "gay", "tribe", "actress"]`

As this is the first time I hear about something called "bias language", the way I chose seed words are completely random, all of them are taken from these 2 websites:

- https://blog.ongig.com/diversity-and-inclusion/biased-language-examples/
- https://www.niu.edu/writingtutorial/style/bias-free-language.shtml

For each seed word, 100 most similar words are printed out along with their cosine distances. Result are stored in `/results/result.csv` file if desired.

Here I list out 10 most similar words for the first 5 seed words, for the complete result please see the `/results/result.csv` file.

housewife | old | policeman | maid | homosexual
--------- | --- | --------- | ---- | ----------
macwilliams:0.9962 | last:0.9798 | colon: 09414 | kamala:0.9747 | centered:0.994
justin:0.9961 | starter:0.9294 | anja:0.9323 | slideshow:0.972 | sarah:0.994
run:0.9959 | olds:0.9276 | vacancies:0.9315 | texting:0.9715 | industrial:0.9939
tennis:0.9958 | exceeds:0.9146 | exceeds:0.9314 | marin:0.9707 | writer:0.9938
magazine:0.9958 | 503million:0.9137 | hiatus:0.9252 | girlfriends:0.9695 | trials:0.9937
mahrez:0.9957 | vacancies:0.9111 | payton:0.9233 | trap:0.9695 | walters:0.9936
australia:0.9957 | phanerozoic:0.9035 | demi:0.9231 | vice:0.9694 | dancers:0.9936
college:0.9955 | racked:0.9028 | ciulla:0.9201 | spector:0.9692 | cnet:0.9936
angela:0.9953 | 15m:0.9028 | sequences:0.9171 | declaring:0.9675 | sofia:0.9936
himself:0.9953 | annus:0.9023 | four:0.9169 | robertson:0.9673 | anti:0.9935

## 3. How to run
This project relies on the following libraries, be sure to have them installed before you run: `newspaper`, `nltk`, `gensim`.

All Python code are in the `main` folder. There are 3 functions you can play with in the `main.py` file:

- `doDownload(articleLinksFile=None, saveFileName=None)` : this function will download all articles from all the links inside `articleUrls.txt` file, then store them inside `articles.csv` file using the structure defined in the class `IArticle` (`models.py`)
    * `articleLinksFile`: if nothing is passed, the file `articlesUrls.txt` will be used.
    * `saveFileName`: if nothing is passed, the file `articles.csv` will be used.

- `doTraining()` : will read all articles from `articles.csv` file, then build a Word2Vec model and store the model in `model/word2vec.model`.

- `doDisplayResult(resultFileName=None, biasedWords=None)` : will list out 100 most similar words for the chosen seed words. The result can be stored in a file if desired. 
    * `resultFileName`: if nothing is passed in, no data will be saved, otherwise the resulted file will be created and stored inside the `results` folder
    * `biasedWords`: if nothing is passed, default seed words from section 2 shall be used


## 4. Ways to improvements

### 4.1 Data selection
The scrapped articles varied in a lot of topics, focusing on a few specific topics or even only one topic should produce more accurate results, this also leads to the seed words selection less random. 

### 4.2 More preprocessing
We can see that there are some strange words appear in the resulted table above and do not have much meaning, such words are personal name, e.g Justin, Payton, Anja... and words that represent unit e.g 503millions, 15m...etc. Also there is a project which store a list of non-biased-stop-words, which should be considered.

Some words are basically the same but appear in different forms, like `old` and `olds`, they should be in the same form, base form is personally preferred.

### 4.3 Try with more hyperparameters and validation
Here I use Gensim to build a word2vec model with default hyperparameters, try with more variations and even using some k-fold-validation may give new insights. 