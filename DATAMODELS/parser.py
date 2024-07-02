from mappings import classToAnsible
import json
import sys
from pprint import pprint

f          = open('tenant.json', 'r')
mods       = open('aci_modules_parsed.json', 'r')
tenant     = json.loads(f.read())
modsJson   = json.loads(mods.read())
collection = "cisco.aci."
verbose    = 1
noAnsible  = []

recurseMiss = []
recurseHit  = []
def recurseKids(childrenList):
    '''
    arg is a list of 1st-level children [7 elements here] e.g.:

    fvCtx {2}
      attributes
      children [7]
        0 {1}
          leakRoutes {2}
            attributes
            children [4]
              0 {1}
                leakInternalSubnet {2}
                  attributes
                  children [1]
                    leakTo {1}
                      attributes
              1 ..
         1 ..
    '''
    print(f"      recursing through {len(childrenList)} gc")      
    for child in childrenList:
        childName = list(child.keys())[0]
        print(f"        *recurse* child {childName}")
        if childName in classToAnsible:
            childModule = classToAnsible[childName]
            print(f"         *recurse* gc {childName} has ansible {childModule}")
            recurseHit.append(childModule)
            gc = child[childName].values()
            if len(gc) == 2:
                nextChildList = child[childName]["children"]
                recurseKids(nextChildList)
        else:
            print(f"        *recurse MISS* no ansible for {childName}")
            recurseMiss.append(childName)

def collectAttributes(tnAttr):
    for key in list(tnAttr.keys()):
        if tnAttr[key] == "":
            del tnAttr[key]
    return tnAttr

def lookupAnsibleAttr(module,cfgAttr):
    attrList = modsJson[module]
    # list of dicts, each key is a parameter for the ansible module (value is data type)
    for attr in attrList:
        param = list(attr.keys())[0]
        # find the value for the Ansible parameter from the filtered attributes found in config
        if param in cfgAttr.keys():
            print(f"{param}: {cfgAttr[param]}")

def main():
    testAnz    = {}
    tnModule   = collection + classToAnsible['fvTenant']
    tnAttr     = tenant['fvTenant']['attributes']
    filterAttr = collectAttributes(tnAttr)
    lookupAnsibleAttr(tnModule, filterAttr) 
    sys.exit(1)
    tnChildren = tenant['fvTenant']['children']
    recurseKids(tnChildren)

if __name__ == "__main__":
    main()            
