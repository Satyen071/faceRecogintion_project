# Importing module
import mysql.connector


# Creating connection object
# mydb = mysql.connector.connect(
#     host="localhost",
#     user="root",
#     password="Ladder@123"
# )
#
# # Printing the connection object
# print(mydb)
# cursor = mydb.cursor()
#
# # Show database
# cursor.execute("SHOW DATABASES")
#
# for x in cursor:
#     print(x)

def connect_mysql_database(server: str, username: str, password: str) -> tuple:
    '''Connects to a MySQL server and sets the table names for 3 required tables'''
    try:
        config = {
            "host": server,
            "user": username,
            "password": password
        }

        connection = mysql.connector.connect(**config)
        cursor = connection.cursor()

        return connection, cursor

    except:
        print("Couldn't connect to MySQL database server! Please check your credentials.")
        exit()
