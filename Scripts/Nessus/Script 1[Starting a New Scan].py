import requests

def start_nessus_scan(scan_name, target_ip, api_key):
    """
    Start a new Nessus scan with the given scan name and target IP.

    Args:
    scan_name (str): The name of the scan.
    target_ip (str): The target IP address or range.
    api_key (str): Your Nessus API key.

    Returns:
    None
    """
    headers = {"X-ApiKeys": f"accessKey={api_key}"}
    data = {
        "uuid": "abac9b6a-fb52-4ef2-b357-e4cba6ebd3b6",  # UUID for 'Basic Network Scan' template
        "settings": {
            "name": scan_name,
            "text_targets": target_ip,
            "description": "Automated scan",
            "launch_now": True
        }
    }
    
    response = requests.post("https://nessus-server:8834/scans", headers=headers, json=data)
    print(f"Started Nessus scan: {response.json().get('scan')}")

# Example usage
start_nessus_scan("My Scan", "192.168.1.1", "your_api_key_here")
