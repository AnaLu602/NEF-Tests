# Monitoring Subscription Test

## 1. Test Goals

This test serves to ensure that a VNF is capable of creating a monitoring subscription on the 5G NEF. In this test, a NEF Emulator is used.

## 2. Test Description

This test requires a json file containing information on the monitoring subscription payload needed to create a monitoring subscription on NEF. The Monitoring Subscription Test FAILS if the payload sent by the VNF doesn't match the payload retrieved on a report documenting the communications made with the NEF.

## 3. Inputs

The Monitoring Subscription Test takes as an input:

Example:
- `export nef_monitoring_subscription_report_api_ip=10.255.28.238`
- `export nef_monitoring_subscription_report_api_port=3000`
- `export nef_monitoring_subscription_report_name=report.json`
- `export nef_monitoring_subscription_mini_api_ip=10.255.28.163`
- `export nef_monitoring_subscription_mini_api_port=3001`
- `export nef_monitoring_subscription_nef_ip=10.255.28.238`
- `export nef_monitoring_subscription_nef_port=8888`
- `export nef_monitoring_subscription_nef_user=admin@my-email.com`
- `export nef_monitoring_subscription_nef_pass=pass`

## 4. Outputs

### 4.1. Example - Test Succeeded

``` 
→ python3 -m robot test_monitoring_subscription.robot 
==============================================================================
Test Monitoring Subscription                                                  
==============================================================================
Testing the creating of a monitoring subscription in NEF              | PASS |
Successful test
------------------------------------------------------------------------------
Test Monitoring Subscription                                          | PASS |
1 test, 1 passed, 0 failed
==============================================================================
Output:  /home/analu/Documents/NEF-Tests/monitoring_subscription/output.xml
Log:     /home/analu/Documents/NEF-Tests/monitoring_subscription/log.html
Report:  /home/analu/Documents/NEF-Tests/monitoring_subscription/report.html
```

### 4.2. Example - Test Failed Due To Invalid Payload

``` 
→ python3 -m robot test_nef_monitoring_subscription.robot 
==============================================================================
Test Monitoring Subscription                                                  
==============================================================================
Testing the creating of a monitoring subscription in NEF              | FAIL |
Test failed with status code: 400. Reason: Error=(payload_location=body/maximumNumberOfReports, message='value is not a valid integer')
------------------------------------------------------------------------------
Test Monitoring Subscription                                          | FAIL |
1 test, 0 passed, 1 failed
==============================================================================
Output:  /home/analu/Documents/NEF-Tests/monitoring_subscription/output.xml
Log:     /home/analu/Documents/NEF-Tests/monitoring_subscription/log.html
Report:  /home/analu/Documents/NEF-Tests/monitoring_subscription/report.html
```

### 4.3. Example - Test Failed - Other Error

``` 
→ python3 -m robot test_nef_monitoring_subscription.robot 
==============================================================================
Test Monitoring Subscription                                                  
==============================================================================
Testing the creating of a monitoring subscription in NEF              | FAIL |
An error occured. Exception Impossible to monitoring subscription info. Exception [Errno 2] No such file or directory: 'monitoring_payloa.json'
------------------------------------------------------------------------------
Test Monitoring Subscription                                          | FAIL |
1 test, 0 passed, 1 failed
==============================================================================
Output:  /home/analu/Documents/NEF-Tests/monitoring_subscription/output.xml
Log:     /home/analu/Documents/NEF-Tests/monitoring_subscription/log.html
Report:  /home/analu/Documents/NEF-Tests/monitoring_subscription/report.html
```



## 5. Requirements

### 5.1. OS-Level Requirements

`None`

### 5.2. Python Requirements

```
robotframework==6.0.2
requests
```

