#Python Menu Program FINAL PROJECT

import os
import time         
import sys

def type_print(text, speed=0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(speed)
    print()

type_print("GREETINGS VISITOR!", 0.05)
time.sleep(0.5)
name = input("What's your name?")
os.system('cls')
type_print(f"Hello, {name}. Welcome! \nThis program is a simple interactive menu that shows basic Python concepts, such as: \n• print \n• variables \n• operators \n• conditionals \n• loops \n• lists \n• functions", 0.05)
time.sleep(0.5)
start = input("Would you like to start the program? (yes / no):")
enter = input("\nPlease type 'Enter' to continue:")



def main_menu():
    while True:
        os.system('cls')
        type_print(f"Hi, {name}. You are in the Main Menu. You may select anything.", 0.05)
        time.sleep(0.5)
        print("-----------------------")
        print("-------MAIN MENU-------")
        print("-----------------------")
        print("|1 - Print Statements |")
        print("|2 - Variables        |")
        print("|3 - Operators        |")
        print("|4 - Conditionals     |")
        print("|5 - Loops            |")
        print("|6 - Lists            |")
        print("|7 - Functions        |")
        print("|0 - Exit             |")
        print("-----------------------")
        print("|8 - Quiz             |")
        print("-----------------------")
        
        select = input("Select your choice (0 - 8):")
        os.system('cls')
        
        #MAIN MENU 1
        if select == "1":
            while True:
                os.system('cls')
                type_print(f"Hi, {name}. Welcome to PRINT STATEMENTS, let's explore!", 0.05)  #it's like pagbati when someone enters on a specific sub menu hehe:)
                time.sleep(0.5)
                print("------------------------------")
                print("-------PRINT STATEMENTS-------")
                print("------------------------------")
                print("|1 - Definition              |")
                print("|2 - Syntax                  |")
                print("|3 - Example                 |")
                print("|4 - Try It Yourself         |")
                print("|0 - Return to the Main Menu |")   
                print("------------------------------")
            
                choice = input("Select your choice (0 - 4):")

                #SUB MENU 1
                if choice == '1':
                    os.system('cls')
                    print("============================================================================")
                    print("\t\t\t\tDEFINITION\t\t\t\t\n")
                    type_print(" - A print statement is used to display text, numbers, or results on the screen. \n - It is the simplest and most important Python command because it shows output.", 0.05)     
                    time.sleep(0.5)
                    print("\n============================================================================")
                    choice = input("\nEnter (0) to return:")
                   
                   
                elif choice == '2':
                    os.system('cls')
                    print("============================================================================")
                    print("\t\t\t\tSYNTAX\t\t\t\t\n") 
                    print("============================================================================")
                    type_print("\nSyntax = the correct structure and format of code so Python can understand it.")
                    time.sleep(0.5)
                    print("\n============================================================================")
                    print("\nCORRECT SYNTAX:")
                    print("\nprint(\"Message\"")
                    print("print(variable)")
                    print("\n============================================================================")
                    print("\nSYNTAX ERROR:")
                    print("\nprint \"message\"")
                    print("print('Message'    #missing )")
                    print("\n============================================================================")
                    type_print("\nThe print syntax shows the correct way to display text using print() with parentheses.")
                    time.sleep(0.5)
                    print("\n============================================================================")
                    choice = input("\nEnter (0) to return:")
                
                   
                   
                elif choice == '3':
                    os.system('cls')
                    print("============================================================================")
                    print("\t\t\t\tEXAMPLE\t\t\t\t\n")      
                    type_print("\nInput: \n\nprint(\"Hello, World!\")", 0.05)
                    time.sleep(0.5)
                    type_print("\nOutput: \n\nHello, World!", 0.05)
                    time.sleep(0.5)
                    print("\n============================================================================")
                    choice = input("\nEnter (0) to return:")
                    
                elif choice == '4':
                    os.system('cls')
                    print("============================================================================")
                    print("\t\t\t\tTRY IT YOURSELF\t\t\t\t\n")        
                    type_print("\nType your Python code below.", 0.05)
                    time.sleep(0.5)
                    print("\n============================================================================")
                    type_print("\nSample code: print(\"Hello World\")", 0.05)
                    time.sleep(0.5)
                    print("\n============================================================================")
                    type_print("\nPress ENTER on an empty line to run your code.", 0.05)
                    time.sleep(0.5)
                    print("\n============================================================================")
                    print("Now, Try it Yourself:\n")

                    user_lines = []

                    while True:
                        line = input()
                        if line.strip() == "":     #Studied about this so that the user can also code inside the environment of python
                            break
                        user_lines.append(line)

                    user_code = "\n".join(user_lines)

                    print("\nOutput:")
                    try:
                        exec(user_code)
                        type_print("You did a great job!", 0.05)
                        time.sleep(0.5)
                    except Exception as e:
                        type_print("Error in code.", 0.05)
                        time.sleep(0.5)
                        type_print("Nice try, do it again!", 0.05)
                        time.sleep(0.5)
                        type_print("Error message:", e, 0.05)
                        time.sleep(0.5)
                    print("============================================================================")
                            
                    choice = input("\nEnter (0) to return:")
                    
  
                elif choice == '0':
                    os.system('cls')
                    break
                
                else:
                    print("Invalid choice.")


                               
                               
                               
                               
                    
        #MAIN MENU 2            
        elif select == "2":
            while True:
                os.system('cls')
                type_print(f"Hello, {name}. Time to learn how to store information with VARIABLES.", 0.05)
                time.sleep(0.5)
                print("-------------------------------")
                print("-----------VARIABLES-----------")
                print("-------------------------------")
                print("|1 - Definition               |")
                print("|2 - Syntax                   |")
                print("|3 - Example                  |")
                print("|4 - Try It Yourself          |")
                print("|0 - Return to the Main Menu  |")   
                print("------------------------------")
            
                choice = input("Select your choice (0-4):")

                #SUB MENU 2
                if choice == '1':
                    os.system('cls')
                    print("============================================================================")
                    print("\t\t\t\tDEFINITION\t\t\t\t\n")
                    type_print("\n - Variables are containers that store information.\n - They hold data like names, numbers, or words.", 0.05)
                    time.sleep(0.5)     
                    print("\n============================================================================")
                    choice = input("\nEnter (0) to return:")
                
                
                elif choice == '2':
                    os.system('cls')
                    print("============================================================================")
                    print("\t\t\t\tSYNTAX\t\t\t\t\n") 
                    print("============================================================================")
                    type_print("\nSyntax = the correct structure and format of code so Python can understand it.")
                    time.sleep(0.5)
                    print("\n============================================================================")
                    print("\nCORRECT SYNTAX:")
                    print("\nage = 18")
                    print("name = \"Angela\"")
                    print("\n============================================================================")
                    print("\nSYNTAX ERROR:")
                    print("\n1age = 18")
                    print("page == 18")
                    print("\n============================================================================")
                    type_print("\nVariable syntax tells Python how to create and assign values to variables.")
                    time.sleep(0.5)
                    print("\n============================================================================")
                    choice = input("\nEnter (0) to return:")
                
                           
                elif choice == '3':
                    os.system('cls')
                    print("============================================================================")
                    print("\t\t\t\tEXAMPLE\t\t\t\t\n")      
                    type_print("\nname = \"Angela\" \n age = 18\nprint(name, age)", 0.05)
                    time.sleep(0.5)
                    type_print("\nOutput: Angela 18", 0.05)
                    time.sleep(0.5)
                    print("\n============================================================================")
                    choice = input("\nEnter (0) to return:")
                    
                elif choice == '4':
                    os.system('cls')
                    print("============================================================================")
                    print("\t\t\t\tTRY IT YOURSELF\t\t\t\t\n")        
                    type_print("Type your Python code below.", 0.05)
                    time.sleep(0.5)
                    print("============================================================================")
                    type_print("Sample code: \nnum = input(\"Enter a number: \")\nprint(\"Your number is:\", num)", 0.0)
                    time.sleep(0.5)
                    print("============================================================================")
                    type_print("Press ENTER on an empty line to run your code.", 0.05)
                    time.sleep(0.5)
                    print("============================================================================")
                    print("Now, try it yourself:\n")

                    user_lines = []
                    while True:
                        line = input()
                        if line.strip() == "": 
                            break
                        user_lines.append(line)

                    user_code = "\n".join(user_lines) 

                    print("\nOutput:")
                    try:
                        exec(user_code)
                        type_print("You did a great job!", 0.05)
                        time.sleep(0.5)
                    except Exception as e:
                        type_print("Error in code.", 0.05)
                        time.sleep(0.5)
                        type_print("Nice try, do it again!", 0.05)
                        time.sleep(0.5)
                        type_print("Error message:", e, 0.05)
                        time.sleep(0.5)

                    print("============================================================================")
                    choice = input("\nEnter (0) to return: ")

            
                elif choice == '0':
                    os.system('cls')
                    break
                
                else:
                    print("Invalid choice.")
            
            
            
            
              
        #MAIN MENU 3    
        elif select == "3":
            os.system('cls')
            while True:
                os.system('cls')
                type_print(f"Hey, {name}. Let's see how Python can calculate and compare values.", 0.05)
                time.sleep(0.5)
                print("-------------------------------")
                print("-----------OPERATORS-----------")
                print("-------------------------------")
                print("|1 - Definition               |")
                print("|2 - Syntax                   |")
                print("|3 - Example                  |")
                print("|4 - Try It Yourself          |")
                print("|0 - Return to the Main Menu  |")   
                print("------------------------------")
                choice = input("Select your choice (0-4):")
            
                #SUB MENU 3
                if choice == '1':
                    os.system('cls')
                    print("============================================================================")
                    print("\t\t\t\tTYPES OF OPERATORS\t\t\t\t\n")
                    type_print("\n1. Arithmetic Operators: (+, -, *, /, //, %, **)", 0.05)#For arithmetic operators with example each
                    time.sleep(0.5)
                    print("\n   •  +  : addition (e.g., 5 + 3 = 8)")
                    print("\n   •  -  : subtraction (e.g., 5 - 3 = 2)")
                    print("\n   •  *  : multiplication (e.g., 5 * 3 = 15)")
                    print("\n   •  /  : division (e.g., 5 / 3 = 1.666...)")
                    print("\n   •  // : floor division, returns integer result (e.g., 5 // 3 = 1)")
                    print("\n   •  %  : modulo, returns remainder (e.g., 5 % 3 = 2)")
                    print("\n   •  ** : exponentiation (e.g., 5 ** 3 = 125)\n")
                    print("\n============================================================================")
                    type_print("\n2. Assignment Operators: (=, +=, -=, *=, /=, %=, **=, //= )", 0.05) #For assignment operators
                    time.sleep(0.5)
                    print("\n   •  =  : Assign (e.g, x = 5 → x is 5)")
                    print("\n   •  += : Add and assign (e.g, x += 3 → x = x + 3)")
                    print("\n   •  -= : Subtract and assign(e.g, x -= 2 → x = x - 2)")
                    print("\n   •  *= : Multiply and assign (e.g, x *= 4 → x = x * 4)")
                    print("\n   •  /= : Divide and assign (e.g, x /= 2 → x = x / 2)")
                    print("\n   •  %= : Modulus and assign (e.g, x = x %= 3 → x = x % 3)")
                    print("\n   • **= : Exponent and assign (e.g, x **= 2 → x = x ** 2)")
                    print("\n   • //= : Floor divide and assign (e.g, x //= 3 → x = x // 3)")
                    print("\n============================================================================")
                    type_print("\n3. Relational Operators: (==, !=, >, <, >=, <=)", 0.05) #For relational operators
                    time.sleep(0.5)
                    print("\n   •  == : equal to (e.g., 5 == 3 → False)")
                    print("\n   •  != : not equal to (e.g., 5 != 3 → True)")
                    print("\n   •  >  : greater than (e.g., 5 > 3 → True)")
                    print("\n   •  <  : less than (e.g., 5 < 3 → False)")
                    print("\n   •  >= : greater than or equal to (e.g., 5 >= 5 → True)")
                    print("\n   •  <= : less than or equal to (e.g., 5 <= 3 → False)\n")   
                    print("\n============================================================================")
                    type_print("\n4. Logical Operators: (and or not)", 0.05) #For logical operators
                    time.sleep(0.5)
                    print("\n   • and : returns True if both conditions are True (e.g., True and False → False)")
                    print("\n   • or  : returns True if at least one condition is True (e.g., True or False → True)")
                    print("\n   • not   : reverses boolean value (e.g., not True → False)\n")
                    print("\n============================================================================")
                    choice = input("\nEnter (0) to return:")


                elif choice == '2':
                    os.system('cls')
                    print("============================================================================")
                    print("\t\t\t\tSYNTAX\t\t\t\t\n") 
                    print("============================================================================")
                    type_print("\nSyntax = the correct structure and format of code so Python can understand it.")
                    time.sleep(0.5)
                    print("\n============================================================================")
                    print("\nCORRECT SYNTAX:")
                    print("\nARITHMETIC OPERATORS")
                    print("a + b")
                    print("a - b")
                    print("a * b")                  
                    print("a / b")
                    print("a % b")
                    print("a ** b")
                    print("\nASSIGNMENT OPERATORS")
                    print("x = 5")
                    print("x += 3")
                    print("x -= 2")                  
                    print("x *= 4")
                    print("x /= 2")
                    print("x %= 3")
                    print("x **= 2")
                    print("x **= 2")
                    print("\nRELATIONAL OPERATORS")
                    print("a == b")
                    print("a != b")
                    print("a > b")                  
                    print("a > b")
                    print("a > b")
                    print("a > b")
                    print("\nLOGICAL OPERATORS")
                    print("a and b")
                    print("a and b")
                    print("not a")                  
                    print("\n============================================================================")
                    print("\nSYNTAX ERROR:")
                    print("\nARITHMETIC OPERATORS")
                    print("a +                 #Missing second operand.")
                    print("- a b               #Wrong symbol placement.")
                    print("a ** * b            #Python will not understand mixed operators.")
                    print("a // / b            #Two different division operators combined incorrectly.")
                    print("a %                 #Missing operand.")
                    print("a *** b             #Python doesn't recognize ***")
                    print("\nASSIGNMENT OPERATORS")
                    print("= 5                 #No variable to assign to.")
                    print("x + = 5             #Spaces break the operator.")
                    print("x -== 2             #Wrong operator combination.")
                    print("* x = 4             #Operator cannot start before variable.")
                    print("x /=                #Missing operand.")
                    print("x %== 3             #%= and == mixed incorrectly.")
                    print("x // = 3            #Space breaks the operator.")
                    print("\nRELATIONAL OPERATORS")
                    print("a = = b             #Python does not allow separated equals.")
                    print("a ! = b             #! cannot be separated from =.")
                    print("na >                 #Missing second value.")
                    print("< a b               #Operator cannot start the line.")
                    print("a >== b             #Invalid operator combination.")
                    print("a <== b             #Invalid operator combination.")
                    print("\nLOGICAL OPERATORS")
                    print("and a b             #'and' must be between two expressions.")
                    print("a or                #Missing second expression.")
                    print("not                 #Needs an expression.")
                    print("\n============================================================================")
                    type_print("\nOperators syntax describes how to write mathematical, logical, and comparison expressions correctly.")
                    time.sleep(0.5)
                    print("\n============================================================================")
                    choice = input("\nEnter (0) to return:")




                elif choice == '3':
                    os.system('cls')
                    print("============================================================================")
                    print("\t\t\t\tEXAMPLES\t\t\t\t\n")
                    type_print("# Arithmetic Examples", 0.05)
                    time.sleep(0.5)
                    print("\na = 10; b = 3")
                    print("\nprint(a + b)  # Output: 13")
                    print("\nprint(a - b)  # Output: 7")
                    print("\nprint(a * b)  # Output: 30")
                    print("\nprint(a / b)  # Output: 3.333...")

                    type_print("\n# Assignment Examples", 0.05)
                    time.sleep(0.5)
                    print("\nx = 5; x += 3; print(x)  # Output: 8")
                    print("\nx -= 2; print(x)         # Output: 6")
                    print("\nx *= 4; print(x)         # Output: 24")
                    print("\nx /= 2; print(x)         # Output: 12.0")

                    type_print("\n# Relational Examples", 0.05)
                    time.sleep(0.5)
                    print("\na = 10; b = 3")
                    print("\nprint(a == b)  # Output: False")
                    print("\nprint(a != b)  # Output: True")
                    print("\nprint(a > b)   # Output: True")
                    print("\nprint(a < b)   # Output: False")

                    type_print("\n# Logical Examples", 0.05)
                    time.sleep(0.5)
                    print("\nprint(True and False)  # Output: False")
                    print("\nprint(True or False)   # Output: True")
                    print("\nprint(not True)        # Output: False")
                    print("\nprint(not False)       # Output: True")
                    print("\n============================================================================")
                    choice = input("\nEnter (0) to return:")

                        
                elif choice == '4':
                    os.system('cls')
                    print("============================================================================")
                    print("\t\t\t\tTRY IT YOURSELF\t\t\t\t\n")
                    type_print("Type your Python code below.", 0.05)
                    time.sleep(0.5)
                    print("============================================================================")
                    type_print("Sample code:", 0.05)
                    time.sleep(0.5)
                    print("\nx = int(input(\"Enter first number: \"))")
                    print("\ny = int(input(\"Enter second number: \"))")
                    print("\nprint(\"Sum =\", x + y)")
                    print("\n============================================================================")
                    type_print("Press ENTER on an empty line to run your code.", 0.05)
                    time.sleep(0.5)
                    print("\n============================================================================")
                    print("Now, try it yourself:\n")

    
                    user_lines = []
                    while True:
                        line = input()
                        if line.strip() == "":  
                            break
                        user_lines.append(line)

                    user_code = "\n".join(user_lines)

                    print("\nOutput:")
                    try:
                        exec(user_code)
                        type_print("You did a great job!", 0.05)
                        time.sleep(0.5)
                    except Exception as e:
                        type_print("Error in code.", 0.05)
                        time.sleep(0.5)
                        type_print("Nice try, do it again!", 0.05)
                        time.sleep(0.5)
                        type_print("Error message:", e, 0.05)
                        time.sleep(0.5)

                    print("============================================================================")
                    choice = input("\nEnter (0) to return:")
                    
                elif choice == '0':
                    os.system('cls')
                    break
                
                else:
                    print("Invalid choice.")
            
            
            
            
            
            
            
            
            
        #MAIN MENU 4    
        elif select == "4":
            os.system('cls')
            while True:
                type_print(f"Hi, {name}. We will now explore how Python uses CONDITIONAL statements to make decisions.", 0.05)
                time.sleep(0.5)
                print("-------------------------------")
                print("----------CONDITIONALS---------")
                print("-------------------------------")
                print("|1 - Definition               |")
                print("|2 - Syntax                   |")
                print("|3 - Example                  |")
                print("|4 - Try It Yourself          |")
                print("|0 - Return to the Main Menu  |")   
                print("------------------------------")
            
                choice = input("Select your choice (0-4):")

                #SUB MENU  4
                if choice == '1':
                    os.system('cls')
                    print("============================================================================")
                    print("\t\t\t\tDEFINITION\t\t\t\t\n")
                    type_print(" - What are If/Else Statements?\n - Conditionals let your program make decisions.\n - If something is true, do something. \n - Otherwise, do something else.", 0.05)     
                    time.sleep(0.5)
                    print("\n============================================================================")
                    choice = input("\nEnter (0) to return:")
            
            
                elif choice == '2':
                    os.system('cls')
                    print("============================================================================")
                    print("\t\t\t\tSYNTAX\t\t\t\t\n") 
                    print("============================================================================")
                    type_print("\nSyntax = the correct structure and format of code so Python can understand it.")
                    time.sleep(0.5)
                    print("\n============================================================================")
                    print("\nCORRECT SYNTAX:")
                    print("if condition:")
                    print("\tstatement")
                    print("elif other_condition:")
                    print("\tstatement")
                    print("else:")
                    print("\tstatement")
                    print("\n============================================================================")
                    print("\nSYNTAX ERROR:")
                    print("\nif(condition)      # parentheses optional but not needed")
                    print("print(\"Hi\")        # missing ':' -colon")
                    print("\n============================================================================")
                    type_print("\nConditional syntax defines the correct structure for making decisions in Python.")
                    time.sleep(0.5)
                    print("\n============================================================================")
                    choice = input("\nEnter (0) to return:")
            
            
            
            
                elif choice == '3':
                    os.system('cls')
                    print("============================================================================")
                    print("\t\t\t\tEXAMPLE\t\t\t\t\n")      
                    print("\nage = 18")
                    print("\nif age >= 18:")
                    print("\n\tprint(\"Adult\")")
                    print("\nelse:")
                    print("\n\tprint(\"Minor\")")
                    type_print("\nOutput when age = 18: Adult", 0.05)
                    time.sleep(0.5)
                    type_print("\nOutput when age < 18: Minor", 0.05)
                    time.sleep(0.5)
                    print("\n============================================================================")
                    choice = input("\nEnter (0) to return:")
                    
                elif choice == '4':
                    os.system('cls')
                    print("============================================================================")
                    print("\t\t\t\tTRY IT YOURSELF\t\t\t\t\n")        
                    type_print("Type your Python code below.", 0.05)
                    time.sleep(0.5)
                    print("============================================================================")
                    type_print("\nSample code:", 0.05)
                    time.sleep(0.5)
                    print("\nnum = int(input(\"Enter a number: \"))")
                    print("\nif num % 2 == 0:")
                    print("\n\tprint(\"Even\")")
                    print("\nelse:")
                    print("\n\tprint(\"Odd\")")
                    print("\n============================================================================")
                    type_print("Press ENTER on an empty line to run your code.", 0.05)
                    time.sleep(0.5)
                    print("\n============================================================================")
                    print("Now, try it yourself:\n")
                    choice = input("\nEnter (0) to return:")

                    user_lines = []
                    while True:
                        line = input()
                        if line.strip() == "":
                            break
                        user_lines.append(line)

                    user_code = "\n".join(user_lines)

                    print("\nOutput:")
                    try:
                        exec(user_code)
                        type_print("You did a great job!", 0.05)
                        time.sleep(0.5)
                    except Exception as e:
                        type_print("Error in code.", 0.05)
                        time.sleep(0.5)
                        type_print("Nice try, do it again!", 0.05)
                        time.sleep(0.5)
                        type_print("Error message:", e, 0.05)
                        time.sleep(0.5)

                    print("============================================================================")
                    choice = input("\nEnter (0) to return:")
            
                elif choice == '0':
                    os.system('cls')
                    break
                
                else:
                    print("Invalid choice.")
                    
                    
                    
                    
                    
                    
                    
                    
            
        #MAIN MENU 5 
        elif select == "5":
            os.system('cls')
            while True:
                type_print(f"Hi, {name}. Let's see how Python can repeat actions using LOOPS.", 0.05)
                time.sleep(0.5)
                print("-------------------------------")
                print("-------------LOOPS-------------")
                print("-------------------------------")
                print("|1 - Definition               |")
                print("|2 - Syntax                   |")
                print("|3 - Example                  |")
                print("|4 - Try It Yourself          |")
                print("|0 - Return to the Main Menu  |")   
                print("------------------------------")
            
                choice = input("Select your choice (0-4):")

                #SUB MENU 5
                if choice == '1':
                    os.system('cls')
                    print("============================================================================")
                    print("\t\t\t\tDEFINITION\t\t\t\t\n")
                    type_print(" - Loops repeat actions automatically. \n - Python has for loops and while loops.", 0.05)
                    time.sleep(0.5)     
                    print("\n============================================================================")
                    choice = input("\nEnter (0) to return:")
            

                elif choice == '2':
                    os.system('cls')
                    print("============================================================================")
                    print("\t\t\t\tSYNTAX\t\t\t\t\n") 
                    print("============================================================================")
                    type_print("\nSyntax = the correct structure and format of code so Python can understand it.")
                    time.sleep(0.5)
                    print("\n============================================================================")
                    print("\nCORRECT SYNTAX:")
                    print("\nFOR LOOP")
                    print("for i in range(5):")
                    print("\tprint(i)")
                    print("\nWHILE LOOP")
                    print("while condition:")
                    print("\tstatement")
                    print("\n============================================================================")
                    print("\nSYNTAX ERROR:")
                    print("\nFOR LOOP")
                    print("\nfor i in range(5)")
                    print("print(i)")
                    print("\nWHILE LOOP")
                    print("\nwhile condition")
                    print("\tprint(x)")
                    print("\n============================================================================")
                    type_print("\nLoop syntax tells Python how to repeat actions until a condition is met.")
                    time.sleep(0.5)
                    print("\n============================================================================")
                    choice = input("\nEnter (0) to return:")
    
        
                elif choice == '3':
                    os.system('cls')
                    print("============================================================================")
                    print("\t\t\t\tFOR LOOP EXAMPLE\t\t\t\t\n")      
                    print("\nfor i in range(5):")
                    print("\n\tprint(i)")
                    print("\nOutput: 0 1 2 3 4")
                    print("\n============================================================================")
                    print("\t\t\t\tFOR LOOP EXAMPLE\t\t\t\t\n")      
                    print("\nfor i in range(5):")
                    print("\n\tprint(i)")
                    print("\nOutput: 0 1 2 3 4")
                    print("\n============================================================================")
                    choice = input("\nEnter (0) to return:")
            

                elif choice == '4':
                    os.system('cls')
                    print("============================================================================")
                    print("\t\t\t\tTRY IT YOURSELF\t\t\t\t\n")        
                    type_print("Type your Python code below.", 0.05)
                    time.sleep(0.5)
                    print("============================================================================")
                    type_print("\nSample code:", 0.05)
                    time.sleep(0.5)
                    print("\nlimit = int(input(\"Enter a number: \"))")
                    print("\nfor i in range(limit):")
                    print("\n\tprint(i)")
                    print("\n============================================================================")
                    type_print("Press ENTER on an empty line to run your code.", 0.05)
                    time.sleep(0.5)
                    print("\n============================================================================")
                    print("\nNow, try it yourself:\n")

                    user_lines = []
                    while True:
                        line = input()
                        if line.strip() == "":
                            break
                        user_lines.append(line)

                    user_code = "\n".join(user_lines)

                    print("\nOutput:")
                    try:
                        exec(user_code)
                        type_print("You did a great job!", 0.05)
                        time.sleep(0.5)
                    except Exception as e:
                        type_print("Error in code.", 0.05)
                        time.sleep(0.5)
                        type_print("Nice try, do it again!", 0.05)
                        time.sleep(0.5)
                        type_print("Error message:", e, 0.05)
                        time.sleep(0.5)

                    print("============================================================================")
                    choice = input("\nEnter (0) to return:")
            

                    
                elif choice == '0':
                    os.system('cls')
                    break
                
                else:
                    print("Invalid choice.")
                
            
            
            
            
            
            
            
            
            
        #MAIN MENU 6   
        elif select == "6":
            os.system('cls')
            while True:
                type_print(f"Hi, {name}. Time to organize and use collections of items with Python LISTS.", 0.05)
                print("-------------------------------")
                print("-------------LISTS-------------")
                print("-------------------------------")
                print("|1 - Definition               |")
                print("|2 - Syntax                   |")
                print("|3 - Example                  |")
                print("|4 - Try It Yourself          |")
                print("|0 - Return to the Main Menu  |")   
                print("------------------------------")
            
                choice = input("Select your choice (0-4):")

                #SUB MENU 6
                if choice == '1':
                    os.system('cls')
                    print("============================================================================")
                    print("\t\t\t\tDEFINITION\t\t\t\t\n")
                    type_print(" - Lists hold multiple items in a single variable. \n - Items are ordered and can be changed.", 0.05)
                    time.sleep(0.5)     
                    print("\n============================================================================")
                    choice = input("\nEnter (0) to return:")
            

                elif choice == '2':
                    os.system('cls')
                    print("============================================================================")
                    print("\t\t\t\tSYNTAX\t\t\t\t\n") 
                    print("============================================================================")
                    type_print("\nSyntax = the correct structure and format of code so Python can understand it.")
                    time.sleep(0.5)
                    print("\n============================================================================")
                    print("\nCORRECT SYNTAX:")
                    print("\nCreating a List:")
                    print("items = [1, 2, 3]")
                    print("\nAccessing Elements:")
                    print("items[0]")
                    print("\nAdding Items:")
                    print("items.append(\"apple\")")
                    print("\nRemoving Items:")
                    print("items.pop")
                    print("items.remove(\"apple\")")
                    print("\n============================================================================")
                    print("\nSYNTAX ERROR:")
                    print("\nitems.append \"apple\"")
                    print("items[1 2 3]")
                    print("\n============================================================================")
                    type_print("\nList syntax tells Python how to store multiple items and interact with them.")
                    time.sleep(0.5)
                    print("\n============================================================================")
                    choice = input("\nEnter (0) to return:")


                elif choice == '3':
                    os.system('cls')
                    print("============================================================================")
                    print("\t\t\t\tEXAMPLE\t\t\t\t\n")  
                    print("\nfruits = ['apple', 'banana', 'mango']")
                    print("\nprint(fruits)        # Output: ['apple', 'banana', 'mango']")
                    print("\nprint(fruits[1])     # Output: 'banana'\n")
                    print("\n============================================================================")
                    type_print("\n# Common list methods", 0.05)
                    time.sleep(0.5)
                    print("\nfruits.append('orange')      # Adds 'orange' at the end")
                    print("\nfruits.insert(1, 'grape')    # Inserts 'grape' at index 1")
                    print("\nfruits.pop()                 # Removes the last item")
                    print("\nfruits.pop(1)                # Removes the item at index 1")
                    print("\nfruits.remove('mango')       # Removes 'mango' by value")
                    print("\nfruits.sort()                # Sorts the list alphabetically/numerically")
                    print("\nfruits.reverse()             # Reverses the list\n")
                    print("\nprint(fruits)")
                    print("\n============================================================================")
                    choice = input("\nEnter (0) to return:")
            

                elif choice == '4':
                    os.system('cls')
                    print("============================================================================")
                    print("\t\t\t\tTRY IT YOURSELF\t\t\t\t\n")        
                    type_print("Type your Python code below.", 0.05)
                    time.sleep(0.5)
                    print("============================================================================")
                    type_print("Sample code:", 0.05)
                    time.sleep(0.5)
                    print("my_list = []")
                    print("item = input(\"Add something to the list: \")")
                    print("my_list.append(item)")
                    print("print(\"Your list:\", my_list)")
                    print("============================================================================")
                    type_print("Press ENTER on an empty line to run your code.", 0.05)
                    time.sleep(0.5)
                    print("============================================================================")
                    print("\nNow, try it yourself:\n")

                    user_lines = []
                    while True:
                        line = input()
                        if line.strip() == "":
                            break
                        user_lines.append(line)

                    user_code = "\n".join(user_lines)

                    print("\nOutput:")
                    try:
                        exec(user_code)
                        type_print("You did a great job!", 0.05)
                        time.sleep(0.5)
                    except Exception as e:
                        type_print("Error in code.", 0.05)
                        time.sleep(0.5)
                        type_print("Nice try, do it again!", 0.05)
                        time.sleep(0.5)
                        type_print("Error message:", e, 0.05)
                        time.sleep(0.5)

                    print("============================================================================")
                    choice = input("\nEnter (0) to return:")
                    
                    
                elif choice == '0':
                    os.system('cls')
                    break
                
                else:
                    print("Invalid choice.")
                    
                    
                                 
                    
                    
                    
                    
                    
                    
                    
                    
        #MAIN MENU 7  
        elif select == "7":
            os.system('cls')
            while True:
                type_print(f"Hi, {name}. Let's try out Python FUNCTIONS. ", 0.05)
                time.sleep(0.5)
                print("-------------------------------")
                print("-----------FUNCTIONS-----------")
                print("-------------------------------")
                print("|1 - Definition               |")
                print("|2 - Syntax                   |")
                print("|3 - Example                  |")
                print("|4 - Try It Yourself          |")
                print("|0 - Return to the Main Menu  |")   
                print("------------------------------")
            
                choice = input("Select your choice (0-4):")

                #SUB MENU 7
                if choice == '1':
                    os.system('cls')
                    print("============================================================================")
                    print("\t\t\t\tDEFINITION\t\t\t\t\n")
                    type_print(" - Functions are reusable blocks of code.\nThey let you organize your program and avoid repeating code.", 0.05)
                    time.sleep(0.5)     
                    print("============================================================================")
                    choice = input("\nEnter (0) to return:")
            


                elif choice == '2':
                    os.system('cls')
                    print("============================================================================")
                    print("\t\t\t\tSYNTAX\t\t\t\t\n") 
                    print("============================================================================")
                    type_print("\nSyntax = the correct structure and format of code so Python can understand it.")
                    time.sleep(0.5)
                    print("\n============================================================================")
                    print("\nCORRECT SYNTAX:")
                    print("\ndef greet():")
                    print("\tprint(\"Hello\")\n")
                    print("def add(a, b):")
                    print("\treturn a + b")
                    print("\n============================================================================")
                    print("\nSYNTAX ERROR:")
                    print("\ndef greet()")
                    print("\tprint(\"Hello\")")
                    print("\n============================================================================")
                    type_print("\nFunction syntax shows Python how to define reusable blocks of code.")
                    time.sleep(0.5)
                    print("\n============================================================================")
                    choice = input("\nEnter (0) to return:")


                elif choice == '3':
                    os.system('cls')
                    print("============================================================================")
                    print("\t\t\t\tEXAMPLE\t\t\t\t\n")  
                    type_print("# Function without parameters", 0.05)
                    time.sleep(0.5)
                    print("def greet():")
                    print("    print(\"Hello!\")")
                    print("greet()          # Output: Hello!\n")
                    type_print("# Function with parameters", 0.05)
                    time.sleep(0.5)
                    print("def greet(name):")
                    print("    print(\"Hello,\", name)")
                    print("greet(\"Angela\")  # Output: Hello, Angela")
                    print("============================================================================")
                    choice = input("\nEnter (0) to return:")
            

                elif choice == '4':
                    os.system('cls')
                    print("============================================================================")
                    print("\t\t\t\tTRY IT YOURSELF\t\t\t\t\n")        
                    type_print("Type your Python code below.", 0.05)
                    time.sleep(0.5)
                    type_print("Sample code:", 0.05)
                    time.sleep(0.5)
                    print("def greet(name):")
                    print("    print(\"Hello,\", name)")
                    print("user = input(\"Enter your name: \")")
                    print("greet(user)")
                    print("============================================================================")
                    type_print("Press ENTER on an empty line to run your code.", 0.05)
                    time.sleep(0.5)
                    print("============================================================================")
                    print("\nNow, try it yourself:\n")

                    user_lines = []
                    while True:
                        line = input()
                        if line.strip() == "":
                            break
                        user_lines.append(line)

                    user_code = "\n".join(user_lines)

                    print("\nOutput:")
                    try:
                        exec(user_code)
                        type_print("You did a great job!", 0.05)
                        time.sleep(0.5)
                    except Exception as e:
                        type_print("Error in code.", 0.05)
                        time.sleep(0.5)
                        type_print("Nice try, do it again!", 0.05)
                        time.sleep(0.5)
                        type_print("Error message:", e, 0.05)
                        time.sleep(0.5)

                    print("============================================================================")
                    choice = input("\nEnter (0) to return:")
                    
                    
                elif choice == '0':
                    os.system('cls')
                    break
                
                else:
                    print("Invalid choice.")
        
    
        
        
           
        #MAIN MENU 0
        elif select == "0":
            os.system('cls')
            type_print(f"\nYou are EXITING the program... Hope you've learned something, Thank you, {name}!", 0.05)
            time.sleep(0.5)
            break



        #MAIN MENU 8
        elif select == '8':
            os.system('cls')
            while True:
                type_print(f"Hi, {name}. Welcome to the PYTHON QUIZ!", 0.05)
                time.sleep(0.5)
                print("==========================")
                print("=======PYTHON QUIZ========")
                print("==========================")
                print("|1 - Easy                |")
                print("|2 - Medium              |")
                print("|3 - Hard                |")
                print("|0 - Return to Main Menu |")
                print("==========================")
                choice = input("Choose quiz level (0-3): ")
                
                
                total_q = 5  
                score = 0
                os.system("cls")
                
                
                
                quiz_name = "EASY" if choice == "1" else "MEDIUM" if choice == "2" else "HARD" if choice == "3" else "UNKNOWN"
                type_print(f"Hi, {name}. YOU CHOSE {quiz_name} QUIZ! Best of luck!\n", 0.05)
                time.sleep(0.5)
                
                
                
                #EASY QUESTIONS
        
                if choice == "1":
                    type_print("1. What function prints output in Python?", 0.05)
                    time.sleep(0.5)
                    print("a. echo()")
                    print("b. print()")
                    print("c. say()")
                    ans = input("Your answer: ").lower()
                    if ans == "b": score += 1

                    type_print("\n2. What symbol is used for addition?", 0.05)
                    time.sleep(0.5)
                    print("a. +")
                    print("b. -")
                    print("c. *")
                    ans = input("Your answer: ").lower()
                    if ans == "a": score += 1

                    type_print("\n3. Which of the following is a valid variable name?", 0.05)
                    time.sleep(0.5)
                    print("a. 2name")
                    print("b. @hello")
                    print("c. name")
                    ans = input("Your answer: ").lower()
                    if ans == "c": score += 1

                    type_print("\n4. Which creates a list?", 0.05)
                    time.sleep(0.5)
                    print("a. {}")
                    print("b. []")
                    print("c. ()")
                    ans = input("Your answer: ").lower()
                    if ans == "b": score += 1

                    type_print("\n5. What data type is 'Hello'?", 0.05)
                    time.sleep(0.5)
                    print("a. Integer")
                    print("b. Boolean")
                    print("c. String")
                    ans = input("Your answer: ").lower()
                    if ans == "c": score += 1
                    
                    print("\n============================================================================")
                    type_print(f"QUIZ FINISHED! Your Score: {score}/{total_q}", 0.05)
                    time.sleep(0.5)
                    print("============================================================================")
                    choice = input("\nEnter (0) to return:")
                
                
                
                # MEDIUM QUESTIONS
                if choice == "2":
                    type_print("1. What does this expression return?  10 > 5 and 5 > 2", 0.05)
                    time.sleep(0.5)
                    print("a. True")
                    print("b. False")
                    print("c. Error")
                    ans = input("Your answer: ").lower()
                    if ans == "a": score += 1

                    type_print("\n2. What is the correct way to remove the LAST item in a list?", 0.05)
                    time.sleep(0.5)
                    print("a. list.delete()")
                    print("b. list.remove()")
                    print("c. list.pop()")
                    ans = input("Your answer: ").lower()
                    if ans == "c": score += 1

                    type_print("\n3. What will range(1, 5) generate?", 0.05)
                    time.sleep(0.5)
                    print("a. 1 2 3 4")
                    print("b. 1 2 3 4 5")
                    print("c. 0 1 2 3 4")
                    ans = input("Your answer: ").lower()
                    if ans == "a": score += 1

                    type_print("\n4. What keyword allows a loop to skip the current iteration?", 0.05)
                    time.sleep(0.5)
                    print("a. break")
                    print("b. continue")
                    print("c. skip")
                    ans = input("Your answer: ").lower()
                    if ans == "b": score += 1

                    type_print("\n5. What will be the OUTPUT of:  len(['A', ['B', 'C']])", 0.05)
                    time.sleep(0.5)
                    print("a. 3")
                    print("b. 2")
                    print("c. 1")
                    ans = input("Your answer: ").lower()
                    if ans == "b": score += 1

                    print("\n============================================================================")
                    type_print(f"{quiz_name} QUIZ FINISHED! Your Score: {score}/{total_q}", 0.05)
                    time.sleep(0.5)
                    print("============================================================================")
                    input("\nEnter (0) to return:")
                    os.system("cls")
                
                # HARD QUESTIONS
                if choice == "3":
                    type_print("1. What is the output?  print( 3 * '2' )", 0.05)
                    time.sleep(0.5)
                    print("a. 222")
                    print("b. 6")
                    print("c. Error")
                    ans = input("Your answer: ").lower()
                    if ans == "a": score += 1

                    type_print("\n2. Which expression will return \"True\"?", 0.05)
                    time.sleep(0.5)
                    print("a. 10 == '10'")
                    print("b. [] == False")
                    print("c. bool('False')")
                    ans = input("Your answer: ").lower()
                    if ans == "c": score += 1  # non-empty strings are True

                    type_print("\n3. What happens if you call a function before defining it?", 0.05)
                    time.sleep(0.5)
                    print("a. It works normally")
                    print("b. NameError")
                    print("c. SyntaxError")
                    ans = input("Your answer: ").lower()
                    if ans == "b": score += 1

                    type_print("\n4. What does this return?  [1, 2, 3][1]", 0.05)
                    time.sleep(0.5)
                    print("a. 1")
                    print("b. 2")
                    print("c. 3")
                    ans = input("Your answer: ").lower()
                    if ans == "b": score += 1

                    type_print("\n5. What is the output of:  print(type({}))", 0.05)
                    time.sleep(0.5)
                    print("a. <class 'dict'>")
                    print("b. <class 'set'>")
                    print("c. <class 'tuple'>")
                    ans = input("Your answer: ").lower()
                    if ans == "a": score += 1

                    print("\n============================================================================")
                    type_print(f"{quiz_name} QUIZ FINISHED! Your Score: {score}/{total_q}", 0.05)
                    time.sleep(0.5)
                    print("============================================================================")
                    input("\nEnter (0) to return:")
                    os.system("cls")

                elif choice == '0':
                    os.system('cls')
                    break
                
                else:
                    print("Invalid choice.")


if enter.lower() == "enter":
    os.system('cls')
    print("Going to the Main Menu...\n")
    main_menu()
else:
    print("You did not type 'Enter'. Exiting program.")
    