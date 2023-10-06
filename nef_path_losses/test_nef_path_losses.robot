*** Settings ***
Library       nef_path_losses.py
Test Timeout  15 minutes

*** Test Cases ***
Testing the Path Losses Information
    ${nef_path_losses_status}=    Test NEF Path Losses   %{nef_path_losses_report_api_ip}    %{nef_path_losses_report_api_port}    %{nef_path_losses_report_name}    %{nef_path_losses_mini_api_ip}    %{nef_path_losses_mini_api_port}    %{nef_path_losses_nef_ip}    %{nef_path_losses_nef_port}    %{nef_path_losses_nef_user}     %{nef_path_losses_nef_pass}    %{nef_path_losses_nef_supi}    %{nef_path_losses_napp_endpoint}

    IF  '${nef_path_losses_status[0]}' in ['0']
        Pass Execution  \n${nef_path_losses_status[1]}
    ELSE IF  '${nef_path_losses_status[0]}' in ['1', '2', '3', '4']
        Fail  \n${nef_path_losses_status[1]}
    ELSE
        Fail  \nUnknown Error
    END