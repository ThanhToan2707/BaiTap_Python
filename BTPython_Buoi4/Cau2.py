from random import randrange #thu vien randrange tra ve mot so nguyen ngẫu nhiên trongkhoang xđ

while True:
    somay=randrange(1,101)

    solandoan=0

    win =False

    while (solandoan <7):
        solandoan +=1 #tang so lan doan+1
        songuoinhap= int(input("Nhap So Ban doan Trung giai thuong (1-100):"))
        print("Ban da Doan lan thu: ",solandoan)

        #TH so may bang so nguoi
        if(somay==songuoinhap):
            print("Chuc Mung, Ban da Doan Trung so {0} cua may Trung voi so {0} ban nhap".format(somay,songuoinhap))
            win= True
            break
        if(somay > songuoinhap):
            print("Ban DoanSai so {0} cua may > so {1} ban vua nhap!!!".format(somay,songuoinhap))
        else:
            print("Ban DoanSai so {0} cua may < so {1} ban vua nhap!!!".format(somay,songuoinhap))

    #neu nhap lon hon 7 lan thi game ket thuc!
    if(win==False):
        print("Ban da Nhap du 7 lan, Game da ket thuc!")

    luaChon=input("Ban co muon nhap tiep hay khong(c/k): ")
    if(luaChon=='k'):
        print("Cam on, hen gap lai ^-^")
        break




