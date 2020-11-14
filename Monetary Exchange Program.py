#NAME: Görkem
#SURNAME: Yelken


# For the wait
from time import sleep


# Monetary conversion of Turkish Lira
def tl(amount):
    print("""

>>>>>In TL

            """)

    # To use in another process
    girilen_tutar = amount

    # List of values of TL
    tl = [10000, 5000, 1000, 500, 100, 10]

    # Dictionary for TL
    TL = {10: 'students', 100: 'Mehmet Akif Ersoy', 500: 'İzmir Clock Tower',
          1000: 'Fatih Sultan Mehmet', 5000: 'Mevlana', 10000: 'Mimar Sinan'}

    # List of numbers which dividing the amount and remaining is "0"
    list1 = []

    # List of how many of the numbers which dividing the amount and remaining is "0"
    multiple_list1 = []

    # List of numbers which less than amount
    list2 = []

    # List of how many of the numbers which less than amount in the amount
    multiple_list2 = []

    for value in tl:
        if amount % value == 0:
            list1.append(value)
            multiple_list1.append(int(amount / value))

    for value in tl:
        if value <= amount:
            list2.append(value)
            multiple = int(amount / value)
            multiple_list2.append(multiple)
            amount = amount - (multiple * value)

    # Amount is equal to banknote
    if girilen_tutar == 10000 or girilen_tutar == 5000 or girilen_tutar == 1000 or girilen_tutar == 500 or girilen_tutar == 100 or girilen_tutar == 10:
        keys = []
        for a in list1:
            if a in TL:
                keys.append(TL[a])

        keys_dict = dict(zip(multiple_list1, keys))

        for a, b in keys_dict.items():
            print("{} {} .".format(a, b))

    # Amount is not equal to banknote
    else:

        # List of corresponding keys
        keys1 = []
        for a in list1:
            if a in TL:
                keys1.append(TL[a])

        # List of combination of multiple_list1 and keys1
        keys_list = list(zip(multiple_list1, keys1))

        for i in keys_list:
            print(i[0], i[1], ".")

        print("""
              OR
              """)

        # List of corresponding keys
        keys2 = []
        for a in list2:
            if a in TL:
                keys2.append(TL[a])

        # List of combination of multiple_list2 and keys2
        liste = list(zip(multiple_list2, keys2))

        for i in liste:
            print(i[0], i[1], ".", end=' ')


# Monetary conversion of French Franc

def ff(amount):
    print("""
            
        ***************
            
        """)
    print("""

>>>>>In FF

            """)

    # To use in another process
    ınput_amount = amount

    # List of values of FF
    ff = [500, 200, 100, 50, 20, 10]

    # Dictionary for TL
    FF = {10: 'Hector Berlioz', 20: 'Claude-Achille Debussy', 50: 'Antoine de Saint-Exupery',
              100: 'Paul Cezanne', 200: 'Gustave Eiffel', 500: 'Marie Curie'}

    # List of numbers which dividing the amount and remaining is "0"
    list1 = []

    # List of how many of the numbers which dividing the amount and remaining is "0"
    multiple_list1 = []

    # List of numbers which less than amount
    list2 = []

    # List of how many of the numbers which less than amount in the amount
    multiple_list2 = []

    for value in ff:
        if amount % value == 0:
            list1.append(value)
            multiple_list1.append(int(amount / value))

    for value in ff:
        if value <= amount:
            list2.append(value)
            multiple = int(amount / value)
            multiple_list2.append(multiple)
            amount = amount - (multiple * value)

    # Amount is equal to banknote
    if ınput_amount == 10000 or ınput_amount == 5000 or ınput_amount == 1000 or ınput_amount == 500 or ınput_amount == 100 or ınput_amount == 10:
        keys = []
        for a in list1:
            if a in FF:
                keys.append(FF[a])

        keys_dict = dict(zip(multiple_list1, keys))

        for a, b in keys_dict.items():
            print("{} {} .".format(a, b))

    # Amount is not equal to banknote
    else:

        # List of corresponding keys
        keys1 = []
        for a in list1:
            if a in FF:
                keys1.append(FF[a])

        # List of combination of multiple_list1 and keys1
        keys_list = list(zip(multiple_list1, keys1))

        for i in keys_list:
            print(i[0], i[1], ".")

        print("""
              OR
              """)

        # List of corresponding keys
        keys2 = []
        for a in list2:
            if a in FF:
                keys2.append(FF[a])

        # List of combination of multiple_list2 and keys2
        liste = list(zip(multiple_list2, keys2))

        for i in liste:
            print(i[0], i[1], ".", end=' ')


