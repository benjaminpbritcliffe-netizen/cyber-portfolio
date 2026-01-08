# 🧠 Wireshark Tutorial

Wireshark is one of the most widely used **network protocol analyzers**. It
allows you to capture and inspect network traffic in real time, providing deep
visibility into how devices communicate over a network.

Whether you’re troubleshooting connectivity issues, analyzing security events,
or learning how network protocols work, Wireshark is an essential tool in a
cybersecurity analyst’s toolkit.

---

## 🧩 What Wireshark Can Be Used For

### 🔹 Detecting and Troubleshooting Network Problems

Wireshark can help you:

- Identify **network bottlenecks** or **latency**.
- Detect **failure points** in communication paths.
- Observe **bandwidth utilization** and **network congestion**.
- Verify **network configuration** issues (e.g., DHCP, DNS).
- Track **retransmissions**, **dropped packets**, or **routing loops**.

---

### 🔹 Detecting Security Anomalies

Wireshark is also a powerful **security investigation tool**. It helps you:

- Identify **rogue hosts** or **unauthorized devices**.
- Detect **abnormal port usage** or **unusual traffic patterns**.
- Spot **malformed or suspicious packets** (e.g., crafted attacks).
- Investigate **failed encryption handshakes** and **TLS alerts**.
- Trace **data exfiltration** or **covert communication channels**.

---

### 🔹 Investigating and Learning Protocol Details

Wireshark is great for hands-on learning about how protocols operate. You can:

- Examine how **TCP handshakes**, **DNS lookups**, or **HTTP requests** behave.
- Inspect **response codes**, **headers**, and **payload data**.
- Understand **protocol layering** and **encapsulation**.
- Compare **expected vs. actual** network behavior for applications.

---

## 🧱 Packet Dissection (Protocol Dissection)

**Packet dissection** — also known as **protocol dissection** — means breaking
down captured packets into their protocol layers and fields.

Wireshark can decode hundreds of network protocols such as:

- Ethernet
- IPv4 / IPv6
- TCP / UDP / ICMP
- DNS, HTTP, FTP, TLS, QUIC, MQTT, and many more.

You can even create **custom dissectors** in **Lua** or **Python** to analyze
proprietary protocols.

When you click on a packet in the **Packet List Pane**, details appear below in
a hierarchical view. Double-clicking opens the packet in a separate window for
deep analysis.

---

## 🧬 OSI Model Layers

Each packet may contain **5 to 7 layers**, depending on the protocol stack.
These correspond to the **OSI model**:

| Layer | Description  | Example Protocols                |
| ----- | ------------ | -------------------------------- |
| 7     | Application  | HTTP, DNS, FTP, SMTP             |
| 6     | Presentation | SSL/TLS (encryption, formatting) |
| 5     | Session      | RPC, NetBIOS                     |
| 4     | Transport    | TCP, UDP                         |
| 3     | Network      | IP, ICMP                         |
| 2     | Data Link    | Ethernet, ARP                    |
| 1     | Physical     | Bitstream over cable or radio    |

---

## 🎨 Severity Colour Codes

Wireshark highlights packets with different colours to help you interpret
traffic quickly.

| **Severity** | **Colour** | **Meaning**                               |
| ------------ | ---------- | ----------------------------------------- |
| Chat         | Blue       | Regular workflow information              |
| Note         | Cyan       | Notable events or non-critical errors     |
| Warn         | Yellow     | Warnings, unusual or unexpected behaviour |
| Error        | Red        | Serious problems or malformed packets     |

To view or modify colours: `View → Coloring Rules`

---

## 🔍 Filtering Traffic

Filtering is the heart of packet analysis in Wireshark. You can use two main
types of filters:

### 🎯 Capture Filters

- Applied **before** you start capturing.
- Limit what packets Wireshark records.

**Examples:**

```bash
tcp port 80
host 192.168.1.10
net 10.0.0.0/24
```

### 🧮 Display Filters

- Applied **after** capture.
- Filter what is displayed in the results.

**Examples:**

```bash
http.request
ip.addr == 10.0.0.5
tcp.flags.syn == 1 and tcp.flags.ack == 0
dns.qry.name == "example.com"
```

To apply a filter interactively:

- Right-click a field and select **Apply as Filter → Selected** or
- Use **Analyse → Apply as Filter**.

---

## 🌐 Following Streams

To view the **entire conversation** between two hosts (e.g., client and server):

- Right-click a packet and choose: **Follow → TCP Stream / UDP Stream / HTTP
  Stream**
- Or from the menu: **Analyse → Follow → TCP/UDP/HTTP Stream**

This reconstructs the **full bidirectional data flow**, showing the exchange in
a readable format. It’s especially useful for:

- Reconstructing HTTP sessions.
- Viewing chat messages or plaintext protocols.
- Analyzing suspicious traffic.

---

## 🚀 Advanced Uses

As networks evolve, Wireshark remains crucial for:

- **Incident response** – tracing attacker activity.
- **Threat hunting** – finding hidden or encrypted tunnels.
- **Machine learning research** – generating labeled packet datasets.
- **Protocol testing** – verifying new or custom protocols.
- **Forensic analysis** – identifying compromised systems or exfiltration
  routes.

---

## 🧠 Pro Tip

Combine Wireshark with other tools for a more complete workflow:

- **Nmap** – for network scanning and host discovery.
- **tcpdump** – for command-line packet capture.
- **Zeek/Bro** – for network security monitoring and scripting.
- **NetworkMiner** – for extracting files and credentials from captures.

---

## 🧭 Summary

Wireshark empowers you to:

- Capture and decode live network traffic.
- Investigate protocol behavior and anomalies.
- Diagnose connectivity and performance issues.
- Understand network security at the packet level.

Mastering Wireshark takes practice. Start small — capture a simple web request,
analyze DNS traffic, or trace a TCP handshake — and gradually explore more
complex scenarios like encrypted communication or malware C2 channels.

---

## 📚 Next Steps

- Practice capturing traffic in a **controlled lab environment**.
- Learn how to **use capture filters effectively** to minimize noise.
- Explore **decryption options** for TLS (with private keys).
- Try building **custom display filters** for repetitive tasks.
- Gradually integrate Wireshark into **incident response workflows**.

---

> 💡 **Remember:** Every packet tells a story. The more you analyze, the better
> you’ll understand the language of networks.
