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
    q = deque()
    visited = set()
    distances = {} # 這個字典在你的實現中其實不是必需的，因為距離資訊已經在佇列的元組中了，但保留它也無妨

    q.append((start_station, 0))
    visited.add(start_station)
    # distances[start_station] = 0 # 如果不使用 distances 字典來儲存距離，這行可以省略。我們透過佇列中的元組來傳遞距離。

    while q:
        current_station, current_distance = q.popleft()

        if current_station == target_station:
            return current_distance

        for next_station in graph[current_station]:
            # 修正 1: 判斷是否訪問過，並將「未訪問過」的節點加入佇列和 visited 集合
            if next_station not in visited: # 原本是 next_station in visited: continue，這樣寫更直接
                visited.add(next_station)
                # 修正 2: 將「next_station」加入佇列，而不是 current_station
                # 同時更新 distances 字典時，鍵應該是 next_station，值是新的距離
                q.append((next_station, current_distance + 1))
                # distances[next_station] = current_distance + 1 # 如果不使用 distances 字典，這行可以省略
    
    # 如果迴圈結束都沒找到目標，表示無法到達
    return -1

# 測試你的函數
start_station = 'A'
target_station = 'G'
min_transfers = find_min_transfers(graph, start_station, target_station)
print(f"從 {start_station} 到 {target_station} 的最少轉乘次數是：{min_transfers}")

# 你可以試試看其他路徑，例如 A 到 F
start_station_2 = 'A'
target_station_2 = 'F'
min_transfers_2 = find_min_transfers(graph, start_station_2, target_station_2)
print(f"從 {start_station_2} 到 {target_station_2} 的最少轉乘次數是：{min_transfers_2}")

# 測試無法到達的路徑 (假設沒有路徑從 A 到 Z)
start_station_3 = 'A'
target_station_3 = 'Z'
min_transfers_3 = find_min_transfers(graph, start_station_3, target_station_3)
print(f"從 {start_station_3} 到 {target_station_3} 的最少轉乘次數是：{min_transfers_3}")