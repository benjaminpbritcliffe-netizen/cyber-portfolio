# IDORS

Insecure Direct Object References (IDORs)

Understand the concept of authentication and authorization Learn how to spot
potential opportunities for Insecure Direct Object References (IDORs) Exploit
IDOR to perform horizontal privilege escalation Learn how to turn IDOR into SDOR
(Secure Direct Object Reference)

Understand the concept of authentication and authorization Learn how to spot
potential opportunities for Insecure Direct Object References (IDORs) Exploit
IDOR to perform horizontal privilege escalation Learn how to turn IDOR into SDOR
(Secure Direct Object Reference)

Authentication: The process by which you verify who you are. For example,
supplying your username and password. Authorization: The process by which the
web application verifies your permissions. For example, are you allowed to visit
the admin page of a web application, or are you allowed to make a payment using
a specific account?

Authorization cannot happen before authentication. If the application doesn't
know who you are, it cannot verify what permissions your user has. This is very
important to remember. If your IDOR doesn't require you to authenticate (login
or provide session information), such as in our package tracking example, we
will have to fix authentication first before we can fix the authorization issue
of making sure that users can only get information about packages they own.

The last bit of theory to cover is privilege escalation types:

Vertical privilege escalation: This refers to privilege escalation where you
gain access to more features. For example, you may be a normal user on the
application, but can perform actions that should be restricted for an
administrator.

Horizontal privilege escalation: This refers to privilege escalation where you
use a feature you are authorized to use, but gain access to data that you are
not allowed to access. For example, you should only be able to see your
accounts, not someone else's accounts.
