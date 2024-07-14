import pprint
import json

PATH_TO_META = "aci-meta-5.3-2c.json"

def getClassRnFormat(dir):

    with open(dir, 'r') as file:
        data = json.load(file)

    out = {}

    def process_data(data, parent_key = None):
        if isinstance(data, dict):
            for key, value in data.items():

                if key == "rnFormat":
                    out[parent_key] = value if len(value) > 0 else None

                if isinstance(value, (dict, list)):
                    process_data(value, key if parent_key is None else key)

        elif isinstance(data, list):
            for item in data:
                if isinstance(item, (dict, list)):
                    process_data(item, parent_key)

    process_data(data)

    return out

if __name__ == "main":

    out = getClassRnFormat(PATH_TO_META)

    # save to file
    with open("classRnFormat.py", 'w') as file:
        file.write("rnFormat = ")
        pprint.pprint(out, stream=file)

    print(f"Dictionary has been saved to classRnFormat.py")
