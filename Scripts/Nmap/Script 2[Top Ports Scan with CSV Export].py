import nmap
import csv
import datetime

def top_ports_scan(target_ip):
    """
    Scan the top 20 most commonly used ports on the target IP and export results to a CSV file.

    Args:
    target_ip (str): The IP address to scan.

    Returns:
    None
    """
    scanner = nmap.PortScanner()
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    result_file = f"top_ports_scan_{timestamp}.csv"

    print(f"Scanning top ports on {target_ip}")
    scanner.scan(target_ip, arguments='--top-ports 20')

    with open(result_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Host', 'Port', 'State', 'Service'])

        for host in scanner.all_hosts():
            for proto in scanner[host].all_protocols():
                for port in scanner[host][proto].keys():
                    state = scanner[host][proto][port]['state']
                    service = scanner[host][proto][port]['name']
                    writer.writerow([host, port, state, service])
    
    print(f"Scan complete. Results saved to {result_file}")

# Example usage
top_ports_scan('192.168.1.1')
