import os
import re
import pprint

PATH_TO_MODULE_DIR = ""

def get_file_paths(dir):
    py_files = []
    for file in os.listdir(dir):
        file_path = os.path.join(dir, file)
        if file.endswith(".py"):
            py_files.append(file_path)
    return py_files

# code is bad at the moment, will address if needed, for the time being it runs well enough

def extract_parameter_aliases(dir):
    py_files = get_file_paths(dir)
    out = {}

    # regex 
    pattern = re.compile(r'argument_spec\.update\(\s*(.*?)^\s*\)', re.DOTALL | re.MULTILINE)
    pattern2 = re.compile(r"([a-zA-Z_]+)\s*=\s*dict", re.MULTILINE)
    pattern3 = re.compile(r"([a-zA-Z_]+)\s*=\s*dict\s*\((.*?)\)", re.DOTALL)
    pattern4 = re.compile(r'(?<=aliases=\[)([^\]]*)', re.DOTALL | re.MULTILINE)

    for file_path in py_files:
        with open(file_path, 'r') as file:
            file_content = file.read()

        matches = pattern.findall(file_content)

        entry_dict = {}  # nested dict

        for entries_str in matches:
            match2 = pattern2.findall(entries_str) # list of the parameters
            match3 = pattern3.findall(entries_str)

            if match3:
                for idx, i in enumerate(match3): # get idx to find correspondance in match2
                    match4 = pattern4.findall(str(i)) # need string otherwise error sometimes
                    if match4:
                        for j in match4:
                            entry_dict[match2[idx]] = [i.replace("\"", "").replace(" ", "") for i in j.split(",")] # clean string
                    else:
                        entry_dict[match2[idx]] = None

        print("\n")

        out[file_path.split("/")[-1][:-3]] = entry_dict

    return out

if __name__ == "main":
    out = extract_parameter_aliases(PATH_TO_MODULE_DIR)

        # save to file
    with open("paramAliasesMap.py", 'w') as file:
        file.write("requiredParams = ")
        pprint.pprint(out, stream=file)

    print("Dictionary has been saved to {requiredParamMap.py}")
