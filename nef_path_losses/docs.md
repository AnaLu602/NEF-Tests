# Path Losses Test

## 1. Test Goals

This test will validate that a Network Application is able to retrieve information about an indicative UE handover event (servicing cell switch) In this test, a NEF Emulator is used.

## 2. Test Description

This test verifies if a VNF is able to get the path losses.

## 3. Inputs

The Path Losses Test takes as an input:

Example:
- `export nef_path_losses_report_api_ip=10.255.28.238`
- `export nef_path_losses_report_api_port=3000`
- `export nef_path_losses_report_name=report.json`
- `export nef_path_losses_mini_api_ip=10.255.28.163`
- `export nef_path_losses_mini_api_port=3001`
- `export nef_path_losses_nef_ip=10.255.28.238`
- `export nef_path_losses_nef_port=8888`
- `export nef_path_losses_nef_user=admin@my-email.com`
- `export nef_path_losses_nef_pass=pass`
- `export nef_path_losses_nef_supi=202010000000001`

## 4. Outputs

### 4.1. Example - Test Succeeded

``` 
→ python3 -m robot test_nef_path_losses.robot
==============================================================================
Test Nef Path Losses                                                          
==============================================================================
Testing the Path Losses Information                                   | PASS |
Successful test
------------------------------------------------------------------------------
Test Nef Path Losses                                                  | PASS |
1 test, 1 passed, 0 failed
==============================================================================
Output:  /home/analu/Documents/NEF-Tests/nef_path_losses/output.xml
Log:     /home/analu/Documents/NEF-Tests/nef_path_losses/log.html
Report:  /home/analu/Documents/NEF-Tests/nef_path_losses/report.html
```

## 5. Requirements

### 5.1. OS-Level Requirements

`None`

### 5.2. Python Requirements

```
robotframework==6.0.2
requests
```

