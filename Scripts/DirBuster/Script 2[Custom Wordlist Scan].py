import subprocess

def custom_dirb_scan(target_url, wordlist):
    """
    Perform a Dirb scan with a custom wordlist.

    Args:
    target_url (str): The URL to scan.
    wordlist (str): Path to the custom wordlist.

    Returns:
    None
    """
    print(f"Running Dirb scan on {target_url} with wordlist {wordlist}...")
    subprocess.run(["dirb", target_url, wordlist])

# Example usage
custom_dirb_scan("http://example.com", "/usr/share/wordlists/custom.txt")
