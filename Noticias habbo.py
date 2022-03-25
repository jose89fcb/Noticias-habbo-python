from bs4 import BeautifulSoup
import requests
import os

HotelNoticia="es" ## es -> en -> it -> de-> fr -> fi -> fi -> tr -> nl -> pt 
url = f"https://images.habbo.com/habbo-web-news/{HotelNoticia}/production/front.html"
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

hotel="es" ## es -> com ->it -> de -> fr -> com.tr ->nl -> com.br

titulo = soup.find_all('h2', class_='news-header__title')[1].text

imagen = soup.find_all('img')[2]

urlNoticia = soup.find_all('a')[3]

descripcion = soup.find_all('p', class_='news-header__wrapper news-header__summary')[1].text

os.system('cls')

print("Titulo:"+ f"{titulo}")
print("\n")
print("Imagen: "+ f"{imagen['src']}")
print("\n")
print("Url: "+ f"https://habbo.{hotel}{urlNoticia['href']}")
print("\n")
print("Descripción: "+ f"{descripcion}")
