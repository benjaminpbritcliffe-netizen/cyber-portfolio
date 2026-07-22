# pfSense Firewall — Installation & Full Walkthrough

A complete guide to deploying pfSense in VMware as a test/lab environment,
covering installation through full configuration.

---

## Overview

pfSense is an open-source firewall/router distribution based on FreeBSD. In a
lab environment it acts as the network gateway between segments, giving you
full control over traffic, firewall rules, VLANs, VPN, and IDS/IPS.

**Lab topology used in this guide:**

```text
Internet (NAT)
     │
 ┌───┴────────────────────────────────┐
 │          pfSense VM                │
 │  WAN (em0)       LAN (em1)         │
 └────┬─────────────────┬─────────────┘
      │                 │
  VMware NAT       VMware Host-Only
  (external)       192.168.1.1/24
                        │
                   Lab VMs / clients
```

---

## Prerequisites

| Item        | Detail                                                                                                           |
|-------------|------------------------------------------------------------------------------------------------------------------|
| Hypervisor  | VMware Workstation Pro / Player (or Fusion on macOS)                                                             |
| pfSense ISO | Download from [netgate.com/downloads](https://www.netgate.com/downloads) — select **AMD64**, **DVD Image (ISO)** |
| RAM         | 512 MB minimum, 1–2 GB recommended                                                                               |
| Disk        | 8 GB minimum                                                                                                     |
| vNICs       | 2 × network adapters (WAN + LAN)                                                                                 |

---

## Part 1 — Creating the VMware VM

### 1.1 New Virtual Machine Wizard

1. Open VMware → **File → New Virtual Machine**
2. Select **Custom (advanced)** → click **Next**
3. Hardware compatibility: leave default → **Next**
4. Installer disc image file (ISO): browse to your pfSense `.iso` → **Next**
5. Guest OS:
   - Type: **Other**
   - Version: **FreeBSD 14 64-bit** (or closest available)
6. VM name: `pfSense-Lab` — choose a location → **Next**
7. Processors: **1 CPU, 1 core** → **Next**
8. Memory: **1024 MB** → **Next**

### 1.2 Network Adapters

This is the critical step — pfSense needs two NICs.

**Adapter 1 (WAN):**

- Network connection: **NAT**
- This gives pfSense outbound internet access via your host machine

**Adapter 2 (LAN):**

- Network connection: **Host-only** (or a custom VMnet, e.g. VMnet2)
- This is the internal lab network your other VMs will connect to

> To add the second adapter: after the wizard finishes, go to **VM →
> Settings → Add → Network Adapter** and set it to Host-only.

### 1.3 Disk & Finish

1. Disk: **Create a new virtual disk**
2. Disk size: **20 GB**, store as single file → **Next**
3. Review settings → **Finish**

---

## Part 2 — Installing pfSense

### 2.1 Boot from ISO

Power on the VM. The pfSense installer boots automatically. At the
copyright/distribution screen press **Enter** to accept.

### 2.2 Installation Steps

| Prompt               | Selection                                                      |
|----------------------|----------------------------------------------------------------|
| Welcome              | **Install**                                                    |
| Keymap               | **Continue with default keymap** (or select yours)             |
| Partitioning         | **Auto (ZFS)** — recommended for labs                          |
| ZFS config           | **Stripe — No Redundancy** (single disk lab)                   |
| Select disk          | `da0` (your 20 GB virtual disk) → **Space** to select → **OK** |
| Destroy disk warning | **YES**                                                        |

The installer copies files. When complete:

- Select **No** at the shell prompt (unless you need manual config)
- Select **Reboot**

**Before it reboots:** go to **VM → Settings → CD/DVD** and disconnect the
ISO so it doesn't boot back into the installer.

---

## Part 3 — Initial Console Configuration

On first boot you land at the pfSense console menu. The system will ask to
assign interfaces.

### 3.1 Interface Assignment

```text
Valid interfaces are:
  em0   00:0c:29:xx:xx:xx  (vmxnet3/e1000)
  em1   00:0c:29:xx:xx:xx  (vmxnet3/e1000)

Should VLANs be set up now? n

Enter WAN interface name: em0
Enter LAN interface name: em1
```

Confirm with **y**.

### 3.2 Set LAN IP (Option 2)

From the console menu select **2) Set interface(s) IP address**, then choose **LAN**.

