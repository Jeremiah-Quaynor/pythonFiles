"""
    Add an additional 20 random places and print their locations using the format [(x1,y1),(x2,y2)...].

    The obstacles should not overlap the existing ones and should not be places at the starting points and
    delivery points.
    
    Your algorithm should calculate a valid path avoiding the obstacles and reaching the delivery point.

    Your solution should print the path in the format of [(x1,y1), (x2,y2)...]
"""

import random, math

def randomize_obstacles(length = 20, grid = 10, start_point = (0,0), delivery_point = (9,9)):
    generated_obstacles = []

    while len(generated_obstacles) <= length: 
        x = math.floor(random.random() * (grid -1))
        y = math.floor(random.random() * (grid -1))
        point = (x,y)

        if point not in generated_obstacles and (point != start_point or point != delivery_point):
            generated_obstacles.append((x,y))
    return generated_obstacles


def valid_path(grid = 10, start_point = (0,0), delivery_point = (9,9), obstacle_points = [(9,7),(8,7),(6,7),(6,8)]):
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
    

    path.reverse()
    return path

print(valid_path(grid=10,start_point=(0,0),delivery_point=(9,9),obstacle_points=[(9,7),(8,7),(6,7),(6,8)]+ randomize_obstacles()))