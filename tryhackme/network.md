
Topologies
Star Topology
The main premise of a star topology is that devices are individually connected via a central networking device such as a switch or hub. This topology is the most commonly found today because of its reliability and scalability - despite the cost.

Bus Topology
This type of connection relies upon a single connection which is known as a backbone cable. This type of topology is similar to the leaf off of a tree in the sense that devices (leaves) stem from where the branches are on this cable.

Because all data destined for each device travels along the same cable, it is very quickly prone to becoming slow and bottlenecked if devices within the topology are simultaneously requesting data. This bottleneck also results in very difficult troubleshooting because it quickly becomes difficult to identify which device is experiencing issues with data all travelling along the same route.

However, with this said, bus topologies are one of the easier and more cost-efficient topologies to set up because of their expenses, such as cabling or dedicated networking equipment used to connect these devices.


Ring Topology
The ring topology (also known as token topology) boasts some similarities. Devices such as computers are connected directly to each other to form a loop, meaning that there is little cabling required and less dependence on dedicated hardware such as within a star topology.

A ring topology works by sending data across the loop until it reaches the destined device, using other devices along the loop to forward the data. Interestingly, a device will only send received data from another device in this topology if it does not have any to send itself. If the device happens to have data to send, it will send its own data first before sending data from another device.

Because there is only one direction for data to travel across this topology, it is fairly easy to troubleshoot any faults that arise. However, this is a double-edged sword because it isn't an efficient way of data travelling across a network, as it may have to visit many multiple devices first before reaching the intended device.

 Subnetting is the term given to splitting up a network into smaller, miniature networks within itself. 
 
 Subnetting is achieved by splitting up the number of hosts that can fit within the network, represented by a number called a subnet mask.

A subnet mask which is also represented as a number of four bytes (32 bits), ranging from 0 to 255 (0-255).
 
 Now, in small networks such as at home, you will be on one subnet as there is an unlikely chance that you need more than 254 devices connected at one time.

However, places such as businesses and offices will have much more of these devices (PCs, printers, cameras and sensors), where subnetting takes place.

Subnetting provides a range of benefits, including:

Efficiency
Security
Full control


Type	Purpose	Explanation	Example
Network Address 
This address identifies the start of the actual network and is used to identify a network's existence.
For example, a device with the IP address of 192.168.1.100 will be on the network identified by 192.168.1.0
192.168.1.0
Host Address
An IP address here is used to identify a device on the subnet
For example, a device will have the network address of 192.168.1.1
192.168.1.100
Default Gateway
The default gateway address is a special address assigned to a device on the network that is capable of sending information to another network 
Any data that needs to go to a device that isn't on the same network (i.e. isn't on 192.168.1.0) will be sent to this device. These devices can use any host address but usually use either the first or last host address in a network (.1 or .254)
192.168.1.254



Recalling from our previous tasks that devices can have two identifiers: A MAC address and an IP address, the Address Resolution Protocol or ARP for short, is the technology that is responsible for allowing devices to identify themselves on a network.

Each device within a network has a ledger to store information on, which is called a cache. In the context of ARP, this cache stores the identifiers of other devices on the network.

In order to map these two identifiers together (IP address and MAC address), ARP sends two types of messages:

ARP Request
ARP Reply


IP addresses can be assigned either manually, by entering them physically into a device, or automatically and most commonly by using a DHCP (Dynamic Host Configuration Protocol) server. When a device connects to a network, if it has not already been manually assigned an IP address, it sends out a request (DHCP Discover) to see if any DHCP servers are on the network. The DHCP server then replies back with an IP address the device could use (DHCP Offer). 




The OSI model (or Open Systems Interconnection Model) is an essential model used in networking.  This critical model provides a framework dictating how all networked devices will send, receive and interpret data.

# Physical

The physical components of hardware used for networking


- Ethernet Cable

# Data Link

 focuses on the physical addressing of the transmission. It receives a packet from the network layer (including the IP address for the remote computer) and adds in the physical MAC (Media Access Control) address of the receiving endpoint. Inside every network-enabled computer is a Network Interface Card (NIC) which comes with a unique MAC address to identify it.

- Network Interface Card

# Network

 where the magic of routing & re-assembly of data takes place (from these small chunks to the larger chunk). Firstly, routing simply determines the most optimal path in which these chunks of data should be sent.

Whilst some protocols at this layer determine exactly what is the "optimal" path that data should take to reach a device, we should only know about their existence at this stage of the networking module. Briefly, these protocols include OSPF (Open Shortest Path First) and RIP (Routing Information Protocol).

- Routing 

- IP Addresses

# Transport

When data is sent between devices, it follows one of two different protocols that are decided based upon several factors:

TCP 
UDP

- TCP
- UDP

# Session

 the session layer (layer 5) will begin to create and maintain the connection to other computer for which the data is destined. When a connection is established, a session is created. Whilst this connection is active, so is the session.

The session layer is also responsible for closing the connection if it hasn't been used in a while or if it is lost. Additionally, a session can contain "checkpoints," where if the data is lost, only the newest pieces of data are required to be sent, saving bandwidth. 

- Connection Checking

# Presentation

Layer 6 of the OSI model is the layer in which standardisation starts to take place. Because software developers can develop any software such as an email client differently, the data still needs to be handled in the same way — no matter how the software works.

