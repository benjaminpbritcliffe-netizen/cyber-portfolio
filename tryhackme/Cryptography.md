# Cryptography

## Different Types Of Cryptography

### PCI DSS

When handling credit cards, the company must enforce the Payment Card Industry
Data Security Standard (PCI DSS).

ensures a minimum level of security to:

- Store
- Process
- transmit data related to card credits.

If you check the PCI DSS for Large Organizations, you will learn that the data
should be encrypted both while:

- being stored (at rest)
- while being transmitted (in motion).

Plaintext is the original, readable message or data before it’s encrypted. It
can be a document, an image, a multimedia file, or any other binary data.

Ciphertext is the scrambled, unreadable version of the message after encryption.
Ideally, we cannot get any information about the original plaintext except its
approximate size.

Cipher is an algorithm or method to convert plaintext into ciphertext and back
again. A cipher is usually developed by a mathematician.

Key is a string of bits the cipher uses to encrypt or decrypt data. In general,
the used cipher is public knowledge; however, the key must remain secret unless
it is the public key in asymmetric encryption. We will visit asymmetric
encryption in a later task.

Encryption is the process of converting plaintext into ciphertext using a cipher
and a key. Unlike the key, the choice of the cipher is disclosed.

Decryption is the reverse process of encryption, converting ciphertext back into
plaintext using a cipher and a key. Although the cipher would be public
knowledge, recovering the plaintext without knowledge of the key should be
impossible (infeasible).

## Caesar Cipher

One of the simplest historical ciphers is the Caesar Cipher.

The idea is simple: shift each letter by a certain number to encrypt the
message.

Consider the following example:

Plaintext: TRYHACKME Key: 3 (Assume it is a right shift of 3.) Cipher: Caesar
Cipher

We can easily figure out that T becomes W, R becomes U, Y becomes B, and so on.
As you noticed, once we reach Z, we start all over, as shown in the figure
below. Consequently, we get the ciphertext of WUBKDFNPH.

Ciphertext: WUBKDFNPH Key: 3 Cipher: Caesar Cipher

For encryption, we shift to the right by three; for decryption, we shift to the
left by three and recover the original plaintext, as illustrated in the image
above.

- recovering the original text would be a trivial task.
- there are only 25 possible keys. But it could be from 1 to 25.

## Symmetric Encryption

Also known as symmetric cryptography, uses the same key to encrypt and decrypt
the data.

Examples of symmetric encryption are DES (Data Encryption Standard), 3DES
(Triple DES) and AES (Advanced Encryption Standard).

DES was adopted as a standard in 1977 and uses a 56-bit key. With the
advancement in computing power, in 1999, a DES key was successfully broken in
less than 24 hours, motivating the shift to 3DES.

3DES is DES applied three times; consequently, the key size is 168 bits, though
the effective security is 112 bits. 3DES was more of an ad-hoc solution when DES
was no longer considered secure. 3DES was deprecated in 2019 and should be
replaced by AES; however, it may still be found in some legacy systems.

AES was adopted as a standard in 2001. Its key size can be 128, 192, or 256
bits.

## Asymmetric Encryption

Unlike symmetric encryption, which uses the same key for encryption and decryption,
Asymmetric encryption uses a pair of keys, one to encrypt and the other to decrypt.

asymmetric encryption encrypts the data using the public key;
hence, it is also called public key cryptography.

## XOR Cryptography

The XOR operator is extremely common as a component in more complex ciphers.
By itself, using a constant repeating key,
a simple XOR cipher can trivially be broken using frequency analysis.

XOR (exclusive OR) is a logical operation applied bit by bit.

The rule is simple:

0 ⊕ 0 = 0

0 ⊕ 1 = 1

1 ⊕ 0 = 1

1 ⊕ 1 = 0

So, XOR outputs 1 only when the two bits differ.

### Why XOR is Important in Cryptography

Reversibility

XOR is its own inverse:

If C = P ⊕ K (ciphertext = plaintext XOR key),
then P = C ⊕ K (plaintext = ciphertext XOR key).

This property makes encryption/decryption with XOR extremely efficient.

Randomness Mixing

If you XOR data with something unpredictable (like a random key/stream),
the result looks random.

Example: One-Time Pad (OTP) encryption -
works entirely by XORing plaintext with a truly random key.

Lightweight & Fast

XOR is cheap to compute (just a single machine instruction).

This makes it suitable for use in block ciphers, stream ciphers, and hashing.

Suppose we want to encrypt the 8-bit message P = 10110101 using key K = 11001010:

``` text

Phrase - 10110101
Key -    11001010
--------------

   C: 01111111   (ciphertext)

To decrypt:

C: 01111111
K: 11001010
--------------

P: 10110101   (original plaintext)

```

### Where XOR Appears in Cryptography

One-Time Pad → Perfect secrecy when key is truly random and used only once.

Stream Ciphers (e.g., RC4, Salsa20) → Keystream XORed with plaintext.

Block Ciphers (e.g., AES) → Use XOR in key mixing steps.

Hash functions → XOR is used in combining intermediate values.

XOR alone is not secure unless the key is truly random.
Cryptographic algorithms generate pseudo-random keystreams to XOR with the data.

<https://www.tutorialspoint.com/cryptography/cryptography_xor_encryption.htm> Tutorial

``` python

import os

def xor_encrypt_decrypt(data: bytes, key: bytes) -> bytes:
    """Encrypt or decrypt data using XOR with the given key."""
    return bytes([d ^ key[i % len(key)] for i, d in enumerate(data)])

# --- Example usage ---
if __name__ == "__main__":
    # Generate a random key (16 bytes = 128 bits)
    key = os.urandom(16)
    print("Key (hex):", key.hex())

    # Message to encrypt
    message = "Hello! XOR Crypto demo.".encode()
    print("Plaintext:", message.decode())

    # Encrypt
    ciphertext = xor_encrypt_decrypt(message, key)
    print("Ciphertext (hex):", ciphertext.hex())

    # Decrypt (same function!)
    decrypted = xor_encrypt_decrypt(ciphertext, key)
    print("Decrypted:", decrypted.decode())

```
