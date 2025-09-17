
# TCPDump

The libpcap library is the foundation for various other networking tools today.
Moreover, it was ported to MS Windows as winpcap.

A command such as ip address show (or merely ip a s) would list the available network interfaces.

- In many cases, you should check the captured packets again later. This can be achieved by saving to a file using -w FILE.
- You can use Tcpdump to read packets from a file by using -r FILE.
- You can specify the number of packets to capture by specifying the count using -c COUNT.
- Tcpdump will resolve IP addresses and print friendly domain names where possible.
- To avoid making such DNS lookups, you can use the -n argument.
- If you want to print more details about the packets, you can use -v to produce a slightly more verbose output.
- Let’s say you are only interested in IP packets exchanged with your network printer or a specific game server.
- You can easily limit the captured packets to this host using host IP or host HOSTNAME

- If you want to limit the packets to those from a particular source IP address or host you must use src host IP or src host HOSTNAME.
- Similarly, you can limit packets to those sent to a specific destination using dst host IP or dst host HOSTNAME.

- If you want to capture all DNS traffic, you can limit the captured packets to those on port 53.

- You can limit your packet capture to a specific protocol; examples include: ip, ip6, udp, tcp, and icmp.