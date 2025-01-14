import json

f = open('data.json')
file = json.load(f)

#print(file['Info'])

#for key, value in file.items():
#    print(f"{key[0]}: {value[0]}")
#    print(f"{key[1]}: {value[1]}")

#print(file['Info'])
#print()

for i in 0,1:
    print(f"ID: {file['Info'][i]['ID']}")
    print(f"Name: {file['Info'][i]['Name']}") 
    print(f"Mobile Number: {file['Info'][i]['Mobile Number']}") 
    print(f"Address:")
    print(f"    State: {file['Info'][i]['Address']['State']}")
    print(f"    Country: {file['Info'][i]['Address']['Country']}")
    print()
'''
print(f"Name: {file['Info'][0]['Name']}")
print(f"Mobile Number: {file['Info'][0]['Mobile Number']}")
print(f"Address: ")
print(f"    State: {addr['State']}")
print(f"    Country: {addr['Country']}")
print("**********************************************")
print(f"Name: {file['Info'][1]['Name']}")
print(f"Mobile Number: {file['Info'][1]['Mobile Number']}")
print(f"Address: ")
print(f"    State: {addr1['State']}")
print(f"    Country: {addr1['Country']}")
'''