| Setting          | Value                                  |
|------------------|----------------------------------------|
| LAN IPv4 address | `192.168.1.1`                          |
| Subnet mask bits | `24`                                   |
| Gateway          | (leave blank — pfSense is the gateway) |
| IPv6             | leave blank for now                    |
| Enable DHCP      | **y**                                  |
| DHCP start       | `192.168.1.100`                        |
| DHCP end         | `192.168.1.200`                        |
| Revert to HTTP   | **n** (keep HTTPS)                     |

The WebGUI URL will be shown: `https://192.168.1.1`

---

## Part 4 — WebGUI Setup Wizard

From a VM on the LAN network (or the VMware host if using host-only) browse to `https://192.168.1.1`.

- Accept the self-signed certificate warning
- Default credentials: **admin / pfsense**

### 4.1 Setup Wizard

Work through each screen:

| Screen              | Action                                                                                                   |
|---------------------|----------------------------------------------------------------------------------------------------------|
| General Information | Set **Hostname** (e.g. `pfsense-lab`), **Domain** (e.g. `lab.local`), DNS servers (`1.1.1.1`, `8.8.8.8`) |
| Time Server         | Leave default NTP or set your preferred server                                                           |
| WAN Interface       | Type: **DHCP** (VMware NAT assigns an IP automatically)                                                  |
| LAN Interface       | Confirm `192.168.1.1 / 24`                                                                               |
| Admin Password      | **Change the default password immediately**                                                              |
| Reload              | Click **Reload** — pfSense applies settings                                                              |

---

## Part 5 — Dashboard & Basic Navigation

After the wizard you land on the **Dashboard**.

```text
Status → Dashboard       — system overview, CPU, memory, interfaces
Interfaces               — WAN / LAN status and configuration
Firewall → Rules         — inbound/outbound rule management
Firewall → Aliases       — named IP/port groups for cleaner rules
Services → DHCP Server   — LAN DHCP leases and reservations
Services → DNS Resolver  — local DNS / ad-blocking
VPN                      — OpenVPN, IPsec, WireGuard
System → Package Manager — install add-ons (Suricata, pfBlockerNG, etc.)
Diagnostics → Ping       — connectivity testing from pfSense itself
```

---

## Part 6 — Firewall Rules

### 6.1 How pfSense Rules Work

- Rules are evaluated **top to bottom**, first match wins
- Rules are applied on the **ingress** interface (traffic coming *in* to
  pfSense from that interface)
- The **LAN** tab covers traffic from your lab VMs heading outward
- The **WAN** tab covers traffic arriving from the internet

### 6.2 Default Rules

Out of the box:

- LAN → **Allow All** (any traffic from LAN is permitted)
- WAN → **Block All** (no unsolicited inbound traffic)

This is fine for a basic lab. For a segmented lab you'll tighten the LAN rules.

### 6.3 Creating a Rule (Example: Block a VM from the internet)

#### Firewall → Rules → LAN → Add (↑ top)

| Field          | Value                                             |
|----------------|---------------------------------------------------|
| Action         | **Block**                                         |
| Interface      | LAN                                               |
| Address Family | IPv4                                              |
| Protocol       | Any                                               |
| Source         | Single host — `192.168.1.105` (the VM to isolate) |
| Destination    | Any                                               |
| Description    | `Block isolated-vm outbound`                      |

Click **Save** → **Apply Changes**.

### 6.4 Aliases

Keep rules readable by using aliases.

#### Firewall → Aliases → Add

| Field   | Value            |
|---------|------------------|
| Name    | `Lab_VMs`        |
| Type    | Network          |
| Network | `192.168.1.0/24` |

