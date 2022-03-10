def func(args):
    first = 0
    second = 0
    third = 0
    i = 0
    while (i<len(args)):
        if int(args[i])>first:
            third = second
            second = first
            first = args[i]
        i+=1
        
    print(first,second,third)


k=0
check=0
list1 = [1,64,128,32,16,2,975,"1024"]
list2 = []
while (k<len(list1)):
    if str(list1[k]).isdigit() != True:
        list2.append(list1[k])
        check=1
    k+=1
if(check==0):
    func(list1)
else:
    print("I can't parse: ",list2)
