import random
from itertools import combinations
file = open("test.txt","w")
for i in range (100):
    line = str(random.sample(range(1,6),4))
    file.write(line)
    file.write('\n')
file.close()


nums = input('Give 6 numbers : ',).split(',')
combs = list(combinations(nums, 4))
with open("test.txt" , 'r') as infile:
    
    for i in range(len(combs)):
        for line in infile:
            
            if (combs[i]==line):
                f='true'
            else:
                f='false'
if (f=='true'):
    print('matched')
else:
    print('no match')
