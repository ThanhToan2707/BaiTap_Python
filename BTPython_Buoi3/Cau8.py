def menu():
    print("--------------")
    print("|1. Cong(a+b)|")
    print("|2. Cong(a-b)|")
    print("|3. Cong(a*b)|")
    print("|4. Cong(a/b)|")
    print("--------------")


def tinh(a,b,luaChon):
    if(luaChon==1):
        return a+b
    elif(luaChon==2):
        return a-b
    elif(luaChon==3):
        return a*b
    elif(luaChon==4):
        return a/b
    else:
        print("Loi Nhap qua gioi han!!!")

#luu y while true thuc hien lien tuc nen cai break de thoat

while True:
#Nhap hai so a,b
    a=int(input("Nhap so a: "))
    b=int(input("Nhap so b: "))
    if(a<0 and b<0):
        print("Nhap Sai!!!")
        a=int(input("Nhap so a: "))
        b=int(input("Nhap so b: "))

    menu()

    luaChon=int(input("Nhap LuaChon (1->4): "))
    
    ketqua=tinh(a,b,luaChon)

    print("KetQua: ",ketqua)

    tieptuc=input("Co Muon Tiep Tuc hay Khong( c/k):")
    if(tieptuc=="k"):
        break





