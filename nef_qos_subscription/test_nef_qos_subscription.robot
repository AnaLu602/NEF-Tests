*** Settings ***
Library       nef_qos_subscription.py
Test Timeout  15 minutes

*** Test Cases ***
Testing the QoS Subscription
    ${nef_qos_subscription_status}=    Test NEF QoS Subscription   %{nef_qos_subscription_report_api_ip}    %{nef_qos_subscription_report_api_port}    %{nef_qos_subscription_report_name}    %{nef_qos_subscription_mini_api_ip}    %{nef_qos_subscription_mini_api_port}    %{nef_qos_subscription_nef_ip}    %{nef_qos_subscription_nef_port}    %{nef_qos_subscription_nef_user}     %{nef_qos_subscription_nef_pass}

    IF  '${nef_qos_subscription_status[0]}' in ['0']
        Pass Execution  \n${nef_qos_subscription_status[1]}
    ELSE IF  '${nef_qos_subscription_status[0]}' in ['1', '2', '3', '4']
        Fail  \n${nef_qos_subscription_status[1]}
    ELSE
        Fail  \nUnknown Error
    END