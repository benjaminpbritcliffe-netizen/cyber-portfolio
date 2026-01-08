# GoBuster


``` bash

root@ip-10-82-121-118:~# gobuster dir -u "http://www.offensivetools.thm/secret" -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -x .js
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:                     http://www.offensivetools.thm/secret
[+] Method:                  GET
[+] Threads:                 10
[+] Wordlist:                /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt
[+] Negative Status codes:   404
[+] User Agent:              gobuster/3.6
[+] Extensions:              js
[+] Timeout:                 10s
===============================================================
Starting gobuster in directory enumeration mode
===============================================================
/content              (Status: 301) [Size: 341] [--> http://www.offensivetools.thm/secret/content/]
/uploads              (Status: 301) [Size: 341] [--> http://www.offensivetools.thm/secret/uploads/]
/flag.js              (Status: 200) [Size: 22]
Progress: 4527 / 436552 (1.04%)^C
[!] Keyboard interrupt detected, terminating.
Progress: 4530 / 436552 (1.04%)
===============================================================
Finished
===============================================================
root@ip-10-82-121-118:~# gobuster dns -d offensivetools.thm -w /usr/share/wordlists/SecLists/Discovery/DNS/subdomains-top1million-5000.txt
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Domain:     offensivetools.thm
[+] Threads:    10
[+] Timeout:    1s
[+] Wordlist:   /usr/share/wordlists/SecLists/Discovery/DNS/subdomains-top1million-5000.txt
===============================================================
Starting gobuster in DNS enumeration mode
===============================================================
Found: www.offensivetools.thm

Found: forum.offensivetools.thm

Found: store.offensivetools.thm

Found: WWW.offensivetools.thm

Found: primary.offensivetools.thm

Progress: 4997 / 4998 (99.98%)
===============================================================
Finished
===============================================================
root@ip-10-82-121-118:~#  gobuster vhost -u "http://10.82.134.67" --domain offensivetools.thm -w /usr/share/wordlists/SecLists/Discovery/DNS/subdomains-top1million-5000.txt --append-domain --exclude-length 250-320
===============================================================
Gobuster v3.6
by OJ Reeves (@TheColonial) & Christian Mehlmauer (@firefart)
===============================================================
[+] Url:              http://10.82.134.67
[+] Method:           GET
[+] Threads:          10
[+] Wordlist:         /usr/share/wordlists/SecLists/Discovery/DNS/subdomains-top1million-5000.txt
[+] User Agent:       gobuster/3.6
[+] Timeout:          10s
[+] Append Domain:    true
[+] Exclude Length:   271,293,311,313,269,280,283,305,318,255,281,282,298,300,310,315,253,284,295,301,308,265,289,291,264,259,263,270,304,306,256,302,278,251,273,292,312,314,317,250,262,303,320,260,261,252,274,286,290,294,257,267,299,316,258,272,275,276,277,296,307,309,268,288,319,254,297,279,285,287,266
===============================================================
Starting gobuster in VHOST enumeration mode
===============================================================
Found: forum.offensivetools.thm Status: 200 [Size: 2635]
Found: store.offensivetools.thm Status: 200 [Size: 3014]
Found: www.offensivetools.thm Status: 200 [Size: 8806]
Found: secret.offensivetools.thm Status: 200 [Size: 1550]
Found: WWW.offensivetools.thm Status: 200 [Size: 8806]
Progress: 4997 / 4998 (99.98%)
===============================================================
Finished
===============================================================
root@ip-10-82-121-118:~#

```