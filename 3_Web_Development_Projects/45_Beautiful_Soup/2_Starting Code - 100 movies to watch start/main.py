import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(url=URL)

soup = BeautifulSoup(response.text, "html.parser")

print(soup.title)

# movie_title_heading = soup.find(name="h3", class_="title")
# print(movie_title_heading.string)

reverse_movie_list = [headings.string for headings in soup.find_all(name="h3", class_="title")]

reverse_movie_list.reverse()
# print('Reversed List:', reverse_movie_list)

with open("Top_100_Movies", mode="w") as file:
    for movie in reverse_movie_list:
        file.write(f"{movie}\n")

