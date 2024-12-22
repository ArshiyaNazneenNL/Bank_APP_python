import mysql.connector


# 10. Update Information
def update_info(user):
    print(f"Update Account Information of {user[0]}:")
    new_address = input("Enter new address: ")

    # Loop until a valid mobile number is entered
    while True:
        new_mobile = input("Enter new mobile number: ")
        if len(new_mobile) == 10 and new_mobile.isdigit() and new_mobile[0] in ['6', '7', '8', '9']:
            break
        else:
            print("Invalid mobile number. Mobile number must be 10 digits starting with 7, 8, or 9.")

    try:
        connection = mysql.connector.connect(host="localhost", user="root", password="Arshiya@2307",auth_plugin="mysql_native_password", database="Bank_Sch")
        cursor = connection.cursor()

        # Update the address and mobile number in the database
        cursor.execute("UPDATE acc_info SET address = %s, mobile_no = %s WHERE user_name = %s", (new_address, new_mobile, user[1]))
        connection.commit()
        print("Account information updated successfully!")

        # user[2] = new_address
        # user[4] = new_mobile

    except mysql.connector.Error as error:
        print("Error while updating account information:", error)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

    from Options import show_options
    show_options(user)
