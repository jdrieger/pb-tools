import json
import requests
import time
import pb_lib_general as general


# --Description-- #
# Productboard API Helper library.  Contains shared API call functions.
# --End Description-- #


# --Helper Methods-- #
# Main API Call Function
def pb_call_api(action, api_url, headers=None, data=None, params=None, try_count=0, max_retries=2):
    retry_statuses = [429, 500, 502, 503, 504]
    retry_wait_timer = 5

    # Make the API Call
    if data:
        data=json.dumps(data)

    response = requests.request(action, api_url, params=params, headers=headers, data=data)

    # Check for an error to retry, re-auth, or fail
    if response.status_code in retry_statuses:
        try_count = try_count + 1
        if try_count <= max_retries:
            print("retrying API call: " + api_url)
            time.sleep(retry_wait_timer)
            return pb_call_api(action=action, api_url=api_url, headers=headers, data=data, params=params,
                               try_count=try_count, max_retries=max_retries)
        else:
            if not response:
                print(response.json())
            response.raise_for_status()
    else:
        if not response:
                print(response.json())
        response.raise_for_status()

    # Check for valid response and catch if blank or unexpected
    api_response_package = {}
    api_response_package['statusCode'] = response.status_code
    try:
        api_response_package['data'] = response.json()
    except ValueError:
        if response.text == '':
            api_response_package['data'] = None
        else:
            general.exit_error(501, 'The server returned an unexpected server response.')
    return api_response_package

# Page wrapper for API Call
def pb_call_api_page(action, api_url, headers=None, data=None, params={}, max_retries=2):
    # Validate (or set) Params defaults
    if not params:
        params = {}
    params['pageCursor'] = None
    full_data_list = []

    # Call the API initially
    api_time_start = time.time()
    api_response_package = pb_call_api(action, api_url, headers=headers, data=data, params=params, max_retries=max_retries)
    api_time_end = time.time()
    api_time_total = api_time_end - api_time_start
    print("Total time for call: " + str(api_time_total))

    # Loop through pages, if needed
    page_count = 0
    while True:
        page_count=page_count + 1
        if 'pageLimit' in params:
            del params['pageLimit']
        print("Page " + str(page_count))
        if api_response_package['data']:
            print(len(api_response_package['data']['data']))
            full_data_list.extend(api_response_package['data']['data'])
            if 'pageCursor' in api_response_package['data']:
                if api_response_package['data']['pageCursor']:
                    params['pageCursor'] = api_response_package['data']['pageCursor']

                    # Call the API for the next page
                    api_time_start = time.time()
                    api_response_package = pb_call_api(action, api_url, headers=headers, data=data, params=params, max_retries=max_retries)
                    api_time_end = time.time()
                    api_time_total = api_time_end - api_time_start
                    print("Total time for call: " + str(api_time_total))

                else:
                    api_response_package['data'] = full_data_list
                    return api_response_package
            elif 'links' in api_response_package['data']:
                if 'next' in api_response_package['data']['links']:
                    if api_response_package['data']['links']['next']:
                        api_url = api_response_package['data']['links']['next']

                        # Call the API for the next page
                        api_time_start = time.time()
                        api_response_package = pb_call_api(action, api_url, headers=headers, data=data, params=params, max_retries=max_retries)
                        api_time_end = time.time()
                        api_time_total = api_time_end - api_time_start
                        print("Total time for call: " + str(api_time_total))
                        
                    else:
                        api_response_package['data'] = full_data_list
                        return api_response_package
                else:
                    api_response_package['data'] = full_data_list
                    return api_response_package
            else:
                api_response_package['data'] = full_data_list
                return api_response_package
        else:
            return api_response_package


# Get user list
def pb_list_all_users(pb_api_key):
    url = "https://api.productboard.com/users"
    action = "GET"
    headers = {'accept': 'application/json',
               'X-Version': '1',
               'Authorization': 'Bearer ' + pb_api_key}
    # Call the API
    return pb_call_api_page(action, url, headers=headers)

# Get company list
def pb_list_all_companies(pb_api_key):
    url = "https://api.productboard.com/companies"
    action = "GET"
    headers = {'accept': 'application/json',
               'X-Version': '1',
               'Authorization': 'Bearer ' + pb_api_key}
    # Call the API
    return pb_call_api_page(action, url, headers=headers)

