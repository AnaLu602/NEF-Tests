
# Return Codes:
# 0 - Success (PASS)
# 1 - The audit reavealed that the TLS configuration is not compliant, but in 
# the context of 5GASP, the non-compliant characteristics are not required
# 2 - The audit reavealed that the TLS configuration is not compliant (FAIL)
# 3 - No audit results were gathered (FAIL)
# 4 - Other error

import subprocess
import re

def ssl_audit(url):

    try:
        cmd = ["sslyze", url]
        response_sslyze = subprocess.run(
            cmd, 
            capture_output=True, 
            text=True
        )
        
        stdout_lines = response_sslyze.stdout.splitlines()
        
        # Get the compliance report against mozilla's directives
        compliance_info = None
        for i in range(len(stdout_lines)-1, 0, -1):
            if "COMPLIANCE AGAINST MOZILLA TLS" in stdout_lines[i]:
                compliance_info = stdout_lines[i+2:]
                break
        
        # in the case there is no report
        if not compliance_info:
            return 3, "No audit results were gathered!"
            
        # clease compliance report
        compliance_info = [
            l.strip() for l in compliance_info 
            if 
                len(l)>0 
                and "Checking results against Mozilla's" not in l
            ]
        
        # 1. Check if successfull according to mozilla's directives
        if re.search(rf"^{url}.* OK - Compliant.$", compliance_info[-1]):
            return 0, f"\nResult: {compliance_info[-1]}"
            
        # 2. Even if not compliant with mozilla's directive, the SSL analysis 
        # may still be successful. There is a collection of compliance rules 
        # that can be ignored
        compliance_errors = []
        ignore_compliance_errors_regexes = [
            r"^\* certificate_hostname_validation:.*"
        ]

        # First, check if there was an error
        if len(compliance_info)==1\
        and re.search(rf"^{url}.* ERROR -.*", compliance_info[0]):
            compliance_errors.append(compliance_info[0])
        else:
            for i in range(1, len(compliance_info)):
                match_ignore_rule = False
                for ignore_regex in ignore_compliance_errors_regexes:
                    if re.search(ignore_regex, compliance_info[i]):
                        match_ignore_rule = True
                        break
                if not match_ignore_rule:
                    compliance_errors.append(compliance_info[i][2:])

        # If there are compliancy errors, even after applying the ignore rules       
        if len(compliance_errors) != 0:
            error_str = f"RESULT: {compliance_info[0]}"
            error_str += "\nERRORS:"
            for error in compliance_errors:
                error_str+=(f"\n\t-> {error}")

            # Print results
            return 2, error_str
        
        # Test
        result = compliance_info[0]\
            .replace('Not compliant', 'Compliant with 5GASP requirements')\
            .replace('FAILED', 'OK')
        return 1, f"\nResult: {result}"
    except Exception as e:
        return 4, f"An error occured. Exception {e}"
    