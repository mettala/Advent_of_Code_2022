input = open('.\Desktop\AoC\AoC9\input.txt','r').read().splitlines()

location_short = {'H':[0,0],1:[0,0]} #start location is [0,0]
node_path_short = {'H':[[0,0]],1:[[0,0]]}

location_long = {'H': [0,0]}
for i in range(1,9+1):
    location_long[i] = [0,0]

node_path_long = {'H': [[0,0]]}
for i in range(1,9+1):
    node_path_long[i] = [0,0]

def calculate_distance(location_1, location_2):
    i = location_1[0]-location_2[0]
    j = location_1[1]-location_2[1]
    distance = ((i)**2 + (j)**2)**0.5
    return distance, i, j

def calculate_node_location(i,j,node_location):
    if i > 0:
        node_location[0] = node_location[0] + 1 
    if i < 0:
        node_location[0] = node_location[0] - 1 
    if j > 0:
        node_location[1] = node_location[1] + 1 
    if j < 0:
        node_location[1] = node_location[1] - 1
    return node_location

def move_rope(input,node_location,node_path):
    count = 1
    for r in input:
        direction, steps = r.split(' ')
        for _ in range(int(steps)):

            #update head location
            if direction == 'U':
                node_location['H'][0] = node_location['H'][0] + 1 
            if direction == 'D':
                node_location['H'][0] = node_location['H'][0] - 1 
            if direction == 'L':
                node_location['H'][1] = node_location['H'][1] - 1 
            if direction == 'R':
                node_location['H'][1] = node_location['H'][1] + 1
            node_path['H'].append([node_location['H'][0],node_location['H'][1]])

            #update node location(s)
            for k in range(1,len(node_location)):
                if k == 1:
                    distance,i,j = calculate_distance(node_location['H'], node_location[k])
                else:
                    distance,i,j = calculate_distance(node_location[k-1], node_location[k])

                if distance >= 2:
                    node_location[k] = calculate_node_location(i,j,node_location[k])

                if len(node_location) - 1 == k and node_location[k] not in node_path[k]:
                    count = count + 1
                node_path[k].append([node_location[k][0],node_location[k][1]])
    
    return count,node_location,node_path

count, _, _ = move_rope(input, location_short, node_path_short)
print("Short rope's tail's unique locations:",count)

count, _, _ = move_rope(input, location_long, node_path_long)
print("Long rope's tail's unique locations:",count)