# coding=utf-8
import random
passwordPool = ""
lc = "abcdefghijklmnopqrstuvwxyz"
uc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers = "1234567890"
specials = "!()?%&/,.;:-_"
userInput = input("Do you want to generate a password? (y/n)")
if userInput == "y":
    pwLength = int(input("Password length: "))
    while pwLength <1 or pwLength > 20:
        print("Your password-length must be between 1 or 20 long")
        pwLength = int(input("Password length: "))
    boolLowercase = input("Allow lowercase(y/n)? ")
    if boolLowercase == "y":
        passwordPool = passwordPool + lc
    boolUppercase = input("Allow uppercase(y/n)? ")
    if boolUppercase == "y":
        passwordPool = passwordPool + uc
    allowNumbers = input("Allow numbers? ")
    if allowNumbers == "y":
        passwordPool = passwordPool + numbers
    allowSpecials = input("Allow special characters(y/n)? ")
    if allowSpecials == "y":
        passwordPool = passwordPool + specials
    i = 1
    newPassword = ""
    while i <= pwLength:
        newPassword = newPassword + random.choice(passwordPool)
        i = i +1
    print("Your generated password is: " + newPassword)
elif == "n":
	userInput = input("Do you want to choose your own password? (y/n")
    if userInput == "y":
        passwordInput = input("Please write your desired password")
        if passwordInput != "":
            print("Your new password is " + passwordInput)
        else: 
            print("You can't have a empty password")
            passwordInput = input("Please write your desired password")

else: 
	print("That is not a valid option. Session terminating")




