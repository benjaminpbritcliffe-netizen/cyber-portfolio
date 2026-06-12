# PKI

Public Key Infrastructure

Public key infrastructure (PKI) provides a suite of tools designed to support public and private key management, integrity checks via digital signatures, and authentication

PKI provides the mechanisms required to confidently identify the owners of public keys. It issues digital certificates guaranteed by a trusted certificate authority (CA). Trusted CAs are pre-established by recording their information within operating system certificate stores or browsers and by using special hardware storage components. Digital certificates are foundational to HTTPS traffic.

## SSL

Secure Sockets Layer (SSL) inspection is the process of inspecting encrypted HTTPS traffic. Without SSL inspection, network administrators can't monitor encrypted traffic for threats, making HTTPS traffic an easy method for attackers to avoid detection. SSL inspection is also essential for verifying that website certificates are valid, helping protect against on-path attacks (where an attacker intercepts communications between two parties) and detecting traffic encrypted with anything other than a trusted third-party certificate.