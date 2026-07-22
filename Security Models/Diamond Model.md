
# Diamond Model

The Diamond Model of Intrusion Analysis is set out in a paper by Sergio Caltagirone,
Andrew Pendergast, and Christopher Betz
( activeresponse.org/wp-content/uploads/2013/07/diamond.pdf ).

The Diamond Model suggests a framework to analyze an intrusion event
by exploring the relationships among four core features:

adversary,

This element represents the individual or group responsible for the intrusion.
Adversaries can include nation states, criminal organizations, hacktivists,
or malicious insiders.

capability,

This element describes the technical skills and aptitude of the adversary,
such as their ability to craft advanced techniques to evade detection,
exploit vulnerabilities, and persist on target systems.

infrastructure,

This element refers to the tools
and resources used by the adversary to carry out the intrusion.
Tools include malware, exploit kits, command and control servers,
and other types of network infrastructure.
and victim.

The victim element represents the organization or individual the adversary has targeted,
such as government agencies, businesses, or individuals.
Victims vary in size, industry type, and defensive capabilities.

Events can be linked into attack graphs and activity threads,
graphed along each vertex,
representing the paths an adversary could take (if analyzing an attack in progress)
and those that were taken (if analyzing past activity).
Also, threads can be assigned to activity groups,
which can be used to represent campaigns by particular adversaries.
