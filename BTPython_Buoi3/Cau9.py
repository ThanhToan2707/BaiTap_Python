print("Xuat ra so quy thuoc thang nao trong nam!!")

n=int(input("Nhap vao Thang cua nam de biet thuoc quy nao(1->12):"))
if(n<1 or n>12):
    print("Nhap Sai nhap lai!!!")
    n=int(input("Nhap vao Thang cua nam de biet thuoc quy nao(1->12):"))


if n in (1,2,3):
    print("Thang",n,"vua nhap thuoc Quy 1")
elif n in (4,5,6):
    print("Thang",n,"vua nhap thuoc Quy 2")
elif n in (7,8,9):
    print("Thang",n,"vua nhap thuoc Quy 3")
elif n in (10,11,12):
    print("Thang",n,"vua nhap thuoc Quy 4")

