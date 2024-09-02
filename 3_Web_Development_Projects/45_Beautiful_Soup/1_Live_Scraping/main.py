from bs4 import BeautifulSoup
import requests

"""Get the most upvoted article on the YCombinator website."""

response = requests.get(url="https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

link_list = []
title_list = []
article_span = soup.find_all(name="span", class_="titleline")
for span in article_span:
    article_anchor = span.a
    link = article_anchor.get("href")
    title = article_anchor.string
    link_list.append(link)
    title_list.append(title)
# print(len(link_list))
# print(len(title_list))

upvotes_list = [int(span.text.split()[0]) for span in soup.find_all(name="span", class_="score")] 
print(upvotes_list)

for i in range(0, len(upvotes_list)):
    if upvotes_list[i] == max(upvotes_list):
        print(link_list[i])
        print(title_list[i])
        print(upvotes_list[i])
