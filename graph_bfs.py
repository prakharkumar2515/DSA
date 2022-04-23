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
  q.append(source)
  
  while q:
    current = q.popleft()
    print(q)
    
    # Add all braches of current node to Queue
    for neigh in graph[current]:
      q.append(neigh)
