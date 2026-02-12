
# Active Directory

The core of any Windows Domain is **Active Directory Domain Services (AD DS)** —
a catalogue holding information about all **objects** (users, groups, machines,
printers, shares, etc.).

**Users** can represent:

- **People**: individuals needing access.
- **Services**: special accounts with only the privileges needed for a service.

**Machines**: When a computer joins the domain, a machine object is created.

**Security Groups**: Assign rights to groups rather than individuals.

By default, OUs are protected against accidental deletion. To delete an OU,
enable **Advanced Features** in the **View** menu, then right-click the OU →
**Properties** → **Object** tab → uncheck protection.

```powershell
C:\Users\phillip> Set-ADAccountPassword sophie -Reset -NewPassword (Read-Host -AsSecureString -Prompt 'New Password') -Verbose

New Password: *********

VERBOSE: Performing the operation "Set-ADAccountPassword" on target "CN=Sophie,OU=Sales,OU=THM,DC=thm,DC=local".
```

## Device Categories

- **Workstations**: Used by end users; should never have privileged users signed
  in.
- **Servers**: Provide services to users/servers.
- **Domain Controllers**: Manage the domain; most sensitive; contain hashed
  passwords for all users.

## Group Policy Objects (GPOs)

GPOs are collections of settings applied to OUs (to users or computers).
Configure with **Group Policy Management**. Distributed via the **SYSVOL**
share.

## Domain Controllers & Authentication

Credentials are stored in Domain Controllers. Two protocols:

- **Kerberos** (default in modern domains)
- **NetNTLM** (legacy compatibility)

**Kerberos flow**: After obtaining a **TGT**, users request **TGS** tickets to
access specific services.

**NetNTLM flow** (challenge/response):

1. Client requests access
2. Server sends challenge (random number)
3. Client responds using NTLM hash + challenge
4. Server forwards to DC for verification
5. DC validates; server relays result

## Trees & Forests

- **Tree**: Multiple domains sharing a namespace.
- **Forest**: Union of trees with different namespaces.
- **Trusts** connect domains/trees so users can access resources across
  boundaries.

## Learning Objectives

- Learn more about **HTML Injection**.
- Learn **Active Directory** further.
