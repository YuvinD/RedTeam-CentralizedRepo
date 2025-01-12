import requests

def list_nessus_scans(api_key):
    """
    List all existing Nessus scans.

    Args:
    api_key (str): Your Nessus API key.

    Returns:
    None
    """
    headers = {"X-ApiKeys": f"accessKey={api_key}"}
    response = requests.get("https://nessus-server:8834/scans", headers=headers)
    scans = response.json().get('scans', [])
    
    print("Available Scans:")
    for scan in scans:
        print(f"ID: {scan['id']}, Name: {scan['name']}, Status: {scan['status']}")

# Example usage
list_nessus_scans("your_api_key_here")
