def insert_in_rooms(data_rooms, cursor):
    for room in data_rooms:
        sql_room = "INSERT IGNORE INTO rooms (id, name) VALUES (%s, %s)"

        room_val = (room["id"], room["name"])
        cursor.execute(sql_room, room_val)


def insert_in_students(data_students, cursor):
    for student in data_students:
        sql_student = "INSERT IGNORE INTO  students (birthday,id, name,room,sex) VALUES (%s , %s,%s,%s,%s)"
        student_val = (student["birthday"], student["id"], student["name"], student["room"], student["sex"])
        cursor.execute(sql_student, student_val)
