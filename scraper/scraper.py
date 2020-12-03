# configure and select wiki page
import requests
from bs4 import BeautifulSoup




# print the content of the page


# print the soup

# find the spans with title This claim needs references to reliable sources. (March 2020)

URL = 'https://en.wikipedia.org/wiki/Bay_of_Pigs_Invasion'

def get_citations_needed_count(URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    spans = soup.find_all('span', string="citation needed")
    print(len(spans))
    return len(spans)

get_citations_needed_count(URL)

def get_citation_needed_report(URL):
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    spans = soup.find_all('span', string="citation needed")
    for span in spans:
        report = span.find_parent('p').prettify()
        print(report)
    return report

get_citation_needed_report(URL)