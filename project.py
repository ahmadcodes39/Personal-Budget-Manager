income_source=[]
budget_items=[]


def add_income():
    existing_sources=set()
    print('\t----------------Income Sources----------------')
    while True:
        print("\tPress 1 to add income source, 0 to exit")
        try:
            choice = int(input('\t> '))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        
        if choice == 1:
            while True:
                print("\tEnter Name: ")
                name = input("\t> ").strip().capitalize()
                if name in existing_sources:
                    print('This income source already exist, try with different one ')
                    continue
                print(f'\tEnter amount for {name}')
                try:
                    amount = int(input('\t> '))
                except ValueError:
                    print("Invalid amount. Please enter a valid number.")
                    continue
                
                income_source.append((name, amount))
                existing_sources.add(name)
                
                print('\tAdd more income sources (y/n) ')
                option = input('\t> ').strip().lower()
                
                if option == 'n':
                    break  
        elif choice == 0:
            break  
        else:
            print("\tInvalid choice. Please enter 1 to add or 0 to exit.")
    
    print("\n\tIncome Sources Added:")
    i=1
    for source in income_source:
        print(f"\t{i}:{source[0]}: {source[1]}")
        i+=1

def record_expense():
    print('\t----------------Record Expense----------------')
    while True:
        print('\tPress 1 to record Expenses, 0 for Exit ')
        try:
            option = int(input('\t> '))
        except ValueError:
            print("\tInvalid input. Please enter a number.")
            continue
        if option == 1:
            while True:
                print('\tEnter Item name')
                name = input('\t> ').strip().capitalize()
                
                item_exists = False
                for item in budget_items:
                    if item['name'] == name:
                        item_exists = True
                        print(f'\tEnter expense amount for {name}:')
                        try:
                            amount = int(input('\t> '))
                        except ValueError:
                            print("\tInvalid input. Please enter a number.")
                            continue
                        if amount <= 0:
                            print('Amount cannot be Zero or negative')
                            continue
                        
                        item['spent'] += amount
                        item['remaining'] -= amount
                        break

                if not item_exists:
                    print(f'\tEnter expense amount for {name}:')
                    try:
                        amount = int(input('\t> '))
                    except ValueError:
                        print("\tInvalid input. Please enter a number.")
                        continue
                    if amount <= 0:
                        print('Amount cannot be Zero or negative')
                        continue
                    print('\tEnter description (optional): ')
                    description = input('\t> ')
                    if not description:
                        description = 'No description Provided'
                    budget_items.append({
                        'name': name,
                        'budget': 0,
                        'spent': amount,
                        'remaining': -amount, 
                        'description': description
                    })

                print('\tAdd more Items (y/n): ')
                choice = input('\t> ').strip().lower()
                if choice == 'n':
                    break
        elif option == 0:
            break
        else:
            print("\tInvalid choice. Please enter 1 to add or 0 to exit.")
        print('\tAll Expenses Recorded Successfully!')
    
def set_budget():
    print('\t----------------Set Budgets----------------')
    while True:
        print("\tPress 1 to set Budgets, 0 to exit")
        try:
            choice = int(input('\t> '))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        if choice == 1:
            while True:
                print("\tEnter Name: ")
                name = input("\t> ").strip().capitalize()
                
                item_exists = False
                for item in budget_items:
                    if item['name'] == name:
                        item_exists = True
                        print(f'\tEnter amount for {name}')
                        try:
                            amount = int(input('\t> '))
                        except ValueError:
                            print("Invalid amount. Please enter a valid number.")
                            continue

                        item['budget'] = amount
                        item['remaining'] = amount - item['spent']
                        break

                if not item_exists:
                    print(f'\tEnter amount for {name}')
                    try:
                        amount = int(input('\t> '))
                    except ValueError:
                        print("Invalid amount. Please enter a valid number.")
                        continue

                    budget_items.append({
                        'name': name,
                        'budget': amount,
                        'spent': 0,
                        'remaining': amount,
                        'description': 'No description provided'
                    })

                print('\tSet more Budgets (y/n) ')
                option = input('\t> ').strip().lower()

                if option == 'n':
                    break
        elif choice == 0:
            break
        else:
            print("\tInvalid choice. Please enter 1 to add or 0 to exit.")

    print("\n\tBudgets set successfully:")


def budget_summary():
    i=j=total_income=total_expensee=0
    print('\n\t\t===========================Budget Summary==========================\n')
    print("\t\tIncome Sources\n")
    for source in income_source:
        print(f"\t\t{i+1}:  {source[0]} - ${source[1]}")
        total_income+=int(source[1])
        i+=1
    print(f'\n\t\tTotal Income: {total_income}')
    print('\t\tTotal Expenses:\n')
    for items in budget_items:
        if 'spent' in items:
            print(f"\t\t{j+1}:  {items['name']} - ${items['spent']} [Desceiption: {items['description']}] ")
            total_expensee+=int(items['spent'])
            j+=1
    print(f'\n\t\tTotal Expense: {total_expensee}\n')
    net_profit = total_income-total_expensee
    print(f'\t\tNet Profit:{net_profit}\n')
    if total_expensee>total_income:
        print('\t\t===========================================================')
        print("\t\t|| NOTE: DANGER ⚠ Your Expenses are more then Total Income||")
        print('\t\t||========================================================||')
    elif total_expensee<total_income:
        print('\t\t==============================================================')
        print("\t\t|| NOTE: GOOD JOB 👋 Your Expenses are less then Total Income||")
        print('\t\t||===========================================================||\n')
    else:
        print('\t\t==============================================================')
        print("\t\t|| NOTE: SAVE ZONE ✅ Your Expenses are equal to Total Income||")
        print('\t\t||===========================================================||\n')

def budget_overview():
    print('------------------ Budget Overview -------------------\n')
    print('Category\t\t | Budget\t\t | Spent\t\t| Remaining\t\t| Details')
    for product in budget_items:
        print(f"{product['name']}\t\t\t | {product['budget']}\t\t\t | {product['spent']}\t\t\t| {product['remaining']}\t\t\t| {product['description']}")

def view_summary():
    budget_summary()
    budget_overview()
  



# Main Function
while True:
        print('\t=============================')
        print('\t Personal Budget Manager')
        print('\t=============================')
        print('\t1. Add Income')
        print('\t2. Record Expense')
        print('\t3. Set Budget')
        print('\t4. View Summary')
        print('\t5. Exit')
        option = int(input('\tPlease select an opt     ion (1-5): '))
        if option == 1:
            add_income()
        elif option == 2:
            record_expense()
        elif option == 3:
            set_budget()
        elif option == 4:
            view_summary()
        elif option == 5:
            break
        else:
            print("Invalid option, please select a number between 1 and 5.")
