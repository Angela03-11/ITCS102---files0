name = input("Enter your name: ")
print("Hi", name, "Welcome to ODD NUMBER SUMMATION PROGRAM")
print("Mechanics: You may enter random number. Then, press 0 if you want the program to stop\n")
number = True
sum = 0
odd = " "

while number == True:
    value = eval(input("Input any number: "))
    
    if value % 2 == 1:
        print("Odd Number Detected, proceed to next number ")
        sum += value
        odd += str(value) + " "
        continue
    elif  value == 0:
        print("Program stops. ")
        break
       
    else:
           if value % 2 == 0:
               print("Even Number Detected, proceed to next number ")
           else:
                print("Invalid")
                continue
print(f"Hi {name}, the total sum of all odd numbers is {sum}")
print(f"ODD numbers detected {odd}")                