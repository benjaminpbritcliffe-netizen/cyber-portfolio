# Wireshark

Wireshark can be used for:

- Detecting and troubleshooting network problems,
such as network load failure points and congestion.

- Detecting security anomalies, such as rogue hosts,
abnormal port usage, and suspicious traffic.

- Investigating and learning protocol details, such as response codes
and payload data.


Packet dissection is also known as protocol dissection, which investigates packet details by decoding available protocols and fields. Wireshark supports a long list of protocols for dissection, and you can also write your dissection scripts.

You can click on a packet in the packet list pane to open its details (double-click will open details in a new window). Packets consist of 5 to 7 layers based on the OSI model. 


Severity	Colour	Info
Chat	Blue	Information on usual workflow.
Note	Cyan	Notable events like application error codes.
Warn	Yellow	Warnings like unusual error codes or problem statements.
Error	Red	Problems like malformed packets.


This is the most basic way of filtering traffic. While investigating a capture file, you can click on the field you want to filter and use the "right-click menu" or "Analyse --> Apply as Filter"

You can use the"right-click menu" or  "Analyse --> Follow TCP/UDP/HTTP Stream" menu to follow traffic streams.

