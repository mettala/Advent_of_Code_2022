import string
from collections import Counter

def compare_strings(s1,s2,s3):
    for i in s1:
        if i in s2:
            if i in s3:
                return i
    return "strings don't share char"

input = open('.\Desktop\AoC\AoC3\input.txt','r').read().splitlines()

sum = 0
letters = string.ascii_lowercase + string.ascii_uppercase

for r in input:
    string1 = r[:len(r)//2]
    string2 = r[len(r)//2:]
    for item in string1:
        if item in string2:
            sum = sum + letters.index(item) + 1
            break

print("round one sum: ", sum)

i = 1
combined = []
sum = 0

for r in input:
    combined.append(r)
    if i < 3:
        i = i + 1
    else:
        item = compare_strings(combined[0], combined[1], combined[2])
        sum = sum + letters.index(item) + 1
        i = 1
        combined = []
                

print("round two sum: ", sum)