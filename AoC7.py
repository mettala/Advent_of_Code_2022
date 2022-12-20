import numpy as np

def update_location(r,location):
    # function updates the current location within the nested dictionary
    if r[0:4] == '$ cd':
        if r[-1] == '/':
            location = []
        if r[-1] == '.':
            if len(location) == 1:
                print('here ',location)
                location = location['/']
                print(location)
            else:
                location = location[:-1]
        else:
            location.append('dir '+r[r.rindex(' ')+1:])
    return location

def get_value(tree, location):
    for key in location:
        tree = tree[key]
    return tree

def set_value(tree, location, value):
    # sets value within nested dictionary according to location list
    for key in location[:-1]:
        tree = tree.setdefault(key, {})
    tree[location[-1]] = value

def get_dict_sizes(tree, limit = 100_000, sum = 0, accepted_dicts = [], all_dicts= []):
    # function returns two lists of dictionary sizes. One containing only dicts where size <= limit and one containing all dictionaries
    for key, value in tree.items():
        if isinstance(value, dict):
            dict_sum, accepted_dicts, all_dicts = get_dict_sizes(value, accepted_dicts = accepted_dicts, all_dicts = all_dicts)
            sum = sum + dict_sum
            all_dicts.append(dict_sum)
            if dict_sum <= limit:
                accepted_dicts.append(dict_sum)
        else:
            sum = sum + value
    return sum, accepted_dicts, all_dicts

def sum_files(tree, total_file_sum = 0):
    # function calculates the total sum of all files inside the nested dictionary
    for _, value in tree.items():
        if isinstance(value, dict):
            total_file_sum = sum_files(value, total_file_sum = total_file_sum)
        else:
            total_file_sum = total_file_sum + value
    return total_file_sum

input = open('.\Desktop\AoC\AoC7\input.txt','r').read().splitlines()

tree = dict()
location = []

for r in input:
    location = update_location(r,location)
    if r[0:4] == '$':
        location = update_location(r,location)
    if r[0:3] == 'dir':
        set_value(tree,location+['dir '+r[r.rindex(' ')+1:]],{})
    if r[0].isnumeric():
        value = int(r.split()[0])
        set_value(tree,location+[r[r.rindex(' ')+1:]],value)

_, accepted_dicts, all_dicts = get_dict_sizes(tree)

print('The total size of accepted directories: ',sum(accepted_dicts))
all_files = sum_files(tree)
print('The total size of all files:', all_files)
space_needed = 30_000_000 - (70_000_000 - all_files)
print('How much more space is needed: ',space_needed)
all_dicts = np.array(all_dicts)
all_dicts.sort()
print('Smallest dictionary size to delete to meet the requirement: ',all_dicts[(np.where(all_dicts >= space_needed)[0][0])])