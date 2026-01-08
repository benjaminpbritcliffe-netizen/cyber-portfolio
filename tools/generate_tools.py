import os

# Your raw tool list
tool_data = """
Vulnerability Analysis
OpenVAS – Advanced open-source vulnerability scanner
Nessus – Popular vulnerability assessment tool
Nikto – Web server vulnerability scanner
Lynis – System auditing tool
Skipfish – Web security scanner

Web Application Analysis
Burp Suite – Comprehensive web security testing tool
OWASP ZAP – Open-source web application scanner
Sqlmap – Automated SQL injection tool
Wfuzz – Web application brute-forcing tool
XSStrike – Advanced XSS detection tool
Commix – Command injection tool
Dirb – Web content scanner

Database Assessment
Sqlmap – Automated SQL injection and database takeover tool
NoSQLMap – NoSQL injection testing tool
BBQSQL – Blind SQL injection framework

Password Attacks
John the Ripper – Fast password cracker
Hashcat – Advanced password recovery tool
Hydra – Network login cracker
Medusa – Parallel brute-forcing tool
Crunch – Wordlist generator
CeWL – Custom wordlist generator

Wireless Attacks
Aircrack-ng – Wireless network security testing tool
Reaver – WPS attack tool
Fern WiFi Cracker – GUI-based wireless security tool
Wifite – Automated wireless attack tool
Kismet – Wireless network detector and sniffer

Reverse Engineering
Ghidra – NSA’s reverse engineering tool
Radare2 – Open-source reverse engineering framework
IDA Free – Interactive disassembler and debugger
OllyDbg – Assembly-level debugger

Exploitation Tools
Metasploit Framework – Powerful penetration testing framework
Exploit-db – Public repository of exploits
Armitage – GUI for Metasploit
SearchSploit – CLI for Exploit-db

Sniffing & Spoofing
Wireshark – Network packet analyzer
Ettercap – Man-in-the-middle attack tool
Tcpdump – Command-line packet sniffer
Macchanger – MAC address changer
Bettercap – Advanced network attack tool

Post Exploitation
Empire – Post-exploitation framework
Meterpreter – Advanced payload in Metasploit
Powersploit – PowerShell-based post-exploitation tools
BeEF – Browser exploitation framework

Forensics
Autopsy – GUI-based digital forensics tool
Volatility – Memory forensics framework
Binwalk – Firmware analysis tool
Bulk Extractor – Extracts useful data from disk images

Reporting Tools
MagicTree – Penetration testing reporting tool
Dradis – Collaboration and report generation tool
Faraday – Centralized security analysis tool

Social Engineering Tools
SET – Social-Engineer Toolkit
Evilginx – Phishing framework
BeEF – Browser exploitation tool
Phishing Frenzy – Email phishing campaign framework
"""

def clean_filename(name):
    """Formats the tool name for a safe filename."""
    return name.strip().replace(" ", "-").replace("/", "-").lower()

def run_automation():
    lines = [line.strip() for line in tool_data.split('\n') if line.strip()]
    current_category = "General"

    for line in lines:
        # Check if it's a category header (no dash)
        if " – " not in line:
            current_category = line
            category_path = clean_filename(current_category)
            if not os.path.exists(category_path):
                os.makedirs(category_path)
            continue

        # It's a tool line: Extract everything BEFORE the dash
        tool_name = line.split(" – ")[0].strip()

        # Define file path and content
        file_name = f"{clean_filename(tool_name)}.md"
        category_folder = clean_filename(current_category)
        full_path = os.path.join(category_folder, file_name)

        markdown_content = f"# {tool_name}\n\n" \
                           f"> **Category:** {current_category}\n\n" \
                           f"## 🛠️ Overview\nDetails about {tool_name} go here.\n\n" \
                           f"## 🚀 Usage\n```bash\n# Example command\n{tool_name.lower()} --help\n```"

        with open(full_path, "w", encoding="utf-8") as f:
            f.write(markdown_content)

    print(f"✅ Successfully created documentation folders and files!")

if __name__ == "__main__":
    run_automation()