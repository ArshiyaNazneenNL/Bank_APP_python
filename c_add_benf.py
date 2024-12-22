import mysql.connector
from d_list_benf import list_beneficiaries


# 3. Add Beneficiaries
def add_beneficiary(user):
    print("Add Beneficiary Details:")
    while True:
        # username = user[1]
        benef_name = input("Enter beneficiary name: ")
        benef_account_number = int(input("Enter beneficiary account number: "))
        benef_ifsc = input("Enter beneficiary IFSC Code: ")

        try:
            connection = mysql.connector.connect(host="localhost", user="root", password="Arshiya@2307", auth_plugin="mysql_native_password", database="Bank_Sch")

            cursor = connection.cursor()

            # Check if the beneficiary account number and name match in the users table
            cursor.execute("SELECT * FROM acc_info WHERE acc_no = %s AND user_name = %s", (benef_account_number, benef_name))
            beneficiary_data = cursor.fetchone()
            if beneficiary_data is None:
                print("Beneficiary account number does not match the provided name.")
                retry = input("Do you want to retry? (yes/no): ").lower()
                if retry != 'yes':
                    break
                continue

            # Check if the benef_ifsc exists in the Benf table
            # cursor.execute("SELECT * FROM BankIFSC WHERE IFSC_Code = %s", (benef_ifsc,))
            # if not cursor.fetchone():
            #     print("Beneficiary IFSC Code does not exist in the database.")
            #     retry = input("Do you want to retry? (yes/no): ").lower()
            #     if retry != 'yes':
            #         break
            #     continue

            # Insert the beneficiary into the beneficiaries table
            sql = "INSERT INTO Benf (user_name, benf_name, benf_acc_no, Benf_ifsc) VALUES (%s, %s, %s, %s)"
            val = (user[1], benef_name, benef_account_number, benef_ifsc)
            cursor.execute(sql, val)
            connection.commit()
            print("Beneficiary added successfully!")
            break

        except mysql.connector.Error as error:
            print("Error while adding beneficiary:", error)
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()

            list_beneficiaries(user)
