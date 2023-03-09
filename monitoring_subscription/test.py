

# Return Codes:
# 0 - OK
# 1 - Report doesn't exist
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


def create_report():
    report_api_url = f"http://{REPORT_API_IP}:{REPORT_API_PORT}/report/"

    requests.post(report_api_url, params={"filename":REPORT_FILE_NAME})

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
    

def test_login():

    try:
        nef_base_url = f"http://{str(NEF_IP)}:{str(NEF_PORT)}"

        user_pass = {
            "username": USERNAME,
            "password": PASSWORD
        }

        key = get_token(nef_base_url+"/api/v1/login/access-token", user_pass)

        report_base_url = f"http://{REPORT_API_IP}:{REPORT_API_PORT}"

        report_api_url = report_base_url + "/report/"

        response = requests.get(report_api_url, params={"filename":REPORT_FILE_NAME})

        if response.status_code == 404:
            print(f"Report named{REPORT_FILE_NAME} does not exist")
            return 1, f"Report named{REPORT_FILE_NAME} does not exist"

        report = response.json()

        with open(REPORT_FILE_NAME, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=4)

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

        report_base_url = f"http://{REPORT_API_IP}:{REPORT_API_PORT}"

        report_api_url = report_base_url + "/report/"

        response = requests.get(report_api_url, params={"filename":REPORT_FILE_NAME})

        if response.status_code == 404:
            print(f"Report named{REPORT_FILE_NAME} does not exist")
            return 1, f"Report named{REPORT_FILE_NAME} does not exist"

        report = response.json()

        with open(REPORT_FILE_NAME, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=4)

    except Exception as e:
        print(f"An error occured. Exception {e}")
        return 4, f"An error occured. Exception {e}"

    
    # if response.status_code == 404:
    #     print(f"Report named{REPORT_FILE_NAME} does not exist")
    #     return 1, f"Report named{REPORT_FILE_NAME} does not exist"

    # report = response.json()

    # with open(REPORT_FILE_NAME, 'w', encoding='utf-8') as f:
    #     json.dump(report, f, ensure_ascii=False, indent=4)

    # return report



if __name__ == '__main__':
    # open_ports("10.0.13.21", "22/tcp,9042/tcp,9160/tcp,12341/tcp")
    create_report()
    test_login()
    # monitoring_payload = {
    #     "externalId": "123456789@domain.com",
    #     "notificationDestination": "http://localhost:80/api/v1/utils/monitoring/callback",
    #     "monitoringType": "LOCATION_REPORTING",
    #     "maximumNumberOfReports": 1,
    #     "monitorExpireTime": "2023-03-09T13:18:19.495Z",
    #     "maximumDetectionTime": 1,
    #     "reachabilityType": "DATA"
    # }
    # test_monitoring_subscription(monitoring_payload)