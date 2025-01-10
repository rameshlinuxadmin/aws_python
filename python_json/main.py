'''
import json

f = open('data.json')

x = json.load(f)

for i in x['marvel']:
    print(i)

f.close()

import json

# Open and read the JSON file
with open('data.json', 'r') as file:
    data = json.load(file)

# Print the data
print(data)

import json

# Opening JSON file
f = open('data.json')

# returns JSON object as a dictionary
data = json.load(f)

# Iterating through the json list
for i in data['emp_details']:
    print(i)

# Closing file
f.close()
'''

import json

# Opening JSON file
f = open('data.json')

# returns JSON object as a dictionary
data = json.load(f)

# Iterating through the json list
for i in data['marvel']:
    print(f" Name of Ironman is {i['Ironman']}")
    print(f" Name of Captain America is {i['Captain America']}")

# Closing file
f.close()