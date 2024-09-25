import requests
from bs4 import BeautifulSoup

url = 'https://maryjess.github.io/jessica-mary/'
html_text = requests.get(url).json()["results"][0]["content"]
soup = BeautifulSoup(html_text, "html.parser")

data = soup.find_all()

with open('data.txt', 'w') as file:
	for item in data:
		file.write(soup.get_text(strip=True, separator=" "))
