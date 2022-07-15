import os
import time

ancii = """
  _____                      __         
 / ___/__  ___ _  _____ ____/ /____ ____
/ /__/ _ \/ _ \ |/ / -_) __/ __/ -_) __/
\___/\___/_//_/___/\__/_/  \__/\__/_/   
""" #Defining the ANCII art used in the program for easier and cleaner future reference

def main(): #Defining the entire function to loop
    os.system("cls") #Clears the screen
    print(ancii) #Prints the ancii art
    print("""
        1. Binary to Decimal/Denary
        2. Decimal/Denary to Binary
        3. Binary to Hexadecimal
        4. Hexadecimal to Binary
        5. Decimal/Denary to Hexadecimal
        6. Hexadecimal to Decimal/Denary
    """)#Prints the menu
    user_input = input("Enter a number: ") #Asks the user for input

    if user_input == "1": #If the user inputs 1
        os.system("cls") #Clears the screen
        print(ancii) #Prints the ancii art
        number= input("Enter a Binary number: ") #Asks the user for a binary number
        decimal_number = int(number, 2) #Converts the binary number to a decimal number by LCM of 2
        print(f"The Decimal/Denary value of {number} is: ", decimal_number) #Prints the decimal numbers

    elif user_input == "2": #If the user inputs 2
        os.system("cls") #Clears the screen
        print(ancii) #Prints the ancii art
        number= int(input("Enter a Decimal/Denary number: ")) #Asks the user for a Decimal/Denary Number

        def d2b(n): #defines the function to convert a decimal number to binary
            return bin(n).replace("0b", "") #Returns the binary number of the decimal number

        print(f"The binary value of {number} is: ", d2b(number)) #Prints the binary number of the decimal number

    elif user_input == "3":
        os.system("cls")
        print(ancii)
        number = input("Enter a Binary number: ") #Asks the user for a binary number
        def b2h(n):
            num = int(n, 2) #Converts the binary number to a Hexadecimal number
            hex_num = hex(num) #Converts the Hexadecimal number to a string
            return(hex_num) #Returns the Hexadecimal number

        final = b2h(number) #Defines the value
        print(f"The hexadecimal value of {number} is: ", final.upper()) #Converts the lowercase characters into upper case while printing also

    elif user_input == "4": #If the user inputs 4
        os.system("cls") #Clears the screen
        print(ancii) #Prints the ancii art
        number = input("Enter a Hexadecimal number: ") #Asks the user for a Hexadecimal number
        base = 16 #Defines the base value
        h2b = bin(int(number, base)).zfill(8) #Converts the Hexadecimal number to a binary number
        print (f"The binary value of {number} is: ", str(h2b)) #Prints the result

    elif user_input == "5": #If the user inputs 5
        os.system("cls") #Clears the screen
        print(ancii) #Prints the ancii art
        number = int(input("Enter a Decimal/Denary number: ")) #Asks the user for a Decimal/Denary number
        num = hex(number) #Converts the Decimal/Denary number to a Hexadecimal number
        final = num.upper() #Converts the lowercase characters into upper case
        print(f"The hexadecimal value of {number} is: ", final) #Prints the hexadecimal number
    
    elif user_input == "6": #If the user inputs 6
        os.system("cls") #Clears the screen
        print(ancii) #Prints the ancii art
        number = input("Enter a Hexadecimal number: ") #Asks the user for a Hexadecimal number
        convert = int(number, 16) #Converts the Hexadecimal number to a decimal number
        print(f"The decimal, Denary value of {number} is: ",convert) #Prints the decimal number

    else: #If the user inputs anything else
        main() #Runs the main function again

while 69 < 420: #While loop to keep the program running
    time.sleep(7) #Waits 7 seconds
    main() #Runs the main function
