def find_last_char(list, input_char):
    output_char = 'something went wrong'
    for i in list:
        if input_char == i[0]:
            output_char = i[-2]
    return output_char

input = open('.\Desktop\AoC\AoC2\input.txt','r').readlines()

outcomes = {'win' : ['A Y\n', 'B Z\n','C X\n'],'lose' : ['A Z\n', 'B X\n','C Y\n'],'draw' : ['A X\n', 'B Y\n','C Z\n']}
additional_points = {'X':1, 'Y':2, 'Z':3}

points = 0

for r in input:
    if r in outcomes['win']: points = points + 6
    if r in outcomes['draw']: points = points + 3
    if r in outcomes['lose']: points = points + 0
    points = additional_points[r[-2]] + points

print("round one points: ", points)

points = 0

for r in input:
    if r[-2] == 'X': points = points + additional_points[find_last_char(outcomes['lose'],r[0])] + 0
    if r[-2] == 'Y': points = points + additional_points[find_last_char(outcomes['draw'],r[0])] + 3
    if r[-2] == 'Z': points = points + additional_points[find_last_char(outcomes['win'],r[0])] + 6

print("round two points: ", points)