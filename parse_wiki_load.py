import pickle
import pandas as pd
import re


def edit(value):
    string = str(value)
    pattern = r"\d+[\s,]?\d*[\s,]?\d*"
    return re.search(pattern, string)


with open('countries_params.db', 'rb') as file:
    data = pickle.load(file)

pd.set_option('display.max_columns', None)

data['T'] = data['Территория государства'].apply(edit)

# print(data[['Территория государства', 'Население']])
# print(data.info())
print(data['T'])
