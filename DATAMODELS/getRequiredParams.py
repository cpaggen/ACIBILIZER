import os
import re
from mappings import ansibleToClass
from collections import Counter

def get_file_paths(dir):
    py_files = [] # save files
    for file in os.listdir(dir):
        file_path = str(dir) + r'/' + str(file)
        py_files.append(file_path)
    return py_files

def get_config_map_list(c_map):
    out = []
    for config in c_map:
        result = config.split(",")
        for i in result:
            out.append(i.strip().split("="))
    return out

def to_dict(list):
    out = {}
    for i in list:
        try:
            out[i[0]] = i[1]
        except:
            pass
    return out

def get_config_map(dir):
    py_files = get_file_paths(dir)
    out = {}

    # Regex to capture the content inside argument_spec.update()
    pattern = re.compile(r'argument_spec\.update\(\s*(.*?)^\s*\)', re.DOTALL | re.MULTILINE)


    for file_path in py_files:
        with open(file_path, 'r') as file:
            file_content = file.read()

        matches = pattern.findall(file_content)

        if matches:
            config_list = []
            for match in matches:
                # Find all dictionary assignments within the match
                dict_matches = re.findall(r'(\w+)=dict\(', match)
                config_list.extend(dict_matches)

            if config_list:
                out[file_path.split("/")[-1][:-3]] = config_list

    return out

b = get_config_map("/Users/lpaggen/Documents/research_project/ansible-aci/modules")

def extract_required_if(dir):
    py_files = get_file_paths(dir)
    out = {}
    
    pattern = re.compile(r'"state",\s*"present",\s*\[([^\]]+)\]')

    for file_path in py_files:
        with open(file_path, 'r') as file:
            file_content = file.read()

        match = pattern.search(file_content)

        if match:
            required_list = match.group(1).strip().replace('"', '').replace("'", '').split(", ")
            required_items = [item.strip() for item in required_list]
            out[file_path.split("/")[-1][:-3]] = required_items

    return out

c = extract_required_if("/Users/lpaggen/Documents/research_project/ansible-aci/modules")

def get_overlap(dict1, dict2): # pass in the full dict at 1, required in 2
    overlap = {}
    for key, value in dict1.items():
        try:
            c1 = Counter(value)
            c2 = Counter(dict2[key])
            overlap[key] = c1 + c2 # check if overlap (overlap means param is required)
        except(KeyError):
            # print(f"KEY '{key}' NOT PRESENT IN DICT2")
            pass
        
    return overlap

x = get_overlap(b, c)

def add_required_flag(dict1, overlap):            
    for key, value in overlap.items():
        idx = 0 # reset every time switch keys (dict -> value = list)
        for param in value:
            try:
                if value[param] == 2: # 2 means parameter is required
                    dict1[key][idx] = str(dict1[key][idx]) + "*"
                idx += 1

            except(KeyError):
                # print(f"KEY '{key}' NOT PRESENT IN OVERLAP")
                pass

    return dict1

h = add_required_flag(b, x)
