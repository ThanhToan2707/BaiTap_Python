from math import sqrt

a=int(input("Nhap canh a tamgiac(a>0): "))
b=int(input("Nhap canh b tamgiac(b>0): "))
c=int(input("Nhap canh c tamgiac(c>0): "))
#kt dk Nhap >0
if(a<=0 or b<=0 or c<=0):
    print("Nhap Sai. Hay nhap lai!!!")
    a=int(input("Nhap canh a tamgiac(a>0): "))
    b=int(input("Nhap canh b tamgiac(b>0): "))
    c=int(input("Nhap canh c tamgiac(c>0): "))

#kt loai tamgiac  
if(a+b>c or a+c>b or b+c>a):
    if(a+b==c**2 or a+c==b**2 or b+c==a**2):
        print("3 Canh vua nhap tao thanh TamGiac Vuong!!")
    elif(a==b and b==c):
        print("3 Canh vua nhap tao thanh TamGiac Dieu!!")
    elif(a==b or a==c or b==c):
        print("3 Canh vua nhap tao thanh TamGiac Can!!")
    elif(a**2>(b**2+c**2) or b**2>(a**2+c**2) or c**2>(b**2+a**2) ):
        print("3 Canh vua nhap tao thanh TamGiac Tu")
    else:
        print("Tao Thanh TamGiac Nhon tu 3 canh!")

else:
    print("Cac Canh ban nhap ko tao thanh 1 tam giac!!!")

def tinhDT(a,b,c):
    cv=a+b+c 
    p=cv/2
    dienTich=sqrt(p*(p-a)*(p-b)*(p-c))
    return dienTich

def tinhCV(a,b,c):
    cv=a+b+c 
    return cv

kq1=tinhCV(a,b,c)
kq2=tinhDT(a,b,c)
print(f"ChuVi cac canh vua nhap=",kq1)
print(f"DienTich cac canh vua nhap=",kq2)