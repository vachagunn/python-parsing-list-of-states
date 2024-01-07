import pickle
import pandas as pd
import re


def edit(x):
    return type(x)  # не все значения string, есть none и float


with open('countries_params.db', 'rb') as file:
    data = pickle.load(file)

pd.set_option('display.max_columns', None)

data['T'] = data['Территория государства'].apply(edit)

# print(data[['Территория государства', 'Население']])
# print(data.info())
print(data['T'])
