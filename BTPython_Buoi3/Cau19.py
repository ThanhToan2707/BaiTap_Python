
import math

def tinh_S(x, n):

  S = x
  exponent = 3
  for i in range(1, n+1):
    S += (x**exponent) / math.factorial(i)
    exponent += 2
  return S


x = float(input("Nhập giá trị của x: "))
n = int(input("Nhập giá trị của n: "))

# Tính và in kết quả
ket_qua = tinh_S(x, n)
print("KetQua S({0},{1}):{2}".format(x,n,ket_qua))