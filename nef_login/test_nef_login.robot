*** Settings ***
Library       nef_login.py
Test Timeout  15 minutes

*** Test Cases ***
Testing the VNF authentication on NEF
    ${nef_login_status}=    Test Login    %{report_api_ip}    %{report_api_port}    %{report_name}

    IF  '${nef_login_status[0]}' in ['0']
        Pass Execution  \n${nef_login_status[1]}
    ELSE IF  '${nef_login_status[0]}' in ['1', '2', '3', '4']
        Fail  \n${nef_login_status[1]}
    ELSE
        Fail  \nUnknown Error
    END