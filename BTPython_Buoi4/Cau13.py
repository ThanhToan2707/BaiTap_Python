print ("KiemTra so HHao va so ThinhVuong")

#6=1+2+3=6 la sohonhao, 12=1+2+3+4+6<12 La so thinhvuong

def TongUocSoChung(n):
    tong=0;
    for i in range(1,n):
        if(n%i==0):
            tong +=1
    return tong

def KiemTraSoHoanHao(n):
        return TongUocSoChung(n)==n

def KiemTraSoThinhVuong(n):
        return TongUocSoChung(n)>n
#nhap n
n=int(input("Nhap vao N(N>0): "))

if(KiemTraSoHoanHao(n)):
    print("So {0} vua nhap la SoHoanHao".format(n))
elif(KiemTraSoThinhVuong(n)):
    print("So {0} vua nhap la SoThinhVuong".format(n))
else:
    print(f"So {n} vua nhap Khong Tim Thay")


