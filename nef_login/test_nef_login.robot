*** Settings ***
Library       nef_login.py
Test Timeout  15 minutes

*** Test Cases ***
Testing the VNF authentication on NEF
    ${nef_login_status}=    Test Login    %{nef_login_report_api_ip}    %{nef_login_report_api_port}    %{nef_login_report_name}    %{nef_login_mini_api_ip}    %{nef_login_mini_api_port}    %{nef_login_nef_ip}    %{nef_login_nef_port}    %{nef_login_nef_user}    %{nef_login_nef_pass}    %{nef_login_napp_endpoint}   

    IF  '${nef_login_status[0]}' in ['0']
        Pass Execution  \n${nef_login_status[1]}
    ELSE IF  '${nef_login_status[0]}' in ['1', '2', '3', '4']
        Fail  \n${nef_login_status[1]}
    ELSE
        Fail  \nUnknown Error
    END