# NEF Login Test

## 1. Test Goals

This test serves to ensure that a VNF is capable of authenticating with the 5G NEF. In this test, a NEF Emulator is used.

## 2. Test Description

This test verifies if a VNF is authenticating correctly against the NEF. It FAILS if the wrong credentials are given.

## 3. Inputs

The NEF Login Test takes as an input:

Example:
- `export report_api_ip=10.0.12.168`
- `export report_api_port=8000`
- `export report_api_filename=test.json`
- `export nef_ip=10.0.12.95`
- `export nef_port=8888`
- `export nef_username=admin@my-email.com`
- `export nef_password=pass`
- `export monitoring_payload_path=monitoring_payload.json`

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
Output:  /home/analu/Documents/NEF-Tests/login/output.xml
Log:     /home/analu/Documents/NEF-Tests/login/log.html
Report:  /home/analu/Documents/NEF-Tests/login/report.html
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
Output:  /home/analu/Documents/NEF-Tests/login/output.xml
Log:     /home/analu/Documents/NEF-Tests/login/log.html
Report:  /home/analu/Documents/NEF-Tests/login/report.html
```


## 5. Requirements

### 5.1. OS-Level Requirements

`None`

### 5.2. Python Requirements

```
robotframework==6.0.2
requests
```

