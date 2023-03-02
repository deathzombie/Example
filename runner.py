import json

code_file = open('main.py', 'r')
Lines = code_file.readlines()

count = 0
# Strips the newline character
dict_to_export = {}

for line in Lines:
    count += 1
    if "=" in line:
        line_split = line.split('=')
        line_split[0] = line_split[0].strip()
        line_split[1] = line_split[1].strip()
        if "+" in line_split[1]:
            dict_to_export[count] = {'var':line_split[0], 'sub_vars': {'var1':line_split[1].split('+')[0], 'var2':line_split[1].split('+')[1]}}
        else:
            dict_to_export[count] = {'var': line_split[0], 'value': line_split[1]}

    if "print" in line:
        line_split[0] = line_split[0].strip()
        line_split[1] = line_split[1].strip()
        dict_to_export[count] = {'print':line_split[0], 'value':line_split[1]}

with open('data.json', 'w') as fp:
    json.dump(dict_to_export, fp)
