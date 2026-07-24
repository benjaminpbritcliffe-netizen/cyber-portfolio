# Scanning Considerations

Malicious actors want to be as strategic as possible
when selecting scanning tools and methods to use.
They must carefully consider the strengths and weaknesses of each scan type.
Selecting the wrong method not only takes up valuable time
but also increases the chances of detection.

In addition to the type of scan,
a malicious actor considers the time of day that scans are run.
Take into consideration that a malicious actor might be counting on:

A mid-day scan to blend in with legitimate network activity.
An after-hours scan to go unnoticed.

Hardening techniques will cause a hacker to encounter obstacles when running scans.
The obstacles are there to discourage, frustrate, and even detect the hacker.
When encountering obstacles,
a hacker will typically change tactics.
The following table lists some of those tactics.

Tactic

Description
Scan with ACK
This type of scan is designed to determine whether the firewall is stateful or stateless.
It also identifies the open or closed status of ports.
In an ACK scan, only the ACK flag is set.
If a port is unfiltered, open and closed ports return an RST packet.
If a port is filtered, it either returns an error message or no response.

Create fragment packets
Fragmenting is probably one of the most commonly used methods to avoid detection.
The malicious actor continues to send packets;
however, the packets are broken apart,
so intrusion detection systems do not recognize them as a threat.

As long as the fragmented packets are not bombarding the system,
the packet segments are undetected.

Spoof IP addresses
Many scanning tools can recraft a packet
so that the source address reflects a different IP address.
The target system is scanned,
the feedback is returned to the fake IP address,
and there is no record of the hacker's IP address.

Use a proxy
A proxy serves as a less vulnerable access point to a network.
Typically, proxies are placed in networks
to keep external users from accessing the internal network.
Hackers like proxies because they filter incoming and outgoing traffic.
Proxies provide the hacker with anonymity and shield from possible detection.
