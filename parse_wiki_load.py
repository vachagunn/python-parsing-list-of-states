import pickle
import pandas as pd
import re


def edit(value):
    string = "".join(str(value).split()).replace(',', '.')
    pattern = r"\d+[.]?\d*[.]?\d*"
    result = re.search(pattern, string)

    if result:
        result = float(result[0])
        if 'тыс' in string:
            result *= 10 ** 3
        if 'млн' in string:
            result *= 10 ** 6
        if 'млрд' in string:
            result *= 10 ** 9

    return result


with open('countries_params.db', 'rb') as file:
    data = pickle.load(file)

pd.set_option('display.max_columns', None)
pd.set_option('display.float_format', lambda x: '%.2f' % x)

data['T'] = data['Территория государства'].apply(edit)
data['P'] = data['Население'].apply(edit)

print(data[['Страна', 'T', 'P']])

print('Кол-во людей на планете: ', data['T'].sum())

print('\nБольше всего населения:\n', data[data['P'] == data['P'].max()])
print('\nМеньше всего населения:\n', data[data['P'] == data['P'].min()])

print('\nБольше всего площади:\n', data[data['T'] == data['T'].max()])
print('\nМеньше всего площади:\n', data[data['T'] == data['T'].min()])

# Проверка данных (было - стало)
print(data[['Территория государства', 'T']])
print(data[['Население', 'P']])
