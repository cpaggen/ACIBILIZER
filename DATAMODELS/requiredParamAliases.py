from requiredParamsMap import requiredParamsMap
from paramAliasMap import paramAliasesMap
import pprint

def add_required_flags(param_aliases, required_params):
    for key, required_list in required_params.items():
        if key in param_aliases:
            for param in required_list:
                if param.endswith('*'):
                    stripped_param = param.rstrip('*')
                    if stripped_param in param_aliases[key]:
                        if param_aliases[key][stripped_param] is None:
                            param_aliases[key][stripped_param] = []
                        param_aliases[key][param] = param_aliases[key].pop(stripped_param)
                        
    return param_aliases

out = add_required_flags(paramAliasesMap, requiredParamsMap)

with open("requiredParamsAliases.py", 'w') as file:
        file.write("requiredParamsAliases = ")
        pprint.pprint(out, stream = file)

print("Dictionary has been saved to {requiredParamsAliases.py}")
