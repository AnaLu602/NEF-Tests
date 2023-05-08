*** Settings ***
Library       nef_serving_cell.py
Test Timeout  15 minutes

*** Test Cases ***
Testing the serving cell information acquisition
    ${nef_serving_cell_status}=    Test NEF Serving Cell    %{nef_serving_cell_report_api_ip}    %{nef_serving_cell_report_api_port}    %{nef_serving_cell_report_name}    %{nef_serving_cell_mini_api_ip}    %{nef_serving_cell_mini_api_port}    %{nef_serving_cell_nef_ip}    %{nef_serving_cell_nef_port}    %{nef_serving_cell_nef_user}     %{nef_serving_cell_nef_pass}    %{nef_serving_cell_nef_supi}

    IF  '${nef_serving_cell_status[0]}' in ['0']
        Pass Execution  \n${nef_serving_cell_status[1]}
    ELSE IF  '${nef_serving_cell_status[0]}' in ['1', '2', '3', '4']
        Fail  \n${nef_serving_cell_status[1]}
    ELSE
        Fail  \nUnknown Error
    END