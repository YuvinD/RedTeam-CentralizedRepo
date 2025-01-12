import subprocess

def capture_packets(interface="eth0", duration=60, filter_expr="tcp"):
    """
    Capture packets on a specific interface with a given filter expression.

    Args:
    interface (str): The network interface to capture packets from.
    duration (int): The duration of the capture in seconds.
    filter_expr (str): The capture filter expression.

    Returns:
    None
    """
    output_file = f"capture_{interface}_{duration}s.pcap"
    print(f"Starting capture on {interface} with filter '{filter_expr}' for {duration} seconds.")
    subprocess.run(["tshark", "-i", interface, "-a", f"duration:{duration}", "-f", filter_expr, "-w", output_file])
    print(f"Capture complete. Results saved to {output_file}")

# Example usage
capture_packets(interface="eth0", duration=60, filter_expr="tcp port 80")
