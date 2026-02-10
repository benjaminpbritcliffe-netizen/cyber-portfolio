
# Networking Fundamentals

## Hardware

### Repeater

Data can decay across long distances.
Repeaters regenerate signals to allow communications across greater distances.

### Hub

Connecting hosts directly to each other doesn't scale well.
A hub is simply a multi port repeater
Packets would be duplicated acoross all hosts.
Everyone receives everyones packets.

 Anything that comes in on one end simply gets regenerated out the other side.

### Bridge

Bridges sit between hub-connected hosts.
Bridges only have two ports.

 One port facing one set of hub-connected devices,
 and another port facing the other set of hub-connected devices.

Bridges learn which hosts on each side.

### Switch

Switches are a combination of Hubs and Bridges
Multiple Ports
Learns which hosts are on each port

 The main difference is that they are doing it on a per-port basis,
  which means if these two hosts want to speak to each other,
 the switch will know that the only ports that need to receive this traffic,
 are the two that are connected to those green hosts,
 and it will keep that communication contained to just those ports.

 The formal definition of a switch that we want to use is:
 A switch is a device which facilitates communication within a network.

  In one way or another, since all these devices are connected with a switch,
  they all belong to the same network.
 The reason you might want to separate two sets of devices into their own network
 is because they might have different connectivity requirements.

### Router

Router facilitates communication between networks. (internet and local subnets)
Provide traffic control point between networks. (Security, Filtering,Redirecting)
Routing table - all networks a router knows about.
Each hosts way out of their local network using the Gateway.

Routers create the hiercachy in networks and the entire intenet.

 The internet is nothing more than a bunch of different routers itself.

Routers provide traffic control points between networks.

### Routing vs Switching

Routing is the process of moving data BETWEEN networks.

Switching is the process of moving data WITHIN networks.

### Cabling

## Protocols

### Network

 A network is what actually does the transportation of traffic between hosts.

- Anytime two hosts are connected, a network is created.

- A logical grouping of hosts which require similar connectivity.

- A network can contain other networks (Sub-Networks or Subnets.)

- Networks connect to other networks (Internet!)

instead of having each of these networks connect directly to each other,
in every possible combination,
instead all those networks are connected to a central resource, namely the Internet.
In fact, what we know of as the Internet is simply a bunch of interconnected networks.

### Network Scenario

Here is a breakdown of how your factory scenario works in practice:

The Perimeter (Public IP):

The factory has one (or a small handful) of Public IPs,
assigned to its main router or firewall.

To the outside world,any traffic coming from the factory looks like it originated
from that one specific address.

The Internal Hierarchy (Subnets) Inside the factory:

you use Private IP ranges (like 10.x.x.x).

You divide these into subnets to keep things organized and secure:

Accounting Subnet: 10.0.1.x
Production Floor Subnet: 10.0.2.x
Guest Wi-Fi Subnet: 10.0.3.x

Inter-Departmental Communication:

If a computer in Accounting needs to send to a machine on the Production Floor,
the traffic stays "local."
It goes to the internal router, which sees both subnets and passes the data across.
This never touches the public internet.

Going External (The NAT Process):

