cat = True
sum = 0

while cat == True:
    meow = input("Do you want the cat to meow? ")
    sum += 1
    
    if meow == 'yes':
        print("Meowwwww~~~ ")
        continue
    else:
        print("Meow stops ")
        break
        
print("Count of Meow is", sum)
    
        
    