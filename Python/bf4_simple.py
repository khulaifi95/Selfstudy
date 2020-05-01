from bs4 import BeautifulSoup
import requests

with open('simple.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')  # [1] parser

# print(soup.prettify())

match = soup.title.text
# print(match)

match = soup.find('div')
# print(match)

article = soup.find('div', class_='article')
# print(article)

headline = article.h2.a.text
# print(headline)

summary = article.p.text
# print(summary)

for article in soup.find_all('div', class_='article'):
    headline = article.h2.a.text
    print(headline)

    summary = article.p.text
    print(summary)

    print()
