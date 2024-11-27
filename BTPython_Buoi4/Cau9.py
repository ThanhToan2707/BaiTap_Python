import math
n=int(input("Nhap vao n: "))
count =0 # dem cho  bang 0 de khi nhap n se tang len 1 cho den n vao trong cang

for i in range(n):
    kq=math.sqrt(2+count)

print(f"KetQua: {kq: .2f}")

