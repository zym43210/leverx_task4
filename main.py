import connection_db
import args_parsing
import file_worker
import db_table_creators
import data_insert
import task_queries
import formatter
from xml.dom import minidom

args = args_parsing.parse_arguments()

data_rooms = file_worker.rooms_transformer(args.rooms_path)
data_students = file_worker.file_reader(args.students_path)

my_database = connection_db.sql_connector()

my_cursor = my_database.cursor()

db_table_creators.create_db(my_cursor)

db_table_creators.create_rooms_table(my_cursor)
db_table_creators.create_students_table(my_cursor)

data_insert.insert_in_rooms(data_rooms, my_cursor)

data_insert.insert_in_students(data_students, my_cursor)
task_list = [task_queries.room_list_and_stud_number(my_cursor), task_queries.top_five_rooms_lowest_avg_age(my_cursor),
             task_queries.top_five_with_biggest_dif(my_cursor), task_queries.list_with_dif_sex(my_cursor)]
formatter.to_format(args.ended_format, task_list)

my_database.commit()
