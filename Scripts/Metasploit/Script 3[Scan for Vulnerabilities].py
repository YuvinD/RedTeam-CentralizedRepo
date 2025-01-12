import subprocess

def scan_vulnerabilities(target_ip):
    """
    Perform a vulnerability scan on the target IP using Metasploit.

    Args:
    target_ip (str): The target IP address.

    Returns:
    None
    """
    print(f"Scanning for vulnerabilities on {target_ip}...")
    commands = [
        "use auxiliary/scanner/vulnerabilities/dir_scanner",
        f"set RHOSTS {target_ip}",
        "run"
    ]
    subprocess.run(["msfconsole", "-q", "-x", "; ".join(commands)])

# Example usage
scan_vulnerabilities("192.168.1.1")
