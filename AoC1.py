import pandas as pd

input_file = open('.\Desktop\AoC\AoC1\input.txt','r')
lines = input_file.readlines()

sums = []
sum = 0

for r in lines:
    if r == ('\n'):
        sums.append(sum)
        sum = 0
    else:
        sum = sum + int(r)

df = pd.DataFrame(sums,columns =['Sums'])

print(df.nlargest(n=1, columns='Sums'))
print(df.nlargest(n=3, columns='Sums').sum())