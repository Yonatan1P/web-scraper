# configure and select wiki page
import requests
from bs4 import BeautifulSoup

URL = 'https://en.wikipedia.org/wiki/Bay_of_Pigs_Invasion'

page = requests.get(URL)


# print the content of the page

soup = BeautifulSoup(page.content, 'html.parser')
content = soup.find('')

# print the soup

# find the spans with title This claim needs references to reliable sources. (March 2020)

spans = soup.find_all('span', string="citation needed")

print(spans) 