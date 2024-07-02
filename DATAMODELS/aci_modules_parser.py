from mappings import classToAnsible
import json
import sys

with open('aci_modules.json', 'r') as f:
    j = json.loads(f.read())

for mods in j:
    for k,v in mods.items():
        module  = k
        print(f"{module}:[")
        options = v['doc']['options']
        for k,v in options.items():
            option     = k
            optionType = v['type']
            isRequired = ''
            try:
                if v['required']:
                    isRequired = '*'
            except KeyError:
                pass
            
            print(f"{option}: {optionType},")
        print('],')

json_data = {}

for mods in j:
    for k,v in mods.items():
        options = v['doc']['options']      
        optList = []
        optDict = {}  
        for kp, vp in options.items():
            optDict[kp] = {
                "name": kp,
                "type": vp['type'],
                }
            optList.append(optDict[kp])
        json_data[k] = optList

json_string = json.dumps(json_data)
print(json_string)
