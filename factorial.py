def factorial(n):
    if n==1:
        return 1
    else:
        return n*factorial(n-1)
i=int(input("enter a number"))

res=factorial(i)
print(res)
