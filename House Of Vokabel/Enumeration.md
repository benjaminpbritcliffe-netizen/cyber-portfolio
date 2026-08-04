# Enumeration

Security professionals or attackers actively interact with a system to extract information such as usernames, machine names, shared resources, network services, and system configurations

Unlike passive reconnaissance, which observes from a distance, enumeration involves direct probing of services and protocols to uncover actionable intelligence that can be used for exploitation or defense

Enumeration is essential because it allows security professionals to:

Discover user accounts and group memberships
Identify open ports and running services
Access shared folders and network devices
Determine system architecture and configurations
Gather data for targeted attacks like brute-force or privilege escalation
webasha.com
webasha.com

For attackers, enumeration is often the precursor to more damaging exploits, while for defenders, it helps identify misconfigurations and reduce attack surfaces

## Enumeration Types

Common types of enumeration include:

NetBIOS Enumeration: Collects computer names, workgroups/domains, logged-in users, and shared resources, typically on Windows networks using TCP port 139
SNMP Enumeration: Extracts device information, routing tables, ARP tables, and network topology from SNMP-enabled devices on UDP port 161
LDAP Enumeration: Queries directory services like Active Directory to reveal usernames, group memberships, and policies via port 389
DNS Enumeration: Gathers domain names, IP addresses, and network structure information.
NTP Enumeration: Can leak internal IP addresses and client information.
SMTP and SMB Enumeration: Used to identify email servers, shared files, and network resources


Enumeration can be performed using both command-line utilities and specialized tools:

## Tools

Nmap: For port scanning and service detection
Enum4linux: For NetBIOS and SMB enumeration
SNMPWalk: For SNMP data extraction
LDAPSearch: For querying directory services
Netcat and Metasploit: For interactive probing and exploitation
webasha.com
webasha.com