# Derive the Fibonacci Formulation through discussion and explanatin
# Fib(n) = Fib(n-1) + Fib(n-2)

def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

# print(fibonacci(6))
# print(fibonacci(5))

def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(5))
# print(factorial(8))

def sumOfNumber(n):
    if n == 1 or n == 0:
        return n
    else:
        return n + sumOfNumber(n-1)

# print(sumOfNumber(6))
# print(sumOfNumber(9))

def pow(x,y):
  if y == 1:
    return x
  else:
    if y % 2 == 0:
      return (pow(x, y//2) * pow(x, y//2)) 
    else:
      return (y* pow(x, y//2) * pow(x, y//2))


# print(pow(3, 6))
# print(pow(3, 7))