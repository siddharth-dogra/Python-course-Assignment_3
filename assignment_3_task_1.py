
def factorial(n):
    if(n<2):
        return 1
    else:
        return n*factorial(n-1)

number=int(input("Enter the number:"))
result=factorial(number)
print("The factorial of",number,"is:",result)