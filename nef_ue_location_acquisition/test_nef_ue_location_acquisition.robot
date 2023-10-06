*** Settings ***
Library       nef_ue_location_acquisition.py
Test Timeout  15 minutes

*** Test Cases ***
Testing the UE location acquisition
    ${nef_ue_location_acquisition_status}=    Test NEF UE Location Acquisition    %{nef_ue_location_acquisition_report_api_ip}    %{nef_ue_location_acquisition_report_api_port}    %{nef_ue_location_acquisition_report_name}    %{nef_ue_location_acquisition_mini_api_ip}    %{nef_ue_location_acquisition_mini_api_port}    %{nef_ue_location_acquisition_nef_ip}    %{nef_ue_location_acquisition_nef_port}    %{nef_ue_location_acquisition_nef_user}    %{nef_ue_location_acquisition_nef_pass}    %{nef_ue_location_acquisition_napp_endpoint}

    IF  '${nef_ue_location_acquisition_status[0]}' in ['0']
        Pass Execution  \n${nef_ue_location_acquisition_status[1]}
    ELSE IF  '${nef_ue_location_acquisition_status[0]}' in ['1', '2', '3', '4']
        Fail  \n${nef_ue_location_acquisition_status[1]}
    ELSE
        Fail  \nUnknown Error
    END