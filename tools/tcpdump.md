
# TCPDump

The libpcap library is the foundation for various other networking tools today.
Moreover, it was ported to MS Windows as winpcap.

A command such as ip address show (or merely ip a s)
would list the available network interfaces.

- In many cases, you should check the captured packets again later.
- This can be achieved by saving to a file using -w FILE.
- You can use Tcpdump to read packets from a file by using -r FILE.
- You can specify the number of packets to capture by specifying the count -c COUNT.
- Tcpdump will resolve IP addresses and print friendly domain names where possible.
- To avoid making such DNS lookups, you can use the -n argument.
- If you want to print more details about the packets,
- you can use -v to produce a slightly more verbose output.
- Let’s say you are only interested in IP packets exchanged with your network printer
- You can easily limit the captured packets to this host using host IP or host HOSTNAME

- If you want to limit the packets to those from a particular source IP address,
or host you must use src host IP or src host HOSTNAME.
- Similarly, you can limit packets to those sent to a specific destination.
Using dst host IP or dst host HOSTNAME.

- If you want to capture all DNS traffic,
you can limit the captured packets to those on port 53.

- You can limit your packet capture to a specific protocol;
examples include: ip, ip6, udp, tcp, and icmp.

Command Explanation
tcpdump -i INTERFACE Captures packets on a specific network interface
tcpdump -w FILE Writes captured packets to a file
tcpdump -r FILE Reads captured packets from a file
tcpdump -c COUNT Captures a specific number of packets
tcpdump -n Don’t resolve IP addresses
tcpdump -nn Don’t resolve IP addresses and don’t resolve protocol numbers
tcpdump -v Verbose display; verbosity can be increased with -vv and -vvv

Command Explanation
tcpdump host IP or tcpdump host HOSTNAME Filters packets by IP address or hostname
tcpdump src host IP or Filters packets by a specific source host
tcpdump dst host IP Filters packets by a specific destination host
tcpdump port PORT_NUMBER Filters packets by port number
tcpdump src port PORT_NUMBER Filters packets by the specified source port number
tcpdump dst port PORT_NUMBER Filters packets by the specified destination port number
tcpdump PROTOCOL Filters packets by protocol; examples include ip, ip6, and icmp

sudo tcpdump -r traffic.pcap icmp | wc

 sudo tcpdump -r traffic.pcap -nn arp
reading from file traffic.pcap, link-type EN10MB (Ethernet)
07:18:29.940761 ARP, Request who-has 192.168.124.137 tell 192.168.124.148,
length 28
07:18:29.940776 ARP, Reply 192.168.124.137 is-at 52:54:00:23:60:2b, length 28

sudo tcpdump -r traffic.pcap port 53

You can use tcp[tcpflags] to refer to the TCP flags field.
The following TCP flags are available to compare with:

tcp-syn TCP SYN (Synchronize)
tcp-ack TCP ACK (Acknowledge)
tcp-fin TCP FIN (Finish)
tcp-rst TCP RST (Reset)
tcp-push TCP Push
Based on the above, we can write:

``` bash
tcpdump "tcp[tcpflags] == tcp-syn"
to capture TCP packets with only the SYN (Synchronize) flag set,
while all the other flags are unset.
tcpdump "tcp[tcpflags] & tcp-syn != 0" to capture TCP packets with at least the SYN (Synchronize) flag set.
tcpdump "tcp[tcpflags] & (tcp-syn|tcp-ack) != 0" to capture TCP packets with at least the SYN (Synchronize) or ACK (Acknowledge) flags set.

 sudo tcpdump -r traffic.pcap "tcp[tcpflags] == tcp-rst" | wc

 greater LENGTH: Filters packets that have a length greater than or equal to the specified length
less LENGTH: Filters packets that have a length less than or equal to the specified length

Command Explanation
tcpdump -q Quick and quite: brief packet information
tcpdump -e Include MAC addresses
tcpdump -A Print packets as ASCII encoding
tcpdump -xx Display packets in hexadecimal format
tcpdump -X Show packets in both hexadecimal and ASCII formats

sudo tcpdump -r traffic.pcap greater 15000 -n

user@ip-10-10-35-8:~$  sudo tcpdump -r traffic.pcap -nn arp -e
reading from file traffic.pcap, link-type EN10MB (Ethernet)
07:18:29.940761 52:54:00:7c:d3:5b > ff:ff:ff:ff:ff:ff, ethertype ARP (0x0806), length 42: Request who-has 192.168.124.137 tell 192.168.124.148, length 28
07:18:29.940776 52:54:00:23:60:2b > 52:54:00:7c:d3:5b, ethertype ARP (0x0806), length 42: Reply 192.168.124.137 is-at 52:54:00:23:60:2b, length 28
```
