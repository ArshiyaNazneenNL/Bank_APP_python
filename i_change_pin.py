import mysql.connector

# 9. Change Pin
def change_pin(user):
    from Options import show_options

    card_number = input("Enter card number: ").replace(" ", "")  # Remove spaces from the card number

    try:
        connection = mysql.connector.connect(host="localhost", user="root", password="Arshiya@2307", auth_plugin="mysql_native_password", database="Bank_Sch")
        cursor = connection.cursor()

        # Check if the card exists in the database
        query = "SELECT * FROM card WHERE card_no = %s"
        cursor.execute(query, (card_number,))
        card = cursor.fetchone()

        if not card:
            print("Card not found. Please enter valid card details.")
            return show_options(user)
        else:
            old_pin = int(card[3])
            print('Old pin is: ', old_pin)

        while True:
            new_pin = input("Enter new PIN: ")
            if len(new_pin) != 4:
                print("Please enter 4 digit PIN.")
                continue

            if old_pin == new_pin:
                print("Entered Old PIN. Please enter new PIN.")
                continue

            if not new_pin.isdigit():
                print("Invalid PIN. Please enter only digits.")
                continue

            break  # Exit loop once a valid PIN is entered

        # Update the PIN
        query = "UPDATE card SET pin = %s WHERE card_no = %s"
        cursor.execute(query, (new_pin, card_number))
        connection.commit()  # Ensure commit after update

        print("PIN changed successfully.")

    except mysql.connector.Error as err:
        print("Error:", err)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

    show_options(user)
