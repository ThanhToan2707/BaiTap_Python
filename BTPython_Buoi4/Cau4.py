print("Tinh ROI!")

def TinhROI(doanhThu, chiPhi):
    return (doanhThu-chiPhi)/chiPhi

def DauTu(roi):
    if(roi>=0.75):
        return("Nen bat dau DauTu!")
    else:
        return("TiLe ROI <0,75 Khong nen DauTu")

doanhThu=float(input("Nhap DoanhThu cua CongTy: "))
chiPhi=float(input("Nhap ChiPhi cho CongTy:"))

roi=TinhROI(doanhThu,chiPhi)

dautu=DauTu(roi)

print("TiLe ROI cua Cong Ty la: ",roi)
print("Goi Y DauTu cho CongTY:",dautu)