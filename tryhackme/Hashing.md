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

Hashing can be used to check that files haven’t been changed. If you put the same data in, you always get the same data out

HMAC (Keyed-Hash Message Authentication Code) is a type of message authentication code (MAC) that uses a cryptographic hash function in combination with a secret key to verify the authenticity and integrity of data.


The secret key is padded to the block size of the hash function.
The padded key is XORed with a constant (usually a block of zeros or ones).
The message is hashed using the hash function with the XORed key.
The result from Step 3 is then hashed again with the same hash function but using the padded key XORed with another constant.
The final output is the HMAC value, typically a fixed-size string.

## Rainbow Tables#

A Rainbow Table is a lookup table of hashes to plaintexts, so you can quickly find out what password a user had just from the hash. A rainbow table trades the time to crack a hash for hard disk space, but it takes time to create. Here’s a quick example to get an idea of what a rainbow table looks like.

To protect against rainbow tables, we add a salt to the passwords. The salt is a randomly generated value stored in the database and should be unique to each user. In theory, you could use the same salt for all users, but duplicate passwords would still have the same hash and a rainbow table could still be created for passwords with that salt.


You can’t “decrypt” password hashes. They’re not encrypted. You have to crack the hashes by hashing many different inputs (such as rockyou.txt as it covers many possible passwords), potentially adding the salt if there is one and comparing it to the target hash. Once it matches, you know what the password was. Tools like Hashcat and John the Ripper are commonly used for these purposes.


If you want to run Hashcat, it’s best to run it on your host to make the most of your GPU, if available. If you prefer MS Windows, you are in luck; MS Windows builds are available on the website, and you can run it from PowerShell. You can get Hashcat working with OpenCL in a VM, but the speeds will likely be worse than cracking on your host.

John the Ripper uses CPU by default and works in a VM out of the box, although you may get better speeds running it on the host OS to avoid any virtualisation overhead and make the most of your CPU cores and threads.



Hashcat uses the following basic syntax: hashcat -m <hash_type> -a <attack_mode> hashfile wordlist, where:

-m <hash_type> specifies the hash-type in numeric format. For example, -m 1000 is for NTLM. Check the official documentation (man hashcat) and example page to find the hash type code to use.
-a <attack_mode> specifies the attack-mode. For example, -a 0 is for straight, i.e., trying one password from the wordlist after the other.
hashfile is the file containing the hash you want to crack.
wordlist is the security word list you want to use in your attack.
For example, hashcat -m 3200 -a 0 hash.txt /usr/share/wordlists/rockyou.txt will treat the hash as Bcrypt and try the passwords in the rockyou.txt file.

### Hashcat

For example,

``` plaintext
hashcat -m 3200 -a 0 hash.txt /usr/share/wordlists/rockyou.txt 
```

will treat the hash as Bcrypt and try the passwords in the rockyou.txt file.

not placing a hash mode, hashcat will search for the nearest one(s) to match the value.


### Conclusion

Hashing, as already stated, is a process that takes input data and produces a hash value, a fixed-size string of characters, also referred to as digest. This hash value uniquely represents the data, and any change in the data, no matter how small, should lead to a change in the hash value. Hashing should not be confused with encryption or encoding; hashing is one-way, and you can’t reverse the process to get the original data.

Encoding converts data from one form to another to make it compatible with a specific system. ASCII, UTF-8, UTF-16, UTF-32, ISO-8859-1, and Windows-1252 are valid encoding methods for the English language. Note that UTF-8, UTF-16, and UTF-32 are Unicode encodings, and they can represent characters from other languages, such as Arabic and Japanese.

Another type of encoding commonly used when sending or saving data is not for any specific language. Examples include Base32 and Base64 encoding. Consider the following example of using base64 to encode and decode.

### Base64 Decode

``` plaintext
~$ base64 -d  ~/Hashing-Basics/Task-8/decode-this.txt
```
