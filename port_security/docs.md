# VNFs Port Security Test

## 1. Test Goals

This test serves to ensure all VNFs deployed in Openstack have port security enabled.
If a VNF's interfaces doesn't have port security enabled, all incoming traffic will be allowed. Thus, the VNF is fully exposed to attacks. With port security enabled, the developer may manage which traffic should be allowed to enter the VNF.

## 2. Test Description

This test requires a json file containing information on all VNFs/NSs deployed in Openstack. Based on such information, the Openstack Port Security Test verifies if there is any interface without port security enabled. If this is the case, the Openstack Port Security Test FAILS, given that 5GASP's security considerations were not taken into account by the Network Application Developer. Furthermore, the VNFs Port Security Test indicates which interfaces were not configured with port security enabled, so as the developer may fix this issue.

## 3. Inputs

The VNFs Port Security Test takes as an input the location of the Json file containing the VNFs/NSs deployment information.


Example:
- `export openstack_port_security_deployment_info_file_path=netapp_instantiation_information_with_port_security_enabled.json` 

## 4. Outputs

### 4.1. Example - Test Failed

``` 
→ python3 -m robot test_nfv_port_security.robot
==============================================================================
Test Nfv Port Security                                                        
==============================================================================
Testing the port security of VNF interfaces                           | FAIL |
NOT all ports have port security enabled! Ports: [{'vnfd_id': '27836018-57c0-44fc-9405-f4c14a874af9', 'interface_id': 'c8f9f8f5-3e67-4870-8570-e7e46e9d7b73', 'ip_adress': '10.0.30.108', 'port_security': 'false'}]
------------------------------------------------------------------------------
Test Nfv Port Security                                                | FAIL |
1 test, 0 passed, 1 failed
==============================================================================
Output:  /home/analu/Documents/NEF-Tests/port_security/output.xml
Log:     /home/analu/Documents/NEF-Tests/port_security/log.html
Report:  /home/analu/Documents/NEF-Tests/port_security/report.html
```

### 4.2. Example - Test Succeeded

``` 
→ python3 -m robot test_nfv_port_security.robot
==============================================================================
Test Nfv Port Security                                                        
==============================================================================
Testing the port security of VNF interfaces                           | PASS |
Success
------------------------------------------------------------------------------
Test Nfv Port Security                                                | PASS |
1 test, 1 passed, 0 failed
==============================================================================
Output:  /home/analu/Documents/NEF-Tests/port_security/output.xml
Log:     /home/analu/Documents/NEF-Tests/port_security/log.html
Report:  /home/analu/Documents/NEF-Tests/port_security/report.html
```

## 5. Requirements

### 5.1. OS-Level Requirements

`None`

### 5.2. Python Requirements

```
robotframework==6.0.2
```

