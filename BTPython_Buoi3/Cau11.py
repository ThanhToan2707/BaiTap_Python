while True: # lap vo tan
    n=int(input("Nhap vao so nguyen(n>0): "))

    dem=0

    for i in range(1, n+1):
        if n%i==0:
            dem +=1

    if dem==2:
        print(n,"vua nhap la so nguyen!")
    else:
        print(n,"vua nhap khong phai la so nguyen to!")

    luaChon=(input("Co muon nhap tiep de KT soNguyenTo khong(c/k): "))

    if(luaChon=='k'):
        break
    
