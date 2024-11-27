"""
while True:

    print("Ve HinhVuong Rong Tam!!")

    hvr=int(input("Nhap chieu cao HinhVongRong: "))
    for i in range(hvr):
        if i==0 or i==hvr-1: #dong dau va cuoi hinhvuong
            print("*" *hvr)
        else:#dong giua
            print("*"+" "*(hvr-2)+"*")


    print("Ve HinhTamGiacXuoi !!")

    tgx=int(input("Nhap chieu cao TamGiacXuoi: "))
    for i in range(tgx):
        print("*" *(tgx+1))


    print("Ve HinhTamGiacNguoc !!")

    tgn=int(input("Nhap chieu cao TamGiacNguoc: "))
    for i in range(tgn,0,-1):
        print("*" *i)

    luaChon=input("Co muon ve TiepTuc hay khong(c/k): ")
    if(luaChon=="k"):
        break
"""
#Cach 2

def ve_hinh(n):

  # Hình 1: Tam giác đều ngược
  for i in range(n, 0, -1):
    print("*" * i)
    print()

  # Hình 2: Tam giác đều
  for i in range(1, n+1):
    print("*" * i)
    print()
    
  # Hình 3: Hình tam giác cân lệch
  for i in range(n):
    print(" " * (n-i-1) + "*" * (2*i+1))
    print()

  # Hình 4: Hình tam giác vuông cân
  for i in range(n):
    print(" " * (n-i-1) + "*" * (i+1))
    print()

# Nhập chiều cao của hình
n = int(input("Nhập chiều cao của hình: "))

# Gọi hàm vẽ hình
ve_hinh(n)