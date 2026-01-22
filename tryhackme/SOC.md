
# SOC

A SOC (Security Operations Center) is a dedicated facility operated by a specialized security team

## People

SOC Analyst (Level 1): Anything detected by the security solution would pass
through these analysts first. These are the first responders to any detection.

SOC Level 1 Analysts perform basic alert triage to determine if a specific
detection is harmful. They also report these detections through proper channels.

SOC Analyst (Level 2): While Level 1 does the first-level analysis, some
detections may require deeper investigation. Level 2 Analysts help them dive
deeper into the investigations and correlate the data from multiple data sources
to perform a proper analysis.

SOC Analyst (Level 3): Level 3 Analysts are
experienced professionals who proactively look for any threat indicators and
support in the incident response activities. The critical severity detection
reported by Level 1 and Level 2 Analysts are often security incidents that need
detailed responses, including containment, eradication, and recovery. This is
where Level 3 analysts’ experience comes in handy.

Security Engineer: All
analysts work on security solutions. These solutions need deployment and
configuration. Security Engineers deploy and configure these security solutions
to ensure their smooth operation.

Detection Engineer: Security rules are the
logic built behind security solutions to detect harmful activities. Level 2 and
3 Analysts often create these rules, while the SOC team can sometimes also
utilize the detection engineer role independently for this responsibility.

SOC Manager: The SOC Manager manages the processes the SOC team follows and provides
support. The SOC Manager also remains in contact with the organization’s CISO
(Chief Information Security Officer) to provide him with updates on the SOC
team’s current security posture and efforts. Note: The roles in the SOC team can
increase or decrease depending on the size and criticality of the organizations

## Process

The Alert triage is all about answering the 5 Ws. What are these 5 Ws?


5 Ws	Answers
What?	A malicious file was detected on one of the hosts inside the organization’s network.
When?	The file was detected at 13:20 on June 5, 2024.
Where?	The file was detected in the directory of the host: "GEORGE PC".
Who?	The file was detected for the user George.
Why?	After the investigation, it was found that the file was downloaded from a pirated software-selling website. The investigation with the user revealed that they downloaded the file as they wanted to use a software for free.

## Tehcnology

SIEM: Security Information and Event Management (SIEM) is a popular tool used in almost every SOC environment. This tool collects logs from various network devices, referred to as log sources. The SIEM solution only provides the Detection capabilities in a SOC environment.

EDR: Endpoint Detection and Response (EDR) provides the SOC team with detailed real-time and historical visibility of the devices’ activities. It operates on the endpoint level and can carry out automated responses. EDR has extensive detection capabilities for endpoints, allowing you to investigate them in detail and respond with a few clicks.

Firewall: A firewall functions purely for network security and acts as a barrier between your internal and external networks (such as the Internet). It monitors incoming and outgoing network traffic and filters any unauthorized traffic.