n=int(input("Enter a number "))
for i in range (1,n+1):
    if(i==1 or i==n):   
        '''if i=1 or i=n then it will
        print equal number of star to 
        n'''           
        print("*"*n,end="")
    else:
        print("*",end="")
        print(" "*(n-2),end="")
        print("*",end="")
    print("")
    