area1=lambda x:x*x
area2=lambda x, y:x*y
area3=lambda x,y:0.5*x*y
a=int(input("enter the length of the squares:"))
print("area of the a square is",area1(a))
l=int(input("enter the width of the rectangle:"))
w=int(input("enter the width of the rectangles:"))
print("area of rectangle is",area2(l,w))
h=int(input("enter the height of the triangle:"))
b=int(input("enter the base of the triangle:"))
print("area of the triangle is",area3(h,b))