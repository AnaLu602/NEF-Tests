# NEF Login Test

## 1. Test Goals

This test serves to ensure that a VNF is capable of authenticating with the 5G NEF. In this test, a NEF Emulator is used.

## 2. Test Description

This test verifies if a VNF is authenticating correctly against the NEF. It FAILS if the wrong credentials are given.

## 3. Inputs

The NEF Login Test takes as an input:

Example:
- `export nef_login_report_api_ip=10.255.28.238`
- `export nef_login_report_api_port=3000`
- `export nef_login_report_name=report.json`
- `export nef_login_mini_api_ip=10.255.28.163`
- `export nef_login_mini_api_port=3001`
- `export nef_login_nef_ip=10.255.28.238`
- `export nef_login_nef_port=8888`
- `export nef_login_nef_user=admin@my-email.com`
- `export nef_login_nef_pass=pass`

## 4. Outputs

### 4.1. Example - Test Succeeded

``` 
→ python3 -m robot test_nef_login.robot 
==============================================================================
Test Nef Login                                                                
==============================================================================
Testing the VNF authentication on NEF                                 | PASS |
Successful test
------------------------------------------------------------------------------
Test Nef Login                                                        | PASS |
1 test, 1 passed, 0 failed
==============================================================================
Output:  /home/analu/Documents/NEF-Tests/nef_login/output.xml
Log:     /home/analu/Documents/NEF-Tests/nef_login/log.html
Report:  /home/analu/Documents/NEF-Tests/nef_login/report.html
```

### 4.2. Example - Test Failed Due to Invalid Authentication

``` 
→ python3 -m robot test_nef_login.robot 
==============================================================================
Test Nef Login                                                                
==============================================================================
Testing the VNF authentication on NEF                                 | FAIL |
Test failed with status code: 400. Reason: Incorrect email or password
------------------------------------------------------------------------------
Test Nef Login                                                        | FAIL |
1 test, 0 passed, 1 failed
==============================================================================
Output:  /home/analu/Documents/NEF-Tests/login_v2/output.xml
Log:     /home/analu/Documents/NEF-Tests/login_v2/log.html
Report:  /home/analu/Documents/NEF-Tests/login_v2/report.html
```
### 4.3. Example - Wrong endpoint used

```
python3 -m robot test_nef_login.robot 
==============================================================================
Test Nef Login                                                                
==============================================================================
Testing the VNF authentication on NEF                                 | FAIL |
Test failed. Wrong endpoint used: /nef/api/v1/3gpp-monitoring-event/v1/netapp/subscriptions.
------------------------------------------------------------------------------
Test Nef Login                                                        | FAIL |
1 test, 0 passed, 1 failed
==============================================================================
Output:  /home/analu/Documents/NEF-Tests/login_v2/output.xml
Log:     /home/analu/Documents/NEF-Tests/login_v2/log.html
Report:  /home/analu/Documents/NEF-Tests/login_v2/report.html
```

### 4.4. Example - Other

```
python3 -m robot test_nef_login.robot 
==============================================================================
Test Nef Login                                                                
==============================================================================
Testing the VNF authentication on NEF                                 | FAIL |
An error occured. Exception list index out of range
------------------------------------------------------------------------------
Test Nef Login                                                        | FAIL |
1 test, 0 passed, 1 failed
==============================================================================
Output:  /home/analu/Documents/NEF-Tests/login_v2/output.xml
Log:     /home/analu/Documents/NEF-Tests/login_v2/log.html
Report:  /home/analu/Documents/NEF-Tests/login_v2/report.html
```


## 5. Requirements

### 5.1. OS-Level Requirements

`None`

### 5.2. Python Requirements

```
robotframework==6.0.2
requests
```

