# Security Engineering

Created: 9 May 2025 20:33
Is Completed: Yes

![image.png](Security%20Engineering%201ee3d034d9f780dba174d7c8c67951cf/image.png)

Authentication verifies that presented tokens are genuine and sufficient to prove legitimacy. Systems need a way to validate token authenticity before acceptance.

The username-password model demonstrates this through challenge-response: first present a username (a weak identity claim), then verify with a password (a stronger token).

Passwords, while convenient, have limitations due to common reuse and predictable choices. Still, they remain prevalent due to their ease of use.

As a shared secret, passwords require both parties to know the correct value. This creates a challenge in securely distributing and mapping credentials while ensuring they reach only authorized parties.

i.e. - we lack **trust.**

While trust establishment extends beyond token issuance, we'll focus on its role in Identification and Authentication.

### Simple trust concepts

Trust develops from implicit childhood acceptance to reliance on authority figures. Parents and teachers form a hierarchical trust structure through delegation.

This creates a "chain of trust", where each entity connects to previous trusted entities, ultimately leading to the **root authority**.

This model works when external authorities exist, as with government-issued IDs. Sometimes, however, we must establish our own trust evaluation rules.

### Enrolment and issuance

After establishing trust, entities must undergo enrollment before receiving tokens, with careful management of the issuance process.

Enrollment typically involves a trusted subject introducing new ones to the system, creating tokens, and defining their authority - preferably through class assignments rather than individual permissions.