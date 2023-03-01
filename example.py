import json
function = [obj1 := {"func" : "+", "description" : 100,"value" : 542.23},
            obj2 := {"func" : "-", "description" : -100,"value" : 5124},] 

x = input("Enter char :")

for i in range(0, len(function)):
    if x == function[i]["func"]:
        with open('data.json', 'w') as fp:
            json.dump(function, fp)
        


