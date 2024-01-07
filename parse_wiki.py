# Подключиться к странице со списком государств
# Далее перейти на страницу каждого государства и вытянуть от туда информацию о населении и территории

import pandas as pd
import requests
import pickle
from bs4 import BeautifulSoup

# Показ всех записей (192 страны)
pd.set_option('display.max_rows', None)

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

base_url = "https://ru.wikipedia.org/wiki/"
countries = list(data['Страна'])

# Параметры для поиска
params = ['Территория государства', 'Население']

# Переход на страницы государств по отдельности для сбора данных по параметрам
for country in countries[:14]:
    page = requests.get(base_url + country)
    soup = BeautifulSoup(page.text, 'lxml')

    info_table = soup.find('table')
    tr = info_table.find_all('tr')

    for param in params:
        for row in tr:
            if row.find('a', title=param):
                index = tr.index(row) + 1
                td = tr[index].find('td').text.strip()

                index = data[data['Страна'] == country].index
                data.loc[index, param] = td

# Запись результатов в файл
with open('countries_params.db', 'wb') as file:
    pickle.dump(data, file)

print(data)
