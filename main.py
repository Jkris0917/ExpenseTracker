from func import ExpenseManager

manager = ExpenseManager()

print("=" *30)
print("Welcome to Expense Tracker!")
print("=" *30)

while True:
    choice = input("\n[1]View [2]Add [3]Delete [4]Search [5]Total [6]Exit\nChoose: ")
    
    if not choice.isdigit():
        print("Invalid — please enter a number.")
        continue
    
    choice = int(choice)
    
    if choice == 1:
        manager.display_all()
    elif choice == 2:
        manager.add(input("Category: "), input("Amount: "), input("Note: ") or None)
    elif choice == 3:
        manager.display_all()
        manager.delete(int(input("ID to delete: ")))
    elif choice == 4:
        results = manager.search(input("Keyword: "))
        if results:
            for e in results: print(e)
        else:
            print("No matching expenses found.")
    elif choice == 5:
        print(f"\nTotal: ¥{manager.total()}")
        print("By category:")
        for cat, total in manager.by_category().items():
            print(f"  {cat}: ¥{total}")
    elif choice == 6:
        print("=" * 40)
        print("Thank you for using Expense Tracker!")
        print("=" * 40)
        break
    else:
        print("Invalid choice. Please select 1–6.")