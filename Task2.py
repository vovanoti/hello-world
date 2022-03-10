def evennum(arg):
    i = 0
    while(i<len(arg)):
        if arg[i] % 2 == 0:
            if arg[i] == 254:
                break
            print (arg[i], " ", end='')
        i += 1      
a = [1,2,3,4,5,6,7,254,82,76]
evennum(a)
