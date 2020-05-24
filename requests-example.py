#! python3
import requests
page = requests.get("http://dataquestio.github.io/web-scraping-pages/simple.html")
page.status_code
print(page.status_code)