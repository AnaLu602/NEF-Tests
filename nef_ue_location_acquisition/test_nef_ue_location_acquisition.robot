*** Settings ***
Library       nef_ue_location_acquisition.py
Test Timeout  15 minutes

*** Test Cases ***
Testing the VNF authentication on NEF
    ${nef_ue_location_acquisition}=    Test NEF UE Location Acquisition    %{nef_login_report_api_ip}    %{nef_login_report_api_port}    %{nef_login_report_name}    %{nef_login_mini_api_ip}    %{nef_login_mini_api_port}    %{nef_login_nef_ip}    %{nef_login_nef_port}    %{nef_login_nef_user}    %{nef_login_nef_pass}

    IF  '${nef_ue_location_acquisition[0]}' in ['0']
        Pass Execution  \n${nef_ue_location_acquisition[1]}
    ELSE IF  '${nef_ue_location_acquisition[0]}' in ['1', '2', '3', '4']
        Fail  \n${nef_ue_location_acquisition[1]}
    ELSE
        Fail  \nUnknown Error
    END