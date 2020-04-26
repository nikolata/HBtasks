graph = {'A': ['B', 'C'],
         'B': ['D', 'E'],
         'C': ['F'],
         'D': [],
         'E': [],
         'F': {'M': ['P', 'N'], 'P': [], 'N': []}}


def deep_find(graph, key):
    result = None

    def dfs(graph, start, visited=None, found_one=False):
        if visited is None:
            visited = set()
            nonlocal result
        print(start)
        if isinstance(graph[start], dict):
            dfs(graph[start], list(graph[start].keys())[0], None)
        if result is not None:
            return
        visited.add(start)
        for next in graph[start]:
            if key == next or key in visited:
                result = graph[key]
                found_one = True
                break
            elif found_one is False:
                dfs(graph, next, visited)
    dfs(graph, list(graph.keys())[0])
    return result


result = deep_find(graph, 'F')
print(result)
