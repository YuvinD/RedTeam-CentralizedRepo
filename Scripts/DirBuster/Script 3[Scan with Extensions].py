import subprocess

def dirb_scan_with_extensions(target_url, wordlist, extensions):
    """
    Perform a Dirb scan with specified extensions.

    Args:
    target_url (str): The URL to scan.
    wordlist (str): Path to the wordlist.
    extensions (str): File extensions to include in the scan.

    Returns:
    None
    """
    print(f"Running Dirb scan on {target_url} with extensions {extensions}...")
    subprocess.run(["dirb", target_url, wordlist, "-X", extensions])

# Example usage
dirb_scan_with_extensions("http://example.com", "/usr/share/wordlists/common.txt", ".php,.html,.txt")
