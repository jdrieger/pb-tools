import json
import os.path
import sys
import csv

# --Description-- #
# General Helper library and tools
# --End Description-- #


# --Helper Methods-- #
# Exit handler (Error)
def exit_error(error_code, error_message=None, system_message=None):
    print(error_code)
    if error_message is not None:
        print(error_message)
    if system_message is not None:
        print(system_message)
    sys.exit(1)


# Exit handler (Success)
def exit_success():
    sys.exit(0)


# Check to see if a file exists
def file_exists(file_name):
    file_name_and_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), file_name)
    if os.path.isfile(file_name_and_path):
        return True    
    else:
        return False

# Load the 2 column CSV directly into a Dict
def file_load_csv_simple(file_name):
    with open(file_name,mode='r') as csv_file:
        file_reader = csv.reader(csv_file)
        csv_dict = dict(file_reader)
    return csv_dict


# Load the CSV file into Dict
def file_load_csv(file_name,file_encoding='utf-8-sig'):
    csv_list = []
    with open(file_name, mode='r',encoding=file_encoding) as csv_file:
        file_reader = csv.DictReader(csv_file)
        for row in file_reader:
            csv_list.append(row)
    return csv_list


# Read txt file into string
def file_read_txt(file_name):
    txt_data = None
    file_name_and_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), file_name)
    try:
        with open(file_name_and_path, 'r') as f:
            txt_data = f.read()
    except Exception as ex:
        exit_error(500, "Failed to read text file.  Check the file name?", ex)
    return txt_data


# Write Dict to JSON file
def file_write_json(file_name, data_to_write):
    file_name_and_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), file_name)
    try:
        with open(file_name_and_path, 'w') as f:
            json.dump(data_to_write, f)
    except Exception as ex:
        exit_error(500, "Failed to write JSON file.", ex)


# Read JSON file into Dict
def file_read_json(file_name):
    json_data = None
    file_name_and_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), file_name)
    try:
        with open(file_name_and_path, 'r') as f:
            json_data = json.load(f)
    except Exception as ex:
        exit_error(500, "Failed to read JSON file.  Check the file name?", ex)
    return json_data


# JSON Dumps - formatted and default set to avoid unserializable attribs
def json_dumps(var_to_convert):
    return json.dumps(var_to_convert, indent = 4, sort_keys=True, default=str)


# Check for duplicates in a list
def duplicate_check(object_list):  
    object_set = set()
    for single_object in object_list:
        if single_object in object_set:
            return single_object
        else:
            object_set.add(single_object)         
    return None


# Exit and print out a JSON based variable (for debugging)
def json_dumps_and_exit(var_to_convert):
    print()
    print('##############JSON STARTS BELOW#############')
    print()
    print(json_dumps(var_to_convert))
    print()
    exit_success()


# Write CSV file
def file_write_csv(file_name, data_to_write, csv_header):
    file_name_and_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), file_name)
    try:
        with open(file_name_and_path, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames = csv_header)
            writer.writeheader()
            writer.writerows(data_to_write)
    except Exception as ex:
        exit_error(500, "Failed to write CSV file.", ex)


# Create CSV Header from Dict Keys
def csv_create_header_list(dict_to_get_headers_from):
    return list(dict_to_get_headers_from.keys())