import time

# Hàm vẽ hình 1
def hinh_1():
    print("Hình 1:")
    print("  *  ")
    print(" * * ")
    print("*   *")
    print(" * * ")
    print("  *  ")

# Hàm vẽ hình 2
def hinh_2():
    print("Hình 2:")
    print("*    ")
    print("*    ")
    print("*****")
    print("*    ")
    print("*    ")

# Hàm vẽ hình 3
def hinh_3():
    print("Hình 3:")
    print("*****")
    print("*   *")
    print("*   *")
    print("*   *")
    print("*****")

# Hàm vẽ hình 4
def hinh_4():
    print("Hình 4:")
    print("*****")
    print("*    ")
    print("*****")
    print("    *")
    print("*****")

# Vẽ từng hình sau mỗi 5 giây
hinh_1()
time.sleep(3)

hinh_2()
time.sleep(5)

hinh_3()
time.sleep(15)

hinh_4()
time.sleep(5)
