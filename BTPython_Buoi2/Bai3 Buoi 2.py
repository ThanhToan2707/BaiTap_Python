print("Tính Điểm TB Toán Lý Hóa")

toan=float(input("Nhap điểmToán:"))
ly=float(input("Nhap điểmLý:"))
hoa=float(input("Nhap điểmHóa:"))
# canh 2 toan,ly,hoa= eval(input("Nhập điểm Toán,Lý,Hóa (cách nhau dấu phẩy):"))
print("Điểm Toán vừa nhập: ", toan)
print("Điểm Lý vừa nhập: ", ly)
print("Điểm Hóa vừa nhập: ", hoa)

dtb=(toan+ly+hoa)/3

print(f"Diểm TB ba môn:{dtb: .2f}")
