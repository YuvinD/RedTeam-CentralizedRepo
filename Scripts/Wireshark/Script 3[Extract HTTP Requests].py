import subprocess

def extract_http_requests(input_file, output_file):
    """
    Extract HTTP request details from a packet capture file and save to a text file.

    Args:
    input_file (str): The path to the packet capture file.
    output_file (str): The path to save the extracted HTTP request details.

    Returns:
    None
    """
    print(f"Extracting HTTP requests from {input_file}")
    subprocess.run(["tshark", "-r", input_file, "-Y", "http.request", "-T", "fields", "-e", "http.host", "-e", "http.request.uri", "-e", "http.user_agent", "-w", output_file])
    print(f"HTTP requests extracted and saved to {output_file}")

# Example usage
extract_http_requests("capture_eth0_60s.pcap", "http_requests.txt")
