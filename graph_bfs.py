# Traverse Graph with Breadth First using Stack

graph = {
    "a" : ["b", "c"],
    "b" : ["d"]
}

def bfs(graph, source):
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
  
  # define queue
  q = collections.deque()
  visited = set()
  q.append(source)
  
  while q:
    current = q.popleft()
    print(q)
    visited.add(current)
    
    # Add all braches of current node to Queue
    for neigh in graph[current]:
      if neigh not in visited:
        q.append(neigh)
