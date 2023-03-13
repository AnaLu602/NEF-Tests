

# Return Codes:
# 0 - OK
# 1 - Report doesn't exist
# 2 - Invalid Payload
# 3 - Payloads doesn't match
# 4 - Other

from requests.structures import CaseInsensitiveDict
import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

REPORT_API_IP = os.getenv('REPORT_API_IP')
REPORT_API_PORT = os.getenv('REPORT_API_PORT')
REPORT_FILE_NAME = os.getenv('REPORT_FILE_NAME')
NEF_IP = os.getenv('NEF_IP')
NEF_PORT = os.getenv('NEF_PORT')
USERNAME = os.getenv('EMAIL')
PASSWORD = os.getenv('PASS')

report_api_base_url = f"http://{REPORT_API_IP}:{REPORT_API_PORT}"


def create_report():
    report_api_url = report_api_base_url + "/report/"

    requests.post(report_api_url, params={"filename":REPORT_FILE_NAME})

def delete_report():
    report_api_url = report_api_base_url + "/report/"

    requests.delete(report_api_url, params={"filename":REPORT_FILE_NAME})

def get_token(url, user_pass):
    
    try:
        headers = CaseInsensitiveDict()
        headers["accept"] = "application/json"
        headers["Content-Type"] = "application/x-www-form-urlencoded"

        data = {
            "grant_type": "",
            "username": user_pass["username"],
            "password": user_pass["password"],
            "scope": "",
            "client_id": "",
            "client_secret": ""
        }

        resp = requests.post(url, headers=headers, data=data)

        resp_content = resp.json()

        token = resp_content["access_token"]

        return token
    
    except Exception as e:
        print(f"An error occured. Exception {e}")
        return 4, f"An error occured. Exception {e}"

def test_monitoring_subscription(monitoring_payload):

    try:
        nef_base_url = f"http://{str(NEF_IP)}:{str(NEF_PORT)}"

        user_pass = {
            "username": USERNAME,
            "password": PASSWORD
        }

        key = get_token(nef_base_url+"/api/v1/login/access-token", user_pass)

        headers = CaseInsensitiveDict()
        headers["accept"] = "application/json"
        headers["Authorization"] = "Bearer " + key
        headers["Content-Type"] = "application/json"

        requests.post(nef_base_url + "/nef/api/v1/3gpp-monitoring-event/v1/netapp/subscriptions",
                    headers=headers, data=json.dumps(monitoring_payload))

        report_api_url = report_api_base_url + "/report/"

        response = requests.get(report_api_url, params={"filename":REPORT_FILE_NAME})

        if response.status_code == 404:
            print(f"Report named{REPORT_FILE_NAME} does not exist")
            return 1, f"Report named{REPORT_FILE_NAME} does not exist"

        report = response.json()

        with open(REPORT_FILE_NAME, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=4)

        if report["requests"][1]["response"]["code"] != 200:
            print(f"Test failed with status code: {report['requests'][1]['response']['code']}. "\
                  f"Reason: {report['requests'][1]['response']['reason']}")
            return 2, f"Test failed with status code: {report['requests'][1]['response']['code']}. "\
                  f"Reason: {report['requests'][1]['response']['reason']}"
        else:
            nef_payload_received = sorted(report["requests"][1]["details"]["payload"].items())
            payload_sent= sorted(monitoring_payload.items())
            if nef_payload_received == payload_sent:
                print("Successful test")
                return 0, f"Successful test"
            else:
                print("Payload received by NEF doesn't match the one sent.")
                return 3, f"Payload received by NEF doesn't match the one sent."

    except Exception as e:
        print(f"An error occured. Exception {e}")
        return 4, f"An error occured. Exception {e}"


if __name__ == '__main__':
    create_report()
    monitoring_payload = {
        "externalId": "123456789@domain.com",
        "notificationDestination": "http://localhost:80/api/v1/utils/monitoring/callback",
        "monitoringType": "LOCATION_REPORTING",
        "maximumNumberOfReports": 1,
        "monitorExpireTime": "2023-03-09T13:18:19.495000+00:00",
        "maximumDetectionTime": 1,
        "reachabilityType": "DATA"
    }

    wrong_monitoring_payload = {
        "externalId": "123456789@domain.com",
        "notificationDestination": "http://localhost:80/api/v1/utils/monitoring/callback",
        "monitoringType": "LOCATION_REPORTING",
        "maximumNumberOfReports": "str",
        "monitorExpireTime": "2023-03-09T13:18:19.495000+00:00",
        "maximumDetectionTime": 1,
        "reachabilityType": "DATA"
    }

    test_monitoring_subscription(monitoring_payload)
    delete_report()
