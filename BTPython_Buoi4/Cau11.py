''''
x = 10  # Biến toàn cục

def my_function():
  global x  # Khai báo x là biến toàn cục bên trong hàm
  x = x + 5
  print(x)

my_function()
print(x)
'''
def sum1(n):
    s = 0
    while n > 0:
        s += 1
        n -= 1
    return s
def sum2():
    global val
    s = 0
    while val > 0:
        s += 1
        val -= 1
    return s
def sum3():
    s = 0
    for i in range(val, 0, -1):
        s += 1
    return s

#global la bien toan cuc thay doi gitri trong va ngoai ham
def main():
    global val
    val = 5
    print(sum1(5))
    print(sum2())
    print(sum3())
main()

