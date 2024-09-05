import requests
import html
from bs4 import BeautifulSoup



URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
response = requests.get(URL)
movies_webpage = response.text

soup = BeautifulSoup(movies_webpage, "html.parser")

all_movies = soup.find_all(name="h3", class_="title")

movies_list = [movie.getText() for movie in all_movies]
movies = movies_list[::-1]
# sorted_movies_list = movies_list[::1]
print(movies)
with open("100_movies_to_watch.txt", mode="w") as file:
    for movie in movies:
        if movie == "59) E.T. â\\x80\\x93 The Extra Terrestrial":
            movie = "59) E.T. - The Extra Terrestrial"
            file.write(f"{movie}\n")
        else:
            file.write(f"{movie}\n")

