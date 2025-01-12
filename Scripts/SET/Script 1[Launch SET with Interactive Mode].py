import subprocess

def launch_set_interactive():
    """
    Launch the Social Engineering Toolkit (SET) in interactive mode.

    Returns:
    None
    """
    print("Launching Social Engineering Toolkit...")
    subprocess.run(["sudo", "setoolkit"])

# Example usage
launch_set_interactive()
