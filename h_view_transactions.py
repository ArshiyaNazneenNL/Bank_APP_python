import mysql.connector


# 8. View Transaction
def view_transactions(user):

    try:
        connection = mysql.connector.connect(host="localhost", user="root", password="Arshiya@2307", auth_plugin="mysql_native_password",database="Bank_Sch")
        cursor = connection.cursor()
        # SQL query to fetch transaction details along with sender and beneficiary names for a specific user
        query = """
        SELECT 
            t.idtransaction, 
            u.user_name AS sender_name, 
            b.benf_name, 
            t.amount, 
            t.tr_timestamp
        FROM Transaction t
        INNER JOIN acc_info u ON t.sender_acc_no = u.acc_no
        INNER JOIN Benf b ON t.benf_acc_no = b.benf_acc_no
        WHERE t.sender_acc_no = %s OR t.benf_acc_no = %s
        """

        # Execute the query with user_id as parameter
        cursor.execute(query, (user[0], user[0]))

        # Fetch all rows
        transactions = cursor.fetchall()

        # Check if transactions are not found
        if not transactions:
            print("No transactions found.")
        else:
            # Print column headers
            print("{:<15} {:<20} {:<20} {:<10} {:<25}".format(
                "Transaction ID", "Sender Name", "Beneficiary Name", "Amount", "Transaction Date"))
            print("= " * 90)

            # Print each transaction
            for transaction in transactions:
                # Determine if the user is the sender or beneficiary
                if transaction[1] == user[0]:  # User is the sender
                    user_role = "Sender"
                else:  # User is the beneficiary
                    user_role = "Beneficiary"

                # Format the transaction date
                transaction_date = transaction[4].strftime("%Y-%m-%d %H:%M:%S")

                print("{:<15} {:<20} {:<20} {:<10} {:<25}".format(
                    transaction[0], transaction[1], transaction[2], transaction[3], transaction_date))

    except mysql.connector.Error as err:
        print("Error:", err)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

    from Options import show_options
    show_options(user)
