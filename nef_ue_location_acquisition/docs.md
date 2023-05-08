# NEF UE Location Acquisition

## 1. Test Goals

This test will validate if teh VNF is able to retrieve an indicative UE location. In this test, a NEF Emulator is used.

## 2. Test Description

This test verifies if a VNF is able to get a UE location.

## 3. Inputs

The NEF UE Location Acquisition takes as an input:

Example:
- `export nef_ue_location_acquisition_report_api_ip=10.255.28.238`
- `export nef_ue_location_acquisition_report_api_port=3000`
- `export nef_ue_location_acquisition_report_name=report.json`
- `export nef_ue_location_acquisition_mini_api_ip=10.255.28.163`
- `export nef_ue_location_acquisition_mini_api_port=3001`
- `export nef_ue_location_acquisition_nef_ip=10.255.28.238`
- `export nef_ue_location_acquisition_nef_port=8888`
- `export nef_ue_location_acquisition_nef_user=admin@my-email.com`
- `export nef_ue_location_acquisition_nef_pass=pass`

## 4. Outputs

### 4.1. Example - Test Succeeded

``` 
→ python3 -m robot test_nef_ue_location_acquisition.robot 
==============================================================================
Test Nef Ue Location Acquisition                                              
==============================================================================
Testing the UE location acquisition                                   | PASS |
Successful test
------------------------------------------------------------------------------
Test Nef Ue Location Acquisition                                      | PASS |
1 test, 1 passed, 0 failed
==============================================================================
Output:  /home/analu/Documents/NEF-Tests/nef_ue_location_acquisition/output.xml
Log:     /home/analu/Documents/NEF-Tests/nef_ue_location_acquisition/log.html
Report:  /home/analu/Documents/NEF-Tests/nef_ue_location_acquisition/report.html
```

## 5. Requirements

### 5.1. OS-Level Requirements

`None`

### 5.2. Python Requirements

```
robotframework==6.0.2
requests
```