Reference `Lab_VMs` in rules instead of raw CIDRs.

---

## Part 7 — DHCP Reservations

To give a lab VM a fixed IP:

### Services → DHCP Server → LAN → DHCP Static Mappings → Add

| Field       | Value                                                                |
|-------------|----------------------------------------------------------------------|
| MAC address | VM's MAC (find in VMware → VM Settings → Network Adapter → Advanced) |
| IP address  | `192.168.1.10`                                                       |
| Hostname    | `kali-lab`                                                           |

---

## Part 8 — DNS Resolver

pfSense's built-in Unbound DNS resolver handles name resolution for your lab.

**Services → DNS Resolver:**

- Enable: checked
- DNSSEC: enabled (recommended)
- DNS Query Forwarding: optional (forwards to upstream DNS like 1.1.1.1)

**Add a local override** (e.g. to resolve `pfsense.lab.local`):

### Services → DNS Resolver → Host Overrides → Add

| Field  | Value         |
|--------|---------------|
| Host   | `pfsense`     |
| Domain | `lab.local`   |
| IP     | `192.168.1.1` |

---

## Part 9 — Snapshots & Base VM Strategy

Because this is a test VM, use VMware snapshots as restore points.

### Recommended Snapshot Strategy

```text
[Base Install]          ← clean install, wizard complete, password changed
       │
[Lab Config]            ← your firewall rules, DHCP reservations, DNS
       │
[Package Testing]       ← Suricata / pfBlockerNG installed
```

**Create a snapshot:**

VMware → **VM → Snapshot → Take Snapshot**

Name it descriptively: `Base - wizard complete - no packages`

Revert at any time via **VM → Snapshot → Snapshot Manager**.

---

## Part 10 — Useful Packages (Optional)

Install via **System → Package Manager → Available Packages**.

| Package                   | Purpose                                               |
|---------------------------|-------------------------------------------------------|
| **pfBlockerNG**           | DNS-based ad/malware blocking (like Pi-hole built in) |
| **Suricata**              | Network IDS/IPS — detect and block malicious traffic  |
| **OpenVPN Client Export** | Easy VPN client config generation                     |
| **nmap**                  | Network scanner accessible from pfSense diagnostics   |
| **darkstat**              | Lightweight traffic statistics                        |

---

## Part 11 — Security Hardening Checklist

- [ ] Change default admin password
- [ ] Disable HTTP access (use HTTPS only) — **System → Advanced → Admin
      Access → HTTPS**
- [ ] Change WebGUI port from 443 if WAN-exposed — `System → Advanced → TCP port`
- [ ] Restrict WebGUI to LAN only (default, verify WAN firewall rule blocks
      port 443 inbound)
- [ ] Enable **Bogon Networks** blocking on WAN — **Interfaces → WAN → Block
      bogon networks**
- [ ] Enable **Scrub** (traffic normalisation) — on by default in modern pfSense
- [ ] Disable unused services
- [ ] Keep pfSense updated — **System → Update**

---

## Troubleshooting

| Symptom                  | Check                                                                                         |
|--------------------------|-----------------------------------------------------------------------------------------------|
| Can't reach WebGUI       | Confirm LAN VM is on `192.168.1.x`, ping `192.168.1.1`, check VMware network adapter settings |
| No internet from LAN VMs | Check WAN has an IP (`Status → Interfaces`), check default LAN allow-all rule exists          |
| DNS not resolving        | `Services → DNS Resolver` enabled, DNS servers set in General Setup                           |
| Rule not taking effect   | Check rule order (top-to-bottom), click **Apply Changes** after saving                        |
| Wrong interface assigned | Console menu → Option 1 to reassign interfaces                                                |

---

## References

- [pfSense Official Documentation](https://docs.netgate.com/pfsense/en/latest/)
- [Netgate Downloads](https://www.netgate.com/downloads)
- [pfSense Forum](https://forum.netgate.com/)
