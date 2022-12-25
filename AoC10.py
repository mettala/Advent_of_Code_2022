def check_cycle(cycle, value, x, sum):
    x = x + value
    if  cycle == 20 or (cycle > 20 and (cycle-20) % 40 == 0):
        sum = sum + x * cycle
    return x, sum

def add_pixel_row(pixels):
    pixels.append('')
    return pixels

def add_pixel(pixels,cycle,x):
    if x - 1 <= cycle and cycle <= x + 1:
        pixel = '#'
    else:
        pixel = '.'
    pixels[-1] = pixels[-1] + pixel
    return pixels

def add_cycle(cycle, pixels):
    cycle = cycle + 1
    if cycle % 41 == 0:
        pixels = add_pixel_row(pixels)
        cycle = 1    
    return cycle, pixels

input = open('.\\Desktop\\AoC\\AoC10\\input.txt','r').read().splitlines()

cycle = 1
x = 1
sum = 0

for r in input:
    cycle = cycle + 1
    if r == 'noop':
        x, sum = check_cycle(cycle, 0, x, sum)
        continue
    x, sum = check_cycle(cycle, 0, x, sum)
    cycle = cycle + 1
    _, value = r.split(' ')
    x, sum = check_cycle(cycle, int(value), x, sum)

print('sum of signal strengths:',sum)

pixels = ['']
x = 1
cycle = 1

for r in input:
    pixels = add_pixel(pixels,cycle,x)
    cycle, pixels = add_cycle(cycle,pixels)

    if r != 'noop':        
        _, value = r.split(' ')
        x = x + int(value)
        pixels = add_pixel(pixels,cycle,x)
        cycle, pixels = add_cycle(cycle,pixels)

for i in pixels: print(i)