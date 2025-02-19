print("***Fibonacci Series***")
a=1
b=1
for i in range(1,11):
    if (i%2!=0):
        print(i,". terim:",a)
        a=a+b
    else:
        print(i,". terim:",b)
        b=a+b