

# Return Codes:
# 0 - OK
# 1 - Report doesn't exists
# 2 - Impossible to load deployment info
# 3 - Impossible to load all deployed NFs
# 4 - Impossible to get the information of all network interfaces.

from requests.structures import CaseInsensitiveDict
import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

REPORT_API_IP = os.getenv('REPORT_API_IP')
REPORT_API_PORT = os.getenv('REPORT_API_PORT')
REPORT_FILE_NAME = os.getenv('REPORT_FILE_NAME')

def get_token(url, user_pass):
    """Function to get the access token from the login request"""

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


def create_report():
    report_api_url = f"http://{REPORT_API_IP}:{REPORT_API_PORT}/report/"

    requests.post(report_api_url, params={"filename":REPORT_FILE_NAME})


def test_monitoring_subscription():

    #Get the report
    report_api_url = f"http://{REPORT_API_IP}:{REPORT_API_PORT}/report/"

    print(report_api_url)
    
    response = requests.get(report_api_url,params={"filename":REPORT_FILE_NAME})

    if response.status_code == 404:
        print(f"Report named{REPORT_FILE_NAME} does not exist")
        return 1, f"Report named{REPORT_FILE_NAME} does not exist"

    print(response.status_code)
    pass
    # print(report)

    # with open('report.json', 'w', encoding='utf-8') as f:
    #     json.dump(report, f, ensure_ascii=False, indent=4)

    # return report



if __name__ == '__main__':
    # open_ports("10.0.13.21", "22/tcp,9042/tcp,9160/tcp,12341/tcp")
    #create_report()
    test_monitoring_subscription()