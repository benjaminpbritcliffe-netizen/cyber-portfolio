# Hackers Hijacking Hotel Wi-Fi

Hackers are changing the DNS settings on Wi-Fi devices at hotels
and conference centers to redirect users to fake Microsoft 365 login pages.

It is unclear how initial access to the Wi-Fi appliances was gained,
but ReliaQuest says the threat actor could have exploited weakly protected,
exposed management interfaces (e.g., SSH, SNMP, web admin dashboards)
or vulnerabilities.

Once the attacker gains administrator access,
they can modify the gateway’s DNS settings to redirect connections
to legitimate domains to infrastructure under the attacker's control.

ReliaQuest says that the attacker registered at least four domains
for setting up fake Microsoft login portals:
m365-owa[.]com,
owa-ms365[.]com,
ms365-device[.]com,
and ms365-live[.]com.

With DNS settings changed,
users trying to access legitimate Microsoft login portals
would land on the hacker's phishing pages and enter their credentials.

What the user can't see is that approving the prompt authorizes a session
initiated by the attacker," ReliaQuest says.
The researchers note that authorizing the attacker-initiated request causes a
legitimate OAuth token to be issued to the attacker's client.

This bypasses the multi-factor authentication (MFA) protection without stealing
any credentials or intercepting access tokens.

the attackers also attempted to abuse Web Proxy Auto-Discovery (WPAD)
by responding to Windows' automatic WPAD lookup with a malicious proxy
auto-configuration (PAC) file.
