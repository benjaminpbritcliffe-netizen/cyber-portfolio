
# CASB

A cloud access security broker (CASB)
is enterprise management software designed to mediate access to cloud services,
by users across all types of devices.
It monitors activity between cloud service consumers
and cloud applications and provides enforcement of security policies.

Enable single sign-on authentication and enforce access controls
and authorizations from the enterprise network to the cloud provider.
Scan for malware and rogue or noncompliant device access.
Monitor and audit user and resource activity.
Mitigate data exfiltration,
by preventing access to unauthorized cloud services from managed devices.

Forward proxy —
This is a security appliance or host positioned at the client network edge
that forwards user traffic to the cloud network if the contents of that traffic comply with policy.
This requires configuration of users' devices or installation of an agent.
In this mode, the proxy can inspect all traffic in real time, even if that traffic is not bound for sanctioned cloud applications.
The problem with this mode is that users may be able to evade the proxy and connect directly.
Proxies are also associated with poor performance as without a load balancing solution they become a bottleneck and potentially a single point of failure.
Reverse proxy —This is positioned at the cloud network edge and directs traffic to cloud services if the contents of that traffic comply with policy.
This does not require configuration of the users' devices. This approach is only possible if the cloud application has proxy support.
Application programming interface (API) —Rather than placing a CASB appliance or host inline with cloud consumers and the cloud services,
an API-based CASB brokers connections between the cloud service and the cloud consumer.
For example, if a user account has been disabled or an authorization has been revoked on the local network,
the CASB would communicate this to the cloud service and use its API to disable access there too.
This depends on the API supporting the range of functions that the CASB and access and authorization policies demand.
CASB solutions are quite likely to use both proxy and API modes for different security management purposes.
