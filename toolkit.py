def find_gcd(num1, num2):
        while num2 != 0:        #This loop continues until the remainder is 0
            num1, num2 = num2, num1 % num2      #This rotates the current num 2 into becoming num 1 and the new num2 becoming the remainder
        return num1         #Once num2/remainder reaches 0, the num1 value will be the GCD

def find_lcm(num1, num2):
    product = num1 * num2
    if product < 0:
        product = -product          #Provides a positive LCM
    return product // find_gcd(num1, num2)          #Divivde the product by the GCD to find the LCM

while True:         #Loop created to keep the main menu active until the user uses 5) Exit
    print("\n=== Math Toolkit ===")
    print("1) GCD & LCM Calculator")
    print("2) Basic Arithmetic Calculator")
    print("3) Sum of Digits")
    print("4) Integer Palindrome Checker")
    print("5) Exit)")
        
    option = input("Select an option (1-5): ")

    if option == "1":
        num1 = int(input("Enter first integer: "))
        num2 = int(input("Enter second integer: "))

        gcd = find_gcd(num1, num2)
        lcm = find_lcm(num1, num2)

        print(f"GCD ({num1}, {num2}) = {gcd}")
        print(f"LCM ({num1}, {num2}) = {lcm}")

        input("# Press Enter to return to menu...")

            
    elif option == "2":         #Use float to handle decimals
        num1 = float(input("First number: "))
        op = input("Operator (+, -, *, /): ")
        num2 = float(input("Second number: "))

        if op == "+":
            result = num1 + num2
        elif op == "-":
            result = num1 - num2
        elif op == "*":
            result = num1 * num2
        elif op == "/":
            result = num1 / num2
        else:
            result = "Invalid operator"

        print(f"{num1} {op} {num2} = {result}")
        input("# Press Enter to return to menu...")


    elif option == "3":
        num1 = int(input("Enter an integer: "))
        integer = num1      #Need this to keep the original number for the print output later.
        total = 0       #Total 

        if num1 < 0:        #Assignment listed assume all inputs are valid, made sure it would sum negative numbers properly.
            num1 = -num1

        while num1 > 0:
            total += num1 % 10
            num1 = num1 // 10

        print(f"Sum of digits of {integer} is {total}")
        input("# Press Enter to return to menu...")


    elif option == "4":
        num1 = int(input("Enter an integer: "))

        if num1 < 0:            #Chose to not accept negative numbers as palindromes, could adjust to include negatives and omit the negative symbole.
            print(f"{num1} is not a palindrome.")

        else:
            reversed_num1 = int(str(num1)[::-1])        #The number converts to a string and then returns to an integer
            if num1 == reversed_num1:           #The comparison for our number and reversed number
                print(f"{num1} is a palindrome.")
                input("# Press Enter to return to menu...")
            else:
                print(f"{num1} is not a palindrome.")
                input("# Press Enter to return to menu...")

    elif option == "5":
        print("Goodbye!")
        break # Exits the while loop

    else:           #Keeps the valid choices between 1 and 5.
        print("Invalid option. Please enter an option between 1 and 5.")
