# CIA Triad

Status: Done

[CIA Triad](../../House%20of%20Vokabel%2017b3d034d9f780f28d12fa401ae23c58/CIA%20Triad%2017b3d034d9f780c782f9f781573a24dd.md)

- Confidentiality

**Confidentiality** means keeping data secret; that is, only authorized people
can access or disclose the data.

Source Code, Customer Records (Think, Doctors Treatment Notes of a specific
patient.)

Ensuring the data is only available to the people who requires access.

- Controls for Confidentiality
  - Encryption, were only someone with the decryption key can understand
  - Access Controls, designed to ensure only people with the correct credentials
    can access. Can either be Passwords on files, biometrics such as
    fingerprints or retinal scans. Can be both for data and physical access.
  - Patch Management , ensuring software is up to date to fix potential security
    weak points that attackers could hit.

- Integrity

**Integrity** means ensuring that data is trustworthy and accurate by protecting
it from unauthorized modification and destruction.

💡

Data Trustworthiness and Accuracy. Think of purchasing something for £10 but
getting billed £100. Consider that although the cause of the error might be
technical, it might be human, too. Maybe someone entered the wrong payment
amount. Unauthorized modifications, deliberate or not, can lead to significant
financial losses or legal repercussions.

📢

To preserve integrity, you must also prevent unauthorized people from editing
the data. In this sense, integrity and confidentiality overlap.

🗣

Ensuring the data that is given is both accurate and trustworthy.

- Controls for Integrity
  - Checksums generating a unique value for a data set, when the data changes
    the checksum will also change, alerting of a change of data.
  - Access controls and user permissions, can limit who can change the data
    (only someone with the correct permissions/knowledge can change the data.
  - Data Backups, help restore the data if changes occur intentionally or
    unintentionally. The data can be reverted back to the original data set.
  - Audit Trails, can track and record changes that have been made. By who or
    what it was changed “from” and “to”.

- Availability

**Availability** means ensuring timely and reliable access to and use of the
data.

💡

Think of your Bank Account, you expect the data to be available immediately.

📢

Availability does not mean available all the time, it means ensuring the data is
available in a timely fashion.

🗣

Ensuring the data is available to the person who has requested it (or not) when
required.

- Controls for availability
  - Redundant Systems and data backup procedures, help protect against data loss
    and system failure. Having multiple servers or data in multiple locations to
    eliminate downtime.
  - Antimalware software and firewalls, protect systems from attacks that can
    disrupt services (DOS and DDOS attacks.)
  - Disaster Recovery and Business Continuity Plans, have steps in place to
    restore services quickly and efficiently in case disruption occurs. Minimise
    downtime. Understand what to do quickly and efficiently to minimise the
    downtime for other users and/or customers.
