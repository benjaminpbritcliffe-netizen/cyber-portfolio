
# Network Architecture

## Network Segmentation

- Segmenting the network to protect against malicious traffic spreading,
- also used to improve performance
- Helps set up control limits

Physical segmentation involves separating different network zones
using separate switches, routers, and cabling.

Virtual segmentation involves using software to create virtual networks
within an existing network, allowing different types of traffic to be separated
and isolated.

Virtual segmentation is associated with cloud computing environments,
where networks are defined using features provided by the virtualization platform.

Logical segmentation involves using software to create logical divisions within
a single network using virtual LANs, or VLANs.

## SDN - Software Defined Networks

- SDNs replace physical network devices like routers and
switches with a virtual control plane that makes all decisions about traffic management.

- Flexibility, replacing of hardware
- Fully automaded links.

- Management Plane > Control Plane > Data Plane
- Use of APIs
- SDN architecture saves security administrators time through centralized
configuration and control.
- It allows for fully automated deployments of network links, appliances, and servers.

Software-defined networking (SDN) abstracts physical network devices,
like routers and switches,
replacing them with a virtual control plane
that makes all decisions regarding traffic management.
SDN allows for building cloud-based networks using virtualized equivalents of
 physical routers, firewalls, and other network devices used in on-premises networks.

Control plane : Makes decisions about how traffic should be prioritized and secured,
and where it should be switched.
Data plane : Handles the actual switching and routing of traffic
and imposition of access control lists (ACLs) for security.
Management plane: Monitors traffic conditions and network status.

## Zero Trust Architecure

- Nothing should be taken for grnnted, network access continuously verified
and authorised.
- Zero-trust architecture implements network and endpoint security
by controlling access to applications, data, and networks.

- Network and Endpoint Security Controls
- IAM to ensure that only verified users can access systems and
- Relies on network segmentation
- Zero-trust restricts network traffic to only legitimate requests
through policy-based enforcement.
- manages access to cloud-based applications, services, and data through cloud security.
- Zero-trust doesn't define security through network boundaries,
but through resources,Users / Services / Workflows

- SASE combines Zero Trust sec with Networking services
- WANS, CASB, Fwaas, Zero Trust

- Important architecutral model.

Greater security — All users, devices, and applications are authenticated
and verified before network access.
Better access controls —
More stringent limits are put in place regarding who or what can access resources
and from what locations resources can be accessed.
Improved governance and compliance — There are limits on data access
and greater operational visibility on user and device activity.
Increased granularity — Users are granted access to what they need
when they need it.

## SASE

Secure Access Service Edge,
a cloud-native framework that unifies networking and security into a single,
cloud-delivered service.

a cloud-based architecture that combines zero-trust security
services with networking services,
provides the protection of a secure access platform with the agility of
a cloud-delivered security architecture.

SASE streamlines the process of granting secure access to all users,
regardless of location.
SASE is a confluence of wide-area networks, network security services,
such as CASB, firewall-as-a-service, and zero-trust in a cloud-delivered service
model.

SASE integrates multiple services, like network access control,
web security gateways, and virtual private network connections.
It also offers advanced features, such as IAM.

SASE eliminates the need for dedicated hardware and
facilities remote management of networks and systems.
