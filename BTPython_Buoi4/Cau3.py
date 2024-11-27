print("Tinh BMI chi so can doi cua co the va du doan benh!!!")

#ham tinh BMI cua co the
def bmi(chieuCao, canNang):
    return canNang/(chieuCao**2)

#Phan loai BMI
def PhanLoai(BMI):
    if(BMI<18.5):
        return("Gay!")
    elif(BMI>=18,5 and BMI<=24,9):
        return("Binh Thuong!")
    elif(BMI>=25 and BMI<=29,9):
        return("Hoi Beo!")
    elif(BMI>=30 and BMI<=34,9):
        return("BeoPhi cap Do 1!")
    elif(BMI>=35 and BMI<=39,9):
        return("BeoPhi cap Do 2!")
    else:
        return("BeoPhi cap Do 3!")

def NguyCoPhatTrienBenh(BMI):
    if(BMI<18.5):
        return("Thap!!!")
    elif(BMI>=18,5 and BMI<=24,9):
        return("TrungBinh!")
    elif(BMI>=25 and BMI<=29,9):
        return("CaoVua!")
    elif(BMI>=30 and BMI<=34,9):
        return("KhaCao!")
    elif(BMI>=35 and BMI<=39,9):
        return ("RatCao!")
    else:
        return ("NguyHiem!!!")

print("Tinh BMI")
chieuCao=float(input("Nhap ChieuCao cua ban(>0): "))
canNang=float(input("Nhap CanNang cua ban(>0): "))

BMI=bmi(chieuCao,canNang)
bmi1=PhanLoai(BMI)
bmi2=NguyCoPhatTrienBenh(BMI)



print("BIM co the cua ban:",BMI)
print("Phan Loai co the cua ban theo chi so BMI: ",bmi1)
print("Nguy Co Phat Trien Benh theo thang do BMI: ",bmi2)




    

