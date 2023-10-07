# Generate Values Test

## 1. Test Goals


## 2. Test Description


## 3. Inputs

The Generate Values Test takes as an input:

Example:
- `export nef_generate_values_report_api_ip=10.255.28.238`
- `export nef_generate_values_report_api_port=3000`
- `export nef_generate_values_report_name=report.json`
- `export nef_generate_values_mini_api_ip=10.255.28.163`
- `export nef_generate_values_mini_api_port=3001`
- `export nef_generate_values_nef_ip=10.255.28.238`
- `export nef_generate_values_nef_port=8888`
- `export nef_generate_values_nef_user=admin@my-email.com`
- `export nef_generate_values_nef_pass=pass`
- `export nef_generate_values_params=usageThreshold-uplinkVolume`
- `export nef_generate_values_napp_endpoint=/start/2/1/`

## 4. Outputs

### 4.1. Example - Test Succeeded

``` 
→ python3 -m robot test_nef_generate_values.robot
==============================================================================
Test Nef Generate Values                                                       
==============================================================================
Testing the Generate Values Information                               | PASS |
Successful test
------------------------------------------------------------------------------
Test Nef Generate Values                                              | PASS |
1 test, 1 passed, 0 failed
==============================================================================
Output:  /home/analu/Documents/NEF-Tests/nef_generate_values/output.xml
Log:     /home/analu/Documents/NEF-Tests/nef_generate_values/log.html
Report:  /home/analu/Documents/NEF-Tests/nef_generate_values/report.html
```

## 5. Requirements

### 5.1. OS-Level Requirements

`None`

### 5.2. Python Requirements

```
robotframework==6.0.2
requests
```

