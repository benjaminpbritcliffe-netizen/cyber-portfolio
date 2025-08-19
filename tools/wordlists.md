# 📂 Wordlists for Penetration Testing & Kali Linux

Wordlists are used for brute-forcing, password cracking, and directory enumeration.  
Here’s where to find them and how to use them effectively.

---

## 1. 🗂 Pre-installed in Kali Linux

### Location:**

```bash
/usr/share/wordlists/
```

### Common Lists

- `rockyou.txt` – famous password cracking list (zipped by default)

  ```bash
  gzip -d /usr/share/wordlists/rockyou.txt.gz
  ```

- `dirb` lists – for directory brute-forcing  
  Path: `/usr/share/wordlists/dirb/`
- `seclists` – massive collection of lists *(if installed)*  
  Path: `/usr/share/seclists/`

---

### 2. 🌐 SecLists (Hacker’s Goldmine)

GitHub: [https://github.com/danielmiessler/SecLists](https://github.com/danielmiessler/SecLists)

#### Contains

- Password lists
- Username lists
- Web fuzzing lists
- Sensitive files & API key lists

Install on Kali:

```bash
sudo apt install seclists
```

Path:

```bash
/usr/share/seclists/
```

---

## 3. 📦 Other GitHub Repositories

- **Assetnote Wordlists** – [https://github.com/assetnote/wordlists](https://github.com/assetnote/wordlists)
- **PayloadAllTheThings** – [https://github.com/swisskyrepo/PayloadsAllTheThings](https://github.com/swisskyrepo/PayloadsAllTheThings)

---

## 4. ☁️ Online Collections

- **CrackStation** – [https://crackstation.net](https://crackstation.net)
- **Weakpass** – [https://weakpass.com/wordlist](https://weakpass.com/wordlist)
- **SecLists Mirror** – [https://seclists.org/](https://seclists.org/)

---

## 5. 🛠 Make Your Own Wordlists

### CeWL – Crawl a website for keywords

```bash
cewl http://target.com -w wordlist.txt
```

### Crunch – Create custom patterns

```bash
crunch 8 8 abcdef1234 -o wordlist.txt
```

---

## ✅ Pro Tips

- Use `rockyou.txt` for Hydra, John, and Hashcat.
- For directory brute-forcing (Gobuster, Dirb), try SecLists’ `common.txt` and `big.txt`.
- Tailor lists to your target’s environment for better success.
