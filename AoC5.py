import numpy as np

def reset_stack():
    #hard-coded default stack
    stack = np.chararray((56,9))
    stack[:] = '-'
    stack[56-8:56,0]= ['G','W','L','J','B','R','T','D']
    stack[56-3:56,1]= ['C','W','S']
    stack[56-4:56,2]= ['M','T','Z','R']
    stack[56-7:56,3]= ['V','P','S','H','C','T','D']
    stack[56-6:56,4]= ['Z','D','L','T','P','G']
    stack[56-8:56,5]= ['D','C','Q','J','Z','R','B','F']
    stack[56-8:56,6]= ['R','T','F','M','J','D','B','S']
    stack[56-7:56,7]= ['M','V','T','B','R','H','L']
    stack[56-5:56,8]= ['V','S','D','P','Q']
    return stack

def move_crates_CM9000(Stack,Qty,From,To):
    k = 0
    while k < Qty:
        i = 0
        while Stack[i,From-1] != b'-':
            i = i + 1
            if Stack[i,From-1] == b'-':
                i = i - 1
                break
        j = 0
        while Stack[j,To-1] != b'-':
            j = j + 1
        Stack[j,To-1] = Stack[i,From-1]
        Stack[i,From-1] = '-'
        k = k + 1
        i = 0
        j = 0
    return Stack

def move_crates_CM9001(Stack,Qty,From,To):
    i = 0
    while Stack[i,From-1] != b'-':
        i = i + 1
    j = 0
    while Stack[j,To-1] != b'-':
        j = j + 1
    Stack[j:j+Qty,To-1] = Stack[i-Qty:i,From-1]
    Stack[i-Qty:i,From-1] = '-'
    i = 0
    j = 0
    return Stack

input = open('.\Desktop\AoC\AoC5\input.txt','r').read().splitlines()

#part 1
stack = reset_stack()
stack = np.flip(stack,0)
for r in input:
    if r[0:4] == 'move':
        moves = [int(s) for s in r.split() if s.isdigit()]
        stack = move_crates_CM9000(stack,moves[0],moves[1],moves[2])
stack = np.flip(stack,0)
print('CrateMover 9000: \n',stack)

#part 2
stack = reset_stack()
stack = np.flip(stack,0)
for r in input:
    if r[0:4] == 'move':
        moves = [int(s) for s in r.split() if s.isdigit()]
        stack = move_crates_CM9001(stack,moves[0],moves[1],moves[2])
stack = np.flip(stack,0)
print('CrateMover 9001: \n',stack)