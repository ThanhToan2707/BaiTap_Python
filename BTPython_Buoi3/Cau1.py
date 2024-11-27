print("Kiem tra nam thuan hay ko!")
t=int(input("Nhap vao So Nam(Nam>0): "))
if(t<0):
    print("Loi nhap lai!")
    t=int(input("Nhap vao So Nam(Nam>0): "))

if(t%4==0 and t%100!=0 or t%400==0):
    print("Nam ",t,"vua nhap la Nam Thuan!")
else:
    print("Nam",t,"vua nhap KHONg phai la Nam Thuan!")