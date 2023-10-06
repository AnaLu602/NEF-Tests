*** Settings ***
Library       nef_monitoring_subscription.py
Test Timeout  15 minutes

*** Test Cases ***
Testing the creating of a monitoring subscription in NEF
    ${nef_monitoring_subscription_status}=    Test NEF Monitoring Subscription    %{nef_monitoring_subscription_report_api_ip}    %{nef_monitoring_subscription_report_api_port}    %{nef_monitoring_subscription_report_name}    %{nef_monitoring_subscription_mini_api_ip}    %{nef_monitoring_subscription_mini_api_port}    %{nef_monitoring_subscription_nef_ip}    %{nef_monitoring_subscription_nef_port}    %{nef_monitoring_subscription_nef_user}    %{nef_monitoring_subscription_nef_pass}    %{nef_monitoring_subscription_napp_endpoint}

    IF  '${nef_monitoring_subscription_status[0]}' in ['0']
        Pass Execution  \n${nef_monitoring_subscription_status[1]}
    ELSE IF  '${nef_monitoring_subscription_status[0]}' in ['1', '2', '3', '4']
        Fail  \n${nef_monitoring_subscription_status[1]}
    ELSE
        Fail  \nUnknown Error
    END