# Get Notes list
def pb_list_all_notes(pb_api_key):
    url = "https://api.productboard.com/notes"
    action = "GET"
    headers = {'accept': 'application/json',
               'X-Version': '1',
               'Authorization': 'Bearer ' + pb_api_key}
    # Call the API
    return pb_call_api_page(action, url, headers=headers)

# Get Features list
def pb_list_all_features(pb_api_key):
    url = "https://api.productboard.com/features"
    action = "GET"
    headers = {'accept': 'application/json',
               'X-Version': '1',
               'Authorization': 'Bearer ' + pb_api_key}
    params = {'pageLimit': 1000}
    # Call the API
    return pb_call_api_page(action, url, headers=headers, params=params)

# Get components list
def pb_list_all_components(pb_api_key):
    url = "https://api.productboard.com/components"
    action = "GET"
    headers = {'accept': 'application/json',
               'X-Version': '1',
               'Authorization': 'Bearer ' + pb_api_key}
    # Call the API
    return pb_call_api_page(action, url, headers=headers)

# Get products list
def pb_list_all_products(pb_api_key):
    url = "https://api.productboard.com/products"
    action = "GET"
    headers = {'accept': 'application/json',
               'X-Version': '1',
               'Authorization': 'Bearer ' + pb_api_key}
    # Call the API
    return pb_call_api_page(action, url, headers=headers)

# Get feature-statuses list
def pb_list_all_feature_statuses(pb_api_key):
    url = "https://api.productboard.com/feature-statuses"
    action = "GET"
    headers = {'accept': 'application/json',
               'X-Version': '1',
               'Authorization': 'Bearer ' + pb_api_key}
    # Call the API
    return pb_call_api_page(action, url, headers=headers)

# Get release-groups list
def pb_list_all_release_groups(pb_api_key):
    url = "https://api.productboard.com/release-groups"
    action = "GET"
    headers = {'accept': 'application/json',
               'X-Version': '1',
               'Authorization': 'Bearer ' + pb_api_key}
    # Call the API
    return pb_call_api_page(action, url, headers=headers)

# Get releases list
def pb_list_all_releases(pb_api_key):
    url = "https://api.productboard.com/releases"
    action = "GET"
    headers = {'accept': 'application/json',
               'X-Version': '1',
               'Authorization': 'Bearer ' + pb_api_key}
    # Call the API
    return pb_call_api_page(action, url, headers=headers)

# Get feature-release-assignments list
def pb_list_all_feature_release_assignments(pb_api_key):
    url = "https://api.productboard.com/feature-release-assignments"
    action = "GET"
    headers = {'accept': 'application/json',
               'X-Version': '1',
               'Authorization': 'Bearer ' + pb_api_key}
    # Call the API
    return pb_call_api_page(action, url, headers=headers)

# Get objectives list
def pb_list_all_objectives(pb_api_key):
    url = "https://api.productboard.com/objectives"
    action = "GET"
    headers = {'accept': 'application/json',
               'X-Version': '1',
               'Authorization': 'Bearer ' + pb_api_key}
    # Call the API
    return pb_call_api_page(action, url, headers=headers)

# Get plugin-integrations list
def pb_list_all_plugin_integrations(pb_api_key):
    url = "https://api.productboard.com/plugin-integrations"
    action = "GET"
    headers = {'accept': 'application/json',
               'X-Version': '1',
               'Authorization': 'Bearer ' + pb_api_key}
    # Call the API
    return pb_call_api_page(action, url, headers=headers)

# Get jira-integrations list
def pb_list_all_jira_integrations(pb_api_key):
    url = "https://api.productboard.com/jira-integrations"
    action = "GET"
    headers = {'accept': 'application/json',
               'X-Version': '1',
               'Authorization': 'Bearer ' + pb_api_key}
    # Call the API
    return pb_call_api_page(action, url, headers=headers)

# Get webhooks list
def pb_list_all_webhooks(pb_api_key):
    url = "https://api.productboard.com/webhooks"
    action = "GET"
    headers = {'accept': 'application/json',
               'X-Version': '1',
               'Authorization': 'Bearer ' + pb_api_key}
    # Call the API
    return pb_call_api_page(action, url, headers=headers)
