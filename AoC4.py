input = open('.\Desktop\AoC\AoC4\input.txt','r').read().splitlines()

def check_if_inside(input1,input2):
    input1 = input1.split('-')
    input2 = input2.split('-')
    if int(input1[0]) >= int(input2[0]) and int(input1[-1]) <= int(input2[-1]):
            return True
    else:
        return False

def check_if_overlap(input1,input2):
    input1 = input1.split('-')
    input2 = input2.split('-')
    if (int(input1[0]) >= int(input2[0]) and int(input1[0]) <= int(input2[-1])) or (int(input1[-1]) >= int(input2[0]) and int(input1[-1]) <= int(input2[-1])):
            return True
    else:
        return False

#input = ['2-4,6-8','2-3,4-5','5-7,7-9','2-8,3-7','6-6,4-6','2-6,4-8']

sum = 0

for r in input:
    r = r.split(',')
    if check_if_inside(r[0],r[1]) or check_if_inside(r[1],r[0]) :
        sum = sum + 1

print('round one sum: ',sum)

sum = 0

for r in input:
    r = r.split(',')
    if check_if_overlap(r[0],r[1]) or check_if_overlap(r[1],r[0]) :
        sum = sum + 1

print('round one sum: ',sum)