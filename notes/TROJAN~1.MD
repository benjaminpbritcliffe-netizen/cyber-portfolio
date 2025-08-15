# Trojan Horses

Created: 2 June 2025 10:00
Is Completed: Yes

- If you wanted to deliberately cause a denial of service attack, by consuming as much CPU time as possible, what sort of operating system design features would make this easier?
- If your malicious program was designed to gain access to sensitive data, how might it attempt to use the OS to assist with this goal? (state any assumptions you need to make about the OS design in order to make your attempt feasible).

A Trojan Horse is software that appears harmless and performs useful functions while secretly causing damage in the background. For example, it could be a text editor that copies text to a hidden file, or a modified Unix command that alters permissions while performing its normal function.

Regarding denial of service attacks and CPU consumption, there are several protection approaches:

- A Trusted Computer Base (TCB) can be implemented that includes:
    - A Reference Monitor to enforce access control policies
    - Access routines for sensitive operations
    - A verified Trojan-free environment

For accessing sensitive data, malicious programs often exploit Discretionary Access Control (DAC) weaknesses because:

- DAC allows Trojans to operate with all the privileges of their host process
DAC assumes all system components are legitimate and doesn't verify intentions before granting access

To protect against these threats, a hybrid system can be implemented that:

- Uses DAC as the primary access control policy
Incorporates Mandatory Access Control (MAC) elements to handle untrusted software
Requires all access requests to go through the TCB's reference monitor

MAC offers stronger protection than DAC because:

- It groups subjects and objects into security classes
Prevents rogue processes from altering permissions directly
Requires changes to go through a formal, controlled approval process