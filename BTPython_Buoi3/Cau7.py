print("tim ngay thang nam ke tiep ngay vua nhap!!!!!")

#thu vien datetime de tim ngay
import datetime

d=int(input("Nhap Ngay:"))
m=int(input("Nhap Thang:"))
y=int(input("Nhap Nam:"))

#tao doi tuong ngay,thang,nam tu thong tin da nhap
ngayDaNhap= datetime.date(y,m,d)
#tim ngay ke tiep = cach cong them 1
ngayKeTiep= ngayDaNhap + datetime.timedelta(days =1) #microseconds =1,milliseconds =1

print("Ngay vua nhapla: ",d,"/",m,"/",y)

print("Ngay Ke Tiep la: {}/{}/{}".format(ngayKeTiep.day, ngayKeTiep.month, ngayKeTiep.year))