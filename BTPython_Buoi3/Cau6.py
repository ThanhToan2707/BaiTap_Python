print("Nhap so Doc thanh Chu!")

def docSo(n):
    #tao ds chua cac cach doc cua so
    hangDonVi=[" ","Mot","Hai","Ba","Bon","Nam","Sau","Bay","Tam","Chin"]
    hangChuc=[" ","Muoi","Hai Muoi","Ba Muoi","Bon Muoi","Nam Muoi","Sau Muoi","Bay Muoi","Tam Muoi","Chin Muoi"]

#doc mot so:
    if(n<10):
        return hangDonVi[n]
    else:
        #doc hai so co 3 truong hop
        chuc=n//10
        donvi=n%10

        if(donvi==0):
            return hangChuc[chuc]
        elif(donvi==5):
            return hangChuc[chuc] + "Lam"
        else:
            return hangChuc[chuc]+" "+ hangDonVi[donvi]
        
n=int(input("Nhap vao N(1->99): "))
if(n<1 or n>99):
    print("Nhap Lai!!")
    n=int(input("Nhap vao N(1->99): "))

print(docSo(n))

            