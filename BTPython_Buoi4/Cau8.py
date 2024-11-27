import math

#loga_(x)=log(x) / log(a)

a=float(input("Nhap vao a(a>0):"))
x=float(input("Nhap vao x(x>0):"))

if(a<0 or x<0 or a==1):
    print("Nhap sai yeu cau nhap lai!")
    a=float(input("Nhap vao a(a>0):"))
    x=float(input("Nhap vao x(x>0):"))
else:
    loga_x=math.log(x)/ math.log(a)

n=loga_x
print("Ketqua Log{0}_({1}): {2}".format(a,x,n))
