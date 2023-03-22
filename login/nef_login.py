

# Return Codes:
# 0 - OK
# 1 - Wrong credencials
# 2 - Other

from requests.structures import CaseInsensitiveDict
import requests
import json

def create_report(url, report_api_filename):

    return requests.post(url, params={"filename":report_api_filename})

def delete_report(url, report_api_filename):

    return requests.delete(url, params={"filename":report_api_filename})
   

def test_login(report_api_ip, report_api_port, report_api_filename,
                nef_ip, nef_port, nef_username, nef_password):

    try:
        # 1. Start by deleting previous reports, if there is any

        report_api_url = f"http://{report_api_ip}:{report_api_port}" + "/report/"

        response = delete_report(report_api_url, report_api_filename)

        print("NEF's Reporting API Response to Report Deletion: " +
              f" {response.text}")
        if response.status_code != 200:
            print("Impossible to delete previous reports from NEF's " +
                  "Reporting API")
            raise Exception("Impossible to delete previous reports from " +
                            "NEF's Reporting API")

        # 2. Then, create a new report
        
        response = create_report(report_api_url, report_api_filename)

        print("NEF's Reporting API Response to Report Creation: " +
              f"{response.text}")
        if response.status_code != 200:
            print("Impossible to create new report on NEF's Reporting API")
            raise Exception("Impossible to create new report on NEF's " +
                            "Reporting API")

        nef_base_url = f"http://{nef_ip}:{nef_port}"

        headers = CaseInsensitiveDict()
        headers["accept"] = "application/json"
        headers["Content-Type"] = "application/x-www-form-urlencoded"

        data = {
            "grant_type": "",
            "username": nef_username,
            "password": nef_password,
            "scope": "",
            "client_id": "",
            "client_secret": ""
        }

        resp = requests.post(nef_base_url+"/api/v1/login/access-token", headers=headers, data=data)

        report_api_url = f"http://{report_api_ip}:{report_api_port}" + "/report/"

        response = requests.get(report_api_url, params={"filename":report_api_filename})

        if response.status_code == 404:
            print(f"Report named{report_api_filename} does not exist")
            raise Exception(f"Report named{report_api_filename} does not exist")

        report = response.json()

        with open(report_api_filename, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=4)

        if report["requests"][0]["response"]["code"] != 200:
            print(f"Test failed with status code: {report['requests'][0]['response']['code']}. "\
                  f"Reason: {report['requests'][0]['response']['reason']}")
            return 2, f"Test failed with status code: {report['requests'][0]['response']['code']}. "\
                  f"Reason: {report['requests'][0]['response']['reason']}"
        else:
            print("Successful test")
            return 0, f"Successful test"

    except Exception as e:
        print(f"An error occured. Exception {e}")
        return 3, f"An error occured. Exception {e}"
