import requests
import time

def start_spider_scan(target_url)
    """
    Start a spider scan on the target URL using OWASP ZAP API.

    Args
    target_url (str) The URL to scan.

    Returns
    None
    """
    zap_api_url = httplocalhost8080
    spider_url = f{zap_api_url}JSONspideractionscanurl={target_url}
    
    response = requests.get(spider_url)
    scan_id = response.json().get('scan')
    print(fSpider scan started with ID {scan_id})

    # Check the progress
    progress_url = f{zap_api_url}JSONspiderviewstatusscanId={scan_id}
    while True
        progress_response = requests.get(progress_url)
        progress = int(progress_response.json().get('status'))
        print(fSpider scan progress {progress}%)
        if progress == 100
            break
        time.sleep(5)
    
    print(Spider scan completed.)

# Example usage
start_spider_scan(httpexample.com)
