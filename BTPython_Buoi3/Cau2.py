print("Xuat so ngay cua thang")
d=int(input("Nhap vao Thang muon xuat ngay(1->12):"))
if(d>12 or d<1):
    print("Nhap vuot gioi han, nhap lai!")
    d=int(input("Nhap vao Thang muon xuat ngay(1->12):"))

#c1
if(d==1 or d==3 or d==5 or d==7 or d==8 or d==10 or d==12): 
    print("Thang vua nhap co 31 ngay!")

# c2 if d in (1,2,3,4):

elif(d==4 or d==6 or d==9 or d==11):
    print("Thang vua nhap co 30 Ngay!")
elif(d==2):
    t=int(input("Nhap vao So Nam(Nam>0): "))
    if(t<0):
        print("Loi nhap lai!")
        t=int(input("Nhap vao So Nam(Nam>0): "))
    
    if(t%4==0 and t%100!=0 or t%400==0):
        print("Thang",d,"vua nhap la Nam Thuan! co 29 ngay")
    else:
        print("Thang",d,"vua nhap KHONg phai la Nam Thuan! co 28 ngay")
    