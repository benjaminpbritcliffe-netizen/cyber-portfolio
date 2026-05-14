# Evilginx

> **Category:** Social Engineering Tools

## 🛠️ Overview

Evilginx is a man-in-the-middle attack framework used for phishing login credentials
along with session cookies, which in turn allows to bypass 2-factor authentication.

This tool is a successor to Evilginx, released in 2017,
which used a custom version of nginx HTTP server to provide man-in-the-middle functionality
to act as a proxy between a browser and phished website.

Present version is fully written in GO as a standalone application,
which implements its own HTTP and DNS server,
making it extremely easy to set up and use.


You receive a convincing phishing email with a link —
often impersonating a Microsoft notification, a shared document,
or a voicemail alert

You click it and land on what looks exactly like the Microsoft login page
— because it's a real-time proxy relay (tools like Evilginx silently forward
everything to the real Microsoft servers)

You type your password — it gets captured and passed through

Microsoft sends your MFA challenge — you complete it —
the attacker's proxy captures the resulting authenticated session cookie

From your perspective, the login may have just redirected you somewhere odd
or failed or even a "legitimate" document  — you think nothing of it

The attacker imports your session cookie into their browser —
they now have full Outlook access with no further MFA challenge

## 🚀 Usage
```bash
# Example command
evilginx --help
```