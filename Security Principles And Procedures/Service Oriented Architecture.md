# SOA

## Service Oriented Architecture

SOA comprises multiple modules

Enterprise Service Bus

Each module is self contained

Promotes Code Reusability

SOA is mostly used in enterprise applications.
This design style combines multiple self-contained services that communicate
with each other over the network to provide the application functionality.

SOA services:

Are independent of each other.
Are easier to maintain than interdependent services.
Can be reused in many applications.
Reduce development costs.

Micro Services

- Specific business needs, HTTP or Thrift API

- Fault tolerance and Scalability as each micro service is independed.
icroservices are a type of SOA, but the services are more granular. Microservices:

Function independent of each other. If one service fails,
the application can keep working.

Scales easily because each service is independent.
Allow large complex applications to be quickly deployed.

## SAML

Security Assertion Markup Language

SAML is an XML-based open standard
that identity providers use to pass authorization credentials to service providers.
This means that one set of credentials can be used to login to multiple websites.

## OpenID

OpenID is a method of authenticating users with certain sites that participate in an OpenID system.

This enables them to retain a single account for all participating sites.
Large companies, such as Google and Amazon, use their own OpenID systems.
OpenID Direct adds a layer of authentication to OAuth 2.0, the latest version of the protocol.

OpenID uses the following process:

A user will register with an OpenID system in a given domain like they would with any other account.
A site under this OpenID domain will then give the user the option to sign in using this system.
The site contacts its external OpenID provider in order to verify that the login credentials supplied by the user are correct.

## SOAP

SOAP is an XML-based messaging protocol used for exchanging data over the internet
between applications that run on different platforms
and are written in different programming languages.

It is built to be extensible, protocol neutral, and independent of any programming model.

SOAP can be used for:

XML messaging
Data transport between web services
Remote procedure calls
Message broadcast
Document transport
A SOAP message contains three parts:

An envelope that defines the structure
A set of encoding rules
A convention for representing calls/responses

## SSO Example

Sign In with Single Sign-on
With single sign-on, the process is much easier.
The website does not have to check its database for user credentials.
It relies on a third party, such as Google or Facebook, for authentication.
With single sign-on, the process is as follows:

The user enters credentials on the home page.

The website checks to see if the logon is SSO.

If so, the website sends the credentials to an authentication server.

The authentication server verifies the credentials.

If the credentials match the authentication server database, the user is granted access.

Authentication data is passed to the web pages.

If the credentials don't match the database, the user is denied access.

## MFA

Multi-factor authentication uses two or more factors of authentication,
such as a password plus a security code sent to a phone number on file.
It can even include authentication attributes such as gait analysis and geo-location to improve its rigor.
MFA provides an extra layer of security to an account.
It is especially useful when using a single sign-on account to make sure it has not been compromised.
For example, a password can be written down, guessed, or shared, or a smart card could be lost or stolen.
When using MFA, abusing authentication becomes far more complex.
When the requirement for a password is combined with a token-generated PIN or to be combined with a fingerprint scan,
abusing authentication becomes many, many factors more complicated.
With MFA in place, a username and password can be breached but are unusable without the additional factor.
