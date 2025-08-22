# 📱 Apktool

## Description

Apktool is used for reverse engineering Android apps.

## Installation

Download the Linux wrapper script. (Right click, Save Link As apktool) Download
the latest version of Apktool. Rename the downloaded jar to apktool.jar. Move
both apktool.jar and apktool to /usr/local/bin. (root needed) Make sure both
files are executable. (chmod +x) Try running apktool via CLI.

## Basic Usage

```bash
apktool d app.apk
```

```bash
root@kali:~# apktool -h
Apktool v2.7.0-dirty - a tool for reengineering Android apk files
with smali v2.5.2.git2771eae-debian and baksmali v2.5.2.git2771eae-debian
Copyright 2010 Ryszard Wi?niewski <brut.alll@gmail.com>
Copyright 2010 Connor Tumbleson <connor.tumbleson@gmail.com>

usage: apktool
 -advance,--advanced   prints advance information.
 -version,--version    prints the version then exits
usage: apktool if|install-framework [options] <framework.apk>
 -p,--frame-path <dir>   Stores framework files into <dir>.
 -t,--tag <tag>          Tag frameworks using <tag>.
usage: apktool d[ecode] [options] <file_apk>
 -f,--force              Force delete destination directory.
 -o,--output <dir>       The name of folder that gets written. Default is apk.out
 -p,--frame-path <dir>   Uses framework files located in <dir>.
 -r,--no-res             Do not decode resources.
 -s,--no-src             Do not decode sources.
 -t,--frame-tag <tag>    Uses framework files tagged by <tag>.
usage: apktool b[uild] [options] <app_path>
 -f,--force-all          Skip changes detection and build all files.
 -o,--output <dir>       The name of apk that gets written. Default is dist/name.apk
 -p,--frame-path <dir>   Uses framework files located in <dir>.

For additional info, see: https://ibotpeaches.github.io/Apktool/
For smali/baksmali info, see: https://github.com/JesusFreke/smali
```

## Use Case

- Decompile APKs
- Inspect app structure
