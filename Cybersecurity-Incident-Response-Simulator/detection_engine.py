def detect(log):

    if "Ransomware" in log:
        return "Ransomware"

    if "Failed Login" in log:
        return "Brute Force"

    if "Data Transfer" in log:
        return "Data Exfiltration"

    return None