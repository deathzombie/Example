import json
function = [obj1 := {"func" : "+", "description" : "Add"},
            obj2 := {"func" : "-", "description" : "Subtract"}] 

x = input("Enter char :")

for i in range(0, len(function)):
    if x == function[i]["func"]:
        with open('data.json', 'w') as fp:
            json.dump(function[i], fp)
        
f = open('data.json', 'r')
dat = json.loads(f.read())

print(dat["description"])    
f.close()