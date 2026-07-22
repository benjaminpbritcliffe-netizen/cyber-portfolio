# OpenID

Status: Done

[OpenID](../House%20Of%20Vokabel/OpenID.md)

OpenID is a method of authenticating users
with sites that participate in an OpenID system,
enabling them to retain a single account for all participating sites.

Large companies such as Google and Amazon use their own OpenID systems.

**OpenID Connect** adds a layer of authentication on top of OAuth 2.0,
the latest version of the protocol.

## Process

1. A user registers with an OpenID system in a given domain
like they would with any other account.
2. A site under this OpenID domain gives the user the option to sign in
using this system.
3. The site contacts its external OpenID provider to verify
that the login credentials supplied by the user are correct.
