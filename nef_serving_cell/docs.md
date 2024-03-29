# Serving Cell Information Test

## 1. Test Goals

This test will validate that a Network Application is able to retrieve indicative information about the serving radio node (cell). In this test, a NEF Emulator is used.

## 2. Test Description

This test verifies if a VNF is able to get the serving cell information.

## 3. Inputs

The Serving Cell Information Test takes as an input:

Example:
- `export nef_serving_cell_report_api_ip=10.255.28.238`
- `export nef_serving_cell_report_api_port=3000`
- `export nef_serving_cell_report_name=report.json`
- `export nef_serving_cell_mini_api_ip=10.255.28.163`
- `export nef_serving_cell_mini_api_port=3001`
- `export nef_serving_cell_nef_ip=10.255.28.238`
- `export nef_serving_cell_nef_port=8888`
- `export nef_serving_cell_nef_user=admin@my-email.com`
- `export nef_serving_cell_nef_pass=pass`
- `export nef_serving_cell_nef_supi=202010000000001`
- `export nef_serving_cell_napp_endpoint=/start/2/1/`

## 4. Outputs

### 4.1. Example - Test Succeeded

``` 
→ python3 -m robot test_nef_serving_cell.robot
==============================================================================
Test Nef Serving Cell                                                         
==============================================================================
Testing the serving cell information acquisition                      | PASS |
Successful test
------------------------------------------------------------------------------
Test Nef Serving Cell                                                 | PASS |
1 test, 1 passed, 0 failed
==============================================================================
Output:  /home/analu/Documents/NEF-Tests/nef_serving_cell/output.xml
Log:     /home/analu/Documents/NEF-Tests/nef_serving_cell/log.html
Report:  /home/analu/Documents/NEF-Tests/nef_serving_cell/report.html
```

## 5. Requirements

### 5.1. OS-Level Requirements

`None`

### 5.2. Python Requirements

```
robotframework==6.0.2
requests
```