This layer acts as a translator for data to and from the application layer (layer 7).

- Translator

# Application

The application layer of the OSI model is the layer that you will be most familiar with. This familiarity is because the application layer is the layer in which protocols and rules are in place to determine how the user should interact with data sent or received.

- Data Interaction


# Headers and Messages

A packet is a piece of data from Layer 3 (Network Layer) of the OSI model, containing information such as an IP header and payload. A frame, however, is used at Layer 2 (Data Link) of the OSI model, which, encapsulates the packet and adds additional information such as MAC addresses.

Some notable headers include:

Header	Description
Time to Live	This field sets an expiry timer for the packet to not clog up your network if it never manages to reach a host or escape!
Checksum	This field provides integrity checking for protocols such as TCP/IP. If any data is changed, this value will be different from what was expected and therefore corrupt.
Source Address	The IP address of the device that the packet is being sent from so that data knows where to return to.
Destination Address	The device's IP address the packet is being sent to so that data knows where to travel next.

Packet = Does Have IP Address information
Frame = Does Not Have IP Address information

The TCP/IP protocol consists of four layers and is arguably just a summarised version of the OSI model. These layers are:

Application
Transport
Internet
Network Interface


One defining feature of TCP is that it is connection-based, which means that TCP must establish a connection between both a client and a device acting as a server before data is sent.

Step	Message	Description
1	SYN	A SYN message is the initial packet sent by a client during the handshake. This packet is used to initiate a connection and synchronise the two devices together (we'll explain this further later on).
2	SYN/ACK	This packet is sent by the receiving device (server) to acknowledge the synchronisation attempt from the client.
3	ACK	The acknowledgement packet can be used by either the client or server to acknowledge that a series of messages/packets have been successfully received.
4	DATA	Once a connection has been established, data (such as bytes of a file) is sent via the "DATA" message.
5	FIN	This packet is used to cleanly (properly) close the connection after it has been complete.
6   RST	This packet abruptly ends all communication. This is the last resort and indicates there was some problem during the process. For example, if the service or application is not working correctly, or the system has faults such as low resources. 


 UDP is a stateless protocol that doesn't require a constant connection between the two devices for data to be sent. For example, the Three-way handshake does not occur, nor is there any synchronisation between the two devices.


# Port Forwarding

If the administrator wanted the website to be accessible to the public (using the Internet), they would have to implement port forwarding.

t port forwarding opens specific ports (recall how packets work). In comparison, firewalls determine if traffic can travel across these ports (even if these ports are open by port forwarding).

Port forwarding is configured at the router of a network.

# Firewall

A firewall is a device within a network responsible for determining what traffic is allowed to enter and exit. 

- Where the traffic is coming from? (has the firewall been told to accept/deny traffic from a specific network?)

- Where is the traffic going to? (has the firewall been told to accept/deny traffic destined for a specific network?)
What port is the traffic for? (has the firewall been told to accept/deny traffic destined for port 80 only?)

- What protocol is the traffic using? (has the firewall been told to accept/deny traffic that is UDP, TCP or both?)

Firewalls perform packet inspection to determine the answers to these questions.



## Stateful	
This type of firewall uses the entire information from a connection; rather than inspecting an individual packet, this firewall determines the behaviour of a device based upon the entire connection.

This firewall type consumes many resources in comparison to stateless firewalls as the decision making is dynamic. For example, a firewall could allow the first parts of a TCP handshake that would later fail.

If a connection from a host is bad, it will block the entire device.

## Stateless	
This firewall type uses a static set of rules to determine whether or not individual packets are acceptable or not. For example, a device sending a bad packet will not necessarily mean that the entire device is then blocked.

Whilst these firewalls use much fewer resources than alternatives, they are much dumber. For example, these firewalls are only effective as the rules that are defined within them. If a rule is not exactly matched, it is effectively useless.

However, these firewalls are great when receiving large amounts of traffic from a set of hosts (such as a Distributed Denial-of-Service attack)

# VPN

A Virtual Private Network (or VPN for short) is a technology that allows devices on separate networks to communicate securely by creating a dedicated path between each other over the Internet (known as a tunnel). Devices connected within this tunnel form their own private network.



For example, only devices within the same network (such as within a business) can directly communicate. However, a VPN allows two offices to be connected. 

VPN Technology	Description

PPP	
This technology is used by PPTP (explained below) to allow for authentication and provide encryption of data. VPNs work by using a private key and public certificate (similar to SSH). A private key & certificate must match for you to connect.

This technology is not capable of leaving a network by itself (non-routable).

PPTP	
The Point-to-Point Tunneling Protocol (PPTP) is the technology that allows the data from PPP to travel and leave a network. 

PPTP is very easy to set up and is supported by most devices. It is, however, weakly encrypted in comparison to alternatives.

IPSec	
Internet Protocol Security (IPsec) encrypts data using the existing Internet Protocol (IP) framework.

IPSec is difficult to set up in comparison to alternatives; however, if successful, it boasts strong encryption and is also supported on many devices.

# Router

It's a router's job to connect networks and pass data between them. It does this by using routing (hence the name router!).
 
Routing is the label given to the process of data travelling across networks. 