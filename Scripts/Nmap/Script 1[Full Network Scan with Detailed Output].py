import requests

def start_nessus_scan(scan_name, target_ip):
    headers = {"X-ApiKeys": "accessKey=YOUR_API_KEY"}
    data = {
        "uuid": "basic",
        "settings": {
            "name": scan_name,
            "text_targets": target_ip
        }
    }
    response = requests.post("https://nessus-server:8834/scans", headers=headers, json=data)
    print(f"Started Nessus scan: {response.json().get('scan')}")
    
# Example usage
start_nessus_scan("New Scan", "192.168.1.1")
