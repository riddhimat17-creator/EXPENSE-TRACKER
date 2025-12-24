while True:
    print("\n---EXPENSE TRACKER---")
    print("1. Add expenses")
    print("2. View total expenses")
    print("3. View category-wise expenses")
    print("4. Exit")
    choice = input("enter your choice(1-4):")
    if choice == "1":
        category = input("enter the name of the category:")
        amount = input("enter the amount of the category:")
        file = open("expenses.txt" , "a")
        file.write(category + "," + amount + "\n")
        file.close()
        print("expenses added successfully!")
    
    elif choice == "2":
        try:
            file = open("expenses.txt" , "r")
            expenses = file.readlines()
            file.close()
            total = 0
            for line in expenses:
                category , amount = line.strip().split(",")
                total += int(amount)
                print("total expenses are :", total)
        except FileNotFoundError:
            print("No expenses file found..")
    elif choice == "3":
        try:
            file = open("expenses.txt", "r")
            expenses = file.readlines()
            file.close()
            category_expenses = {}
            for line in expenses:
                category , amount = line.strip().split(",")
                amount = int(amount)
                if category in category_expenses:
                    category_expenses[category] += amount
                else:
                    category_expenses[category] = amount
            print("\nCATEGORY-WISE EXPENSES :")
            for cat , amt in category_expenses.items():
                print(cat , ":" , amt)
        except FileNotFoundError:
                print("No expenses file found..!")
    elif choice == "4":
        print("exiting the expense tracker...")
        break
    else:
        print("invalid request...")

