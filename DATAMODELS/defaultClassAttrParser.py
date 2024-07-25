import os
import json
import pprint

PATH_TO_JSON_DATA = ""

# this script allows to get a dictionary containing all default attribute values for classes
# its use is to determine which attributes to delete entirely when rebuilding yml playbooks

def parse_attr_defaults(dir):
    out = {} # output
    
    yml_bool_list = ['false', 'False', 'off', 'Off', 'No', 'true', 'True', 'on', 'On', 'Yes']

    yml_bool_map = {'false': 'no', # should cover all boolean cases (?)
                    'off': 'no',
                    'False': 'no',
                    'Off': 'no',
                    'No': 'no',
                    'true': 'yes',
                    'on': 'yes',
                    'True': 'yes',
                    'On': 'yes'}

    for file in os.listdir(dir): # read from the json file
        entry_dict = {} # serves as nested dict in "out"
        file_path = os.path.join(dir, file)
        with open(file_path, 'r') as file_:
            try:
                data = json.load(file_)
            except(json.decoder.JSONDecodeError):
                break
            # will simply need to do a switch to address other prefixes, it is the same logic
            className = "fv:" + file.split(".")[0][2:] # gets the fv:xxxx format in the json
            print(className)
            try:
                for key, value in data[className]['properties'].items():
                    try:
                        result = data[className]['properties'][key]["default"]
                        if data[className]['properties'][key]["default"] in yml_bool_list: # yml -> "true" == "yes", etc
                            result = yml_bool_map[data[className]['properties'][key]["default"]]
                        entry_dict[key] = result # sets value to default
                    except(KeyError):
                        entry_dict[key] = ""
            except(KeyError):
                pass

        out[className.replace(":", "")] = entry_dict
        
    return out

if __name__ == "__main__":

    out = parse_attr_defaults(PATH_TO_JSON_DATA)

    # save to file
    with open("defaultClassAttrValues.py", 'w') as file:
        file.write("defaults = ")
        pprint.pprint(out, stream=file)

    print(f"Dictionary has been saved to defaultClassAttrValues.py")
