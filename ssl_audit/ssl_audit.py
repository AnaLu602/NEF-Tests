
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
        response_sslyze = subprocess.run(cmd, capture_output=True, text=True)
        stdout_lines = response_sslyze.stdout.splitlines()

        # Find compliance info
        compliance_info = None
        for i in range(len(stdout_lines)-1, 0, -1):
            if "COMPLIANCE AGAINST MOZILLA TLS" in stdout_lines[i]:
                compliance_info = stdout_lines[i+2:]
                break

        if not compliance_info:
            return 3, "No audit results were gathered!"

        # Clean compliance report
        compliance_info = [l.strip() for l in compliance_info if len(l)>0 and "Checking results against Mozilla's" not in l]

        # Check if successful according to Mozilla's directives
        if re.search(rf"^{url}.* OK - Compliant.$", compliance_info[-1]):
            return 0, f"Result: {compliance_info[-1]}"

        # Extract compliance errors
        ignore_compliance_errors_regexes = [
            r"^\* certificate_hostname_validation:.*"
        ]

        compliance_errors = []
        for line in compliance_info[1:]:
            match_ignore_rule = any(re.search(ignore_regex, line) for ignore_regex in ignore_compliance_errors_regexes)
            if not match_ignore_rule:
                compliance_errors.append(line)

        if len(compliance_errors) > 0:
            error_str = f"Result: {compliance_info[1]}\nERRORS:"
            for error in compliance_errors:
                error_str += f"\n\t-> {error}"
            return 2, error_str

        # Transform the result
        result = compliance_info[1].replace('Not compliant', 'Compliant with 5GASP requirements').replace('FAILED', 'OK')
        return 1, f"Result: {result}"
    except subprocess.CalledProcessError as e:
        return 4, f"An error occurred. {e}"
    except Exception as e:
        return 4, f"An unexpected error occurred. Exception: {e}"
    