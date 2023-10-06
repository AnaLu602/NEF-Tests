*** Settings ***
Library       nef_handovers.py
Test Timeout  15 minutes

*** Test Cases ***
Testing the Path Losses Information
    ${nef_handovers_status}=    Test NEF Handovers   %{nef_handovers_report_api_ip}    %{nef_handovers_report_api_port}    %{nef_handovers_report_name}    %{nef_handovers_mini_api_ip}    %{nef_handovers_mini_api_port}    %{nef_handovers_nef_ip}    %{nef_handovers_nef_port}    %{nef_handovers_nef_user}     %{nef_handovers_nef_pass}    %{nef_handovers_nef_supi}    %{nef_handovers_napp_endpoint}

    IF  '${nef_handovers_status[0]}' in ['0']
        Pass Execution  \n${nef_handovers_status[1]}
    ELSE IF  '${nef_handovers_status[0]}' in ['1', '2', '3', '4']
        Fail  \n${nef_handovers_status[1]}
    ELSE
        Fail  \nUnknown Error
    END