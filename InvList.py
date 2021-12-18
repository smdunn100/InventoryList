import os
import time

# Author: Stephen Dunn


def Clearer():
    os.system('cls')


def Title():
    print('\nItemized Inventory System')
    print('_________________________\n')


def PList(l1, l2):
    Clearer()
    if l1:
        place = 0
        for i in l1:
            print(f'\nItem {place+1}: {l1[place]}')
            print("Quantity:", l2[place])
            place += 1
        print('\n')
    else:
        Clearer()
        print("List is empty")
        time.sleep(2)
        Clearer()


def AddI(l1, l2):
    Clearer()
    item1 = 'filler'
    item2 = 'filler'
    while not item1 == '':
        item1 = input("\nAdd an item: ")
        if item1 == '':
            print("Exiting to Main Menu")
            time.sleep(2)
        elif item1.isalpha():
            flag = 'N'
            while flag == 'N':
                item2 = input("Add an quantity: ")
                if item2 == '':
                    item1 = ''
                    flag = 'Y'
                    print("Exiting to Main Menu")
                    time.sleep(2)
                elif item2[0].isdigit():
                    l1.append(item1)
                    l2.append(item2)
                    flag = 'Y'
                else:
                    print("You must enter a numeric quantity")
        else:
            print("You must enter the item before quantity: ")

    Clearer()


def RemI(l1, l2):
    item1 = 'filler'
    while item1 != '':
        PList(l1, l2)
        item1 = input("remove an item by name: ")
        if item1 == '':
            print("Exiting to Main Menu")
            time.sleep(2)
        elif item1 not in l1:
            print("Item not in list. Try again or press enter to exit.")
            time.sleep(2)
        else:
            spot = l1.index(item1)
            rem1 = l1.pop(spot)
            rem2 = l2.pop(spot)
            print(f'You Removed - Item: {rem1} | Qty: {rem2}')
            time.sleep(2)
    Clearer()


def ClearL(l1, l2):
    Clearer()
    l1.clear()
    l2.clear()
    print('List Cleared\n')
    time.sleep(2)
    Clearer()


def main():
    listI = []
    listQ = []
    stopper = 'N'
    Title()
    while stopper == 'N':
        print("Menu\n1) PRINT LIST\n2) ADD ITEM\n3) REMOVE ITEM\n4) CLEAR LIST\n5) QUIT")
        choice = input("Enter a selection: ")
        if choice == '1':
            PList(listI, listQ)
            stopper = 'N'
        elif choice == '2':
            AddI(listI, listQ)
            stopper = 'N'
        elif choice == '3':
            RemI(listI, listQ)
            stopper = 'N'
        elif choice == '4':
            ClearL(listI, listQ)
            stopper = 'N'
        elif choice == '5':
            stopper = 'Y'
            Clearer()
            print("\nHave a Nice Day!")
        else:
            stopper = 'N'
            Clearer()
            print("Please enter an option from the list")


main()
