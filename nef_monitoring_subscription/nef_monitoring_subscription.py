

# Return Codes:
# 0 - OK
# 1 - Test failed, wrong endpoint used
# 2 - Test failed, wrong method used
# 3 - Test failed
# 4 - Other

import requests
import json


def test_nef_monitoring_subscription(report_api_ip, report_api_port, report_name, mini_api_ip, mini_api_port, nef_ip, nef_port, nef_user, nef_pass):

    try:

        report_api_url = f"http://{report_api_ip}:{report_api_port}" + "/report/"

        # 1. Delete any existing report

        response = requests.delete(report_api_url)

        if not (response.status_code == 200 or response.status_code == 404):
            print(f"Error deleting the report")
            raise Exception(f"Error deleting the report")

        # 2. Create Report

        response = requests.post(report_api_url)

        if response.status_code == 409:
            print(f"Report cound't be created")
            raise Exception(f"Report cound't be created")
        
        # 3. Call the MiniAPI to run the code

        mini_api_url = f"http://{mini_api_ip}:{mini_api_port}" + "/start/"

        data = {
            "configId": 1,
            "duration": 10,
            "nef_ip": nef_ip,
            "nef_port": nef_port,
            "nef_username": nef_user,
            "nef_pass": nef_pass
        }

        response = requests.post(mini_api_url, data=data)

        if response.status_code != 200:
            print(f"Error while calling the MiniAPI")
            raise Exception(f"Error while calling the MiniAPI")

        # 4. Get Report

        response = requests.get(report_api_url)

        if response.status_code == 404:
            print(f"Report does not exist")
            raise Exception(f"Report does not exist")

        report = response.json()

        with open(report_name, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=4)

        # 5. Validate the Report

        if report[1]["endpoint"] != "/nef/api/v1/3gpp-monitoring-event/v1/netapp/subscriptions":
            print(f"Test failed. Wrong endpoint used: {report[1]['endpoint']}.")
            return 1, f"Test failed. Wrong endpoint used: {report[1]['endpoint']}."
        
        elif report[1]["method"] != "POST":
            print(f"Test failed. Wrong method used: {report[1]['method']}.")
            return 2, f"Test failed. Wrong method used:{report[1]['method']}."


        elif report[1]["nef_response_code"] != 200:
            print(f"Test failed with status code: {report[1]['nef_response_code']}. "\
                  f"Reason: {report[1]['nef_response_message']}")
            return 3, f"Test failed with status code: {report[1]['nef_response_code']}. "\
                  f"Reason: {report[1]['nef_response_message']}"
        else:
            print("Successful test")
            return 0, f"Successful test"

    except Exception as e:
        print(f"An error occured. Exception {e}")
        return 3, f"An error occured. Exception {e}"
    