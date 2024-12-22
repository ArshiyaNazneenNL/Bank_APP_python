import mysql.connector


# 6. Show Cards
def list_cards(user):
    print("List of Cards:")
    try:
        connection = mysql.connector.connect(host="localhost", user="root", password="Arshiya@2307",auth_plugin="mysql_native_password", database="Bank_Sch")

        cursor = connection.cursor()

        sql = "SELECT * FROM card WHERE user_name = %s"
        cursor.execute(sql, (user[1],))
        cards = cursor.fetchall()

        if cards:
            for card in cards:
                print(f"Card Number: {card[1]}, Card Type: {card[2]}, CVV: {card[4]}, PIN: {card[3]}")
        else:
            print("No cards found.")

    except mysql.connector.Error as error:
        print("Error while fetching cards:", error)
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()

    from Options import show_options
    show_options(user)
