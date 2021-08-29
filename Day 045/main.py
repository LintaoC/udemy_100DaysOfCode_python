from bs4 import BeautifulSoup
import requests

response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
empire_page = response.text

soup = BeautifulSoup(empire_page, 'html.parser')

""" !!!!!!! The site is not working anymore as it was when Angela designed the course. 
I'm not able to scrap properly the datas :( I'm missing3-4 names, the one of which empire didn't do a review"""

movies = soup.select(selector=".listicle-container.jsx-3821216435 .listicle-item.jsx-3821216435 "
                              ".listicle-item-content.jsx-4245974604 p a")

movies_list = []

for movie in movies:
    if "Read Empire's review of" in movie.getText():
        str = movie.getText()
        movie_name = str.replace("Read Empire's review of ", "")
        movies_list.append(movie_name)

movies_list.reverse()

with open("movies.txt", "w") as file:
    for movies in movies_list:
        file.write(movies)
        file.write("\n")
