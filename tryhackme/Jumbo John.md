
# Jumbo John

Even though the algorithm is not feasibly reversible,
that doesn’t mean cracking the hashes is impossible.
If you have the hashed version of a password, for example,
and you know the hashing algorithm,
you can use that hashing algorithm to hash a large number of words,
called a dictionary.
You can then compare these hashes to the one you’re trying to crack,
to see if they match.
If they do, you know what word corresponds to that hash- you’ve cracked it!

This process is called a dictionary attack,
and John the Ripper, or John as it’s commonly shortened,
is a tool for conducting fast brute force attacks on various hash types.

- The “Jumbo John” version of John the Ripper
- The RockYou password list.
- <https://hashes.com/en/tools/hash_identifier> hash identifier online
- <https://gitlab.com/kalilinux/packages/hash-identifier/-/tree/kali/master>
hash identifier github

<https://github.com/danielmiessler/SecLists> Rockyou Github

``` plaintext
john [options] [file path]

john: Invokes the John the Ripper program
[options]: Specifies the options you want to use
[file path]: The file containing the hash you’re trying to crack; if it’s in the same directory, you won’t need to name a path, just the file.

john --wordlist=[path to wordlist] [path to file]

--wordlist=: Specifies using wordlist mode, reading from the file that you supply in the provided path
[path to wordlist]: The path to the wordlist you’re using, as described in the previous task
Example Usage:

john --wordlist=/usr/share/wordlists/rockyou.txt hash_to_crack.txt

john --format=[format] --wordlist=[path to wordlist] [path to file]

--format=: This is the flag to tell John that you’re giving it a hash of a specific format and to use the following format to crack it
[format]: The format that the hash is in
Example Usage:

john --format=raw-md5 --wordlist=/usr/share/wordlists/rockyou.txt hash_to_crack.txt


## NTLM Format

john --format=nt --wordlist=/usr/share/wordlists/rockyou.txt hash_to_crack.txt

```

# Unshadow


John can be very particular about the formats it needs data in to be able to work with it; for this reason, to crack /etc/shadow passwords, you must combine it with the /etc/passwd

unshadow local_passwd local_shadow > unshadowed.txt

john --wordlist=/usr/share/wordlists/rockyou.txt --format=sha512crypt unshadowed.txt

# Single Crack

John also has another mode, called the Single Crack mode. In this mode, John uses only the information provided in the username to try and work out possible passwords heuristically by slightly changing the letters and numbers contained within the username.

```plaintext
nano > username:hash

 john --single --format=raw-md5 hash07.txt
 ```