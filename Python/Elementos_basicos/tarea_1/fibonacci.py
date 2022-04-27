
def fibo(n):
  a=0
  b=1
  while a < n:
    print(str(a) + " ")
    c=a+b
    a=b
    b=c
fibo(1000)
