def main():
    print("___ Welcome to Personal Expense Tracker ___ ")
    print("1. Add a new expense")
    print("2. View expense")
    print("3. Exit")

    choice = input("Choose a number from the menu (1-3): ")

    if choice == '1':
        print("Adding an expense ...")
    elif choice == '2':
        print("Viewing expenses ...")   
    else:
         print("Goodbye!")   
main()         