# 🔐 Hacking Methods to Learn for Cybersecurity

A structured checklist of hacking methods to study for penetration testing, red
teaming, and general cybersecurity defense.\
Tick them off as you learn! Each topic includes **resources** (🎥 videos +
practice labs).

---

## 🖥️ System & Network Hacking

- [ ] **Reconnaissance & Enumeration**
  - [ ] OSINT (Shodan, Maltego, recon-ng)
    - 🎥
      [OSINT Techniques -- The Cyber Mentor](https://www.youtube.com/watch?v=5g3Xir2KYi8)\
  - [ ] Port scanning (Nmap)
    - 🎥
      [Nmap Tutorial for Beginners -- NetworkChuck](https://www.youtube.com/watch?v=3pQZ6cZi2Gc)\
  - [ ] Service enumeration (SMB, RDP, SNMP, LDAP)
    - Practice:
      [HackTheBox Starting Point](https://app.hackthebox.com/starting-point)
- [ ] **Network Attacks**
  - [ ] ARP spoofing & MITM (Ettercap, Bettercap)
    - 🎥
      [MITM Attacks Explained -- Computerphile](https://www.youtube.com/watch?v=Y5X1nCzmw9I)\
  - [ ] DNS spoofing & poisoning\
  - [ ] DHCP starvation/rogue DHCP servers\
  - [ ] VLAN hopping
    - 🎥
      [Bettercap Tutorial -- Null Byte](https://www.youtube.com/watch?v=gychqXbjpYk)\
    - Practice:
      [TryHackMe "Intro to Networking"](https://tryhackme.com/room/introtonetworking)
- [ ] **Exploitation**
  - [ ] Buffer overflows
    - 🎥
      [Buffer Overflow Demo -- LiveOverflow](https://www.youtube.com/watch?v=1S0aBV-Waeo)\
  - [ ] Privilege escalation (Windows & Linux)
    - 🎥
      [Privilege Escalation Basics -- IppSec](https://www.youtube.com/watch?v=1dqyeWWq6hU)\
  - [ ] Exploiting misconfigured services (FTP, SMB, RDP, databases)\
  - [ ] Remote code execution (RCE)
    - Practice:
      [TryHackMe "Linux PrivEsc"](https://tryhackme.com/room/linuxprivesc)

---

## 🌐 Web Application Hacking

- [ ] **Injection Attacks**
  - [ ] SQL Injection
    - 🎥
      [SQL Injection Crash Course -- The Cyber Mentor](https://www.youtube.com/watch?v=ciNHn38EyRc)\
  - [ ] Command Injection
    - 🎥
      [Command Injection -- John Hammond](https://www.youtube.com/watch?v=Mo1XneVvLZc)\
  - [ ] LDAP & XML External Entities (XXE)
    - Practice:
      [PortSwigger Web Security Academy](https://portswigger.net/web-security)
- [ ] **Authentication & Session Attacks**
  - [ ] Brute force & credential stuffing\
  - [ ] Password spraying\
  - [ ] Session hijacking (cookies, JWTs, tokens)
    - 🎥
      [Session Hijacking Basics -- Null Byte](https://www.youtube.com/watch?v=EpxsDrlls0A)\
  - [ ] Broken authentication logic
    - 🎥
      [JWT Attacks Explained -- Stök](https://www.youtube.com/watch?v=7p4dZLy6d_c)
- [ ] **Client-Side Attacks**
  - [ ] Cross-Site Scripting (XSS)
    - 🎥
      [XSS Explained -- LiveOverflow](https://www.youtube.com/watch?v=sA0-Gc2l4ZI)\
  - [ ] Cross-Site Request Forgery (CSRF)\
  - [ ] Clickjacking
    - Practice: [TryHackMe "XSS Room"](https://tryhackme.com/room/xssgi)
- [ ] **Advanced Web Attacks**
  - [ ] Server-Side Request Forgery (SSRF)
    - 🎥 [SSRF Demo -- InsiderPhD](https://www.youtube.com/watch?v=QkH8k2QJ2UM)\
  - [ ] Deserialization exploits
    - 🎥
      [Deserialization Exploits -- Hak5](https://www.youtube.com/watch?v=SlCnrJtHi-Y)\
  - [ ] Web cache poisoning

---

## 📡 Wireless & Mobile Hacking

- [ ] **Wi-Fi Attacks**
  - [ ] WEP/WPA/WPA2 cracking (aircrack-ng, hashcat)
    - 🎥
      [Wi-Fi Hacking with Aircrack-ng -- Null Byte](https://www.youtube.com/watch?v=R0-YoMw4D3A)\
    - Practice:
      [Aircrack-ng Docs](https://www.aircrack-ng.org/doku.php?id=Main)\
  - [ ] Evil twin attacks / rogue access points\
  - [ ] KRACK attack concepts
- [ ] **Bluetooth & IoT Exploitation**
  - [ ] Bluejacking, bluesnarfing
    - 🎥
      [Bluetooth Hacking Basics -- Hak5](https://www.youtube.com/watch?v=72_2MpbKBME)\
  - [ ] Zigbee & NFC hacking basics
    - 🎥
      [IoT Hacking Demo -- LiveOverflow](https://www.youtube.com/watch?v=9S5wF3EX_cI)
- [ ] **Mobile Apps**
  - [ ] Android APK reverse engineering
    - 🎥
      [Reverse Engineering Android Apps -- LiveOverflow](https://www.youtube.com/watch?v=szlJwl8FG4I)\
  - [ ] iOS jailbreak attack surface
    - Practice: [OWASP Juice Shop](https://owasp.org/www-project-juice-shop/)

---

## 🔑 Identity & Credential Attacks

- [ ] **Password Attacks**
  - [ ] Dictionary & rainbow table attacks\
  - [ ] Hash cracking (hashcat, John the Ripper)
    - 🎥 [Hashcat Crash Course](https://www.youtube.com/watch?v=fi30Ji-B5Yc)\
    - 🎥
      [John the Ripper Demo -- Null Byte](https://www.youtube.com/watch?v=QkTxIY1Mfzg)
- [ ] **Kerberos & Active Directory**
  - [ ] Kerberoasting
    - 🎥
      [Kerberoasting Explained -- HackTricks](https://www.youtube.com/watch?v=hqf3u3pYSh8)\
  - [ ] Golden Ticket & Silver Ticket attacks\
  - [ ] NTLM relay attacks\
  - [ ] DCSync
    - 🎥
      [Active Directory Attacks -- The Cyber Mentor](https://www.youtube.com/watch?v=4zUYz3fM5lA)\
    - Practice:
      [TryHackMe "AD Basics"](https://tryhackme.com/room/activedirectorybasics)

---

## 🛠️ Social Engineering & Phishing

- [ ] Spear phishing campaigns\
- [ ] Malvertising (ad poisoning)\
- [ ] Watering hole attacks\
- [ ] Business Email Compromise (BEC)
  - 🎥
    [Social Engineering -- Computerphile](https://www.youtube.com/watch?v=Q05rV5JUnxE)\
  - 🎥
    [Phishing Explained -- John Hammond](https://www.youtube.com/watch?v=ADjD3f4McbU)\
  - Practice: [GoPhish Toolkit](https://getgophish.com/)

---

## 🐚 Post-Exploitation & Persistence

- [ ] Reverse shells & bind shells
  - 🎥
    [Reverse Shells -- The Cyber Mentor](https://www.youtube.com/watch?v=Z4mN8g6FYSk)\
- [ ] Web shells\
- [ ] Windows persistence (scheduled tasks, registry keys)
  - 🎥
    [Windows Persistence -- IppSec](https://www.youtube.com/watch?v=20cH-9cT-4Y)\
- [ ] Linux persistence (cronjobs, systemd services)\
- [ ] Lateral movement (PsExec, WMI, RDP hijacking)
  - Practice: [TryHackMe "Persistence"](https://tryhackme.com/room/persistence)

---

## 🎭 Advanced Topics

- [ ] **Cloud Hacking**
  - [ ] AWS IAM misconfigurations
    - 🎥 [AWS Security Misconfigs](https://www.youtube.com/watch?v=vopXg_VKu30)\
  - [ ] Azure AD attacks (token theft, conditional access bypass)
    - 🎥
      [Azure AD Attacks -- Andy Robbins](https://www.youtube.com/watch?v=Yj2i2z2yqxE)\
  - [ ] GCP misconfigurations
- [ ] **Container & DevOps Security**
  - [ ] Docker escape
    - 🎥
      [Docker Escape -- John Hammond](https://www.youtube.com/watch?v=k3A6_io0S3g)\
  - [ ] Kubernetes privilege escalation
    - 🎥
      [Kubernetes Security 101 -- CNCF](https://www.youtube.com/watch?v=7N0fPRzs1iY)
- [ ] **Binary Exploitation & Reverse Engineering**
  - [ ] Assembly basics\
  - [ ] Malware unpacking and analysis
    - 🎥
      [Malware Analysis Basics -- MalwareTech](https://www.youtube.com/watch?v=IlBv6S7ORLw)\
  - [ ] Exploit development (ROP chains, heap spraying)
    - 🎥
      [Binary Exploitation Playlist -- LiveOverflow](https://www.youtube.com/playlist?list=PLhixgUqwRTjxglIswKp9mpkfPNfHkzyeN)

---

✅ Suggested learning order:\

1. System & network basics\
2. Web hacking\
3. Identity attacks\
4. Post-exploitation\
5. Cloud & advanced topics
