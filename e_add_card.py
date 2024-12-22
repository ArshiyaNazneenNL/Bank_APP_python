import mysql.connector

def add_card(user):
    print("Choose the card type, 1.Debit or 2.Credit: ")
    card_type = input("Enter your choice (1/2): ")

    card_no = input("Enter card number: ")

    # Validate card number length and numeric value
    if not card_no.isdigit() or len(card_no) > 16:
        print("Invalid card number. Please enter a numeric value with up to 16 digits.")
        return

    pin = input("Enter a 4-digit PIN: ")
    cvv = input("Enter a 3-digit CVV: ")

    # Validate PIN and CVV lengths
    if not (pin.isdigit() and len(pin) == 4):
        print("Invalid PIN. Ensure it is a 4-digit numeric value.")
        return
    if not (cvv.isdigit() and len(cvv) == 3):
        print("Invalid CVV. Ensure it is a 3-digit numeric value.")
        return

    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Arshiya@2307",
            auth_plugin="mysql_native_password",
            database="Bank_Sch"
        )

        cursor = connection.cursor()

        # Insert the card details into the table
        sql = "INSERT INTO card (user_name, card_no, card_type, pin, cvv) VALUES (%s, %s, %s, %s, %s)"
        val = (user[1], card_no, "Debit" if card_type == "1" else "Credit", pin, cvv)
        cursor.execute(sql, val)
        connection.commit()

        print("Card added successfully!")

    except mysql.connector.Error as error:
        print("Error while adding card:", error)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
