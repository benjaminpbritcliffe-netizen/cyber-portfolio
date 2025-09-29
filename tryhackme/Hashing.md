# Hashing

Hash functions are different from encryption.
There is no key, and it’s meant to be impossible (or computationally impractical)
to go from the output back to the input.

A hash function takes some input data of any size
and creates a summary or digest of that data.
The output has a fixed size.
It’s hard to predict the output for any input and vice versa.
Good hashing algorithms will be relatively fast to compute
and prohibitively slow to reverse, i.e.,
go from the output and determine the input.
Any slight change in the input data, even a single bit,
should cause a significant change in the output.

A hash collision is when two different inputs give the same output.
Hash functions are designed to avoid collisions as best as possible.
Hash functions are designed to prevent an attacker from being able to create,
i.e., engineer, a collision intentionally.
However, because the number of inputs is practically unlimited
and the number of possible outputs is limited, this leads to a pigeonhole effect.

As a numeric example,
if a hash function produces a 4-bit hash value,
we only have 16 different hash values.
The total number of possible hash values is 2number_of_bits = 24 = 16.
The probability of a collision is relatively very high.

Hashing vs. encryption
Hashing and encryption are both cryptographic techniques used to protect data,
but they serve different purposes and have distinct characteristics.

Hashing is a one-way process that turns data into a fixed-length hash value,
using a hash function.

The primary goal of hashing is to ensure data integrity
and validate the original data.

Hash functions are intended to be fast and efficient,
generating unique hash values for each input.

Hashing is irreversible,
it's computationally impractical to recover the original data from the hash value.

Hashing is often used to store passwords,
create digital signatures and verify data integrity.
Hashing algorithms include MD5, SHA-3 and SHA-256.

## How Hashing Works

Input Data:
Any data, like a password, document, or file, is used as input for the hash function.

Hash Function:
A complex mathematical algorithm runs the input data through a series of calculations.

Fixed-Length Output:
A fixed-size string of characters, regardless of the original data's size.

Unique Hash Value:
A unique digital "fingerprint" of the input data.

Key Characteristics

One-Way: It is computationally infeasible to reverse the process
and obtain the original data from the hash value.

Deterministic: The same input data will always produce the same hash value.

Collision-Resistant (Ideal): It is extremely difficult for two different inputs,
to produce the same hash value (hash collision).

🔹 1. Using Command Line

Windows (PowerShell):

``` powershell
Get-FileHash "C:\path\to\your\file.txt" -Algorithm SHA256
```

Linux / macOS (Terminal):

``` powershell
sha256sum file.txt
```

or

``` powershell
md5sum file.txt
```

🔹 2. Using Python

If you prefer scripting:

``` python
import hashlib

file_path = "yourfile.txt"

# Choose hash algorithm (e.g., sha256, md5, sha1)
hash_func = hashlib.sha256()

with open(file_path, "rb") as f:
    for chunk in iter(lambda: f.read(4096), b""):
        hash_func.update(chunk)

print("SHA256:", hash_func.hexdigest())
```
