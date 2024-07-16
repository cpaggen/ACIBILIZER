import os
import re
import pprint

PATH_TO_MODULES = ""

def get_file_paths(dir):
    py_files = [] # save files
    for file in os.listdir(dir):
        file_path = str(dir) + r'/' + str(file)
        py_files.append(file_path)
    return py_files

def get_exception_list(dir):

    py_files = get_file_paths(dir)
    
    out = {}

    for file_path in py_files:
        with open(file_path, 'r') as file:
            file_content = file.read()

        # regex patterns to find block of code within "child_config[]"
        pattern = r'child_configs\s*=\s*\[(.*?)\]'
        match = re.search(pattern, file_content, re.DOTALL)

        if match:
            extracted_content = match.group(1)

            # pattern to find all variables in quotes, and all variables not in quotes - per line
            quotes_pattern = re.compile(r'"([^"]+)"')
            variables_pattern = re.compile(r'\b\w+\b')

            entry_dict = {}  # nested dictionary 

            for line in extracted_content.split('\n'):
                stripped_line = line.strip()

                # skipping empty lines in match
                if not stripped_line:
                    continue

                quoted_strings = quotes_pattern.findall(line)

                all_words = variables_pattern.findall(line)
                non_quoted_vars = [word for word in all_words if word not in quoted_strings]

                # construct nested dictionaries, if more than 1 variable, just save both
                if len(non_quoted_vars) == 1 and len(quoted_strings) == 3:
                    entry_dict[non_quoted_vars[0]] = quoted_strings[0] + "[" + quoted_strings[-1] + "]"

                elif len(non_quoted_vars) == 2 and len(quoted_strings) == 4:
                    entry_dict[non_quoted_vars[0]] = quoted_strings[0] + "[" + quoted_strings[-2] + "]"
                    entry_dict[non_quoted_vars[1]] = quoted_strings[0] + "[" + quoted_strings[-1] + "]"

            out[file_path.split("/")[-1][:-3]] = entry_dict if entry_dict else None

        else: # find no match in the files (due to structure sometimes, double check)
            out[file_path.split("/")[-1][:-3]] = None

    return out

if __name__ == "main":
    
    out = get_exception_list(PATH_TO_MODULES)

    # save to file
    with open("exceptionDict.py", 'w') as file:
        file.write("exceptions = ")
        pprint.pprint(out, stream=file)

    print(f"Dictionary has been saved to exceptionDict.py")
