import requests
from bs4 import BeautifulSoup
import pandas as pd

current_link = f'https://www.bustershop.com.br/buscar?q=Anel+Obscuro'
response = requests.get(current_link)
data = response.text
soup = BeautifulSoup(data, 'html.parser')

names = soup.select('.nome-produto')
names = [name.text.strip() for name in names]

prices = soup.select('.desconto-a-vista > strong')
prices = [price.text.strip() for price in prices]

links = soup.select('.nome-produto')
links = [link.get('href') for link in links]

data = {
	'Name': names,
	'Price': prices,
	'Link': links
}

df = pd.DataFrame(data)
df.to_csv('bustershop-anel-obscuro-prices.csv')

print(df)
