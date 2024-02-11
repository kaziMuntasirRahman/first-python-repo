x = int(input("Enter a number: "))

def fact(n):
  if(n>0):
    return n*fact((n-1))
  else:
    return 1

print("The factorial of", x, "is", fact(x))