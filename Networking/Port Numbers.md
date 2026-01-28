
# Common Port Numbers

Port      |      Protocol    |Service   |    SOC Analyst Context
53        |      UDP/TCP     | DNS      |   Watch for unusually long queries (potential DNS Tunneling).
67 / 68   |      UDP         | DHCP     |   Look for "Rogue DHCP" servers trying to assign malicious gateways.
123       |      UDP         | NTP      |   Often used in NTP Amplification DDoS attacks.
161 / 162 |      UDP         | SNMP     |   Used for monitoring; attackers use it to map out your network hardware.
22	      |      TCP	     | SSH	    |   Encrypted remote login. Watch for brute-force login failures.
23	      |      TCP	     | Telnet	|   Critical Risk. Unencrypted. Seeing this is an immediate "Red Flag."
67 / 68	  |      UDP	     | DHCP	    |   Spot "Rogue DHCP" servers attempting Man-in-the-Middle (MitM) attacks.
123	      |      UDP	     | NTP	    |   Often abused for NTP Amplification DDoS attacks.
161 / 162 |	     UDP	     | SNMP	    |   High-risk; used by attackers to map out routers, switches, and printers.
22	      |      TCP	     | SSH	    |   Check for brute-force login attempts (thousands of failures in a row)
80	      |      TCP	     | HTTP	    |   Cleartext traffic. Look for sensitive data (passwords) being sent unencrypted.
443	      |      TCP	     | HTTPS	|   Encrypted web traffic. Use to hide C2 (Command & Control) communication.
3389	  |      TCP	     | RDP	    |   The primary vector for Ransomware. Should never be exposed to the internet.