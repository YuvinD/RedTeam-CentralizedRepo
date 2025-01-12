import requests
import time

def start_active_scan(target_url):
    """
    Start an active scan on the target URL using OWASP ZAP API and display alerts.

    Args:
    target_url (str): The URL to scan.

    Returns:
    None
    """
    zap_api_url = "http://localhost:8080"
    scan_url = f"{zap_api_url}/JSON/ascan/action/scan/?url={target_url}"
    
    response = requests.get(scan_url)
    scan_id = response.json().get('scan')
    print(f"Active scan started with ID: {scan_id}")

    # Check the progress
    progress_url = f"{zap_api_url}/JSON/ascan/view/status/?scanId={scan_id}"
    while True:
        progress_response = requests.get(progress_url)
        progress = int(progress_response.json().get('status'))
        print(f"Active scan progress: {progress}%")
        if progress == 100:
            break
        time.sleep(5)

    # Fetch alerts
    alerts_url = f"{zap_api_url}/JSON/alert/view/alerts/"
    alerts_response = requests.get(alerts_url)
    print("Alerts:")
    for alert in alerts_response.json()['alerts']:
        print(f"Alert: {alert['alert']}, Risk: {alert['risk']}, URL: {alert['url']}")

# Example usage
start_active_scan("http://example.com")
