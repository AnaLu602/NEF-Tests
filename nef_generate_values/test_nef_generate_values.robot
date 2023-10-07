*** Settings ***
Library       nef_generate_values.py
Test Timeout  15 minutes

*** Test Cases ***
Testing the Generation of Values
    ${nef_generate_values_status}=    Test NEF generate_values   %{nef_generate_values_report_api_ip}    %{nef_generate_values_report_api_port}    %{nef_generate_values_report_name}    %{nef_generate_values_mini_api_ip}    %{nef_generate_values_mini_api_port}    %{nef_generate_values_nef_ip}    %{nef_generate_values_nef_port}    %{nef_generate_values_nef_user}     %{nef_generate_values_nef_pass}    %{nef_generate_values_params}    %{nef_generate_values_napp_endpoint}

    IF  '${nef_generate_values_status[0]}' in ['0']
        Pass Execution  \n${nef_generate_values_status[1]}
    ELSE IF  '${nef_generate_values_status[0]}' in ['1', '2', '3', '4']
        Fail  \n${nef_generate_values_status[1]}
    ELSE
        Fail  \nUnknown Error
    END