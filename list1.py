color1=input("enter list1 colors:").split(",")
color2=input("enter list2 colors:").split(",")
print(color1)
print(color2)
for xyz in color1:
    if xyz not in color2:
        print(xyz)
