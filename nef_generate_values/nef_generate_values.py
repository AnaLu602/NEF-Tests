# Return Codes:
# 0 - Successful test
# 1 - Test Failed due to errors in generating values
# 2 - Test Failed due to an exception

import requests
import json

def validate_report(report, params):
    errors = []
    first_value = None
    second_value = None
    subsId = None
    keys = params.split("-")
    for request in report:
        if request["endpoint"] == f"/nef/api/v1/3gpp-as-session-with-qos/v1/netapp/subscriptions":
            if request["method"] != "POST":
                errors.append("Wrong method used.")
                break
            elif request["nef_response_code"] not in [200, 201 ,409]:
                errors.append(f"Unable to create QoS Subscription due to: {request['nef_response_message']}")
                break
            elif request["nef_response_code"] in [200, 201]:
                msg = request['nef_response_message']
                msg = msg.replace("'", "\"")
                json_msg = json.loads(msg)
                link = json_msg['link']
                url_parts = link.split('/')
                subsId = url_parts[-1]

                if len(keys) > 1:
                    current_doc = json_msg
                    last_key = keys[-1]
                    for key in keys[:-1]:
                        current_doc = current_doc[key]

                    first_value = current_doc[last_key]
                else:
                    first_value = json_msg[params]
                break
            else:
                for req in report:
                    if req["endpoint"] == f"/nef/api/v1/3gpp-as-session-with-qos/v1/netapp/subscriptions":
                        if req["method"] == "GET":
                            msg = req['nef_response_message']
                            msg = msg.replace("'", "\"")
                            json_msg = json.loads(msg)

                            #hardcoded
                            desired_ipv4 = '10.0.0.3'

                            # Using a for loop
                            for item in json_msg:
                                if item['ipv4Addr'] == desired_ipv4:
                                    json_msg = item
                                    break
                            
                            link = json_msg['link']
                            url_parts = link.split('/')
                            subsId = url_parts[-1]

                            if len(keys) > 1:
                                current_doc = json_msg
                                last_key = keys[-1]
                                for key in keys[:-1]:
                                    current_doc = current_doc[key]

                                first_value = current_doc[last_key]
                            else:
                                first_value = json_msg[params]
                            break
                break

    for request in report:
        if request["endpoint"] == f"/nef/api/v1/3gpp-as-session-with-qos/v1/netapp/subscriptions/{subsId}":
            if request["method"] != "GET":
                errors.append("Wrong method used.")
                break
            elif request["nef_response_code"] not in [200, 409]:
                errors.append(f"Unable to get QoS Subscription due to: {request['nef_response_message']}")
                break
            else:
                msg = request['nef_response_message']
                msg = msg.replace("'", "\"")
                json_msg = json.loads(msg)

                if len(keys) > 1:
                    current_doc = json_msg
                    last_key = keys[-1]
                    for key in keys[:-1]:
                        current_doc = current_doc[key]

                    second_value = current_doc[last_key]
                else:
                    second_value = json_msg[params]
                break
    
    if first_value == second_value:
        errors.append("Parameter not updated.")
        print("not updated")
    return errors
  

def test_nef_generate_values(report_api_ip, report_api_port, report_name, mini_api_ip, mini_api_port, nef_ip, nef_port, nef_user, nef_pass, params, napp_endpoint):

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
            raise Exception(f"Error while calling the MiniAPI, {response}")

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
    
    errors = validate_report(report, params)

    if len(errors) != 0:
        errors_str = '\n\t- '.join(errors)
        print(f"Test Failed due to the following errors: {errors_str}")
        return 1, f"Test Failed due to the following errors: {errors_str}"

    else:
        print("Successful test.")
        return 0, f"Successful test."