

# Return Codes:
# 0 - OK
# 1 - Report doesn't exist
# 2 - Wrong credencials
# 3 - Other

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
        return 3, f"An error occured. Exception {e}"
    

def test_login():

    try:
        nef_base_url = f"http://{str(NEF_IP)}:{str(NEF_PORT)}"

        user_pass = {
            "username": USERNAME,
            "password": PASSWORD
        }

        key = get_token(nef_base_url+"/api/v1/login/access-token", user_pass)

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
            print("Successful test")
            return 0, f"Successful test"

    except Exception as e:
        print(f"An error occured. Exception {e}")
        return 3, f"An error occured. Exception {e}"



if __name__ == '__main__':
    create_report()
    test_login()
    delete_report()
