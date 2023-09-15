from queue import PriorityQueue

# Dictionary used to improve recovery speed for less runtime and better way of storing path cost
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'C': 2, 'D': 3},
    'C': {'E': 5},
    'D': {'F': 2, 'G': 4},
    'E': {'G': 3},
    'F': {'G': 1},
    'G': {'':0},
}

'''h(B) has a value of 4 because the minimum value from A to G is 5 
and f(B) cannot be more than 5. Hence, h(B) is 4 since s(B) is 1
'''

h_value = {
    'A': 5,
    'B': 4,
    'C': 4,
    'D': 3,
    'E': 3,
    'F': 1,
    'G': 0,
}


def dfs(graph, start):
    end = 'G' # This dfs has a fixed goal per the question
    visited = []
    stack = [start]

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            if node == end:
                break

        siblings = graph[node].keys() # Represent letter values of child nodes as an iterable
        stack.extend(siblings - set(visited))
    
    return visited



def all_paths(graph, start, end, path=[]):
    path = path + [start]

    if start == end:
        print(path)
        return [path]
    if start == '':
        return []
    
    for sib in graph[start].keys():
        all_paths(graph, sib, end, path)


def greedy(graph, start, end):
    visited = []
    pq = PriorityQueue()
    pq.put((0, start))


    while pq:
        priority_value, node = pq.get() # remove both priority value and node value

        if node not in visited:
            visited.append(node)
            if node == end:
                break
            else:
                compare = PriorityQueue() # Prioritize shorter path amongst neighbours

                for neighbour in graph[node].keys():
                    if neighbour not in visited:
                        compare.put((graph[node][neighbour], neighbour)) # Arrange neighbors based on cost
                
                pq.put(compare.get())
    
    return visited


def a_star(graph, start, end, h_value):
    visited = []
    pq = PriorityQueue()
    pq.put((0 + h_value[start], start)) # Make use of both the path cost and the heuristic value


    while pq:
        priority_value, node = pq.get() # remove both priority value and node value

        if node not in visited:
            visited.append(node)
            if node == end:
                break
            else:
                compare = PriorityQueue() # Prioritize shorter path amongst neighbours

                for neighbour in graph[node].keys():
                    if neighbour not in visited:
                        compare.put((graph[node][neighbour] + h_value[neighbour], neighbour)) # Arrange neighbors based on cost
                
                pq.put(compare.get())
    
    return visited

print("DFS:")
start_node = input("Enter a starting node: ").upper() # take user input for starting node
print(dfs(graph, start_node))
print()

print("All paths")
all_paths(graph, 'A', 'G')
print()

print("Greedy best first search")
print(greedy(graph, 'A', 'G'))
print()

print("A* search")
print(a_star(graph, 'A', 'G', h_value))