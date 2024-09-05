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

yc_webpage = response.text

soup = BeautifulSoup(yc_webpage, "html.parser")
print(soup.select_one(selector=".titleline a").getText())