# Monetary conversion of Deutsche Mark

def dm(amount):
    print("""
            
        ***************
            
        """)
    print("""

>>>>>In DM

            """)

    # To use in another process
    ınput_amount = amount

    # List of values of FF
    dm = [500, 200, 100, 50, 20, 10]

    # Dictionary for TL
    DM = {10: 'Carl Friedrich Gauss', 20: 'Annette von Droste-Hülshoff', 50: 'Balthasar Neumann',
              100: 'Clara Schumann', 200: 'Paul Ehrlich', 500: 'Maria Sibylla Merian', 1000: 'Wilhelm'}

    # List of numbers which dividing the amount and remaining is "0"
    list1 = []

    # List of how many of the numbers which dividing the amount and remaining is "0"
    multiple_list1 = []

    # List of numbers which less than amount
    list2 = []

    # List of how many of the numbers which less than amount in the amount
    multiple_list2 = []

    for value in dm:
        if amount % value == 0:
            list1.append(value)
            multiple_list1.append(int(amount / value))

    for value in dm:
        if value <= amount:
            list2.append(value)
            multiple = int(amount / value)
            multiple_list2.append(multiple)
            amount = amount - (multiple * value)

    # Amount is equal to banknote
    if ınput_amount == 10000 or ınput_amount == 5000 or ınput_amount == 1000 or ınput_amount == 500 or ınput_amount == 100 or ınput_amount == 10:
        keys = []
        for a in list1:
            if a in DM:
                keys.append(DM[a])

        keys_dict = dict(zip(multiple_list1, keys))

        for a, b in keys_dict.items():
            print("{} {} .".format(a, b))

    # Amount is not equal to banknote
    else:

        # List of corresponding keys
        keys1 = []
        for a in list1:
            if a in DM:
                keys1.append(DM[a])

        # List of combination of multiple_list1 and keys1
        keys_list = list(zip(multiple_list1, keys1))

        for i in keys_list:
            print(i[0], i[1], ".")

        print("""
              OR
              """)

        # List of corresponding keys
        keys2 = []
        for a in list2:
            if a in DM:
                keys2.append(DM[a])

        # List of combination of multiple_list2 and keys2
        liste = list(zip(multiple_list2, keys2))

        for i in liste:
            print(i[0], i[1], ".", end=' ')


# Welcome

print("""
      *****************

      Monetary Exchange

      *****************
      """)


# Selection

print("""
      Please select your option;

1 for Currency
2 for Goods

""")


selection = input("Selection : ")


# Selection for Currency

if selection == "1":

    # Selection of Currency

    while True:
        currency = str(input("Please enter currency : ")).lower()
        if currency == "ff" or currency == "tl" or currency == "dm":
            break
        else:
            print("Please try again...")

    # Selection of Amount (Exception Handling)
    
    while True:
        amount = input("Please enter amount : ")
        if not amount:
            break
        try:
            amount = int(amount)
            break
        except:
            print("Invalid amount. Please try again...")
            continue

    print("Your Anahtar result of {} {} is : ".format(amount, currency))

    print("Converting...")

    sleep(5)

    # Run functions

    tl(amount)
    ff(amount)
    dm(amount)


# Selection for Goods

elif selection == "2":
    print(
        "List of objects is : [ Computer , Keyboard , Laptop , Monitor , Mouse ]")

    # Selection of Object

    while True:
        object = str(input("Please Enter Object : ")).lower()
        if object == "computer" or object == "keyboard" or object == "laptop" or object == "monitor" or object == "mouse":
            break
        else:
            print("Please try again...")

    objects = {'computer': 5000, 'monitor': 2080,
               'laptop': 4200, 'keyboard': 120, 'mouse': 220}

    print("The value of a {} is {}.".format(object, objects[object]))

    print("Your Anahtar result of a {} is : ".format(object))

    amount = objects[object]

    print("Converting...")

    sleep(5)

    # Run functions

    tl(amount)
    ff(amount)
    dm(amount)

# Invalid Selection

else:
    print("Invalid operation!")
    print("Exiting...")
    sleep(3)