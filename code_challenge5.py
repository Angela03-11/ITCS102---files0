print("THE FACTORIAL PROGRAM")
number = eval(input("Enter any number: "))
fac = 1
for cat in range(number, 0, -1):
    fac *= cat
print("The factorial of", number, " is ", fac)
