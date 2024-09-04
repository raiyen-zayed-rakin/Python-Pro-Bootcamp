from bs4 import BeautifulSoup
import lxml

with open("website.html") as file:
    contents = file.read()


soup = BeautifulSoup(contents, "html.parser")

# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)

print(soup.find_all(name="a"))
print(soup.find_all(name="p"))