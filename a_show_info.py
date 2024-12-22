import mysql.connector
from b_add_funds import *

# 1. Display Account Information
def show_account_info(user):
    try:
        connection = mysql.connector.connect(host="localhost", user="root", password="Arshiya@2307", auth_plugin="mysql_native_password", database="Bank_Sch")
        cursor = connection.cursor()

        # Query to fetch full account information
        query = """
        SELECT acc_no,user_name, address, mobile_no, aadhar_no, acc_balance 
        FROM acc_info 
        WHERE acc_no = %s
        """
        cursor.execute(query, (user[0],))
        account_info = cursor.fetchone()

        if account_info:
            acc_no,user_name, address, mobile_no, aadhar_no, acc_balance  = account_info
            print("Account Information:")
            print("Account Number:", acc_no)
            print("Account Name:", user_name)
            print("Address:", address)
            print("Phone:", mobile_no)
            print("Aadhar Number:", aadhar_no)
            print("Balance:", acc_balance)
        else:
            print("No account information found.")

    except mysql.connector.Error as err:
        print("Error:", err)

    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

    from Options import show_options
    show_options(user)

    if balance == 0:
        print("Account balance is 0. Make Deposit? (y for yes or another key for no):")
        decision = input().lower()
        if decision == 'yes':
            initiate_deposit(user)
            print("Transaction Successful!")
            show_options(user)
        else:
            show_options(user)
