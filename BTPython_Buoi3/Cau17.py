'''
done = False
n,m=0,100
while not done and n!=m:
    n=int(input())
    if n<0:
        done= True
    print("n= ",n) 
    '''
n,m=0,100
while True:
    n=int(input())
    if n<0:
        break
    elif n==m:
        print("n= ",n)
        break 