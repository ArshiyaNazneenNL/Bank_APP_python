import mysql.connector


# 4. Print Beneficiaries List
def list_beneficiaries(user):
    print("List of Beneficiaries:")
    try:
        connection = mysql.connector.connect(host="localhost", user="root", password="Arshiya@2307",auth_plugin="mysql_native_password", database="Bank_Sch")

        cursor = connection.cursor()

        sql = "SELECT * FROM Benf WHERE user_name = %s"
        cursor.execute(sql, (user[1],))
        beneficiaries = cursor.fetchall()

        if beneficiaries:
            for beneficiary in beneficiaries:
                print(f"Beneficiary Name: {beneficiary[1]}, Account Number: {beneficiary[2]}, IFSC Code: {beneficiary[3]}")
        else:
            print("No beneficiaries found.")

    except mysql.connector.Error as error:
        print("Error while fetching beneficiaries:", error)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

        from Options import show_options
        show_options(user)
