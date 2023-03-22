

# Return Codes:
# 0 - OK
# 1 - Test failed
# 2 - Payloads don't match
# 3 - Other

from requests.structures import CaseInsensitiveDict
import requests
import json



def create_report(url, report_api_filename):

    return requests.post(url, params={"filename":report_api_filename})

def delete_report(url, report_api_filename):

    return requests.delete(url, params={"filename":report_api_filename})

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

def test_monitoring_subscription(report_api_ip, report_api_port, report_api_filename,
                                 nef_ip, nef_port, nef_username, nef_password,
                                 monitoring_payload_path):

    try:
        monitoring_payload = None

        # Load monitoring subscription info file
        try:
            f = open(monitoring_payload_path)
            monitoring_payload = json.load(f)
        except Exception as e:
            print(f"Impossible to monitoring subscription info from \
                '{monitoring_payload_path}'. Exception {e}!")
            raise Exception(f"Impossible to monitoring subscription info. Exception {e}")

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

        user_pass = {
            "username": nef_username,
            "password": nef_password
        }

        key = get_token(nef_base_url+"/api/v1/login/access-token", user_pass)

        headers = CaseInsensitiveDict()
        headers["accept"] = "application/json"
        headers["Authorization"] = "Bearer " + key
        headers["Content-Type"] = "application/json"

        requests.post(nef_base_url + "/nef/api/v1/3gpp-monitoring-event/v1/netapp/subscriptions",
                    headers=headers, data=json.dumps(monitoring_payload))

        response = requests.get(report_api_url, params={"filename":report_api_filename})

        if response.status_code == 404:
            print(f"Report named{report_api_filename} does not exist")
            raise Exception(f"Report named{report_api_filename} does not exist")

        report = response.json()

        with open(report_api_filename, 'w', encoding='utf-8') as f:
            json.dump(report, f, ensure_ascii=False, indent=4)

        if report["requests"][1]["response"]["code"] != 200:
            print(f"Test failed with status code: {report['requests'][1]['response']['code']}. "\
                  f"Reason: {report['requests'][1]['response']['reason']}")
            return 1, f"Test failed with status code: {report['requests'][1]['response']['code']}. "\
                  f"Reason: {report['requests'][1]['response']['reason']}"
        else:
            nef_payload_received = sorted(report["requests"][1]["details"]["payload"].items())
            payload_sent= sorted(monitoring_payload.items())
            if nef_payload_received == payload_sent:
                print("Successful test")
                return 0, f"Successful test"
            else:
                print("Payload received by NEF doesn't match the one sent.")
                return 2, f"Payload received by NEF doesn't match the one sent."

    except Exception as e:
        print(f"An error occured. Exception {e}")
        return 3, f"An error occured. Exception {e}"
