import numpy as np

def populate_forest(forest,input):
    for i in range(forest.shape[0]):
        for j in range(forest.shape[1]):
            forest[i,j] = input[i][j]
    return forest

def check_visibility(value,row,column):
    if value > max(row) or value > max(column):
        return True
    else:
        return False

def check_if_edge_value(array,i,j):
    #i = row index, j = column index
    if i == 0 or i == array.shape[0]-1:
        return True
    if j == 0 or j == array.shape[1]-1:
        return True
    else:
        return False

def calculate_scenic_score(array,i,j):

    def check_direction(list,value):
        if value > max(list):
            visibility = len(list)
        else:
            visibility = np.where(list >= value)[0][0]+1
        return visibility        

    #check north
    if i == 0:
        N = 0
    else:
        N = check_direction(np.flip(array[0:i,j]),array[i,j])        

    #check east
    if j == 0:
        E = 0
    else:
        E = check_direction(np.flip(array[i,0:j]),array[i,j])   

    #check south
    if i == array.shape[0]-1:
        S = 0
    else:
        S = check_direction(array[i+1:,j],array[i,j])   

    #check west
    if j == array.shape[1]-1:
        W = 0
    else:
        W = check_direction(array[i,j+1:],array[i,j]) 

    return N * S * E * W

input = open('.\Desktop\AoC\AoC8\input.txt','r').read().splitlines()

forest = np.zeros([len(input),len(input[0])],dtype=int)
forest = populate_forest(forest,input)

count = 0
scenic_score = 0

for i in range(forest.shape[0]):
    for j in range(forest.shape[1]):
        if check_if_edge_value(forest,i,j):
            count = count + 1
            continue
        if check_visibility(forest[i,j],forest[0:i,j],forest[i,0:j]):
            count = count + 1
            continue
        if check_visibility(forest[i,j],forest[i+1:,j],forest[i,j+1:]):
            count = count + 1
            continue

for i in range(forest.shape[0]):
    for j in range(forest.shape[1]):
        temp = calculate_scenic_score(forest,i,j)
        if temp > scenic_score:
            scenic_score = temp

print('Trees visible outside the grid:', count)
print('Highest possible scenic score:', scenic_score)