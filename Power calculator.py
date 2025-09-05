n = int(input("Enter a number: "))
x = int(input("Enter the exponent: "))
r = 1
for _ in range(x):
    r = r * n
print(n, ' to the power of', x,' is: ',r,'.')