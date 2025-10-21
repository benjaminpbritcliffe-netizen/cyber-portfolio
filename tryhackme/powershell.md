# PowerShell

PowerShell is a powerful command-line shell and scripting language that combines
task automation and configuration management. The following notes outline
essential cmdlets and techniques useful for system administration, security
analysis, and general discovery.

---

## Discovering Commands

- **Get-Command** lists all available cmdlets, functions, aliases, and scripts
  that can be executed in the current session. It is essential for discovering
  what commands are available to you.

- **Get-Help** provides detailed information about cmdlets, including usage,
  parameters, and examples. If you are unsure about a command, start here.

---

## File System and Navigation

- **Get-ChildItem** (similar to `dir` or `ls`) lists files and directories for a
  specified path. If no `-Path` is provided the current directory is used.

- **Set-Location** (alias `cd`) changes the current directory to the specified
  path. Use it to navigate the file system.

- **Get-Content** (similar to `type` or `cat`) reads and displays the contents
  of a file.

- **Copy-Item** and **Move-Item** copy and move files or directories,
  respectively. They are equivalent to `copy` and `move` in Command Prompt.

---

## Piping and Composition

Piping (`|`) allows the output of one command to be used as the input to
another, creating a sequence of operations where data flows from one cmdlet to
the next. Piping is fundamental to PowerShell workflows and data processing.

Example:

```powershell
Get-Process | Where-Object { $_.CPU -gt 100 } | Sort-Object -Property CPU
```

---

## System and Hardware Information

- **Get-ComputerInfo** retrieves comprehensive system information, including OS
  details, hardware specs, BIOS information, and more. It provides a broad
  snapshot of the system configuration. Its traditional counterpart,
  `systeminfo`, returns a smaller subset of similar details.

- **Get-LocalUser** lists local user accounts on the machine.

- **Get-FileHash** generates file hashes (e.g., SHA256) and is useful in
  incident response and malware analysis to verify file integrity.

---

## Networking and IP Information

- **Get-NetIPConfiguration** provides detailed information about network
  interfaces, IP addresses, DNS servers, and gateway settings.

- **Get-NetIPAddress** shows IP address details for all configured interfaces,
  including inactive addresses.

- **Get-NetTCPConnection** lists active TCP connections and includes the
  **OwningProcess** property, which indicates the PID of the process that owns a
  given connection. This helps map network connections to processes.

---

## Processes and Services

- **Get-Process** shows currently running processes, including CPU and memory
  usage. It is powerful for monitoring and troubleshooting resource issues.

- **Get-Service** retrieves information about services and their status
  (running, stopped, paused).

---

## Remote Execution

**Invoke-Command** executes commands on remote computers and is fundamental for
remote administration, automation, and incident response. It can also be used by
penetration testers (or attackers) to execute commands remotely.

**Example:** To run `Get-Service` on a remote machine named RoyalFortune (no
credentials required in this example), use:

```powershell
Invoke-Command -ComputerName RoyalFortune -ScriptBlock { Get-Service }
```

> **Security note:** Remote execution should be used responsibly. When running
> commands across multiple systems, ensure you have authorization, use secure
> channels, and audit activity.

---

## Practical Tips

- Use `Get-Help <cmdlet> -Full` to see detailed examples and parameter
  descriptions.
- Combine `Get-Command` and `Get-Help` when exploring unfamiliar environments.
- Use piping to filter and transform results rather than exporting raw output.
- Prefer `Get-FileHash` over manual checksum utilities when scripting integrity
  checks across Windows systems.
- When investigating network connections, cross-reference `Get-NetTCPConnection`
  with `Get-Process` using the **OwningProcess** PID to find the associated
  executable.

---

## Exercise Ideas

1. List all active services on a remote host and save the result to a file.
2. Capture a list of processes that have used more than 10% CPU in the last
   minute and sort them by memory usage.
3. Generate a SHA256 hash for a suspicious file and compare it to a known
   indicator of compromise (IOC) list.

---

> ✅ **Next steps:** Try these cmdlets in a lab environment. Keep practising
> piping and remote execution to build efficient workflows for administration
> and security tasks.
