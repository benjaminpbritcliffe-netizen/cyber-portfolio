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
