import os
import time

listOfFood = []

def prettyPrint():
    os.system("clear")
    print("List of Food Orders")
    print()
    counter = 1
    for order in listOfFood:
        print(f"{counter}: {order}")
        counter += 1
    time.sleep(1)

while True:
    os.system("clear")
    print("Yummy Food Restaurant")
    menu = input("1. Order food\n2: Delete order\n3. Leave a review\n> ")
    
    if menu == "1":
        order = input("Order > ")
        listOfFood.append(order)
    elif menu == "2":
        order = input("Delete order > ")
        if order in listOfFood:
            listOfFood.remove(order)
        else:
            print("Order not found.")
            time.sleep(1)
    elif menu == "3":
        prettyPrint()
    else:
        print("Invalid option. Please try again.")
        time.sleep(1)
