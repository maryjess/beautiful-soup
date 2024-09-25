import requests
from bs4 import BeautifulSoup # got imports issue, better refactor to setup.py

url = 'https://maryjess.github.io/jessica-mary/'
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')
data = soup.find_all()

with open('data.txt', 'w') as file:
	for item in data:
		file.write(item.text + '\n')
