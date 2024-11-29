def recursive_multiplication(num1,num2):
    if num2==1:
        return num1
    else:
        return num1+recursive_multiplication(num1,num2-1)
num1= int(input("enter num1"))
num2= int(input(" enter num2"))
print(recursive_multiplication(num1,num2))