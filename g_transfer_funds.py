import mysql.connector
import decimal

def transfer_funds(user):
    beneficiary_number = input("Enter beneficiary account number: ")

    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Arshiya@2307",
            auth_plugin="mysql_native_password",
            database="Bank_Sch"
        )
        cursor = connection.cursor()

        # Check if the beneficiary exists
        query = "SELECT * FROM Benf WHERE user_name = %s AND benf_acc_no = %s"
        cursor.execute(query, (user[1], beneficiary_number))
        beneficiary = cursor.fetchone()
        if not beneficiary:
            print("Beneficiary account not found. Please add the beneficiary first.")
            return

        # Input transfer amount
        amount = decimal.Decimal(input("Enter amount to transfer: "))
        if amount <= 0:
            print("Invalid amount. Please enter a positive value.")
            return

        # Check user's current balance
        query = "SELECT acc_balance FROM acc_info WHERE user_name = %s"
        cursor.execute(query, (user[1],))
        sender_balance = cursor.fetchone()
        if not sender_balance:
            print("Sender account not found. Transaction aborted.")
            return

        sender_balance = sender_balance[0]
        if sender_balance < amount:
            print("Insufficient balance. Transaction aborted.")
            return

        # Deduct amount from sender's balance
        new_sender_balance = sender_balance - amount
        update_sender_query = "UPDATE acc_info SET acc_balance = %s WHERE user_name = %s"
        cursor.execute(update_sender_query, (new_sender_balance, user[1]))

        # Add amount to beneficiary's balance
        update_beneficiary_query = "UPDATE acc_info SET acc_balance = acc_balance + %s WHERE user_name = %s"
        cursor.execute(update_beneficiary_query, (amount, beneficiary[0]))

        # Insert the transaction record
        insert_transaction_query = """
            INSERT INTO transaction (sender_acc_no, benf_acc_no, amount) 
            VALUES (%s, %s, %s)
        """
        cursor.execute(insert_transaction_query, (user[0], beneficiary[2], amount))

        connection.commit()  # Commit the changes
        print("Funds transferred successfully.")

    except mysql.connector.Error as error:
        print("Error while updating transaction:", error)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
