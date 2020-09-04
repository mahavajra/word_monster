from SentimentClassifier import SentimentClassifier
from utils import *


# initialize a classifier with the sample word list
print("Loading word list ...")
pos_wl = load_wordlist("wordlist/positive.txt")
neg_wl = load_wordlist("wordlist/negative.txt")
s = SentimentClassifier(pos_wl, neg_wl)
print("Done")


# crawl the naver.com new and print the result
print("Crawling news title ..")
for title in crawl_titles_from_naver(1, 20):
    pretty_print(title, s.evaluate(title))
    print()
