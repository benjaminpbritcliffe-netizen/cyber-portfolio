# Rainbow Tables

1. Numeric
Characters: 0123456789

Use Case: Only passwords consisting entirely of numbers (like a PIN).

Why it fails: It lacks the uppercase, lowercase, and special characters required by your policy.

2. Alpha-numeric
Characters: a-z, A-Z, and 0-9.

Use Case: Basic passwords that don't allow symbols.

Why it fails: Your policy specifically mandates symbols like !, @, and _.

3. Loweralpha-numeric / Mixalpha
Loweralpha-numeric: a-z and 0-9.

Mixalpha: Usually refers to a-z and A-Z.

Why they fail: Neither of these includes the symbols or the combination of both cases and numbers required for a robust policy.

4. ascii-32-95 (The Correct Choice)
This refers to a specific range on the ASCII table. In computing, every character has a decimal number assigned to it.

Range 32–95: This starts at the Space (32) and ends at the Underscore (95).

What's inside: It includes all numbers, all uppercase letters (A-Z), and crucial symbols like !, ", #, $, %, &, ', *, and @.

Why it works: It is the only set that covers every single "special character" requirement listed in your policy.

5. alpha-numeric-symbol32-space
Characters: This is a custom string often used in specific software,
but it is less standardized than the "ascii-32-95" nomenclature used in tools like Rtgen (Rainbow Table Generator).

Why it's secondary: While descriptive,
"ascii-32-95" is the precise technical term for the range that defines the symbols you need.

## Steps

At the prompt, type cat /usr/share/rainbowcrack/charset.txt

Press Enter.

Create and sort an md5 and sha1 rainbow crack table.
At the prompt, type rtgen md5 ascii-32-95 1 20 0 1000 1000 0 and press Enter to create a md5 rainbow crack table.

Type rtgen sha1 ascii-32-95 1 20 0 1000 1000 0 and press Enter to create a sha1 rainbow crack table.

Type rtsort . and press Enter to sort the rainbow table.

Type rcrack . -l /root/captured_hashes.txt and press Enter to crack the password contained in a hash file.
