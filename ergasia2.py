fname = input("Enter file name: ")
with open(fname, 'r') as infile:
    lst = []
    for line in infile:
        words = line.split()
        for word in words:
            if word not in lst:
                lst.append(word)
gletters = list("abdeghijlmnopqstuvwxyzABDEGHIJLMNOPQSTUVWXYZ")
bletters = list("fckrFCKR")

for word in lst:
    count1 = sum(word.count(i) for i in gletters)
    count2 = sum(word.count(j) for j in bletters)
    if (count2 > count1 ):
        print (' Bad word :' , word )
