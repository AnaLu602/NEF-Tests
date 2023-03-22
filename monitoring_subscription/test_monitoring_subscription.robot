*** Settings ***
Library       monitoring_subscription.py
Test Timeout  15 minutes

*** Test Cases ***
Testing the creating of a monitoring subscription in NEF
    ${nef_monitoring_subscription_status}=    Test Monitoring Subscription    %{report_api_ip}    %{report_api_port}    %{report_api_filename}    %{nef_ip}    %{nef_port}    %{nef_username}     %{nef_password}     %{monitoring_payload_path}

    IF  '${nef_monitoring_subscription_status[0]}' in ['0']
        Pass Execution  \n${nef_monitoring_subscription_status[1]}
    ELSE IF  '${nef_monitoring_subscription_status[0]}' in ['1', '2', '3', '4']
        Fail  \n${nef_monitoring_subscription_status[1]}
    ELSE
        Fail  \nUnknown Error
    END