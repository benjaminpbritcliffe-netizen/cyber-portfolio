
# Federation

In normal terms classed as Single Sign On

SSO is a process that allows users to sign into a single trusted account,
such as Google or Facebook.

The user is then allowed to log in to a variety of sites without being required
to log in again.

Federation:

Is a trust relationship that exists between organizations or applications.
Allows one entity to be is responsible for the authentication of the user.
Stores a user's credentials so that trusted third parties can authenticate,
using those credentials without seeing the credentials.

Identity Provider  > eg. Google

Assertion (Account Name and other attributes including a signature)

- An assertion is the message that goes back and forth between the IDP and SP.

Service Provider > website
The SP does not authenticate the user.

Federation Protocols

SAML 1.1 ,  WS-Federation

0Auth2, OpenID Connect, WS-Trust
SAML2

Secure Assertion Markup Language

Shibboleth >
User retrieve resources
SAML Authentication Information
SANL over URL
Authentication Information
Granted based off SAML info

Advantages:

Easier employee onboarding
Simpler end user experience
Better user management

Transitive Trust Model
Transitive Trust Relationship

a trust model defines the relationships between authentication services,

so that they may accept each other's assertions of users' identities
and permissions, when appropriate.

Trust models determine how organizations establish relationships
among authentication services to authorize different users'
and groups' access to various resources.

In a transitive trust relationship,
if resource A trusts resource B, and resource B trusts resource C,
then resource A trusts resource C.
