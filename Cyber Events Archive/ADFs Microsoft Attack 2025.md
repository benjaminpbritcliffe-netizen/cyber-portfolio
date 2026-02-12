# 🚨 Tutorial: How Attackers Abuse Office.com and ADFS for Phishing

This tutorial explains how attackers combine **malvertising, Microsoft
tenants, and Active Directory Federation Services (ADFS)** to deliver
convincing Microsoft 365 phishing pages.

------------------------------------------------------------------------

## 1. Initial Setup by the Attacker

Attackers prepare their infrastructure in several steps:

1. **Register a malicious domain**\
    Example:

        bluegraintours[.]com

    This will later act as a redirector and fake identity provider.

2. **Set up a Microsoft tenant**

    - Attackers create their own **Microsoft 365 tenant**.\
    - They configure **Active Directory Federation Services (ADFS)**
        to control authentication flows.

3. **Deploy a phishing kit**

    - A standard **Microsoft 365 login clone** is hosted on attacker
        infrastructure.\
    - The phishing site is configured to harvest usernames, passwords,
        and MFA codes.

------------------------------------------------------------------------

## 2. Luring the Victim (Malvertising)

Instead of phishing emails, attackers use **Google Ads poisoning**:

1. Register a fake ad for a mistyped query:

        "Office 265 login"

2. When the target clicks the ad, they are sent to
    **outlook.office.com** with crafted redirect parameters.

✅ This gives the illusion of safety since the user *sees Microsoft's
trusted domain first*.

------------------------------------------------------------------------

## 3. Redirect Chain

Here's the redirect path the victim experiences:

1. **Google Ad → outlook.office.com**\
    The initial link points to Microsoft infrastructure.

2. **outlook.office.com → bluegraintours\[.\]com**\
    The attacker's tenant ADFS configuration tricks Office into
    redirecting the user to their malicious domain.

    - At this stage, it still appears legitimate to the browser and
        some security tools.

3. **bluegraintours\[.\]com → phishing page**

    - The victim silently lands on the phishing site.\
    - Attackers apply **conditional rules**:
        - If the request is from a real target → show phishing login.\
        - If it's a scanner/researcher → bounce back to office.com.

------------------------------------------------------------------------

## 4. Exploiting ADFS

The trick lies in how **ADFS handles authorization requests**:

- ADFS is a **Single Sign-On (SSO)** service.\
- The attacker's malicious domain is configured to **act as an
    Identity Provider (IdP)**.\
- When redirected, Office.com **trusts** the flow because the tenant's
    ADFS setup is valid.

➡️ This lets the attacker insert their phishing page into what looks
like a legitimate Microsoft login session.

------------------------------------------------------------------------

## 5. Credential Theft

On the phishing page:

1. The victim enters their Microsoft 365 username + password.\
2. If MFA is prompted, the phishing kit proxies the MFA flow (stealing
    session tokens).\
3. Credentials are exfiltrated to the attacker.

------------------------------------------------------------------------

## 6. Covering Tracks

To stay hidden:

- **Bluegraintours\[.\]com** is filled with fake blog content so
    scanners see a harmless site.\
- Conditional access ensures **only intended victims see the phishing
    kit**.\
- Non-targets are redirected back to *real office.com*.

------------------------------------------------------------------------

## 🛡️ Defender's Checklist

Here's how to detect and block this attack:

- **Monitor for unusual ADFS redirects**
  - Legitimate tenants shouldn't redirect to unknown domains.
- **Inspect ad-based redirects**
  - Log ad click traffic and look for redirects into Office.com with
        suspicious parameters.
- **Block Google malvertising at endpoints**
  - Enforce policies against clicking ads for login portals.
- **Phishing-resistant MFA**
  - Enforce **FIDO2 keys** or **Windows Hello** --- cannot be
        proxied.
- **Educate users**
  - Teach staff to always type *office.com* directly instead of
        clicking ads.

------------------------------------------------------------------------

## 🗂️ MITRE ATT&CK Mapping

- **Initial Access** → \[T1566.002 Phishing via Search Engine Ads\]\
- **Credential Access** → \[T1556.002 Adversary-in-the-Middle: ADFS
    Abuse\]\
- **Defense Evasion** → \[T1070 Indicator Removal\] via conditional
    redirects\
- **Exfiltration** → \[T1041 Exfiltration Over C2 Channel\]

------------------------------------------------------------------------

✅ Now you've got a **step-by-step defender's playbook** on how the
attack works and what to look for.
