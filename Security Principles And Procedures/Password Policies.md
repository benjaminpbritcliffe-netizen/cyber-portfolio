# Password Policies

Password policies are found in Local Security Policy.

policies are going to define the parameters
that users will have to stay within to create accounts.

## The Minimum Password Length Policy

Notice that it's set to zero by default,
this means we could make a password that's one character long.

Right now, the industry standard is at least eight characters. Longer is better,
assuming you can remember it.

## The Password Must Meet Complexity Requirements Policy

Disabled by default.

passwords have to meet the following minimum requirements.

It can't  contain the user's account name,
or parts of the user's full name that exceed two consecutive
characters.

It has to be at least six characters long, and it has to contain characters from
 three of the following four categories.

Uppercase characters,
A through Z.
Lowercase characters,  A through Z.
Numbers 0 through 9.

And non-alphabetical characters like:
exclamation mark,
dollar sign,
pound sign,
percentage,
and so on.

note that when we turn this policy on,
it's not actually going to be enforced on existing
passwords. It'll only be enforced the next time the user changes their password.

## The maximum password age

This parameter specifies how long a user can the same password for.
Microsoft still recommends frequent changes. Recommended of 30 Days.

## Enforced password history

This is how many passwords windows will remember,
to avoid a user from using the same password or previous passwords again.
Recommended to be set to 5.

## The Minimum password age policy

determines the period of time (in days),
that a password must be used before the user can change it.

if you configure the Enforce password history policy setting
to ensure that users can't reuse any of their last x passwords,

but you don't configure the Minimum password age policy
setting to a number that is greater than 0,
users could change their password x + 1 times in a few minutes,
and reuse their original password.
