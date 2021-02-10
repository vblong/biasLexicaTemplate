from functions import *

# 1st argument: the file which stores the article urls to be downloaded
# 2nd argument: the file which stores the downloaded articles
# Some url can't be downloaded due to some backend reasons.
def doDownload():
    downloadArticles('./articleUrls', 'articles3.csv')

# Read articles from ./articles.csv and use Gensim to train a Word2Vec model from these articles
# Then save them to /model/word2vec.model
def doTraining():
    articles = readArticles()
    model = computeBiasWords(articles)
    model.save('../model/word2vec.model')

# The 1o chosen biased words
# These 10 words are chosen from these page:
# https://blog.ongig.com/diversity-and-inclusion/biased-language-examples/
# https://www.niu.edu/writingtutorial/style/bias-free-language.shtml
# Send in a file name if you want to save the result to a file.
# Result file will appear inside 'results' folder
def doDisplayResult(resultFileName=None):
    # Load pre-trained model and print out some results
    model = Word2Vec.load('../model/word2vec.model')
    biasedWords = [
        "housewife",
        "old",
        "policeman",
        "maid",
        "homosexual",
        "aliens",
        "slave",
        "gay",
        "tribe",
        "actress"
    ]
    result = []
    for w in biasedWords:
        try:
            print("Top similar words for the word '", w, "':")
            most100SimilarWords = model.wv.most_similar(positive=[w], topn=100)
            result.append(most100SimilarWords)
            print(most100SimilarWords)
            print()
        except KeyError as e:
            print("Word", w, "does not exist in the training data")
            print()

    if resultFileName != None:
        with open('../results/' + resultFileName, "w", encoding="utf-8") as csvfile:
            writer = csv.writer(csvfile, delimiter=',', lineterminator='\n')
            writer.writerow(tuple(biasedWords))
            for i in range(0, 100):
                row = []
                for j in range(0, 10):
                    row.append(result[j][i][0] + ":" + str(round(result[j][i][1],4)))
                writer.writerow(row)

# doDownload()
# doTraining()
doDisplayResult('result.csv')
