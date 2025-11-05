n=int(input("enter the limit:"))
a=0
b=1
print("fibnocci series upto",n,"terms")
for i in range(n):
    print(a)
    temp=a
    a=b
    b=temp+b