def print_spiral(n):
    p = int(n/2)
    matr=[0]*n
    for i in range(n):
        matr[i] = [0]*n
    i=1
    k=1
    while(k<=p):
        j=k-1
        while(j<n-k+1):
            matr[k-1][j]=i
            i+=1
            j+=1
        j=k
        while(j<n-k+1):
            matr[j][n-k]=i
            i+=1
            j+=1
        j=n-k-1
        while(j>=k-1):
            matr[n-k][j]=i
            i+=1
            j-=1
        j=n-k-1
        while(j>=k):
            matr[j][k-1]=i
            i+=1
            j-=1
        k += 1
    if(n%2==1):
        matr[p][p]=n*n
    i=0
    while(i<n):
        j=0
        while(j<n):
            print(" ",matr[i][j]," ",end="")
            if (j==n-1):
                print ("\n")
            j+=1
        i+=1
    
a = input("enter the number: ")
print_spiral(int(a))
