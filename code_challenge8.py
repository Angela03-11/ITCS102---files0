print("MULTIPLICATION TABLE MAKER")
value = eval(input("Enter a number: "))

print("Multiplication table for: ", value)

for multi in range(1, 11):
    result = value * multi
    print(value, "x", multi, "=", result)
    

