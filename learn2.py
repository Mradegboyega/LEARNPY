import requests
from bs4 import BeautifulSoup

# get html contents from the web using requests
url = "https://en.wikipedia.org/wiki/Brainfuck"
response = requests.get(url)
html = response.content
print(f"html content: {html}")

# parse the html content using beautifulsoup
soup = BeautifulSoup(html, "html.parser")
print(f"title of the page: {soup.title}")
