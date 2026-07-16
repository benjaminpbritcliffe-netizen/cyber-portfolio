
# Nmap

- Discover live hosts

Scanning a Local Network

We use the term “local” to refer to the network we are directly connected to,
such as an Ethernet or WiFi network. In the first demonstration,
we will scan the WiFi network to which we are connected.
Our IP address is 192.168.66.89, and we are scanning the 192.168.66.0/24 network.

nmap -sn 192.168.66.0/24

Scanning a “Remote” Network

Consider the case of a “remote” network.
“remote” means that at least one router separates our system from this network.
As a result, all our traffic to the target systems must go through one or more routers.
Unlike scanning a local network, we cannot send an ARP request to the target.

Our system has the IP address 192.168.66.89 and belongs to the 192.168.66.0/24 network.

As a final point, Nmap offers a list scan with the option -sL.
This scan only lists the targets to scan without actually scanning them.
For example, nmap -sL 192.168.0.1/24 will list the 256 targets that will be scanned.

-Find running services on the live hosts

Option Explanation
-sT TCP connect scan – complete three-way handshake
-sS TCP SYN – only first step of the three-way handshake
-sU UDP scan
-F Fast mode – scans the 100 most common ports
-p[range] Specifies a range of port numbers – -p- scans all the ports
-O You can enable OS detection by adding the -O option

nmap -sT 10.10.169.204

- Detect the versions of the running services

-sV You discovered several open ports and want to know what services are listening.
-sV enables version detection
-A This option enables OS detection, version scanning, and traceroute etc.
-Pn Scan hosts that appear to be down

- Control the timing

Running your scan at its normal speed might trigger an IDS or other security solutions.
It is reasonable to control how fast a scan should go.
Nmap gives you six timing templates, and the names say it all:
paranoid (0), sneaky (1), polite (2), normal (3), aggressive (4), and insane (5).
You can pick the timing template by its name or number.
For example, you can add -T0 (or -T 0) or -T paranoid to opt for the slowest timing.

- Format the output

In some cases, the scan takes a very long time to finish or to produce any output.
The best way to get more updates about what’s happening is to enable verbose,
by adding -v.

Most likely, the -v option is more than enough for verbose output;
however, if you are still unsatisfied, you can increase the verbosity level:
by adding another “v” such as -vv or even -vvvv.
You can also specify the verbosity level directly, for example, -v2 and -v4.
You can even increase the verbosity level by pressing “v” after the scan started.
If all this verbosity does not satisfy your needs,
you must consider the -d for debugging-level output.

## Zenmap

Zenmap is a GUI version of nmap. - More user friendly.
