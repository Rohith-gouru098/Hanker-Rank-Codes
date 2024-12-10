# Input()
x, k = map(int, input().split())  # Read x and k as integers
polynomial = input()  # Read the polynomial as a string
result = eval(polynomial)
print(result == k)