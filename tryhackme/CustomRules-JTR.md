# Custom Rules

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

[List.Rules:THMRules] is used to define the name of your rule; this is what you will use to call your custom rule a John argument.

We then use a regex style pattern match to define where the word will be modified; again, we will only cover the primary and most common modifiers here:

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

Who could have guessed it, another conversion tool? Well, that’s what working with John is all about. As the name suggests, ssh2john converts the id_rsa private key, which is used to log in to the SSH session, into a hash format that John can work with. Jokes aside, it’s another beautiful example of John’s versatility. The syntax is about what you’d expect. Note that if you don’t have ssh2john installed, you can use ssh2john.py, located in the /opt/john/ssh2john.py. If you’re doing this on the AttackBox, replace the ssh2john command with python3 /opt/john/ssh2john.py or on Kali, python /usr/share/john/ssh2john.py.

ssh2john [id_rsa private key file] > [output file]

ssh2john: Invokes the ssh2john tool
[id_rsa private key file]: The path to the id_rsa file you wish to get the hash of
>: This is the output director. We’re using it to redirect the output from this command to another file.
[output file]: This is the file that will store the output from
Example Usage

/opt/john/ssh2john.py id_rsa > id_rsa_hash.txt

Cracking
For the final time, we’re feeding the file we output from ssh2john, which in our example use case is called id_rsa_hash.txt and, as we did with rar2john, we can use this seamlessly with John:

john --wordlist=/usr/share/wordlists/rockyou.txt id_rsa_hash.txt