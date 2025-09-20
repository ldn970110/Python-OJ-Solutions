from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'G'],
    'F': ['C'],
    'G': ['E']
}



def find_min_transfers(graph, start_station, target_station):
    q=deque()
    visited=set()
    distances = {}

    q.append((start_station,0))
    visited.add(start_station)
    distances[start_station]=0

    while q:
        current_station, current_distance = q.popleft()

        if current_station == target_station :
            return current_distance

        for next_station in graph[current_station]:
            if next_station in visited:
                continue
            else:
                visited.add(next_station)
                q.append((current_station,current_distance+1))
                distances[current_station]=next_station+1

    

start_station = 'A'
target_station = 'G'


stations=['A', 'B', 'C', 'D', 'E', 'F', 'G']     