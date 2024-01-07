import pickle
import pandas as pd
import re

with open('countries_params.db', 'rb') as file:
    data = pickle.load(file)

pd.set_option('display.max_columns', None)


print(data[['Территория государства', 'Население']])
# print(data.info())
