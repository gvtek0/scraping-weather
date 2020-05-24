#! python3
import requests
from bs4 import BeautifulSoup

page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
print(page.status_code)
print(page.content)

soup = BeautifulSoup(page.content, 'html.parser')
print(soup.prettify())