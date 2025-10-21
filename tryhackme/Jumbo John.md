
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

## Unshadow

John can be very particular about the formats it needs data in.
for this reason, to crack /etc/shadow passwords, you must combine it with the /etc/passwd

unshadow local_passwd local_shadow > unshadowed.txt

john --wordlist=/usr/share/wordlists/rockyou.txt --format=sha512crypt unshadowed.txt

## Single Crack

John also has another mode, called the Single Crack mode. In this mode,
John uses only the information provided in the username to work out passwords heuristically,
by slightly changing the letters and numbers contained within the username.

```plaintext
nano > username:hash

 john --single --format=raw-md5 hash07.txt
 ```

## Custom Rules

Custom rules are defined in the john.conf file. This file can be found in
/opt/john/john.conf on the TryHackMe Attackbox. It is usually located in
/etc/john/john.conf if you have installed John using a package manager or built
from source with make.

[List.Rules:THMRules] is used to define the name of your rule; this is what you
will use to call your custom rule a John argument.

We then use a regex style pattern match to define where the word will be
modified; again, we will only cover the primary and most common modifiers here:

Az: Takes the word and appends it with the characters you define A0: Takes the
word and prepends it with the characters you define c: Capitalises the character
positionally These can be used in combination to define where and what in the
word you want to modify.

Lastly, we must define what characters should be appended, prepended or
otherwise included. We do this by adding character sets in square brackets [ ]
where they should be used. These follow the modifier patterns inside double
quotes " ". Here are some common examples:

[0-9]: Will include numbers 0-9 [0]: Will include only the number 0 [A-z]: Will
include both upper and lowercase [A-Z]: Will include only uppercase letters
[a-z]: Will include only lowercase letters Please note that:

[a]: Will include only a [!£$%@]: Will include the symbols !, £, $, %, and @
Putting this all together, to generate a wordlist from the rules that would
match the example password Polopassword1! (assuming the word polopassword was in
our wordlist), we would create a rule entry that looks like this:

[List.Rules:PoloPassword]

cAz"[0-9] [!£$%@]"

Utilises the following:

c: Capitalises the first letter Az: Appends to the end of the word [0-9]: A
number in the range 0-9 [!£$%@]: The password is followed by one of these
symbols Using Custom Rules We could then call this custom rule a John argument
using the --rule=PoloPassword flag.

As a full command: john --wordlist=[path to wordlist] --rule=PoloPassword [path
to file]

Q:What do custom rules allow us to exploit?

A: Password complexity predictability

Q:What rule would we use to add all capital letters to the end of the word?

A: Az”[A-Z]”

Q:What flag would we use to call a custom rule called “THMRules”

A: — rule=THMRules

The first line:

[List.Rules:THMRules] is used to define the name of your rule;
this is what you will use to call your custom rule a John argument.

We then use a regex style pattern match to define where the word will be modified;
again, we will only cover the primary and most common modifiers here:

``` plaintext
Az: Takes the word and appends it with the characters you define
A0: Takes the word and prepends it with the characters you define
c: Capitalises the character positionally
These can be used in combination to define where and what in the word you want to modify.

Lastly, we must define what characters should be appended, prepended or otherwise included. We do this by adding character sets in square brackets [ ] where they should be used. These follow the modifier patterns inside double quotes " ". Here are some common examples:

[0-9]: Will include numbers 0-9
[0]: Will include only the number 0
[A-z]: Will include both upper and lowercase
[A-Z]: Will include only uppercase letters
[a-z]: Will include only lowercase letters
Please note that:

[a]: Will include only a
[!£$%@]: Will include the symbols !, £, $, %, and @
Putting this all together, to generate a wordlist from the rules that would match the example password Polopassword1! (assuming the word polopassword was in our wordlist), we would create a rule entry that looks like this:

[List.Rules:PoloPassword]

cAz"[0-9] [!£$%@]"

Utilises the following:

c: Capitalises the first letter
Az: Appends to the end of the word
[0-9]: A number in the range 0-9
[!£$%@]: The password is followed by one of these symbols
```

## ZIP Files Passwords

``` plaintext
zip2john [options] [zip file] > [output file]

[options]: Allows you to pass specific checksum options to zip2john; this shouldn’t often be necessary
[zip file]: The path to the Zip file you wish to get the hash of
>: This redirects the output from this command to another file
[output file]: This is the file that will store the output

zip2john zipfile.zip > zip_hash.txt

john --wordlist=/usr/share/wordlists/rockyou.txt zip_hash.txt
```

## RAR Files

rar2john [rar file] > [output file]

rar2john: Invokes the rar2john tool
[rar file]: The path to the RAR file you wish to get the hash of
>: This redirects the output of this command to another file
[output file]: This is the file that will store the output from the command

/opt/john/rar2john rarfile.rar > rar_hash.txt

john --wordlist=/usr/share/wordlists/rockyou.txt rar_hash.txt

## SSH Files

ssh2john converts the id_rsa private key,
which is used to log in to the SSH session,
iIf you don’t have ssh2john installed, you can use ssh2john.py, located in the /opt/john/ssh2john.py.
If you’re doing this on the AttackBox,
replace the ssh2john command with python3 /opt/john/ssh2john.py
or on Kali, python /usr/share/john/ssh2john.py.

ssh2john [id_rsa private key file] > [output file]

``` plaintext
ssh2john: Invokes the ssh2john tool
[id_rsa private key file]: The path to the id_rsa file you wish to get the hash of
>: This is the output director. We’re using it to redirect the output from this command to another file.
[output file]: This is the file that will store the output from
Example Usage

/opt/john/ssh2john.py id_rsa > id_rsa_hash.txt

Cracking

For the final time, we’re feeding the file we output from ssh2john,

john --wordlist=/usr/share/wordlists/rockyou.txt id_rsa_hash.txt

```
