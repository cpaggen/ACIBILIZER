import pprint
import json

with open('aci-meta-5.3-2c.json', 'r') as file:
    meta = json.load(file)

# this checks if we find isConfigurable parameter in the aci_meta file, and returns a dictionary with that mapping
def configurable_map(data, parent_key=None):
    def process_data(data = data, parent_key = parent_key, cfg_map = None):
        if cfg_map is None:
            cfg_map = {}

        # no need to check for lists in this case, property we are looking for is not found in nested list
        if isinstance(data, dict):
            for key, value in data.items():
                if key == "isConfigurable":
                    cfg_map[parent_key] = value
                    break # exit loop, no need to look further once we find isConfigurable
                elif isinstance(value, dict):
                    process_data(value, parent_key=key, cfg_map=cfg_map)

        return cfg_map
    
    file_name = 'isConfigurableMap.py'
    
    out = process_data(data = data)

    # save to file
    with open(file_name, 'w') as file:
        file.write("isConfigurableMap = ")
        pprint.pprint(out, stream=file)

    print(f"Dictionary has been saved to {file_name}")
    
    return out

if __name__ == "main":
    configurable_map(meta)
