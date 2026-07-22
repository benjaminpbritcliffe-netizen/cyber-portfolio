# SSO

Status: Done

[SSO](../House%20Of%20Vokabel/SSO.md)

## Single Sign-On

With single sign-on, the website does not check its own database for user credentials.
Instead, it relies on a trusted third party — such as Google or Facebook — for authentication.

This simplifies the login experience and centralises credential management.

## SSO Process

1. The user enters credentials on the home page.
2. The website checks to see if the logon is SSO.
3. If so, the website sends the credentials to an authentication server.
4. The authentication server verifies the credentials.
5. If the credentials match the authentication server database,
the user is granted access and authentication data is passed to the web pages.
6. If the credentials do not match, the user is denied access.

## Related

- [[SAML]] — a common protocol used to implement SSO.
- [[OpenID]] — another SSO standard, commonly used with OAuth 2.0.
- [[MFA]] — often layered on top of SSO to strengthen security.
