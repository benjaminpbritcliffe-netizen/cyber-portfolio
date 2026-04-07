# HoneyPots

A honeypot is a decoy network or resource set up to entice a hacker to attack it so that a security analyst can study the attack methods. The goal is for the honeypot to look so much like a legitimate network resource that an attacker finds it indistinguishable from a real resource.


Honeypots and Their Descriptions
Physical Honeypot
Physical honeypots are actual devices with an IP address that are physically placed on the network. They generally provide the highest level of interaction with attackers.

Virtual Honeypot
Virtual honeypots are simulated on a physical device. They are cost-effective because multiple honeypots can be simulated on a single server or device. However, they are not as effective because attackers can more easily detect them as decoys.

Low Interaction Honeypot
A low interaction level honeypot simulates a small number of services and apps on a target system or network. It is generally set to collect information about attacks such as network probes and worms. It is easy to set up and requires little maintenance and oversight.

Medium Interaction Honeypot
A medium interaction level honeypot simulates a real OS, applications, and services. It is more realistic than a low-level honeypot and logs and analyzes more complex attacks. It requires more maintenance and oversight than a low-level honeypot.

High Interaction Honeypot
A high interaction level honeypot does not simulate anything. These honeypots run actual services and applications on real computers. The honeypot can be completely compromised by an attacker, allowing full access to the system in a controlled area. It requires a high level of maintenance and oversight.

Production Honeypot
Production honeypots are deployed inside the production network of the organization along with other production servers. These honeypots improve the overall security but capture only a limited amount of information.

Research Honeypot
Research institutes, governments, and military organizations deploy high-interaction research honeypots to gain detailed knowledge about the actions of attackers.



Honeypot Implementation

Description
Physical
Physical honeypots have three main characteristics.

They are actual devices.
They have an IP address.
They are physically placed on the network.
Physical honeypots generally provide the highest level of interaction with attackers.

Virtual
Virtual honeypots are simulated on a physical device.

They are cost-effective because multiple honeypots can be simulated on a single server or device.
They are not as effective because attackers can more easily detect them as decoys.