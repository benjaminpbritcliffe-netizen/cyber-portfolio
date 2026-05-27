
# Identity and Access Management

IAM is the framework for ensuring the right individuals have the right
access to the right resources — no more, no less.

Core functions:

- **Identify** — verify who or what is requesting access
- **Authorise** — grant or deny access based on policy

---

## Access Control Models

**Superuser** — Has full privileges across the network, including the
ability to grant privileges to other users.

**RBAC (Role-Based Access Control)** — Access is assigned based on a
user's role within the organisation. Users receive only the permissions
necessary to perform their job.

**ABAC (Attribute-Based Access Control)** — Access decisions are based
on a combination of attributes: the user, the object being accessed,
the action being performed, and environmental context (e.g. time of
day, location).

**MAC (Mandatory Access Control)** — Uses security labels applied to
both subjects (users) and objects (data, applications, systems,
networks, physical spaces). Every operation is evaluated against a
central set of authorisation policies before access is permitted.

---

## Authentication Methods

Secure user identification relies on strong authentication:

- Strong, complex passwords
- Multi-Factor Authentication (MFA / 2FA)

---

## Centralised Policy Management

Access control is governed by a central policy applied consistently
across all user types:

- **Administrators** — manage systems, users, and policies
- **Employees** — access resources relevant to their role
- **Customers** — limited access to approved external-facing services
