---
description: Make your AWUS 1900 Alpha card work in Kali
---

# Kali Linux - Alpha card AWUS 1900 (VirtualBox)

## Configuration

My setup is VirtualBox Version 6.1.20 r143896 (Qt5.6.3) with Kali linux 5.10.0-kali7-amd64 (2021-04-12)

## Kali - Update

Update your Kali

```aspnet
apt update
apt upgrade
apt dist-upgrade
```

Install additional packages for later compilation

```aspnet
apt install linux-headers-$(uname -r)
apt install build-essential
apt install bc
apt install dkms
apt install debhelper dpkg-dev
```

## VirtualBox

Make sure that your virtualized Kali has installed Guest Additions and your VirtualBox installation has an extesion pack.

* [Guest Additions](https://www.virtualbox.org/manual/ch04.html) which comes with your VirtualBox in form of insertable CD-ROM  Image (VM menu Devices->Insert Guest Additions). Install and reboot.
* [Extension Pack which improves USB functionality](https://www.virtualbox.org/wiki/Downloads).\
  You need to install the same extension pack version as your VirtualBox version.&#x20;

### USBv2 Ports - VM Setting

My testing VM configuration has the following port options (VM -> Settings > Ports).

![](https://1354665097-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MYLPTPmXutfLTHzDEhx%2F-MZJocZSrvGyL3kYoi8C%2F-MZJpo7JqgYVX1JcviHx%2Fimage.png?alt=media\&token=020f8e5e-c087-4222-968c-ebec069bdfc4)

## Kali - Install Driver (realtek-rtl88xxau-dkms)

Install a Realtek driver for your Alpha card AWUS 1900 using package manager so the driver already exists as a package in your Kali distro.

```aspnet
apt install realtek-rtl88xxau-dkms
```

However, this driver did not work for me. Kali sees the wifi card hardware (lsusb), but no wireless card is detected (iwconfig). This means that driver compilation did not succeed or a driver is wrong for my hardware.

```aspnet
lsusb
Bus 001 Device 002: ID 0bda:8813 Realtek Semiconductor Corp. RTL8814AU 802.11a/b/g/n/ac Wireless Adapter

# shows nothing
iwconfig -a (nothing)
```

## Remove the driver&#x20;

Remove the driver installed via the package manager&#x20;

```aspnet
apt remove realtek-rtl88xxau-dkms
```

## Manual Driver Compilation (RTL8814AU)

Let's try a manual driver compilation with a specific driver we have found using lsusb command. \
Follow Debian Linux installation path in this article.

{% embed url="https://miloserdov.org/?p=5493" %}

### Compile

```bash
apt install git build-essential libelf-dev linux-headers-`uname -r` debhelper dpkg-dev dkms bc
git clone https://github.com/aircrack-ng/rtl8814au
cd rtl8814au

make dkms_install

# test
dkms status
8814au, 5.8.5.1, 5.10.0-kali7-amd64, x86_64: installed
realtek-rtl88xxau, 5.6.4.2~git20210327.c0ce817, 5.10.0-kali7-amd64, x86_64: installed
rtl8814au, 4.3.21: added
```

### Load Driver

```bash
modprobe 8814au           
                                                                             
┌──(root💀kali)-[~]
└─# iwconfig

lo        no wireless extensions.

eth0      no wireless extensions.

wlan0     IEEE 802.11  ESSID:off/any  
          Mode:Managed  Access Point: Not-Associated   Tx-Power=20 dBm   
          Retry short limit:7   RTS thr:off   Fragment thr:off
          Encryption key:off
          Power Management:off
```
