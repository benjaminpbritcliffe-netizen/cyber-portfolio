# 📡 Aircrack-ng

## Description
Aircrack-ng is a suite of tools for auditing wireless networks.

## Basic Usage

Aircrack-ng can be used for Wi-Fi security testing after it has been installed.  These are a few typical commands:

Check Wireless Network Interfaces:

```bash
airmon-ng
```
The network interfaces that are available are listed by this command.

Enable Monitor Mode:

```bash
airmon-ng start wlan0
```

The network adapter enters monitor mode as a result.

Capture Packets:

```bash
airodump-ng wlan0mon
```

This command gathers packets from neighboring Wi-Fi networks.

Crack WEP/WPA Passwords:

```bash
aircrack-ng -a 2 -b [TARGET_BSSID] -w [WORDLIST] [CAPTURE_FILE]
```

This command uses a wordlist to try and crack the Wi-Fi password.

## Use Case
- Capturing WPA handshakes
- Cracking Wi-Fi passwords