When a host needs to reach a server in the outside world
(like Google or a vendor's portal):

Outgoing: The host sends a packet with its Private IP as the "Source.

The Swap: When the packet hits the factory's main router,
the router performs NAT (Network Address Translation).

It swaps the Private IP for the factory’s Public IP.The Table:
The router makes a note in its "NAT Table":
"Host 10.0.1.50 asked for Google on Port XYZ."

The Return Trip - When the external server replies:

it sends the data back to the factory's Public IP.
The router looks at its table,
sees that "Port XYZ" belongs to the request from Host 10.0.1.50,
and tosses the packet back to the correct computer in the Accounting department.

### Host

Any device that sends or receives traffic over a network.
(Including Cloud Services and IoT Devices.)

Hosts typically fall in one of two categories, clients or servers.

Clients are the hosts that are initiating the request,
Servers are the hosts that are responding to requests.

Servers when talking to other servers can become the client.
The terms client and server are specific to the communication that is occurring

Note:

You can turn any device into a server by simply installing the proper server software.
Are merely computers with software that knows how to provide files or provide updates.

### IP Address

IP addresses are the identity of each host.

Every single host must have an IP address if it means to communicate on the internet.

Everything sent on the internet is going to have a source and destination IP address.

The Packet will contain > Source and Destination IP Address.

IP Addresses are 32 bits >  Bit = 1 or 0.

Broken into 4 octets into a decimal number.  (4 octets of 0 through to 255)

IP Addresses are usually Hierachically assigned using Subnetting.

#### Public IP Address

Public IP Address: Assigned by an Internet Service Provider (ISP),
it is used to identify devices on the internet.

Public IPs are unique globally and allow devices to communicate over the internet.

Public IP Ranges
The number of public IP addresses is far greater than the number of private ones.

Because every network on the Internet must have a unique public IP.

The Router is the only device with a Public IP.
It acts as the "gatekeeper" between local network and the global internet.

Devices (phone, laptop, smart fridge) are assigned Private IPs by the router.

NAT allows all these devices to "hide" behind that one Public IP.

- The router sends the request out using its Public IP
- remembers who asked for it
- And then passes the data back to the devices Private IP.

All public IP addresses belong to one of the following public IP address ranges:

1.0.0.0-9.255.255.255
11.0.0.0-100.63.255.255
100.128.0.0-126.255.255.255
128.0.0.0-169.253.255.255
169.255.0.0-172.15.255.255
172.32.0.0-191.255.255.255
192.0.1.0/24
192.0.3.0-192.88.98.255
192.88.100.0-192.167.255.255
192.169.0.0-198.17.255.255
198.20.0.0-198.51.99.255
198.51.101.0-203.0.112.255
203.0.114.0-223.255.255.255

Public IPv4 Addresses: Limited to about 4.3 billion.

### Private IP Address

Private IP Address: Used within a local network,
it is not accessible from the internet.
Private IPs can be reused across different networks,
and are assigned by routers to devices within the same network.

| IP Address range              | number of addresses | classful description    |
|-------------------------------|---------------------|-------------------------|
| 10.0.0.0 – 10.255.255.255     | 16,777,216          | single class A          |
| 172.16.0.0 – 172.31.255.255   | 1,048,576           | 16 contiguous class Bs  |
| 192.168.0.0 – 192.168.255.255 | 65,536              | 256 contiguous class Cs |

### The "Mega-City" (Class A)

The Neighborhood: 10.0.0.0 to 10.255.255.255

| Address        | Description                                       | Can I use it for my PC? |
|----------------|---------------------------------------------------|-------------------------|
| 10.0.0.0       | Network ID: The "Street Name" for the whole city. | No.                     |
| 10.0.0.1       | Default Gateway: The "Front Door" (Router).       | Yes (for the router).   |
| 10.0.0.2       | Host Address: A device (Laptop, Phone, etc.).     | Yes!                    |
| 10.255.255.255 | Broadcast: The city-wide megaphone.               | No.                     |

### The "Suburb" (Class B)

The Neighborhood: 172.16.0.0 to 172.31.255.255

| Address        | Description                                 | Can I use it for my PC? |
|----------------|---------------------------------------------|-------------------------|
| 172.16.0.0     | Network ID: The start of the private slice. | No.                     |
| 172.16.0.1     | Default Gateway: The "Front Door" (Router). | Yes (for the router).   |
| 172.16.0.2     | Host Address: A device in the first room.   | Yes!                    |
| 172.31.255.255 | Broadcast: The megaphone for the 172 zone.  | No.                     |

### The "House" (Class C)

The Neighborhood: 192.168.0.0 to 192.168.255.255

| Address       | Description                                        | Can I use it for my PC? |
|---------------|----------------------------------------------------|-------------------------|
| 192.168.0.0   | Network ID: The name of the specific house/street. | No.                     |
| 192.168.0.1   | Default Gateway: The "Front Door" (Router).        | Yes (for the router).   |
| 192.168.0.2   | Host Address: A device (Your PC or Printer).       | Yes!                    |
| 192.168.0.255 | Broadcast: The megaphone for this specific room.   | No.                     |

Summary Checklist

Class A: Starts with 10, default mask is 255.0.0.0

Class B: Starts with 172, default mask is 255.255.0.0

Class C: Starts with 192, default mask is 255.255.255.0

### Gateway

In the professional networking world,
using .1 as the Default Gateway for every subnet is the de facto industry standard.
While the math allows you to pick any valid IP address to be the "Front Door,"
.1 is the undisputed king of consistency.

The 10s (10.0.0.1 $\rightarrow$ 10.255.255.1)

The 172s (172.16.0.1 $\rightarrow$ 172.31.0.1)

The 192s (192.168.0.1 $\rightarrow$ 192.168.255.1)

| CIDR | Subnet        | Mask        | Network         | Example The Edge (Last Usable IP) The Megaphone (Broadcast) | Explanation                                                                                                      |
|------|---------------|-------------|-----------------|-------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------|
| /8   | 255.0.0.0     | 10.0.0.0    | 10.255.255.254  | 10.255.255.255                                              |                                                                                                                  |
| /12  | 255.240.0.0   | 172.16.0.0  | 172.31.255.254  | 172.31.255.255                                              |                                                                                                                  |
| /16  | 255.255.0.0   | 172.16.0.0  | 172.16.255.254  | 172.16.255.255                                              |                                                                                                                  |
| /16  | 255.255.0.0   | 192.168.0.0 | 192.168.255.254 | 192.168.255.255                                             | Because this covers the entire 192.168 empire (all 256 streets).                                                 |
| /24  | 255.255.255.0 | 192.168.1.0 | 192.168.1.254   | 192.168.1.255                                               | While 0.0 is technically the first street, 1.0 is the "Industry Standard" example for a single home/office room. |

Houses typically use 192.168.0.1 or 1.1 (Depending on ISP)

Note: for /16  172.16.x.x is often the "Pro" Choice

Most network engineers prefer 172.16.x.x for business or lab environments
for one big reason:

VPNs.

Imagine you are working from home.

Your home router is probably 192.168.1.1. If your office also uses 192.168.1.1,
and you connect via VPN, your computer gets "confused."

It won't know if 192.168.1.50 is your printer in the kitchen
or the file server at work.

By using 172.16.x.x for your project/office:

You almost never clash with a home Wi-Fi network.

You have enough "vertical room" (65,000 IPs)
to grow without ever needing to change your subnet mask.

Row Acceptable Range (The "Green Zone")
/8 Anything from 10.0.0.1 to 10.255.255.254
/12 Anything from 172.16.0.1 to 172.31.255.254
/16 Anything from 192.168.0.1 to 192.168.255.254
/16 anything from 172.16.0.1  to 172.16.255.254
/24 Anything from 192.168.1.1 to 192.168.1.254

#### The "Mask is Boss" Rule

In modern networking, the mask always has the final say.
If you use $255.255.255.0$: Your neighborhood is tiny.
192.168.255.x is a completely different world from 192.168.1.x.
If you use $255.255.0.0$: You have "deleted the walls."
Now, 192.168.1.1 and 192.168.255.254 are neighbors on the same massive street.

Networking pros almost never use a Class B mask ($255.255.0.0$) on a $192.168$ network
unless they have a very specific reason.

Address ends in .255? Check the mask.

Small Mask (/24)? It's a Megaphone (Reserved).

Big Mask (/8)? It's a House (Usable).

 | CIDR | Subnet Mask   | What it means                                 | Analogy                            |
 |------|---------------|-----------------------------------------------|------------------------------------|
 | /8   | 255.0.0.0     | Only the 1st number is the street name.       | The Mega-City. (16 million houses) |
 | /16  | 255.255.0.0   | The 1st and 2nd numbers are the street name.  | The Suburb. (65,534 houses)        |
 | /24  | 255.255.255.0 | The 1st, 2nd, and 3rd numbers are the street. | The Single Room. (254 houses)      |

#### The "Stadium Shouting" Problem

Imagine a room with 65,534 people in it.

In a normal "Class C" room ($192.168.1.x$), you only have 254 people.
If one person shouts "Where is the printer?", 253 people ignore it. No big deal.

In your "Massive Street" ($192.168.x.x$ with a $/16$ mask),
if one computer shouts:
"Where is the printer?", all 65,533 other computers have to stop what they are doing,
look at the packet, and realize it's not for them.

"Broadcast Storms" When you have that many devices in one "room,"
the background noise becomes a constant roar.
Eventually, the network spends more time "shouting" than actually "talking."
This is called a Broadcast Storm,
and it can effectively paralyze your internet speed.

### IP Address Last ones

The 10s: 10.0.0.2 -  10.255.255.254

The 172s:  172.16.0.2 - 172.31.255.254

The 192s: 192.168.0.2 - 192.168.255.254

## Subnetting

A subnet mask is used to identify the network and host portions of an IP address.
It helps routers determine the correct subnet for routing data packets.
For example, a subnet mask of 255.255.255.0
indicates that the first three octets represent the network,
and the last octet represents the host.

## TCP/IP networking protocols

### 1. Physical

The physical components of hardware used for networking.

- Ethernet cable

### 2. Data Link

Handles **physical addressing**. Receives a packet from the network layer and
adds the **MAC address** of the receiving endpoint. Network Interface Cards
(NICs) have unique MAC addresses.

- Network Interface Card (NIC)

### 3. Network

Where **routing** and **reassembly** take place. Determines the optimal path for
data. Protocols include OSPF and RIP.

- Routing
- IP Addresses

#### Public IP Addresses

Public IPs are globally routable and uniquely identify devices on the Internet.
[Public IP Addresses](<https://www.geeksforgeeks.org/computer-networks/what-is->
public-ip-address)

#### Private IP Addresses (RFC1918)

- `10.0.0.0/8` → `10.0.0.0 – 10.255.255.255`
- `172.16.0.0/12` → `172.16.0.0 – 172.31.255.255`
- `192.168.0.0/16` → `192.168.0.0 – 192.168.255.255`

Private IPs are non-routable on the Internet and used within local networks.
[Private IP Addresses](<https://www.geeksforgeeks.org/computer-networks/private->
ip-addresses-in-networking/)

### 4. Transport

When data is sent between devices, it follows one of two protocols: **TCP** or
**UDP**.

#### TCP

Transmission Control Protocol is a connection-oriented transport protocol.
It uses various mechanisms to ensure reliable data delivery,
sent by the different processes on the networked hosts.
Like UDP, it is a layer 4 protocol.
Being connection-oriented, it requires the establishment of a TCP connection,
before any data can be sent.

A TCP connection is established using what’s called a three-way handshake.

Two flags are used: SYN (Synchronise) and ACK (Acknowledgment).

The packets are sent as follows:

| Step | Message | Description                                    |
|------|---------|------------------------------------------------|
| 1    | SYN     | Client initiates connection & synchronization. |
| 2    | SYN/ACK | Server acknowledges synchronization.           |
| 3    | ACK     | Acknowledge receipt of previous messages.      |
| 4    | DATA    | Exchange application data.                     |
| 5    | FIN     | Cleanly close the connection.                  |
| 6    | RST     | Abruptly terminate due to error/problem.       |

**Features:**

- Sequencing (numbers each segment)
- Flow control
- Error control
- Congestion awareness

**Applications:**

- Web (WWW)
- Email (SMTP, IMAP/POP via TCP)
- FTP
- SSH
- Some streaming services

**Advantages:**

- Reliable connection
- Ordered delivery
- OS-agnostic operation
- Supports many routing protocols
- Adapts to receiver speed

**Disadvantages:**

- Slower than UDP; more overhead
- Slower start (handshake)
- No native multicast/broadcast
- Sensitive to missing data (head-of-line blocking)

#### UDP

User Datagram Protocol allows us to reach a specific process on this target host.
UDP is a simple connectionless protocol that operates at the transport layer,
layer 4. Being connectionless means that it does not need to establish a connection.
UDP does not even provide a mechanism to know that the packet has been delivered.

**Features:**

- Connectionless, low-overhead
- Suitable for multicast
- Used by some routing protocols (e.g., RIP)
- Good for real-time apps

**Applications:**

- Real-time multimedia streaming
- Online gaming
- DNS queries
- Network monitoring
- Multicasting
- Routing updates

**Advantages:**

- No connection setup
- Broadcast/multicast support
- Works across many networks
- Real-time friendly
- Tolerates partial data

**Disadvantages:**

- No delivery acknowledgment
- No sequencing
- Unreliable by design
- Routers may drop on collision/error

## 5. Session

Creates and maintains connections (sessions). Can include **checkpoints** for
efficient recovery and is responsible for closing idle/lost connections.

- Connection checking

### 6. Presentation

Provides **standardization and translation** between application data formats.

- Translator

### 7. Application

Defines the protocols and rules users/applications interact with.

- Data interaction

The Device: Computers, Smartphones, and Servers.

This is the last and topmost layer of the OSI model.
This layer provides an interface between:
the local system and the application program running on the network.

If an application wants to use the resources available on the remote system,
it interacts with this layer.
Then, this layer provides the protocols and services,
that the application needs to access those resources.

There are two types of application programs: Network-aware and Network-unaware.
An application program is considered a Network-aware application,
if it can make any type of network request.
If an application program cannot make any type of network request,
it is considered a Network-unaware program.

### TCP VS UDP

## HTTP vs HTTPS

## Port Numbers

[Port Numbers Markdown](PortNumbers.md)

## DNS and DHCP

## Three Way Handshake (SYN - ACK - SYN ACK)

| Step | Message | Sender | Purpose                                                                           |
|------|---------|--------|-----------------------------------------------------------------------------------|
| 1    | SYN     | Client | "Hey, I'd like to talk. Here is my starting sequence number."                     |
| 2    | SYN/ACK | Server | "I hear you! I'm ready too. Here is my sequence number, and I acknowledge yours." |
| 3    | ACK     | Client | "Got it. We’re synced. Let’s start the data flow."                                |

| Step | Message | Description                                    |
|------|---------|------------------------------------------------|
| 1    | SYN     | Client initiates connection & synchronization. |
| 2    | SYN/ACK | Server acknowledges synchronization.           |
| 3    | ACK     | Acknowledge receipt of previous messages.      |
| 4    | DATA    | Exchange application data.                     |
| 5    | FIN     | Cleanly close the connection.                  |
| 6    | RST     | Abruptly terminate due to error/problem.       |

## Basic security practices
