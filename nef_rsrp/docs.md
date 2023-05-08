# RSRP Test

## 1. Test Goals

This test will validate that a Network Application is able to retrieve indicative information about RSRP (Reference Signal Received Power). In this test, a NEF Emulator is used.

## 2. Test Description

This test verifies if a VNF is able to get the RSRP.

## 3. Inputs

The RSRP Test takes as an input:

Example:
- `export nef_rsrp_report_api_ip=10.255.28.238`
- `export nef_rsrp_report_api_port=3000`
- `export nef_rsrp_report_name=report.json`
- `export nef_rsrp_mini_api_ip=10.255.28.163`
- `export nef_rsrp_mini_api_port=3001`
- `export nef_rsrp_nef_ip=10.255.28.238`
- `export nef_rsrp_nef_port=8888`
- `export nef_rsrp_nef_user=admin@my-email.com`
- `export nef_rsrp_nef_pass=pass`
- `export nef_rsrp_nef_supi=202010000000001`

## 4. Outputs

### 4.1. Example - Test Succeeded

``` 
→ python3 -m robot test_nef_rsrp.robot
==============================================================================
Test Nef Rsrp                                                                 
==============================================================================
Testing the RSRP information                                          | PASS |
Successful test
------------------------------------------------------------------------------
Test Nef Rsrp                                                         | PASS |
1 test, 1 passed, 0 failed
==============================================================================
Output:  /home/analu/Documents/NEF-Tests/nef_rsrp/output.xml
Log:     /home/analu/Documents/NEF-Tests/nef_rsrp/log.html
Report:  /home/analu/Documents/NEF-Tests/nef_rsrp/report.html
```

## 5. Requirements

### 5.1. OS-Level Requirements

`None`

### 5.2. Python Requirements

```
robotframework==6.0.2
requests
```

