
# Breaking down the WannaCry Hack

## What Was WannaCry

The WannaCry ransomware attack was a worldwide cyberattack in May 2017 by the WannaCry ransomware cryptoworm, which targeted computers running the Microsoft Windows operating system by encrypting data and demanding ransom payments in the form of Bitcoin cryptocurrency. It was propagated using EternalBlue, an exploit developed by the United States National Security Agency (NSA) for Microsoft Windows systems. EternalBlue was stolen and leaked by a group called The Shadow Brokers (TSB) a month prior to the attack.

It is considered a network worm because it also includes a transport mechanism to automatically spread itself. This transport code scans for vulnerable systems, then uses the EternalBlue exploit to gain access, and the DoublePulsar tool to install and execute a copy of itself. WannaCry versions 0, 1 and 2 were created using Microsoft Visual C++ 6.0.

The initial infection was likely through an exposed vulnerable SMB port, rather than email phishing as initially assumed.
Within a day the code was reported to have infected more than 230,000 computers in over 150 countries

Organizations that had not installed Microsoft's security update from March were affected by the attack.

Those still running unsupported versions of Microsoft Windows, such as Windows XP and Windows Server 2003 were at particularly high risk because no security patches had been released since April 2014 for Windows XP and July 2015 for Windows Server 2003.

A Kaspersky Lab study reported, however, that less than 0.1 percent of the affected computers were running Windows XP, and that 98 percent of the affected computers were running Windows 7. In a controlled testing environment, the cybersecurity firm Kryptos Logic found that it was unable to infect a Windows XP system with WannaCry using just the exploits, as the payload failed to load, or caused the operating system to crash rather than actually execute and encrypt files. However, when executed manually, WannaCry could still operate on Windows XP.

## The Failure of WannaCry

The Achilles heel of malware is the need to call home to its operator. For ransomware, there has to be a mechanism for the program’s operator to collect the ransom money and unlock the data. These communications can provide a way for law enforcement to track down the cybercriminals, so they often build into their malware something called a kill switch.

Generally, a kill switch is a mechanism for turning off a device or a piece of software remotely – and abruptly – in an emergency, such as when it has been stolen or accessed without authorisation. In malware, a kill switch is a way for the operator to terminate their connection to the software to prevent authorities from discovering their identity.

One kill switch method is to redirect the malware’s communications to a “sinkhole” server, which can render it ineffective. Investigators can study the malware and look for such a kill switch or a way to take over the software.

In the case of WannaCry, a researcher using the pseudonym MalwareTech ended up accidentally activating the kill switch when he tried to create a sinkhole in order to study the software. WannaCry included code that looked to check if a specified domain had been registered. If it received a response from the domain, it shut down. If not, it continued to work. So when MalwareTech registered the domain, it effectively activated the kill switch.

This kill switch was probably inserted to prevent investigators studying the software in a closed virtual environment called a “sandbox”. These typically respond to all communication attempts by the malware with signals from registered domains. So when WannaCry received a response from the domain, it was tricked into thinking it was in a sandbox and shut down to protect itself.

On 19 May, it was reported that hackers were trying to use a Mirai botnet variant to effect a distributed denial-of-service attack on WannaCry's kill-switch domain with the intention of knocking it offline.[71] On 22 May, Hutchins protected the domain by switching to a cached version of the site, capable of dealing with much higher traffic loads than the live site.
