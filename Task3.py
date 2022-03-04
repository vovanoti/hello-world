import sys

stop = 0
while(1):
        i = 0
        str = input("Write something here: ")
        while (i<len(sys.argv)):
                if str == sys.argv[i]:
                        print("this is works!")
                        stop = 1
                        break
                i += 1
        if stop == 1:
                break
