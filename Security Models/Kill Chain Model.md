# The Lockheed Martin Cyber Kill Chain

The Kill Chain model outlines the seven stages of a cyberattack.
Breaking the chain at any stage can prevent a successful breach.

1. Reconnaissance
The Investigation Phase.
The attacker gathers information on the target.
This includes searching for email addresses, identifying social media profiles,
or scanning for open ports and unpatched software.

2. Weaponization
The Preparation Phase.
The attacker creates a "weapon"
by combining a remote access trojan with an exploit into a deliverable file
(e.g., a PDF or Word document).
This happens on the attacker's system, not the victim's.

3. Delivery
The Transmission Phase.
How the weapon is sent to the victim. Common methods include phishing emails,
malicious USB drives, "watering hole" websites, or cloud storage links.

4. Exploitation
The Trigger Phase.
The malicious code is executed.
This stage triggers the vulnerability in the victim's software
or operating system to gain an initial foothold. This is where the "lock is picked."

5. Installation
The Persistence Phase.
The attacker installs a "backdoor" or malware onto the victim's system.
This ensures they can maintain access even if the computer is restarted
or the initial vulnerability is patched.

6. Command and Control (C2)
The Remote Access Phase.
The infected system opens a communication channel back to the attacker’s server.
This allows the attacker to remotely issue commands, "hands-on-keyboard,"
to the compromised host.

7. Actions on Objectives
The Mission Phase.
With total control, the attacker fulfills their original goal.
This could include data exfiltration (stealing files),
encrypting data for ransom, or destroying systems.
