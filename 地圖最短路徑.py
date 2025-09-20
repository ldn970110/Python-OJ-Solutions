from collections import deque

def find_shortest_path_in_grid(grid, start_char='S', end_char='E'): # 修正 1: 增加 start_char 和 end_char 參數
    rows = len(grid)
    cols = len(grid[0])

    # 1. 找出起點和終點的實際座標
    start_pos = None
    end_pos = None
    for r_idx in range(rows): # 使用 r_idx, c_idx 避免與 r, c 變數名衝突
        for c_idx in range(cols):
            if grid[r_idx][c_idx] == start_char:
                start_pos = (r_idx, c_idx)
            if grid[r_idx][c_idx] == end_char: # 這裡的 if 不需要 elif，因為 S 和 E 可能在不同地方
                end_pos = (r_idx, c_idx)
    
    # 檢查起點或終點是否存在
    if not start_pos or not end_pos:
        print("錯誤：未找到起點或終點字符 ('S' 或 'E')！")
        return -1

    # 2. BFS 初始化
    q = deque()
    # 佇列中存放的元素是 (row, col, distance)
    q.append((start_pos[0], start_pos[1], 0))

    # 修正 2: 將 visited 初始化為 set()
    visited = set()
    visited.add(start_pos) # 將起點標記為已訪問

    # 定義方向向量 (上, 下, 左, 右)
    dr = [-1, 1, 0, 0] # row 的變化
    dc = [0, 0, -1, 1] # col 的變化

    # 3. BFS 核心迴圈
    while q:
        current_r, current_c, current_distance = q.popleft()
        
        # 如果當前格子就是終點，則回傳其距離
        if (current_r, current_c) == end_pos:
            return current_distance

        # 探索所有鄰居
        for i in range(4): # 遍歷四個方向
            next_r = current_r + dr[i]
            next_c = current_c + dc[i]

            # 修正 3: 將所有檢查條件和添加邏輯放入 for 迴圈內部
            # 檢查新座標是否合法：
            # 1. 是否在網格邊界內 (0 <= next_r < rows and 0 <= next_c < cols)
            # 2. 是否不是牆壁 (grid[next_r][next_c] != '#')
            # 3. 是否尚未被訪問過 ((next_r, next_c) not in visited)
            if (0 <= next_r < rows and 
                0 <= next_c < cols and 
                grid[next_r][next_c] != '#' and
                (next_r, next_c) not in visited): 
                
                visited.add((next_r, next_c)) # 將新的合法鄰居標記為已訪問
                q.append((next_r, next_c, current_distance + 1)) # 將新鄰居及其距離加入佇列

    # 如果佇列為空，但仍未找到終點，表示無法從起點到達終點
    return -1

# 測試用例
grid = [
    ['S', '.', '.', '#', '.'],
    ['.', '#', '.', '.', '.'],
    ['.', '.', '.', '#', '.'],
    ['#', '.', '.', '.', '.'],
    ['.', '.', '#', '.', 'E']
]

# 呼叫修正後的函式
result = find_shortest_path_in_grid(grid, 'S', 'E')
print(f"從 'S' 到 'E' 的最少移動步數是: {result}") # 預期輸出應該是 7

# 測試無法到達的路徑
grid_unreachable = [
    ['S', '#'],
    ['#', 'E']
]
result_unreachable = find_shortest_path_in_grid(grid_unreachable, 'S', 'E')
print(f"從 'S' 到 'E' 的最少移動步數 (無法到達) 是: {result_unreachable}") # 預期輸出是 -1

# 測試沒有 S 或 E 的情況
grid_no_se = [
    ['.', '.', '.'],
    ['.', '.', '.'],
    ['.', '.', '.']
]
result_no_se = find_shortest_path_in_grid(grid_no_se, 'S', 'E')
print(f"找不到起點或終點: {result_no_se}") # 預期輸出是 -1