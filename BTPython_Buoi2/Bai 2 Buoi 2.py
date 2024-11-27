t= int(input("Nhập vào số T: "))
if(t<0):
    print("Nhập lại: ")
    t= int(input("Nhập vào số T: "))

h=(t//3600)%24
m=(t%3600)/60
s=(t%3600)%60

print("Thời Gian: ",h,":",m,":",s)
