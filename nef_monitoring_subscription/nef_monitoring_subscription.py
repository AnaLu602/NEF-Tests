

# Return Codes:
# 0 - OK
# 1 - Test failed, wrong endpoint used
# 2 - Test failed, wrong method used
# 3 - Test failed
# 4 - Other

import requests
import json


def test_nef_monitoring_subscription(report_api_ip, report_api_port, report_name):

    try:
        report_api_url = f"http://{report_api_ip}:{report_api_port}" + "/report/"

        response = requests.get(report_api_url)

        if response.status_code == 404:
            print(f"Report does not exist")
            raise Exception(f"Report does not exist")

        report = response.json()

        with open(report_name, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=4)

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
    