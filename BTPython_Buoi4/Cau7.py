import math

xA=float(input("Nhap vao X_a: "))
yA=float(input("Nhap vao Y_a: "))
xB=float(input("Nhap vao X_b: "))
yB=float(input("Nhap vao Y_b: "))

kq=math.sqrt(((xB-xA)**2)+((yB-yA)**2))

print(f"Ket Qua: {kq: .2f}")