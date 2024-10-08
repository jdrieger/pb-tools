import pb_lib_api_pb as api
import pb_lib_general as general
import argparse


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

# Get the User List
print()
print("Getting User List from API...")
pb_user_list = api.pb_list_all_users(pb_api_key)
print("Recieved " + str(len(pb_user_list['data'])) + " records.")

# Get the Company List
print()
print("Getting Company List from API...")
pb_company_list = api.pb_list_all_companies(pb_api_key)
print("Recieved " + str(len(pb_company_list['data'])) + " records.")

# Get the Notes List
print()
print("Getting Notes List from API...")
pb_notes_list = api.pb_list_all_notes(pb_api_key)
print("Recieved " + str(len(pb_notes_list['data'])) + " records.")

# Get the Features List
print()
print("Getting Features List from API...")
pb_features_list = api.pb_list_all_features(pb_api_key)
print("Recieved " + str(len(pb_features_list['data'])) + " records.")

# Get the Components List
print()
print("Getting Components List from API...")
pb_components_list = api.pb_list_all_components(pb_api_key)
print("Recieved " + str(len(pb_components_list['data'])) + " records.")

# Get the Products List
print()
print("Getting Products List from API...")
pb_products_list = api.pb_list_all_products(pb_api_key)
print("Recieved " + str(len(pb_products_list['data'])) + " records.")

# Get the feature statuses list
print()
print("Getting feature statuses List from API...")
pb_feature_statuses_list = api.pb_list_all_feature_statuses(pb_api_key)
print("Recieved " + str(len(pb_feature_statuses_list['data'])) + " records.")

# Get the release groups list
print()
print("Getting release groups List from API...")
pb_release_groups_list = api.pb_list_all_release_groups(pb_api_key)
print("Recieved " + str(len(pb_release_groups_list['data'])) + " records.")

# Get the releases list
print()
print("Getting releases List from API...")
pb_releases_list = api.pb_list_all_releases(pb_api_key)
print("Recieved " + str(len(pb_releases_list['data'])) + " records.")

# Get the feature release assignments list
print()
print("Getting feature release assignments List from API...")
pb_feature_release_assignments_list = api.pb_list_all_feature_release_assignments(pb_api_key)
print("Recieved " + str(len(pb_feature_release_assignments_list['data'])) + " records.")

# Get the objectives list
print()
print("Getting objectives List from API...")
pb_objectives_list = api.pb_list_all_objectives(pb_api_key)
print("Recieved " + str(len(pb_objectives_list['data'])) + " records.")



