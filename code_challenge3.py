name = input("What is your name? ")
fare = eval(input("Enter your fare fee ---> "))
student = input("Are you a Student? ")
if student == 'yes' :
    discount = fare * 0.20
    new_fare = fare - discount
    print("Hi ", name)
    print("Your Discount is ", discount)
    print("Your new fare is ", new_fare)
else:
    print("Sorry ", name, "You are not eligible for a student discount")