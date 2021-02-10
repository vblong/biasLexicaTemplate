# 50 Top level domains are stored in urls.txt
# Source: https://libguides.wlu.edu/c.php?g=357505&p=2412837
# From there more than 1000 article urls are retrieved and stored in articleUrls

from newspaper import Article
import newspaper
import csv
from gensim.models import Word2Vec
from models import IArticle
from nltk.tokenize import sent_tokenize, word_tokenize, RegexpTokenizer

def saveArticlesToFile(fileNameOutput, articles):
    # Download all articles
    with open(fileNameOutput, "w", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow([
            "Authors",
            "Url",
            "Keywords",
            "Meta_description",
            "Meta_keywords",
            "Meta_lang",
            "Publish_date",
            "Source_url",
            "Summary",
            "Tags",
            "Text",
            "Title"
        ])
        cnt = 0
        for article in articles:
            try:
                cnt = cnt + 1
                article.download()
                article.parse()
                writer.writerow([
                    article.description,
                    article.authors,
                    article.url,
                    article.keywords,
                    article.meta_de.meta_keywords,
                    article.meta_lang,
                    article.publish_date,
                    article.source_url,
                    article.summary,
                    article.tags,
                    article.text,
                    article.title
                ])
            except newspaper.article.ArticleException:
                print("404 Exception occured")
            except Exception as e:
                print("An error occured:", e)
        print("Total ", cnt, " articles downloaded.")


# Scrapper used: newspaper
# Link: https://github.com/codelucas/newspaper
def downloadArticles(articleLink, outputFilename):
    print("Starting download articles...")

    with open(articleLink) as f:
        urls = f.read().splitlines()
    cnt = 0
    articles = []
    for url in urls:
        articles.append(Article(url))
        cnt = cnt + 1

    saveArticlesToFile(outputFilename, articles)

# Read all articles stored in articles.csv
def readArticles():
    articles = []
    with open('./articles.csv', 'r') as f:
        reader = csv.reader(f)
        for index, row in enumerate(reader):
            try:
                if checkEmpty(row) == False and index > 0:
                    articles.append(IArticle(
                        row[0],             # Author
                        row[11],            # Title
                        row[10],            # Text
                        row[3],             # Categories
                        row[2],             # Url
                        row[6]              # Date Published
                    ))
            except:
                print("An error occured while reading article #", index)

    return articles

# Inside articles.csv, there are some rows that are complete empty.
# However, column 7th is the column that stores the article's url.
# It's the only column that always has data if the row is valid.
# When the cell at any row at this column is empty, that means this row is a complete empty row
def checkEmpty(row):
    if row[7] == None or row[7] == "":
        return True
    return False

# Remove tokens which represent number and tokens which consist less than 2 character
# Then make them all in lowercase
def preprocessing(tokens):
    print("Start preprocessing...")
    result = []
    numOfToken = 0
    for token in tokens:
        arr = []
        for t in token:
            if t.isdigit() == False and len(t) > 2:
                arr.append(t.lower())
                numOfToken = numOfToken + 1
        result.append(arr)
    return (result, numOfToken)

def computeBiasWords(articles):
    # Tokenizing + removing punctuations
    tokens = []
    tokenizer = RegexpTokenizer(r'\w+')
    for article in articles:
        tokens.append(tokenizer.tokenize(article.text))

    # Preprocessing
    numOfToken = 0
    (tokens, numOfToken) = preprocessing(tokens)

    print(tokens)
    print("Total documents: ", len(tokens))
    print("Total tokens: ", numOfToken)

    # Word Embeddings with Word2Vec from Gensim lib
    # Parameters are default values
    model = Word2Vec(sentences=tokens, size=100, window=5, min_count=1, workers=4)

    return model