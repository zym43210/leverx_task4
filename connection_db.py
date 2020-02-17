import mysql.connector


def sql_connector():
    my_db = mysql.connector.connect(
        user="root",
        passwd="root",
        host="localhost",
        database="task4"
    )
    return my_db
