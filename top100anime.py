import requests
from bs4 import BeautifulSoup
url = 'https://animestars.org/topanime.html'


response = requests.get(url)
data = BeautifulSoup(response.text, 'html.parser')

anime_data = data.find('a',  class_ = "poster grid-item d-flex fd-column has-overlay")
link = anime_data['href']      # ссылка на аниме
name = anime_data.div.img['alt']       # название



for anime_data in data.find_all('a',  class_ = "poster grid-item d-flex fd-column has-overlay"):
    link = anime_data['href']
    name = anime_data.div.img['alt']
    print(name + ' ------- ' + link)


