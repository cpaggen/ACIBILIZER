import os
import json
import pprint

PATH_TO_JSON_DATA = ""

# this script allows to get a dictionary containing all default attribute values for classes
# its use is to determine which attributes to delete entirely when rebuilding yml playbooks

def parse_attr_defaults(dir):
    out = {} # output

    for file in os.listdir(dir): # read from the json file
        entry_dict = {} # serves as nested dict in "out"
        file_path = os.path.join(dir, file)
        with open(file_path, 'r') as file_:
            data = json.load(file_)
            className = "fv:" + file.split(".")[0] # gets the fv:xxxx format in the json
            for key, value in data[className]['properties'].items():
                try:
                    entry_dict[key] = data[className]['properties'][key]["default"] # sets value to default
                except(KeyError):
                    entry_dict[key] = None
                    
        out[className.replace(":", "")] = entry_dict
        
    return out

if __name__ == "__main__":
    out = parse_attr_defaults(PATH_TO_JSON_DATA)

    # save to file
    with open("defaultClassAttrValues.py", 'w') as file:
        file.write("defaults = ")
        pprint.pprint(out, stream=file)

    print(f"Dictionary has been saved to defaultClassAttrValues.py")
