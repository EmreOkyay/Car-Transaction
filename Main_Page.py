import Storage
import Transactions

while True:
    i = int(input("\n1 --> Purchase a Car\n"
                  "2 --> Purchase Options\n"
                  "3 --> Cars with Owners\n"
                  "4 --> Cars without Owners\n"
                  "0 --> Exit\n"
                  "Enter: "))
    if i == 1:
        z = 0
        answer = str(input("\nAre you buying a first-hand or a second-hand car?\n"  # User can either buy a first or 
                           "Enter: "))                                              # a second hand car
        if answer == "first" or answer == "first-hand":
            print("\n", "Accounts: ", Storage.Storage.User_Dic)
            print("\n", "Available Cars: ", Storage.Storage.Car_Name_List)
            x = str(input("\nWho is buying the car?\n"
                          "Enter a name: "))
            y = int(input("\nWhich car?\n"
                          "Enter an index number: "))
            Transactions.Transactions(x, y, z, i)
        elif answer == "second" or answer == "second-hand":
            i = 11
            print("\n", "Accounts: ", Storage.Storage.User_Dic)
            print("\n", "Owned Cars: ", Storage.Storage.Ownership_Dic)
            x = str(input("\nWho is buying the car?\n"
                          "Enter a name: "))
            y = str(input("\nFrom whom he/she is buying?\n"
                          "Enter a name: "))
            print(y, "'s Cars: ", Storage.Storage.Ownership_Dic[y])
            z = int(input("\nSelect the car you want to buy\n"
                          "Enter an index number: "))
            Transactions.Transactions(x, y, z, i)
    elif i == 2:                # User can buy options for his/her car
        print("\n", Storage.Storage.User_Dic)
        print("\n", Storage.Storage.Option_Dic)
        x = str(input("\nWho is buying an option?\n"
                      "Enter a name: "))
        print("\n", Storage.Storage.Ownership_Dic[x])
        y = int(input("\nFor which car?\n"
                      "Enter an index number: "))
        z = str(input("\nWhich option?\n"
                      "Enter an option name: "))
        Transactions.Transactions(x, y, z, i)
    elif i == 3:                # Shows cars with owners
        Transactions.Transactions(0, 0, 0, i)
    elif i == 4:                # Shows cars without owners
        Transactions.Transactions(0, 0, 0, i)
    elif i == 0:
        break
    else:
        print("Unrecognized Option\n")
