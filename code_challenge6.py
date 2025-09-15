print("Enter 7 numbers")

total = 0
for odd in range(1, 8, 1):
    value = eval(input("Enter any number: "))
    if value % 2:
        total += value
    
print("The total sum of all odd number is:", total)