
# Return Codes:
# 0 - OK
# 1 - Tests Failed - Some Ports Are Not Secure!
# 2 - Impossible to load deployment info
# 3 - Impossible to load all deployed NFs
# 4 - Impossible to get the information of all network interfaces.

import json
import re

def test_nfv_port_security(deployment_info_file_path):

    deployment_info = None

    # Load deployment info file
    try:
        f = open(deployment_info_file_path)
        deployment_info = json.load(f)
    except Exception as e:
        print(f"Impossible to load deployment info from \
            '{deployment_info_file_path}'. Exception {e}!")
        return 2, f"Impossible to load deployment info. Exception {e}"
    

    # Get all ConnectionPoints in deployment

    vnfs_info = {}
    try:
        for artifact_data in deployment_info.values():
            if "vnfd-ref" in artifact_data.keys():

                vnfs_info[artifact_data["vnfd-ref"]] = {}

                vnfs_info[artifact_data["vnfd-ref"]]["vnfd-id"] = artifact_data["vnfd-id"]

    except Exception as e:
        print(f"Impossible to load all deployed VNFs. Exception {e}!")
        return 3, f"Impossible to load all deployed VNFs. Exception {e}!"
    
    result = {}
    try:
        for vnf_data in deployment_info.values():
            if "vnfd-ref" in vnf_data.keys() and vnf_data["vnfd-ref"] in vnfs_info.keys():

                result[vnf_data["vnfd-ref"]] = {}

                for vdur in vnf_data["vdur"]:
                    for vim_info in vdur["vim_info"].values():
                        for interface in vim_info["interfaces"]:

                            port_security = re.search(
                                r"port_security_enabled: (false|true)",
                                interface["vim_info"]
                            ).group(1)

                            ip_address = interface["ip_address"]
                            vim_interface_id = interface["vim_interface_id"]

                            result[vnf_data["vnfd-ref"]][vim_interface_id] = {
                                        "vnfd-id": vnf_data["vnfd-id"],
                                        "port_security": port_security,
                                        "ip_adress": ip_address
                                    }
                        
    except Exception as e:
        print("Impossible to get the information of all network interfaces." +
              f"Exception {e}!")
        return 4, "Impossible to get the information of all network "\
            f"interfaces. Exception {e}!"
    
    #Check results

    insecure_ports = []

    for vnfd in result:
        for vim_interface_id in result[vnfd]:
            if result[vnfd][vim_interface_id]["port_security"] == "false":
                insecure_ports.append({
                    "vnfd_id": result[vnfd][vim_interface_id]["vnfd-id"],
                    "interface_id": vim_interface_id,
                    "ip_adress": result[vnfd][vim_interface_id]["ip_adress"],
                    "port_security": result[vnfd][vim_interface_id]["port_security"]
                })
    
    if len(insecure_ports) == 0:
        print("\nAll ports have port security enabled!")
        return 0, "All ports have port security enabled!"

    print("\nNOT all ports have port security enabled! " +
          f"Ports: {insecure_ports}")
    return 1, "NOT all ports have port security enabled! "\
        f"Ports: {insecure_ports}"
 
if __name__ == '__main__':
    test_nfv_port_security("netapp_instantiation_information_with_port_security_enabled.json")