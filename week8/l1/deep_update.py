from copy import deepcopy

graph = {'A': ['B', 'C'],
         'B': ['D', 'E'],
         'C': [],
         'D': [],
         'E': ['F'], 'F': {'M': ['P', 'N'], 'P': [], 'N': []}}

def deep_update(data, key, value):
    def inner(data, key, value, temp_dict, first=False):
        if first is True:
            temp_dict = deepcopy(data)
        if len(temp_dict) == 0:
            return data
        if isinstance(temp_dict[list(temp_dict.keys())[0]], dict) and key != list(temp_dict.keys())[0]:
            inner(data, key, value, temp_dict[list(temp_dict.keys())[0]])
        if key == list(temp_dict.keys())[0]:
            data[key] = value
        del temp_dict[list(temp_dict.keys())[0]]
        inner(data, key, value, temp_dict)
    inner(data, key, value, None, True)
    return data


graph = deep_update(graph, 'N', ['123'])
print(graph)