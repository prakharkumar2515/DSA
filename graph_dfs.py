# Traverse Graph with Depth First using Stack

graph = {
    "a" : ["b", "c"],
    "b" : ["d"]
}

def dfs(graph, source):
  '''
  Input : 
    graph : 
            {
                "a" : ["b", "c"],
                "b" : ["d"]
            }
    source : A graph Node
  Output : None
    Prints value of each node
  '''
  # define stack
  s = [source]

  # Adding visited to avoid infine loop in cyclic graph
  visited = set()
  
  while s != []:
    current = s.pop()
    print(current)
    visited.add(current)
  
    # Add all nodes connect to above node in stack
    for n in graph[current]:
      if n not in visited: # checking for cyclic graph
        s.append(n)

# Traversing graph using recurrsion

def dfs_recur(graph, source, visited=set()): # Time = O(edges), Space = O(Vertex)
  ''' 
  Time = O(edges), Space = O(Vertex)
  
  Input : 
    graph : 
            {
                "a" : ["b", "c"],
                "b" : ["d"],
                "d" : ["a"}
            }
    source : A graph Node
  Output : None
    Prints value of each node
  '''
  if source not in visited:
    print(source)
    visited.add(source)
    
  for i in graph[source]:
    if i not in visited:
      dfs_recur(graph, i, visited)
