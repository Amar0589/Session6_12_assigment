def fib2(n):
    lst=[]
    a=0
    b=1
    lst.append(a)
    lst.append(b)
    for i in range(n):
        a,b=b, a+b
        lst.append(b)
    return lst