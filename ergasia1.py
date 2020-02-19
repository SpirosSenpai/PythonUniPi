fname = input("Enter file name: ")
with open(fname, 'r') as infile:
    lst = []
    for line in infile:
        words = line.split()
        for word in words:
            if word not in lst:
                lst.append(word)
    lst.sort(key=len)
    lst.reverse()
    maxw=[]
    for x in range(5):
      maxw.append(lst[x])
    
    vowels = ['a', 'e', 'i', 'o', 'u']
    for i in range(len(maxw)):
        for v in vowels:
            maxw[i] = maxw[i].replace(v,"")
maxw = [y[::-1] for y in maxw]
print(maxw)
