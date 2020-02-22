string = input('Give a string to convert: ')
cs = ''.join(str(ord(i)) for i in string)
print (cs)
cs = int(cs)
if cs > 1:
        if (cs % 2 ) == 0:
            print ( cs, "is not a prime number")
            
        else:
            print (cs, "is a prime number")

else:
    print (cs, "is not a prime number")


