# Hashing

Hash functions are different from encryption. There is no key, and it’s meant to be impossible (or computationally impractical) to go from the output back to the input.

A hash function takes some input data of any size and creates a summary or digest of that data. The output has a fixed size. It’s hard to predict the output for any input and vice versa. Good hashing algorithms will be relatively fast to compute and prohibitively slow to reverse, i.e., go from the output and determine the input. Any slight change in the input data, even a single bit, should cause a significant change in the output.

A hash collision is when two different inputs give the same output. Hash functions are designed to avoid collisions as best as possible. Furthermore, hash functions are designed to prevent an attacker from being able to create, i.e., engineer, a collision intentionally. However, because the number of inputs is practically unlimited and the number of possible outputs is limited, this leads to a pigeonhole effect.

As a numeric example, if a hash function produces a 4-bit hash value, we only have 16 different hash values. The total number of possible hash values is 2number_of_bits = 24 = 16. The probability of a collision is relatively very high.


Hashing vs. encryption
Hashing and encryption are both cryptographic techniques used to protect data,
but they serve different purposes and have distinct characteristics.

Hashing is a one-way process that turns data into a fixed-length hash value using a hash function.
The primary goal of hashing is to ensure data integrity and validate the original data.
Hash functions are intended to be fast and efficient, generating unique hash values for each input.
Hashing is irreversible, which means it's computationally impractical to recover the original data from the hash value.
Hashing is often used to store passwords, create digital signatures and verify data integrity.
Hashing algorithms include MD5, SHA-3 and SHA-256.