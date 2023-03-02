"""
#palandrome check

a=str(input("enter a word"))
def wordcheck(b):
    if b[0:]==b[::-1]:
        print(b,"is palandrome")
    else:
        print('not a palandrome')
wordcheck(a)

#to find factorial

A=int(input("enter a number"))

def check(B):
    factorial=1

    for i in range(1,A+1):
        factorial=factorial*i
    return("factorial is",factorial)

print(check(A))

#fibonacci series
A=int(input("enter the number"))
def fib(n):
    L=[0]#fibonacci starts with 0 so taking it as a list to append
    a,b=0,1 #a=0 b=1  it should give in single line otherwise no output
    for i in range(n): # i jus tused for itration no use a=b b=a+b
        a,b=b,a+b  #in single line fibnocci standard program mwans a=b b=a+b iteration or it cangive as a=b b=c c=a+b
        L.append(a)
    return L
print(fib(A))