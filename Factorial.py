#factorial
z = 1
x = int(input("Type a number: "))
while x > 1:
    z=x*z
    x = x-1
print(z)