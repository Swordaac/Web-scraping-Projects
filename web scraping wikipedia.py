from bs4 import BeautifulSoup
import requests
import pandas as pd

url = 'https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'

page = requests.get(url)

soup = BeautifulSoup(page.text, 'html')
soup.find('table', class_ = 'wikitable sortable')

table = soup.find_all('table')[1]

world_titles = table.find_all('th')
world_table_titles = [title.text.strip() for title in world_titles]

df = pd.DataFrame(columns = world_table_titles)

row_entity = table.find_all('tr')
row_entity = row_entity[1:]
length = len(df)

for row in row_entity:
    individual  = row.find_all('td')
    data_row = [data.text.strip() for data in individual]
    df.loc[length] = data_row
    length+= 1
    
print(df)