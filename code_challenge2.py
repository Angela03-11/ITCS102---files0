deposit = eval(input("Enter the amount to deposit -->",)) 
print("Here is the breakdown of the deposited amount: ")

thousand = deposit // 1000
deposit = deposit % 1000

five_hundred = deposit // 500
deposit = deposit % 500

two_hundred = deposit // 200
deposit = deposit % 200

one_hundred = deposit // 100
deposit = deposit % 100

fifty = deposit // 50
deposit = deposit % 50

twenty = deposit // 20
deposit = deposit % 20

ten = deposit // 10
deposit = deposit % 10

five = deposit // 5
deposit = deposit % 5

one = deposit // 1
deposit = deposit % 1

print(thousand,"-1000")
print(five_hundred,"-500")
print(two_hundred,"-200")
print(one_hundred,"-100")
print(fifty,"-50")
print(twenty,"-20")
print(ten,"-10")

print(one,"-1")
