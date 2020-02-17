import json


def file_reader(path):
    file_reading = open(path, "r")
    data = json.load(file_reading)
    return data


def rooms_transformer(path):
    rooms_list = []
    data_rooms = file_reader(path)
    for room_step in data_rooms:
        room_number = room_step["name"].split('#')
        dict_with_students = dict(name=room_number[-1], id=room_step["id"])
        rooms_list.append(dict_with_students)
    return rooms_list


def json_writer(object_for_dumping):
    with open("data_file.json", "w") as write_file:
        json.dump(object_for_dumping, write_file, sort_keys=True, indent=4)


def xml_writer(object_for_dumping):
    with open("minidom_example.xml", "w") as write_file:
        write_file.write(str(object_for_dumping))
