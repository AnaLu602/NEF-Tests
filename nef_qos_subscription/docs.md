# QoS Subscription Test

## 1. Test Goals

This test will validate that a Network Application is able to subscribe and eventually retrieve information about a QoS compromised event. In this test, a NEF Emulator is used.

## 2. Test Description

This test verifies if a VNF is able to do a QoS Subscription.

## 3. Inputs

The QoS Subscription Test takes as an input:

Example:
- `export nef_qos_subscription_report_api_ip=10.255.28.238`
- `export nef_qos_subscription_report_api_port=3000`
- `export nef_qos_subscription_report_name=report.json`
- `export nef_qos_subscription_mini_api_ip=10.255.28.163`
- `export nef_qos_subscription_mini_api_port=3001`
- `export nef_qos_subscription_nef_ip=10.255.28.238`
- `export nef_qos_subscription_nef_port=8888`
- `export nef_qos_subscription_nef_user=admin@my-email.com`
- `export nef_qos_subscription_nef_pass=pass`
- `export nef_qos_subscription_napp_endpoint=/start/2/1/`


## 4. Outputs

### 4.1. Example - Test Succeeded

``` 
→ python3 -m robot test_nef_qos_subscription.robot
==============================================================================
Test Nef Qos Subscription                                                          
==============================================================================
Testing the QoS Subscription                                          | PASS |
Successful test
------------------------------------------------------------------------------
Test Nef Qos Subscription                                             | PASS |
1 test, 1 passed, 0 failed
==============================================================================
Output:  /home/analu/Documents/NEF-Tests/nef_qos_subscription/output.xml
Log:     /home/analu/Documents/NEF-Tests/nef_qos_subscription/log.html
Report:  /home/analu/Documents/NEF-Tests/nef_qos_subscription/report.html
```

### 4.2. Example - Subscription already exists

```
python3 -m robot test_nef_qos_subscription.robot
==============================================================================
Test Nef Qos Subscription                                                     
==============================================================================
Testing the QoS Subscription                                          | FAIL |
Test failed with status code: 409. Reason: Subscription for UE with ipv4Addr (10.0.0.1) already exists
------------------------------------------------------------------------------
Test Nef Qos Subscription                                             | FAIL |
1 test, 0 passed, 1 failed
==============================================================================
Output:  /home/analu/Documents/NEF-Tests/nef_qos_subscription/output.xml
Log:     /home/analu/Documents/NEF-Tests/nef_qos_subscription/log.html
Report:  /home/analu/Documents/NEF-Tests/nef_qos_subscription/report.html
```

## 5. Requirements

### 5.1. OS-Level Requirements

`None`

### 5.2. Python Requirements

```
robotframework==6.0.2
requests
```

