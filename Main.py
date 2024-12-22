import Registration
import Login


def main():
    while True:
        print("Welcome to Ash NetBanking:")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Choose an option from above to proceed: ")

        if choice == '1' or choice.lower() == 'register':
            Registration.register_user()
        elif choice == '2' or choice.lower() == 'login':
            Login.login_user()
        elif choice == '3' or choice.lower() == 'exit':
            print("Thank You")
            break
        else:
            print("Invalid option. Please try again.\n")


if __name__ == "__main__":
    main()
