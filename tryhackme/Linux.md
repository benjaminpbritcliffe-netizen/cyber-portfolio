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

the /root folder is actually the home for the "root" system user. There isn't anything more to this folder other than just understanding that this is the home directory for the "root" user.


/tmp

This is a unique root directory found on a Linux install. Short for "temporary", the /tmp directory is volatile and is used to store data that is only needed to be accessed once or twice. Similar to the memory on your computer, once the computer is restarted, the contents of this folder are cleared out.

 log files from running services and applications are written here (/var/log)


 ## Text Editors

 Nano

It is easy to get started with Nano! To create or edit a file using nano, we simply use nano filename -- replacing "filename" with the name of the file you wish to edit.

### Introducing Nano

Once we press enter to execute the command, nano will launch

You can use these features of nano by pressing the "Ctrl" key (which is represented as an ^ on Linux)  and a corresponding letter. For example, to exit, we would want to press "Ctrl" and "X" to exit Nano.


### Introducing VIM

You can use these features of nano by pressing the "Ctrl" key (which is represented as an ^ on Linux)  and a corresponding letter. For example, to exit, we would want to press "Ctrl" and "X" to exit Nano.



## Downloading Files

You can use these features of nano by pressing the "Ctrl" key (which is represented as an ^ on Linux)  and a corresponding letter. For example, to exit, we would want to press "Ctrl" and "X" to exit Nano.


## SCP

Secure copy, or SCP, is just that -- a means of securely copying files. Unlike the regular cp command, this command allows you to transfer files between two computers using the SSH protocol to provide both authentication and encryption.

Working on a model of SOURCE and DESTINATION, SCP allows you to:

- Copy files & directories from your current system to a remote system
- Copy files & directories from a remote system to your current system

scp important.txt ubuntu@192.168.1.30:/home/ubuntu/transferred.txt  

With this information, let's craft our scp command (remembering that the format of SCP is just SOURCE and DESTINATION)

And now let's reverse this and layout the syntax for using scp to copy a file from a remote computer that we're not logged into 

ubuntu@192.168.1.30:/home/ubuntu/documents.txt notes.txt 


## Serving Files

Ubuntu machines come pre-packaged with python3. Python helpfully provides a lightweight and easy-to-use module called "HTTPServer". This module turns your computer into a quick and easy web server that you can use to serve your own files, where they can then be downloaded by another computing using commands such as curl and wget. 

Python3's "HTTPServer" will serve the files in the directory where you run the command, but this can be changed by providing options that can be found within the manual pages. Simply, all we need to do is run python3 -m  http.server in the terminal to start the module!


## WGet

 use wget to download the file using the 10.10.42.35 address and the name of the file. Remember, because the python3 server is running port 8000.

 Note, you will need to open a new terminal to use wget and leave the one that you have started the Python3 web server in. This is because, once you start the Python3 web server, it will run in that terminal until you cancel it.

 ## Processes

 Processes are the programs that are running on your machine. They are managed by the kernel, where each process will have an ID associated with it, also known as its PID.

 To see the processes run by other users and those that don't run from a session (i.e. system processes), we need to provide aux to the ps command like so: ps aux

 You can send signals that terminate processes; there are a variety of types of signals that correlate to exactly how "cleanly" the process is dealt with by the kernel. To kill a command, we can use the appropriately named kill command and the associated PID that we wish to kill. i.e., to kill PID 1337, we'd use kill 1337.

 SIGTERM - Kill the process, but allow it to do some cleanup tasks beforehand
SIGKILL - Kill the process - doesn't do any cleanup after the fact
SIGSTOP - Stop/suspend a process


The Operating System (OS) uses namespaces to ultimately split up the resources available on the computer to (such as CPU, RAM and priority) processes. 

We previously talked about how PID works, and this is where it comes into play. The process with an ID of 0 is a process that is started when the system boots. This process is the system's init on Ubuntu, such as systemd, which is used to provide a way of managing a user's processes and sits in between the operating system and the user. 

Enter the use of systemctl -- this command allows us to interact with the systemd process/daemon. Continuing on with our example, systemctl is an easy to use command that takes the following formatting: systemctl [option] [service]

For example, to tell apache to start up, we'll use systemctl start apache2

We can do four options with systemctl:

Start
Stop
Enable
Disable


With our process backgrounded using either Ctrl + Z or the & operator, we can use fg to bring this back to focus like below, where we can see the fg command is being used to bring the background process back into use on the terminal, where the output of the script is now returned to us.



## Cron 

Users may want to schedule a certain action or task to take place after the system has booted. Take, for example, running commands, backing up files, or launching your favourite programs on, such as Spotify or Google Chrome.

We're going to be talking about the cron process, but more specifically, how we can interact with it via the use of crontabs . Crontab is one of the processes that is started during boot, which is responsible for facilitating and managing cron jobs.

 Crontabs require 6 specific values:

Value	Description
MIN	What minute to execute at
HOUR	What hour to execute at
DOM	What day of the month to execute at
MON	What month of the year to execute at
DOW	What day of the week to execute at
CMD	The actual command that will be executed.

0 */12 * * * cp -R /home/cmnatic/Documents /var/backups/

An interesting feature of crontabs is that these also support the wildcard or asterisk (*). If we do not wish to provide a value for that specific field, i.e. we don't care what month, day, or year it is executed -- only that it is executed every 12 hours, we simply just place an asterisk.


Crontabs can be edited by using crontab -e, where you can select an editor (such as Nano) to edit your crontab.

## Repositories

Whilst Operating System vendors will maintain their own repositories, you can also add community repositories to your list! This allows you to extend the capabilities of your OS. Additional repositories can be added by using the add-apt-repositorycommand or by listing another provider! For example, some vendors will have a repository that is closer to their geographical location.

