# Hydra

Hydra is a brute force online password cracking program, a quick system login
password “hacking” tool.

According to its official repository, Hydra supports, i.e., has the ability to
brute force the following protocols: “Asterisk, AFP, Cisco AAA, Cisco auth,
Cisco enable, CVS, Firebird, FTP, HTTP-FORM-GET, HTTP-FORM-POST, HTTP-GET,
HTTP-HEAD, HTTP-POST, HTTP-PROXY, HTTPS-FORM-GET, HTTPS-FORM-POST, HTTPS-GET,
HTTPS-HEAD, HTTPS-POST, HTTP-Proxy, ICQ, IMAP, IRC, LDAP, MEMCACHED, MONGODB,
MS-SQL, MYSQL, NCP, NNTP, Oracle Listener, Oracle SID, Oracle, PC-Anywhere,
PCNFS, POP3, POSTGRES, Radmin, RDP, Rexec, Rlogin, Rsh, RTSP, SAP/R3, SIP, SMB,
SMTP, SMTP Enum, SNMP v1+v2+v3, SOCKS5, SSH (v1 and v2), SSHKEY, Subversion,
TeamSpeak (TS2), Telnet, VMware-Auth, VNC and XMPP.”

WEBFORM -

``` bash
sudo hydra <username> <wordlist> <IP_ADDRESS> http-post-form
"<path>:<login_credentials>:<invalid_response>"
```

```plaintext
Option Description -l the username for (web form) login -P the password list to
use http-post-form the type of the form is POST <path> the login page URL, for
example, login.php <login_credentials> the username and password used to log in,
for example, username=^USER^&password=^PASS^ <invalid_response> part of the
response when the login fails -V verbose output for every attempt
```

SSH -

``` bash
hydra -l <username> -P <full path to pass> <IP_ADDRESS> -t 4 ssh
```

Option Description -l specifies the (SSH) username for login -P indicates a list
of passwords -t sets the number of threads to spawn
