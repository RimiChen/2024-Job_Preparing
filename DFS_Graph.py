def has_cycle_directed(graph):
    def dfs(v):
        visited[v] = True
        recursion_stack[v] = True
        for neighbor in graph[v]:
            if not visited[neighbor]:
                if dfs(neighbor):
                    ### if neighbor has cycle
                    return True
            elif recursion_stack[neighbor]:
                ### unvisited neighbor was visited
                return True
        ### pop
        recursion_stack[v] = False
        return False
    ### initialize
    visited = {vertex: False for vertex in graph}
    recursion_stack = {vertex: False for vertex in graph}
    
    for vertex in graph:
        if not visited[vertex]:
            if dfs(vertex):
                return True
    return False

# Example usage
graph = {
    'A': ['B'],
    'B': ['C'],
    'C': ['A'],
    'D': ['E'],
    'E': []
}

print(has_cycle_directed(graph))  # Output: True