# Linux

We need to be able to do basic functions like navigating to files, outputting
their contents, and making files! The commands to do so are self-explanatory
(once you know what they are, of course...).

Let's get started with two of the first commands, which I have broken down in
the table below:

| Command | Description                                      |
| ------- | ------------------------------------------------ |
| echo    | Output any text that we provide                  |
| whoami  | Find out what user we're currently logged in as! |

If we wanted to output the text `TryHackMe`, what would our command be?

```bash
echo TryHackMe
```

---

## Interacting With the Filesystem

As I previously stated, being able to navigate the machine that you are logged
into without relying on a desktop environment is pretty important. After all,
what's the point of logging in if we can't go anywhere?

| Command | Full Name               |
| ------- | ----------------------- |
| ls      | listing                 |
| cd      | change directory        |
| cat     | concatenate             |
| pwd     | print working directory |

Now, of course, directories can contain even more directories within themselves.
It becomes a headache when we're having to look through every single one just to
try and look for specific files. We can use `find` to do just this for us!

Another great utility to learn about is the use of `grep`. The `grep` command
allows us to search the contents of files for specific values that we are
looking for.

For example, if we want to see everything that the IP address `81.143.211.90`
has visited in a web server's access log (note that this is fictional), we can
use `grep` to search for it.

```bash
grep "81.143.211.90" access.log
```

---

## Useful Operators

| Operator | Description                                                                                    |
| -------- | ---------------------------------------------------------------------------------------------- |
| `&`      | Run commands in the background of your terminal.                                               |
| `&&`     | Combine multiple commands together in one line of your terminal.                               |
| `>`      | Redirect output from a command (such as using `cat` to output a file) and direct it elsewhere. |
| `>>`     | Same as `>`, but appends the output rather than replacing (nothing is overwritten).            |

---

If I wanted to replace the contents of a file named `passwords` with the word
`password123`, what would my command be?

```bash
echo password123 > passwords
```

Now, if I wanted to add `tryhackme` to this file named `passwords` but also keep
`password123`, what would my command be?

```bash
echo tryhackme >> passwords
```

Using SSH to Login to Your Linux Machine

The syntax to use SSH is very simple. We only need to provide two things:

1. The IP address of the remote machine

2. Correct credentials to a valid account to login with on the remote machine

For this room, we will be logging in as "tryhackme", whose password is
"tryhackme" without the quotation ("") marks. Let's use the IP address of the
machine displayed in the card at the top of the room as the IP address and this
user, to construct a command to log in to the remote machine using SSH. The
command to do so is ssh and then the username of the account, @ the IP address
of the machine.

A majority of commands allow for arguments to be provided. T These arguments are
identified by a hyphen and a certain keyword - known as flags or switches.

When using a command, unless otherwise specified, it will perform its default
behaviour. For example, ls lists the contents of the working directory. However,
hidden files are not shown. We can use flags and switches to extend the
behaviour of commands.

However, after using the -a argument (short for --all), we now suddenly have an
output with a few more files and folders such as ".hiddenfolder". Files and
folders with "." are hidden files.

We covered some of the most fundamental commands when interacting with the
filesystem on the Linux machine. For example, we covered how to list and find
the contents of folders using ls and find and navigating the filesystem using
cd.

More specifically, the following commands:

Command Full Name Purpose touch touch Create file mkdir make directory Create a
folder cp copy Copy a file or folder mv move Move a file or folder rm remove
Remove a file or folder file file Determine the type of a file

Creating files and folders on Linux is a simple process. First, we'll cover
creating a file. The touch command takes exactly one argument -- the name we
want to give the file we create. For example, we can create the file "note" by
using touch note. It's worth noting that touch simply creates a blank file. You
would need to use commands like echo or text editors such as nano to add content
to the blank file.

Creating files and folders on Linux is a simple process. First, we'll cover
creating a file. The touch command takes exactly one argument -- the name we
want to give the file we create. For example, we can create the file "note" by
using touch note. It's worth noting that touch simply creates a blank file. You
would need to use commands like echo or text editors such as nano to add content
to the blank file.

Creating files and folders on Linux is a simple process. First, we'll cover
creating a file. The touch command takes exactly one argument -- the name we
want to give the file we create. For example, we can create the file "note" by
using touch note. It's worth noting that touch simply creates a blank file. You
would need to use commands like echo or text editors such as nano to add content
to the blank file.

Creating files and folders on Linux is a simple process. First, we'll cover
creating a file. The touch command takes exactly one argument -- the name we
want to give the file we create. For example, we can create the file "note" by
using touch note. It's worth noting that touch simply creates a blank file. You
would need to use commands like echo or text editors such as nano to add content
to the blank file.

Moving a file takes two arguments, just like the cp command. However, rather
than copying and/or creating a new file, mv will merge or modify the second file
that we provide as an argument. Not only can you use mv to move a file to a new
folder, but you can also use mv to rename a file or folder.

So far, the files we have used in our examples haven't had an extension. Without
knowing the context of why the file is there -- we don't really know its
purpose. Enter the file command. This command takes one argument. For example,
we'll use file to confirm whether or not the "note" file in our examples is
indeed a text file, like so file note.

Switching between users on a Linux install is easy work thanks to the su
command. Unless you are the root user (or using root permissions through sudo),
then you are required to know two things to facilitate this transition of user
accounts:

- The user we wish to switch to
- The user's password

/etc

This root directory is one of the most important root directories on your
system. The etc folder (short for etcetera) is a commonplace location to store
system files that are used by your operating system. .

/var

The "/var" directory, with "var" being short for variable data, is one of the
main root folders found on a Linux install. This folder stores data that is
frequently accessed or written by services or applications running on the
system.
