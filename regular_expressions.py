# Примеры регулярных выражений для тренировки

import re

string = "DASGDHAJ$#^@374389ajksdhEWHk7832"

# pattern = r"\d"
# pattern = r"\d+"
pattern = r"\d{3}"

result_1 = re.search(pattern, string)
result_2 = re.findall(pattern, string)

print(result_1)  # <re.Match object; span=(12, 15), match='374'>
print(result_1[0])  # 374

print(result_2)  # ['374', '389', '783']
