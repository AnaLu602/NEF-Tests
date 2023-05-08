*** Settings ***
Library       nef_rsrp.py
Test Timeout  15 minutes

*** Test Cases ***
Testing the RSRP information
    ${nef_rsrp_status}=    Test NEF RSRP   %{nef_rsrp_report_api_ip}    %{nef_rsrp_report_api_port}    %{nef_rsrp_report_name}    %{nef_rsrp_mini_api_ip}    %{nef_rsrp_mini_api_port}    %{nef_rsrp_nef_ip}    %{nef_rsrp_nef_port}    %{nef_rsrp_nef_user}     %{nef_rsrp_nef_pass}    %{nef_rsrp_nef_supi}

    IF  '${nef_rsrp_status[0]}' in ['0']
        Pass Execution  \n${nef_rsrp_status[1]}
    ELSE IF  '${nef_rsrp_status[0]}' in ['1', '2', '3', '4']
        Fail  \n${nef_rsrp_status[1]}
    ELSE
        Fail  \nUnknown Error
    END