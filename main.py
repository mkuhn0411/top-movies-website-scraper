from bs4 import BeautifulSoup
import requests

URL = "https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(URL)
webpage = response.text
soup = BeautifulSoup(webpage, "html.parser")

movies_elements = soup.select(".listicle-item")
all_movies = {int(element.select_one(".listicle-item-count").getText().split()[0]): element.select_one("a").getText() for element in movies_elements}

for key, value in all_movies.items():
    print(key, '->', value)

with open("movies.txt", mode="w") as file:
    for key, value in all_movies.items():
        file.write(f"{key}: {value}\n")