import utils
from person import Person
from bank_account import BankAccount

def main():
    people = [] 

    while True:
        print("\nChoose an option:")
        print("1. Add a new person")
        print("2. Add an account to a person")
        print("3. Show all balances")
        print("4. Quit")

        choice = input().strip()

        if choice == "1":
            new_person = utils.person_data()
            people.append(new_person)

        elif choice == "2":
            # Pide el nombre de la persona
            target_name = input("Enter the person's name: ")
            found = False
            
            for person in people:
                if person.name == target_name:
                    acc_num = int(input("Enter a 4-digit account number: "))
                    init_balance = float(input("Enter the initial balance: "))
                    
                    person.add_account(BankAccount(acc_num, init_balance))
                    found = True
                    break
            
            if not found:
                print("Person not found.")

        elif choice == "3":
            if not people:
                print("No data to show.")
            else:
                utils.balance_summary(people)

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid option. Please choose 1-4.")

if __name__ == "__main__":
    main()

