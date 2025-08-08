# 🔍 Nmap

## Description
Nmap (Network Mapper) is an open-source tool for network discovery and security auditing.

## Basic Usage
```bash
nmap -sC -s -oN scan.txt 10.10.10.5
```

## Common Flags
- `-sS`: TCP SYN scan
- `-sC`: Run default scripts
- `-sV`: Version detection
- `-oN`: Output to normal text file

## Use Case
- Host discovery
- Port scanning
- Service enumeration
