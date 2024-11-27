print("Xuat ban Cuu Chuong!!")

for i in range(1,11): #lap tu1 den 10
    for j in range(2,10): #lap tu2 den 9
         
        line= "{0} * {1:>2} = {2:>2}".format(j,i,i*j)
        print(line, end='\t')# ngan cach bang dau tab
    print()
