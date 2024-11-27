print("Tinh gia tri BT: x + (x**2/2!) + (x**3/3!) +...+ (x**n/n!) ")

x=int(input("Nhap vao x(x>0): "))
n=int(input("Nhap vao n(x>0): "))

tong=0

for i in range(1,n+1):
    tu=x**1
    mau=1
    for j in range(i,n+1):
        mau= mau*j
        tong=tong+(tu/mau)
    
print(f"Tong({0},{1})={2}".format(x,n,tong))
