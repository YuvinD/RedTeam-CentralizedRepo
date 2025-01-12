import subprocess

def basic_dirb_scan(target_url):
    """
    Perform a basic directory brute-force scan using Dirb.

    Args:
    target_url (str): The URL to scan.

    Returns:
    None
    """
    print(f"Running Dirb scan on {target_url}...")
    subprocess.run(["dirb", target_url])

# Example usage
basic_dirb_scan("http://example.com")
