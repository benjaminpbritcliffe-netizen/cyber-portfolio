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

## Simple trust concepts

Trust develops from implicit childhood acceptance to reliance on authority figures. Parents and teachers form a hierarchical trust structure through delegation.

This creates a "chain of trust", where each entity connects to previous trusted entities, ultimately leading to the **root authority**.

This model works when external authorities exist, as with government-issued IDs. Sometimes, however, we must establish our own trust evaluation rules.

### Enrolment and issuance

After establishing trust, entities must undergo enrollment before receiving tokens, with careful management of the issuance process.

Enrollment typically involves a trusted subject introducing new ones to the system, creating tokens, and defining their authority - preferably through class assignments rather than individual permissions.

## Security Engineering Models

Created: 21 May 2025 14:32
Is Completed: Yes

## 📘 1. **Bell-LaPadula Model (Confidentiality Focused)**

- **Goal**: Protect **secrets** — primarily used in military and government.
- **Rules**:
  - **No Read Up**: Users cannot read data above their security level.
  - **No Write Down**: Users cannot write data to lower levels (prevents secret leaks).
- **Think**: "Keep confidential data from leaking."

---

## 📗 2. **Biba Model (Integrity Focused)**

- **Goal**: Protect **accuracy and trustworthiness** of data.
- **Rules**:
  - **No Read Down**: Users cannot read data from lower integrity levels.
  - **No Write Up**: Users cannot write data to higher integrity levels.
- **Think**: "Keep data clean and reliable."

---

## 📙 3. **Clark-Wilson Model (Commercial Integrity)**

- **Goal**: Ensure **data is modified properly** and only by authorized users.
- **Key Ideas**:
  - Uses **well-formed transactions** (controlled steps) to enforce rules.
  - Uses **programs** to separate users from data and verify rules.
- **Think**: "Only the right people can make the right changes the right way."

---

## 📕 4. **Brewer-Nash Model (The 'Coca-Cola' Model)**

- **Goal**: Prevent **conflicts of interest** (used in consulting firms).
- **Key Idea**:
  - Access to one company's data blocks access to competitors' data.
- **Think**: "No spying on competitors."

---

## 📒 5. **Graham-Denning Model**

- **Goal**: Manage **secure rights and permissions** in a system.
- **Key Components**:
  - Defines **8 rules** for creating/deleting users and objects and managing access.
- **Think**: "Who can do what, to which data, and how?"

---

## 🧠 Summary Table

| Model | Focus | Common Use |
| --- | --- | --- |
| Bell-LaPadula | Confidentiality | Military/Government |
| Biba | Integrity | Medical, Banking |
| Clark-Wilson | Commercial Integrity | Business Systems |
| Brewer-Nash | Conflict of Interest | Consulting Firms |
| Graham-Denning | Access Control | Operating Systems |
