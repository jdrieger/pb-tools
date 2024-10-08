import pb_lib_api_pb as api
import pb_lib_general as general
import argparse
import time


# --Execution Block-- #
# --Parse command line arguments-- #
parser = argparse.ArgumentParser()

parser.add_argument(
    'pb_api_key_file_name',
    type=str,
    help='Name of the api key file to use.')

args = parser.parse_args()
# --End parse command line arguments-- #


pb_api_key_file_name = args.pb_api_key_file_name

# --Main-- #

# Load API Key from conf file
print()
print("Load API Key from conf file...")
pb_api_key = general.file_read_txt(pb_api_key_file_name)

# Get the Features List
print()
print("Getting Features List from API...")
print()
start_time = time.time()
print("Start time: " + str(start_time))
pb_features_list = api.pb_list_all_features(pb_api_key)
end_time = time.time()
print("End time: " + str(end_time))
total_time = end_time - start_time
print("Total time: " + str(total_time))
print("Recieved " + str(len(pb_features_list['data'])) + " records.")





