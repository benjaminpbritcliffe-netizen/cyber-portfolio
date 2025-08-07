# TryHackMe - Blue

**Date:** August 7, 2025

## Nmap Scan
```
nmap -sC -sV -oN scan.txt 10.10.10.5
```

## Notes
- Open ports: 22, 445
- Exploit: EternalBlue (MS17-010)