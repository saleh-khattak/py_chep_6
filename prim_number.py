num=int(input("Enter a number :"))
for i in range(2,num):
    if(num%i==0):
        print(f"The {num} is not a prim number ")
        break
else:
    print(f"The {num} is prime")