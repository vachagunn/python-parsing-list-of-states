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

# print(data[['Территория государства', 'Население']])
# print(data.info())
print(data['T'])
