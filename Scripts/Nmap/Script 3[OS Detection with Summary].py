import nmap

def os_detection(target_ip):
    """
    Detect the operating system of the target IP.

    Args:
    target_ip (str): The IP address to scan.

    Returns:
    None
    """
    scanner = nmap.PortScanner()
    print(f"Detecting OS for {target_ip}")
    scanner.scan(target_ip, arguments='-O')

    if 'osclass' in scanner[target_ip]:
        for os_class in scanner[target_ip]['osclass']:
            print(f"OS: {os_class['osfamily']}, Accuracy: {os_class['accuracy']}%")
    else:
        print("No OS information available")

# Example usage
os_detection('192.168.1.1')
