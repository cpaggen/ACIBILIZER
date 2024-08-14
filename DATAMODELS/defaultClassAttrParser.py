import os
import json
import pprint

# In this case, follow the order -> fv, vz ... (add more later)
PATH_TO_JSON_DATA = ["fvClasses/", "vzClasses/"]

# This script allows to get a dictionary containing all default attribute values for classes
# Its use is to determine which attributes to delete entirely when rebuilding yml playbooks

def parse_attr_defaults(directories):
    out = {}  # Output dictionary
    
    yml_bool_list = ['false', 'False', 'off', 'Off', 'No', 'no', 'true', 'True', 'on', 'On', 'Yes', 'yes']
    yml_bool_map = {
        'false': 'no',  # Should cover all boolean cases
        'off': 'no',
        'False': 'no',
        'Off': 'no',
        'No': 'no',
        'true': 'yes',
        'on': 'yes',
        'True': 'yes',
        'On': 'yes',
        'Yes': 'yes'
    }

    for path in directories:
        prefix = path[:2]
        for file in os.listdir(path):  # Read from the JSON file
            entry_dict = {}  # Serves as nested dict in "out"
            file_path = os.path.join(path, file)
            with open(file_path, 'r') as file_:
                data = json.load(file_)
                
                # Determine the class name based on the prefix
                if file.split(".")[0][:2] == prefix:
                    className = prefix + ":" + file.split(".")[0][2:]
                else:
                    className = prefix + ":" + file.split(".")[0]  # Gets the fv:xxxx format in the JSON

                for key, value in data[className]['properties'].items():
                    try:
                        result = data[className]['properties'][key]["default"]
                        if data[className]['properties'][key]["default"] in yml_bool_list:  # yml -> "true" == "yes", etc
                            result = yml_bool_map[data[className]['properties'][key]["default"]]
                        entry_dict[key] = str(result)  # Sets value to default
                    except KeyError:
                        entry_dict[key] = ""

            out[className.replace(":", "")] = entry_dict

    return out

if __name__ == "__main__":

    out = parse_attr_defaults(PATH_TO_JSON_DATA)

    # Save to file
    with open("defaultClassAttrValues.py", 'w') as file:
        file.write("defaults = ")
        pprint.pprint(out, stream=file)

    print(f"Dictionary has been saved to defaultClassAttrValues.py")