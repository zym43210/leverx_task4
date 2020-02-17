import file_worker


def to_format(choice, format_list):
    if choice == 1:
        file_worker.json_writer(format_list)
    else:
        file_worker.xml_writer(format_list)
