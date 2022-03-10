a = input("please enter the numbers: \n")
i = 0
j = 0
k = 0
count = 0

while (k<len(a)):
    if a[k].isdigit:
        count += 1
    k += 1
str=[]
print("the string is ",end='')
while (i<len(a)):
    if a[i].isdigit():
        str.append(a[i])
        print (str[j],end="")
        j += 1
    i += 1
tuple = (count)
tuple = str
print()
#print("the str has ", len(str) , " objects")
print("the tuple is", tuple)
