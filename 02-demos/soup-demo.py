from bs4 import BeautifulSoup
import requests

url = "https://en.m.wikipedia.org/wiki/List_of_common_misconceptions"

r = requests.get(url)

soup = BeautifulSoup(r.content, 'html.parser')

# print(soup.prettify())
# print(soup.title)
# print(soup.title.name)
# print(soup.title.string)
# print(soup.title.parent.name)

# print(soup.get_text())

links = soup.find_all("a")
for link in links:
    print(link.get('href'))
