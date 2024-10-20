from bs4 import BeautifulSoup
import requests
import lxml

# with open("website.html") as file:
#     contents = file.read()
#
#
# soup = BeautifulSoup(contents, "html.parser")
#
# # print(soup.title)
# # print(soup.title.name)
# # print(soup.title.string)
#
# # print(soup.find_all(name="a"))
# # print(soup.find_all(name="p").)
#
# all_anchor_tags = soup.find_all(name="a")
#
# for tag in all_anchor_tags:
#     # print(tag.get_text())
#     print(tag.get("href"))
#
# heading = soup.find(name="h1", id="name")
# print(heading)
#
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading.getText())
#
# company_url = soup.select_one(selector="p a")
# print(company_url)
#
# print(soup.select(selector=".heading"))

response1 = requests.get(url="https://appbrewery.github.io/news.ycombinator.com/")
response = requests.get(url="https://news.ycombinator.com/news")

yc_webpage = response1.text

soup = BeautifulSoup(yc_webpage, "html.parser")
articles = soup.find_all(name="a", class_="storylink")
article_texts = []
article_links = []
for article_tag in articles:
    text = article_tag.getText()
    article_texts.append(text)
    link = (article_tag.get("href"))
    article_links.append(link)

article_upvotes = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]

largest_number = max(article_upvotes)
largest_index = article_upvotes.index(largest_number)

print(article_texts[largest_index])
# print(article_texts)
print(article_links[largest_index])
# print(article_links)
# print(article_upvotes)

