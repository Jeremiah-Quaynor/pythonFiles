""""
    Implement a 10x10 grid that contains a starting point (0,0), to a dilivery point of (9,9) and the following
    obstacles are on locations (9,7), (8,7), (6,7), (6,8).

    Your algorithm should calculate a valid path avoiding the obstacles and reaching the delivery point.

    Your solution should print the path in this format [(x1,x2), (y1,y2)...] and also the number of steps.
"""

def valid_path(grid = 10, start_point = (0,0), delivery_point = (9,9), obstacle_points = [(9,7),(8,7),(6,7),(6,8)]):
    # initializing variables 
    valid_points = [start_point]
    prev_points = {}
    directions = [(1,1),(1,0),(1,-1),(0,1),(0,-1)]

    for cur_point in valid_points:
        if valid_points[-1] == delivery_point:
            break
        for direction in directions:
            next_point = (cur_point[0] + direction[0], cur_point[1] + direction[1])
            if next_point in obstacle_points or next_point in valid_points:
                continue
            if next_point[0] < 0 or next_point[0] > (grid -1):
                continue
            if next_point[1] < 0 or next_point[1] > (grid -1):
                continue

            valid_points.append(next_point) 
            prev_points[next_point] = cur_point
    
    path = [delivery_point]
    while path[-1] != start_point:
        path.append(prev_points[path[-1]])
    
    return path

print(valid_path())