
# Networking Fundamentals

## Host

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

## IP Address

IP addresses are the identity of each host.

Every single host must have an IP address if it means to communicate on the internet.

Everything sent on the internet is going to have a source and destination IP address.

The Packet will contain > Source and Destination IP Address.

IP Addresses are 32 bits >  Bit = 1 or 0.

Broken into 4 octets into a decimal number.  (4 octets of 0 through to 255)

IP Addresses are usually Hierachically assigned using Subnetting.

### Public IP Address

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

IP Address range              | number of addresses   |classful description
10.0.0.0 – 10.255.255.255     | 16,777,216            |single class A
172.16.0.0 – 172.31.255.255   | 1,048,576             |16 contiguous class Bs
192.168.0.0 – 192.168.255.255 | 65,536                |256 contiguous class Cs

### The "Mega-City" (Class A)

The Neighborhood: 10.0.0.0 to 10.255.255.255

|Address |Description| Can I use it for my PC?|
|10.0.0.0| Network ID: The "Street Name" for the whole city.| No.|
|10.0.0.1| Default Gateway: The "Front Door" (Router).| Yes (for the router).|
|10.0.0.2| Host Address: A device (Laptop, Phone, etc.).| Yes!|
|10.255.255.255| Broadcast: The city-wide megaphone. |No.|

### The "Suburb" (Class B)

The Neighborhood: 172.16.0.0 to 172.31.255.255

|Address |Description| Can I use it for my PC?|
|172.16.0.0| Network ID: The start of the private slice.| No.|
|172.16.0.1| Default Gateway: The "Front Door" (Router).| Yes (for the router).|
|172.16.0.2| Host Address: A device in the first room.| Yes!|
|172.31.255.255| Broadcast: The megaphone for the 172 zone.| No.|

### The "House" (Class C)

The Neighborhood: 192.168.0.0 to 192.168.255.255

|Address|Description|Can I use it for my PC?|
|192.168.0.0|Network ID: The name of the specific house/street.|No.|
|192.168.0.1|Default Gateway: The "Front Door" (Router).|Yes (for the router).|
|192.168.0.2|Host Address: A device (Your PC or Printer).|Yes!|
|192.168.0.255|Broadcast: The megaphone for this specific room.|No.|

Summary Checklist

Class A: Starts with 10, default mask is 255.0.0.0

Class B: Starts with 172, default mask is 255.255.0.0

Class C: Starts with 192, default mask is 255.255.255.0

#### The "Mask is Boss" Rule

In modern networking, the mask always has the final say.
If you use $255.255.255.0$: Your neighborhood is tiny.
192.168.255.x is a completely different world from 192.168.1.x.
If you use $255.255.0.0$: You have "deleted the walls."
Now, 192.168.1.1 and 192.168.255.254 are neighbors on the same massive street.

Networking pros almost never use a Class B mask ($255.255.0.0$) on a $192.168$ network
unless they have a very specific reason.

It would be incredibly loud.

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

## Network

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

## Repeater

## Hub

## Bridge

## Router
