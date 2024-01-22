#Sebastian de Wijkerslooth
#1/22/23
#Magic 8 Ball
import random
#Initialize
responses = ["Most Definately", "Absolutely Not", "Only Time Will Tell", "Ask Again Later", "Most Likely", "My sources say no", "Concentrate and Ask Again", "Very Doubtful", "You May Rely On It", "Signs point to yes"]
print("Hello, welcome to the Magic 8 Ball!")
while True:
    start = input("Are you ready to get your fortune?(y)(n) ")
    if start == "y":
        fortune = input("What would you like your fortune told on? ")
        x = fortune.endswith("?")
        if x == True: 
            print(random.choice(responses))
            pagain = input("Would you like to play again?(y)(n) ")
            if pagain == "y":
                print("Hello, welcome to the Magic 8 Ball!")
            if pagain == "n":
                print("Thank you for playing!")
                break
        if x == False:
            print("Please try again and make sure to end with a (?)")
    if start == "n":
        break
