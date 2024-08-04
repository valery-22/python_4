import os
import time

listOfEmail = []

def prettyPrint():
    os.system("clear")
    print("List of Emails")
    print()
    counter = 1
    for email in listOfEmail:
        print(f"{counter}: {email}")
        counter += 1
    time.sleep(1)

def spam(max_count):
    for i in range(min(max_count, len(listOfEmail))):
        print(f"""Email {i + 1}

Dear {listOfEmail[i]}
It has come to our attention that you're missing out on the amazing Replit 100 days of code. We insist you do it right away. If you don't we will pass on your email address to every spammer we've ever encountered and also sign you up to the My Little Pony newsletter, because that's neat. We might just do that anyway.

Love and hugs,

Ian Spammington III""")
        time.sleep(1)
        os.system("clear")

while True:
    print("SPAMMER Inc.")
    menu = input("1: Add email\n2: Remove email\n3: Show emails\n4: Get SPAMMING\n> ")
    if menu == "1":
        email = input("Email > ")
        listOfEmail.append(email)
    elif menu == "2":
        email = input("Email > ")
        if email in listOfEmail:
            listOfEmail.remove(email)
    elif menu == "3":
        prettyPrint()
    elif menu == "4":
        max_count = input("Enter the number of emails to spam > ")
        try:
            max_count = int(max_count)
            spam(max_count)
        except ValueError:
            print("Please enter a valid number.")
            time.sleep(1)
    time.sleep(1)
    os.system("clear")

