

# Return Codes:
# 0 - Successful test
# 1 - Test Failed due to errors in creating a monitoring subscription
# 2 - Test Failed due to an exception

import requests
import json

def validate_report(report):
    errors = []
    for request in report:
        if request["endpoint"] == "/nef/api/v1/3gpp-monitoring-event/v1/netapp/subscriptions":
            if request["method"] != "POST":
                errors.append("Wrong method used.")
                break
            elif request["nef_response_code"] not in [200, 201, 409]:
                errors.append(f"Unable to create a monitoring subscription due to: {request['nef_response_message']}")
                break
    return errors


def test_nef_monitoring_subscription(report_api_ip, report_api_port, report_name, mini_api_ip, mini_api_port, nef_ip, nef_port, nef_user, nef_pass, napp_endpoint):

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

        mini_api_url = f"http://{mini_api_ip}:{mini_api_port}" + napp_endpoint

        data = {
            "nef_ip": nef_ip,
            "nef_port": nef_port,
            "nef_username": nef_user,
            "nef_pass": nef_pass
        }

        response = requests.post(mini_api_url, params=data)

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

    except Exception as e:
            print(f"An error occured. Exception {e}")
            return 2, f"An error occured. Exception {e}"

    # 5. Validate the Report
    
    errors = validate_report(report)

    if len(errors) != 0:
        errors_str = '\n\t- '.join(errors)
        print(f"Test Failed due to the following errors: {errors_str}")
        return 1, f"Test Failed due to the following errors: {errors_str}"

    else:
        print("Successful test.")
        return 0, f"Successful test."
    