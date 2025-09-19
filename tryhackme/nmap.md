
# Nmap

- Discover live hosts


Scanning a Local Network

In this context, we use the term “local” to refer to the network we are directly connected to, such as an Ethernet or WiFi network. In the first demonstration, we will scan the WiFi network to which we are connected. Our IP address is 192.168.66.89, and we are scanning the 192.168.66.0/24 network.

nmap -sn 192.168.66.0/24


Scanning a “Remote” Network

Consider the case of a “remote” network. In this context, “remote” means that at least one router separates our system from this network. As a result, all our traffic to the target systems must go through one or more routers. Unlike scanning a local network, we cannot send an ARP request to the target.

Our system has the IP address 192.168.66.89 and belongs to the 192.168.66.0/24 network. In the terminal below we scan the target network 192.168.11.0/24 where there are two or more routers (hops) separate our local system from the target hosts.

As a final point, Nmap offers a list scan with the option -sL.
This scan only lists the targets to scan without actually scanning them.
For example, nmap -sL 192.168.0.1/24 will list the 256 targets that will be scanned.

-Find running services on the live hosts

Option	Explanation
-sT	TCP connect scan – complete three-way handshake
-sS	TCP SYN – only first step of the three-way handshake
-sU	UDP scan
-F	Fast mode – scans the 100 most common ports
-p[range]	Specifies a range of port numbers – -p- scans all the ports

nmap -sT 10.10.169.204



- Detect the versions of the running services

- Control the timing

- Format the output