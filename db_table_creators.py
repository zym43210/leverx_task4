def create_db(cursor):
    cursor.execute(" CREATE DATABASE IF NOT EXISTS task4")


def create_rooms_table(cursor):
    cursor.execute("CREATE TABLE IF NOT EXISTS rooms"
                   " (id varchar (255) unique , "
                   "name INTEGER primary key "
                   ")")


def create_students_table(cursor):
    cursor.execute("CREATE TABLE IF NOT EXISTS students "
                   "(birthday DATE,"
                   "id varchar(100) primary key, "
                   "name VARCHAR(255),"
                   "room INTEGER ,"
                   "sex VARCHAR (2),"
                   " FOREIGN KEY (room)  REFERENCES rooms (name)"
                   ")")
