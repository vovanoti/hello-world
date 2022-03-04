def func(args):
    mydict = {}
    for i in args:
        if i not in mydict:
            mydict[i] = 1
        else:
            mydict[i] += 1
    print(mydict)

inp = input("Enter the text: ")
func(inp)
