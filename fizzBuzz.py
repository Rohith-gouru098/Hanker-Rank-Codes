#Fizz Buzz code give limits
N = int(input().strip())
# Iterate from 1 to N
for n in range(1, N + 1):
    if n % 3 == 0 and n % 5 == 0:
        print("FizzBuzz")
    elif n % 3 == 0:
        print("Fizz")
    elif n % 5 == 0:
        print("Buzz")
    else:
        print(n)