# MFA

Status: Done

[MFA](../House%20Of%20Vokabel/MFA.md)

## Multi-Factor Authentication

Multi-factor authentication (MFA) uses two or more factors of authentication to verify a user's identity.

Examples of factors:

- Something you **know** — a password or PIN.
- Something you **have** — a security code sent to a phone, a smart card, or a hardware token.
- Something you **are** — biometrics such as fingerprint or retinal scan.
- **Contextual attributes** — gait analysis, geo-location.

## Why MFA matters

MFA provides an extra layer of security, especially when using a single sign-on account,
to ensure the account has not been compromised.

- A password can be written down, guessed, or shared.
- A smart card can be lost or stolen.
- When MFA is in place, a breached username and password are unusable without the additional factor.

Combining a password with a token-generated PIN or a fingerprint scan makes abusing authentication
many factors more complex.

## Related

- [[SSO]] — MFA is especially important when SSO is in use, as a single compromised account grants wide access.
