import subprocess

def packet_statistics(input_file):
    """
    Analyze a packet capture file and display basic statistics.

    Args:
    input_file (str): The path to the packet capture file.

    Returns:
    None
    """
    print(f"Analyzing packet capture file: {input_file}")
    subprocess.run(["tshark", "-r", input_file, "-q", "-z", "io,phs"])
    print("Analysis complete.")

# Example usage
packet_statistics("capture_eth0_60s.pcap")
