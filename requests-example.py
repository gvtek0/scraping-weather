#! python3
import requests
page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
print(page.status_code)
print(page.content)