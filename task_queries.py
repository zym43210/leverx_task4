def room_list_and_stud_number(cursor):
    cursor.execute('select room,'
                   'count(room) as count from students '
                   'group by room')
    result_list = cursor.fetchall()
    print("room list and students number")

    return result_list


def top_five_rooms_lowest_avg_age(cursor):
    cursor.execute("SELECT room,"
                   "avg(((YEAR(CURRENT_DATE) - YEAR(students.birthday)) - "
                   "(DATE_FORMAT(CURRENT_DATE, '%m%d') < DATE_FORMAT(birthday, '%m%d'))"
                   ")) AS room_age_avg "
                   "FROM students group by room order by room_age_avg limit 5;")
    result_list = str(cursor.fetchall())
    print("top 5 rooms with lowest average age")

    return result_list

def top_five_with_biggest_dif(cursor):
    cursor.execute(
        "SELECT room FROM students group by room order by (max(((YEAR(CURRENT_DATE) - YEAR(students.birthday)) -"
        "(DATE_FORMAT(CURRENT_DATE, '%m%d') < DATE_FORMAT(birthday, '%m%d'))"
        ")) -"
        "min(((YEAR(CURRENT_DATE) - YEAR(students.birthday)) -"
        "(DATE_FORMAT(CURRENT_DATE, '%m%d') < DATE_FORMAT(birthday, '%m%d'))"
        ")) ) desc limit 5;")

    result_list = cursor.fetchall()
    print("top 5 with biggest difference")

    return result_list
def list_with_dif_sex(cursor):
    cursor.execute(
        'select DISTINCT male.room from students'
        ' as male join students as female on male.room=female.room '
        'where male.sex <> female.sex order by room;')
    result_list = cursor.fetchall()
    print("list with difference sex")
    return result_list

def to_show(showing_list):
    for x in showing_list:
        print(x)
