# Подключиться к странице со списком государств
# Далее перейти на страницу каждого государства и вытянуть от туда информацию о населении и территории

import pandas as pd
import requests
from bs4 import BeautifulSoup

url = "https://ru.wikipedia.org/wiki/Список_государств"

page = requests.get(url)
soup = BeautifulSoup(page.text, 'lxml')

table = soup.find('table')

headers = []

for th in table.find_all('th'):
    headers.append(th.text.strip())

data = pd.DataFrame(columns=headers)

for row in table.find_all('tr')[1:]:
    cells = row.find_all('td')
    cell_data = []

    for cell in cells:
        cell_data.append(cell.text.strip())

    df = pd.DataFrame([cell_data], columns=headers)
    data = pd.concat([data, df], axis=0)

data.index = [i for i in range(data.shape[0])]
data = data.drop(['Номер', 'Флаг'], axis=1)

print(data)
