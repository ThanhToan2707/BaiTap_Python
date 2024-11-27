print("Giai phuong trinh bac 2!!!")
# khai bao thu  vien sqrt
from math import sqrt

a=float(input("Nhap vao a: "))
b=float(input("Nhap vao b: "))
c=float(input("Nhap vao c: "))

if(a==0 ):
    if(b==0 and c==0):
        print("Phuong trinh vo so nghiem!")
    elif(b==0 and c!=0):
        print("Phuong trinh vo nghiem!")
    else:
        x=-c/b
        print("Nghiem cua pt X:",x)
else:
    delta=b**2-4*a*c

    if(delta <0):
        print("Phuong trinh vo nghiem!!")
    elif(delta==0):
        x=-b/2*a
        print("Phuong trinh co nghiem KEP x1=x2:",x)
    else:
        x1=(-b-sqrt(delta))/(2*a)
        x2=(-b+sqrt(delta))/(2*a)
        print("x1=",x1)
        print("x2=",x2)