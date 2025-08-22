# Breaking down the SolarWinds Hack - 2021

Status: In progress

[SolarWinds hack explained: Everything you need to know](https://www.techtarget.com/whatis/feature/SolarWinds-hack-explained-Everything-you-need-to-know)

The Sunburst certificate was properly signed, and the domain was registered a
year before - leaving no reason for anyone to doubt it. The cyber criminals
disabled logging every time they injected the DLL and then re-enabled logging
again. Unless someone was actively looking for an intrusion of this
sophistication, there was no obvious evidence of the DLL being injected. The DLL
made sure it had not been changed. It was also ensured that it was not executed
at SolarWinds, in a Sandbox, by security tools. This is critical because if
security analysts are looking at this DLL, they are going to do so in a Sandbox.
So, the DLL was actually able to evade execution in a sandbox. That’s how
sophisticated the attack was. It was able to avoid detection at every level. The
DLL was also able to execute at random times, up to two weeks after restart. It
had a full process list which allowed it to check for endpoint security tools
and installed drivers and kill them, successfully evading all EDR capabilities

Implementing robust security measures: Organizations should have strong security
measures in place to protect against supply chain attacks. This includes
implementing strong authentication and access controls, as well as regularly
updating and patching systems to fix vulnerabilities. Conducting thorough vendor
risk assessments: Organizations should carefully assess the risk posed by their
vendors and partners, and implement measures to mitigate any potential risks.
This includes conducting thorough background checks and regularly reviewing
vendor security practices. Implementing multi-factor authentication:
Multi-factor authentication (MFA) requires users to provide multiple pieces of
evidence to verify their identity, which can help prevent unauthorized access to
systems. Organizations should consider implementing MFA for all users,
especially those with access to sensitive data or systems. Ensuring secure
software development practices: Organizations should have secure software
development practices in place to ensure that the software they produce or use
is secure. This includes implementing code reviews, testing, and other quality
assurance processes.

💡

The attack affected the
[CIA Triad](../../House%20of%20Vokabel%2017b3d034d9f780f28d12fa401ae23c58/CIA%20Triad%2017b3d034d9f780c782f9f781573a24dd.md)
as it affected the “Integrity” of the system
[(PDF) The Solar Winds Cyber-Attack, the Federal and Private Sector Response, and the Recommendations and Lessons Learned](https://www.researchgate.net/publication/365186053_The_Solar_Winds_Cyber-Attack_the_Federal_and_Private_Sector_Response_and_the_Recommendations_and_Lessons_Learned)

</aside>

The SolarWinds cyberattack indeed had a significant impact on the "Integrity"
component of the CIA Triad (Confidentiality, Integrity, Availability). Integrity
refers to ensuring that the data and systems are accurate, reliable, and
protected from unauthorized modifications.

In the case of the SolarWinds attack, attackers were able to inject malicious
code into a software update for the Orion platform, which was used by both
federal agencies and private sector companies. This altered the integrity of the
systems because:

1. **Malicious Code Injection**: Attackers were able to modify the software
   update with a backdoor, leading to the compromise of systems across multiple
   organizations. This means that the systems were no longer in their original,
   trustworthy state, and the data in those systems could have been altered or
   manipulated without authorization.
2. **Widespread Compromise**: The attack spread undetected for months, affecting
   not only the integrity of the affected systems but also creating a
   vulnerability in critical infrastructure. The attackers could have changed
   system configurations or extracted data, which undermined the system's
   reliability and authenticity.
3. **Unauthorized Access**: While the main focus was on the potential espionage
   and data exfiltration, the integrity of the systems was compromised as
   attackers gained prolonged, hidden access to sensitive information and
   internal communications.

The SolarWinds attack highlights the vulnerability of the integrity aspect of
the CIA Triad, as attackers were able to subvert trusted software update
mechanisms and gain unauthorized access to critical systems.
