import requests

def download_nessus_report(scan_id, api_key):
    """
    Download the Nessus report for a given scan ID.

    Args:
    scan_id (int): The ID of the scan.
    api_key (str): Your Nessus API key.

    Returns:
    None
    """
    headers = {"X-ApiKeys": f"accessKey={api_key}"}
    export_url = f"https://nessus-server:8834/scans/{scan_id}/export"
    
    # Request report export
    export_response = requests.post(export_url, headers=headers, json={"format": "pdf"})
    file_id = export_response.json().get("file")
    
    # Download the report
    download_url = f"{export_url}/{file_id}/download"
    download_response = requests.get(download_url, headers=headers)
    
    with open(f"nessus_scan_{scan_id}.pdf", "wb") as file:
        file.write(download_response.content)
    
    print(f"Report downloaded: nessus_scan_{scan_id}.pdf")

# Example usage
download_nessus_report(123, "your_api_key_here")
