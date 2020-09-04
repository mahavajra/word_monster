## Utility Functions to generate test data for the classifier
import requests
from bs4 import BeautifulSoup
from tqdm import tqdm  # progress bar


# Crawl naver.com news search result and fetch titles to test
#
# NOTE: The search query and page url is hardcoded into the function.
# This code just demonstrates how to retrieve some text data from a webpage.
def crawl_titles_from_naver(start_page, end_page):
    URL = "https://search.naver.com/search.naver?&where=news&query=%EB%AF%B8%EA%B5%AD&sm=tab_pge&sort=0&photo=0&field=0&reporter_article=&pd=0&ds=&de=&docid=&nso=so:r,p:all,a:all&mynews=0&cluster_rank=23&start="
    titles = []
    for page_num in tqdm(range(start_page, end_page)):
        page_url = URL + str(page_num)
        req = requests.get(page_url)
        titles += [tag.text for tag in BeautifulSoup(req.text, 'lxml')
                .select("a._sp_each_title")]
    return titles


# Formatted print
def pretty_print(sentence, val):
    print("SENTENCE:\t" + sentence)
    print("EVALUATION:\t" + str(val))
    print("LABEL:\t\t" + ("neutral"  if val == 0 else
                         ("positive" if val >  0 else "negative")))


# Read word list from the given file path
def load_wordlist(path):
    with open(path, encoding="UTF-8") as f:
        return f.read().strip().split("\n")
