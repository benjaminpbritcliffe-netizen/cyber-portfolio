# Assignment - DUMS

Created: 20 June 2025 16:07
Is Completed: Yes

Task 1 – Outline Design

The Civil Aviation Authority (CAA) has outlined requirements for the safe and secure operation of Unmanned Aerial Vehicles (UAVs). This proposal presents a security-focused architecture for the Drone Universal Management System (DUMS) that addresses these requirements.

1. Run Efficiently on a Low-Power Computer

Given the UAV's real-time constraints, a full operating system is unsuitable. Instead, we recommend a lightweight Real-Time Operating System (RTOS). VxWorks is proposed due to its proven track record in aerospace and unmanned systems.

As noted:

"Leading the industry in this area for more than 25 years, … VxWorks has been certified in more than 750 safety programmes … and more than 120 civilian and military aircraft" [1].

This certification history proves its reliability for real-time drone control and high-assurance security—essential features for managing UAVs in restricted airspace.

1. Allow Updates Without Interference

The system requires a non-intrusive update mechanism to prevent disruption to drone operations. The design includes:

Dual-Partition Firmware Design: The drone maintains active and inactive firmware partitions. New updates are written to the inactive partition while the system continues running on the active one. Updates activate only after verification, allowing recovery if the update fails.

Staging and Verification: Updates are staged in a secure area and verified before deployment to the live system. This prevents corrupt or malicious code from being installed.

Deferred Activation: Updates never activate during flight. The drone must be idle or landed before proceeding.

RTOS Task Prioritization: The RTOS ensures update processes don't interfere with critical real-time functions like GPS processing or flight control.

As Banerjee explains:

"To ensure continuous operation, software updates in real-time embedded systems often use dual-bank flash memory, cryptographic validation, and rollback mechanisms that support atomic switching between versions" [2].

1. Enable Installation During Manufacturing or Servicing (Without Control Node)

The system must support offline installation through secure physical interfaces like USB or serial. This requires a system that can flash drones with bootloader and firmware through a secure physical interface such as USB or Serial.

Authentication can then be enforced through potential offline mechanisms such as:

Service Credentials (e.g., usernames/passwords, One-Time Passwords), and/or Hardware Tokens (e.g., USB keys, smart cards, cryptographic dongles).

These methods ensure identity verification and role-based access control. Alongside the above features, the dual partition structure mentioned earlier can support this secure process, preventing system corruption during installation.

As Smith and O'Donnell state:

"Hardware tokens and digital service credentials are integral to establishing trust in offline environments, especially in embedded systems where central verification authorities may not be accessible" [3].

1. Enable Secure Remote Interaction with Control Nodes

Remote operators (e.g., CAA staff) need secure access to control nodes for software updates and zone file uploads. Access is managed through Role-Based Access Control (RBAC) with defined roles (administrator, technician, viewer). These roles define what actions users can perform on the drone. Strong encryption works alongside RBAC to ensure only authorized operators can access the system, preventing unauthorized access.

All communication must use encryption to ensure data confidentiality and integrity. Combined with RBAC, this prevents unauthorized access or illegitimate changes to drone behavior.

[1] Wind River, "VxWorks RTOS: Trusted for over 25 years in mission-critical systems," Wind River, 2024. [Online]. Available: [https://www.windriver.com/products/vxworks](https://www.windriver.com/products/vxworks)

[2] R. Banerjee, "Firmware update mechanisms for real-time embedded systems," in Proc. IEEE Embedded Syst. Conf., vol. 29, no. 4, pp. 22–27, Apr. 2022.
[3] A. V. Smith and M. O'Donnell, "Authentication methods for secure embedded maintenance," in Proc. IEEE Int. Conf. Trust, Security and Privacy in Comput. Commun., 2023, pp. 55–62.