input = open('.\Desktop\AoC\AoC6\input.txt','r').read()

def loop_thrugh_signal(input,type):
    if type == 'message':
        length = 14
    else:
        length = 4
    tester = False
    marker = 0
    while tester == False:
        tester = len(set(input[marker:marker+length])) == len(input[marker:marker+length])
        if tester == True:
            break
        marker = marker + 1
    return marker

marker = loop_thrugh_signal(input,'SoP')
print('marker:',marker+4,' start-of-packet:', input[marker:marker+4])

marker = loop_thrugh_signal(input,'message')
print('marker:',marker+14,' message:', input[marker:marker+14])