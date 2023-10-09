#WAP to find fibonacci series and importing to other program..
def fibo(n):
    a,b=0,1
    while b<=n:
        print(b,end=' ')
        a,b=b,a+b
    print()
def fibo2(n):#return fibonacci series upto n..
    result=[]
    a,b=0,1
    while b<=n:
        result.append(b)
        a,b=b,a+b
        return result
n=int(input("Enter a number"))
print(fibo(n))