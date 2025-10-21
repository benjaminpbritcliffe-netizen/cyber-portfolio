# 🔐 Hashing

Hash functions are different from encryption. There is **no key**, and it’s
meant to be impossible (or computationally impractical) to go from the output
back to the input.

A hash function takes some input data of any size and creates a summary or
digest of that data. The output has a fixed size. It’s hard to predict the
output for any given input and vice versa. Good hashing algorithms are fast to
compute yet prohibitively slow to reverse, i.e., to go from the output back to
the input.

Any slight change in the input data — even a single bit — should cause a
significant change in the output.

A **hash collision** occurs when two different inputs give the same output. Hash
functions are designed to avoid collisions as much as possible and to make it
computationally infeasible for an attacker to engineer one intentionally.

However, since the number of possible inputs is practically unlimited and the
number of possible outputs is limited, the **pigeonhole principle** applies.

---

## Numeric Example

If a hash function produces a 4-bit hash value, there are only **16 different
hash values** possible.

The total number of possible values is:

```bash
2^(number_of_bits) = 2^4 = 16
```

The probability of a collision is therefore relatively high.

---

## 🔸 Hashing vs. Encryption

Hashing and encryption are both cryptographic techniques used to protect data,
but they serve different purposes and have distinct characteristics.

- **Hashing** is a one-way process that turns data into a fixed-length hash
  value using a hash function.
- The goal is to **ensure data integrity** and **validate** the original data.
- Hash functions are fast and efficient, producing unique hash values for each
  input.
- Hashing is **irreversible** — you cannot recover the original data from the
  hash value.

Hashing is often used to:

- Store passwords securely.
- Create digital signatures.
- Verify data integrity.

Common hashing algorithms include **MD5**, **SHA-1**, **SHA-3**, and
**SHA-256**.

---

## ⚙️ How Hashing Works

**Input Data:** Any data — a password, document, or file — can be used as input
for a hash function.

**Hash Function:** A mathematical algorithm runs the input through a series of
calculations.

**Fixed-Length Output:** A fixed-size string of characters is produced,
regardless of the original input’s size.

**Unique Hash Value:** The result is a unique digital fingerprint of the data.

---

### Key Characteristics

- **One-Way:** Impossible to reverse the process and recover original data.
- **Deterministic:** The same input always produces the same hash.
- **Collision-Resistant (Ideal):** Extremely hard for two inputs to produce the
  same output.

---

## 🔹 1. Using Command Line

**Windows (PowerShell):**

```powershell
Get-FileHash "C:\path\to\your\file.txt" -Algorithm SHA256
```

**Linux / macOS (Terminal):**

```bash
sha256sum file.txt
```

or

```bash
md5sum file.txt
```

---

## 🔹 2. Using Python

If you prefer scripting:

```python
import hashlib

file_path = "yourfile.txt"

# Choose hash algorithm (e.g., sha256, md5, sha1)
hash_func = hashlib.sha256()

with open(file_path, "rb") as f:
    for chunk in iter(lambda: f.read(4096), b""):
        hash_func.update(chunk)

print("SHA256:", hash_func.hexdigest())
```

Hashing can be used to check that files haven’t been changed. If you put the
same data in, you’ll always get the same data out.

---

## 🔑 HMAC (Keyed-Hash Message Authentication Code)

An **HMAC** is a message authentication code that uses a cryptographic hash
function combined with a secret key to verify data integrity and authenticity.

Steps:

1. The secret key is padded to the block size of the hash function.
2. The padded key is XORed with a constant (usually a block of zeros or ones).
3. The message is hashed using the XORed key.
4. The result is hashed again using the padded key XORed with another constant.
5. The final output is the **HMAC value**, typically a fixed-length string.

---

## 🌈 Rainbow Tables

A **Rainbow Table** is a lookup table mapping hashes to plaintexts, allowing an
attacker to quickly find a password by its hash.

It trades **time for disk space** — faster cracking, but large storage
requirements.

To protect against rainbow tables, add a **salt** to passwords. A salt is a
random, unique value stored in the database alongside the hash. Although a
shared salt could work, duplicate passwords would still generate the same hash
and remain vulnerable.

You cannot “decrypt” password hashes — they’re not encrypted. You must **crack**
them by hashing potential passwords (for example, from `rockyou.txt`),
optionally adding the salt, and comparing to the target hash.

Tools such as **Hashcat** and **John the Ripper** are used for this purpose.

---

### ⚡ Hashcat

It’s best to run Hashcat on your host machine to use your GPU effectively.
Windows users can run it from PowerShell; Linux users can use OpenCL builds.

**John the Ripper** uses CPU by default and works in a VM but performs better on
a host OS to avoid virtualization overhead.

Hashcat syntax:

```plaintext
hashcat -m <hash_type> -a <attack_mode> hashfile wordlist
```

- `-m <hash_type>` specifies the numeric hash type (e.g., `-m 1000` for NTLM).
- `-a <attack_mode>` specifies the mode (`-a 0` = straight wordlist attack).
- `hashfile` is the file containing the hash.
- `wordlist` is the password list to use.

**Example:**

```plaintext
hashcat -m 3200 -a 0 hash.txt /usr/share/wordlists/rockyou.txt
```

This treats the hash as **Bcrypt** and tests passwords from `rockyou.txt`.

If no hash mode is specified, Hashcat will attempt to auto-detect it.

---

## 🧭 Conclusion

Hashing transforms input data into a fixed-size hash value (digest). Any small
change in input results in a completely different output. Hashing is **one-way**
— unlike encryption, you cannot reverse it.

**Encoding**, by contrast, converts data into another format for compatibility
(e.g., ASCII, UTF-8, UTF-16, Base32, Base64). Encoding is reversible, hashing is
not.

---

### 🔠 Base64 Decode Example

```bash
~$ base64 -d ~/Hashing-Basics/Task-8/decode-this.txt
```

---

> 💡 **Tip:** Hashing ensures integrity, not confidentiality. Always combine
> hashing with other security controls when protecting data.
