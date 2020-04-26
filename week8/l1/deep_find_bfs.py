graph = {'A': ['B', 'C'],
         'B': ['D', 'E'],
         'C': [],
         'D': [],
         'E': ['F'],
         'F': {'M': ['P', 'N'], 'P': [], 'N': []}}


def deep_find(graph, key):
    visited = []
    queue = []
    res = None

    def bfs(visited, graph, node):
        nonlocal res
        visited.append(node)
        queue.append(node)
        if isinstance(graph[node], dict):
            bfs(visited, graph[node], list(graph[node].keys())[0])
        if len(queue) == 0:
            return
        s = queue.pop(0)
        if key == node:
            res = graph[key]
            return
        for neighbour in graph[s]:
            if neighbour not in visited:
                bfs(visited, graph, neighbour)
                # visited.append(neighbour)
                # queue.append(neighbour)

    bfs(visited, graph, 'A')
    return res


print(deep_find(graph, 'D'))

'''


def deep_find(graph, key):
    visited = []
    queue = []

    def bfs(visited, graph, node):
        visited.append(node)
        queue.append(node)

        while queue:
            s = queue.pop(0)
            print(s, end=" ")

            for neighbour in graph[s]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)
    bfs(visited, graph, 'A')


print(deep_find(graph, 'A'))
'''