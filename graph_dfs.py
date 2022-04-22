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
  while s != []:
    current = s.pop()
    print(current)
  
    # Add all nodes connect to above node in stack
    for n in graph[current]:
      s.append(n)

# Traversing graph using recurrsion

def dfs_recur(graph, source): # Time = O(edges), Space = O(Vertex)
  ''' 
  Time = O(edges), Space = O(Vertex)
  
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
  
  print(source)
  for i in graph[source]:
    dfs_recur(graph, i)
