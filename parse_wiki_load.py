import pickle
import pandas as pd
import re


def edit(value):
    string = "".join(str(value).split()).replace(',', '.')
    pattern = r"\d+[\s,]?\d*[\s,]?\d*"
    result = re.search(pattern, string)

    if result:
        result = float(result[0])

    return result


with open('countries_params.db', 'rb') as file:
    data = pickle.load(file)

pd.set_option('display.max_columns', None)

data['T'] = data['Территория государства'].apply(edit)

# print(data[['Территория государства', 'Население']])
# print(data.info())
print(data['T'])
