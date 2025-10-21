# Introduction to EternalBlue — Tutorial Style (Sanitized)

> **Use responsibly.** This tutorial is written for **authorized**, isolated lab
> environments you own and control. Do **not** test against systems you do not
> have explicit written permission to test.

EternalBlue (CVE‑2017‑0144) is a historical SMBv1 remote-code execution
vulnerability patched by Microsoft in March 2017 (MS17‑010). This document is a
**tutorial‑style, lab‑focused** guide intended to teach defensive and
educational testing practices. It preserves the original workflow order while
removing exploit payloads and long interactive dumps.

---

## Objective

- Demonstrate a safe, repeatable lab workflow for assessing an SMB‑related host.
- Verify exposure and patch status without weaponizing exploits in shared
  documentation.
- Explain post‑access escalation concepts and how to document them in a lab
  report (non‑actionable).

---

## Prerequisites (lab setup)

1. A dedicated, isolated lab network (air‑gapped or VLAN) that cannot reach
   production or the Internet except where intentionally allowed.
2. A vulnerable or intentionally configured Windows VM image you own (snapshot
   before changes).
3. Attacker VM with common toolset (nmap, metasploit-framework installed) on the
   same lab network.
4. Logging & telemetry configured on the victim (enable Windows Event Logs,
   Sysmon if available, packet capture on a span/mirror port).
5. Clear test plan and rollback procedure (VM snapshot IDs recorded).

---

## Step 1 — Reconnaissance (safe, repeatable)

Goal: confirm host reachability, open services, and gather benign metadata for
triage.

```bash
# Basic TCP/service scan with vulnerability script set, save output
root@attacker:~# nmap -sV -sC --script vuln -oN blue.nmap 10.10.26.121
```

Notes & checkpoints:

- Confirm TCP/445 is reachable. Reachability ≠ vulnerability.
- Review blue.nmap for SMB service banner and OS hints. Log findings in your
  report.

---

## Step 2 — Safe verification (non‑exploit checks)

Goal: validate whether SMBv1 is enabled and whether the host has MS17‑010
patch-related updates applied.

### From your admin/workstation (PowerShell):

```powershell
# Check SMB server configuration
Get-SmbServerConfiguration | Select EnableSMB1Protocol, EnableSMB2Protocol

# List recent hotfixes to help identify patching timeline
Get-HotFix | Sort-Object InstalledOn | Select InstalledOn, HotFixID, Description
```

### Quick remote reachability test (from attacker VM)

```bash
# Simple TCP connect test (not an exploit)
nc -vz 10.10.26.121 445
```

Notes:

- If SMBv1 is enabled and appropriate patches are missing, the host should be
  prioritized for remediation. Do not attempt public exploit code on shared
  infrastructure.

---

## Step 3 — Controlled module reconnaissance (Metasploit: discovery only)

Goal: show how to use Metasploit modules to _detect_ MS17‑010 exposure without
including exploit output.

```text
# Start msfconsole and search for MS17-010 helper/check modules
root@attacker:~# msfconsole
msf6 > search ms17-010
# Choose the auxiliary scanner (example) and use it as a non‑destructive check
# (Omitting interactive results in this doc — run within isolated lab and record findings locally)
```

Checklist:

- Prefer modules marked "check" or auxiliary scanners for detection.
- Record module name, options used, and the scan results in your lab notebook
  (session ID, timestamp).

---

## Step 4 — (Redacted) Exploitation step placeholder

This tutorial purposefully **does not** include exploit payloads or live exploit
output. If you are performing a controlled exploit in a closed lab for learning:

- Keep all exploit runs isolated to the target VM snapshot.
- Record the exact module, options, payload, and handler settings before
  executing.
- Immediately capture telemetry (process creation, network connections, event
  logs) and revert the snapshot when finished.

(Replace the interactive exploit transcript with your local lab notes — do not
paste full exploit outputs into shared documents.)

---

## Step 5 — Post‑Access: Conceptual escalation & validation (tutorial style)

Goal: teach how to conceptually validate privilege escalation _impacts_ in a lab
without publishing weaponized commands.

1. **Define starting privilege** — document whether your initial access provided
   a low‑privileged user, service account, or system context.
2. **Enumerate defensive artifacts** — capture process listings, running
   services, scheduled tasks, and registry autorun keys as forensic evidence
   (from the victim). Example telemetry to collect (only):
   - System event log exports
   - Sysmon process creation logs
   - Process list snapshots and parent relationships
   - File and registry ACL snapshots for critical paths
3. **Document possible escalation vectors observed** — e.g., writable service
   paths, exposed credentials in configs, or outdated local drivers. Describe
   them at a high level (do not include step‑by‑step instructions).
4. **Assess impact** — articulate what SYSTEM/Admin access would enable in this
   environment (persistence, credential theft, lateral movement).

**Important:** In your lab report, do not include stepwise, reproducible
exploitation of escalation vectors if the report will be shared outside an
authorized audience.

---

## Step 6 — Lab exercises (safe tasks for students)

Provide these non‑actionable exercises to learn the escalation detection
process:

- Exercise A: **Patch verification** — confirm whether the target host has the
  MS17‑010 fixes (identify KBs or build numbers). Produce a remediation
  checklist.
- Exercise B: **Telemetry correlation** — run a benign service restart and
  observe how Sysmon / Windows Event logs record the event to learn where
  escalation artifacts appear.
- Exercise C: **ACL audit** — list and record file/registry ACLs for common
  autorun paths (document anomalies). Do not modify ACLs in shared environments.

Each exercise should be accompanied by:

- Objective, preconditions, expected observations, and rollback instructions.

---

## Step 7 — Forensic artifacts & detection guidance

When teaching detection, highlight these indicators (non‑procedural):

- Creation/modification of services or scheduled tasks around the time of
  compromise.
- New or unusual parent/child process relationships.
- Evidence of credential access attempts (e.g., LSASS memory access patterns in
  EDR logs).
- Registry Run key modifications and unexpected DLL loads from writable
  locations.

Telemetry sources to practice with in the lab: Windows Event Logs, Sysmon
(ProcessCreate, ImageLoad), EDR traces, and network packet captures. Correlate
timestamps to build a timeline.

---

## Step 8 — Reporting template (tutorial output)

For each step in your lab exercise include a short, reproducible entry in your
report:

- **Title**: e.g., "MS17‑010 reconnaissance — 2025‑10‑20"
- **Objective**: short description
- **Commands/tools used**: list (no exploit payloads)
- **Findings**: concise results & timestamps
- **Telemetry captured**: logs collected and storage path
- **Impact assessment**: high‑level explanation
- **Remediation**: recommended actions and verification method

---

## Step 9 — Cleanup & rollback

- Revert the target VM to pre‑exercise snapshot.
- Securely delete any handlers or temporary tooling on attacker VM.
- Archive telemetry and sanitized notes in a secured repository for instructor
  review.

---

## Appendix — Quick defensive commands (for verification only)

```powershell
# Check SMB v1 status and recent hotfixes (run on the host)
Get-SmbServerConfiguration | Select EnableSMB1Protocol, EnableSMB2Protocol
Get-HotFix | Sort-Object InstalledOn | Select InstalledOn, HotFixID
```

```bash
# Quick reachability test (from attacker/research VM)
nc -vz 10.10.26.121 445
```

---

## Ethics & responsible disclosure reminder

If you discover a real vulnerability outside your lab, collect minimal evidence,
stop exploration, and follow responsible disclosure channels for the affected
vendor or system owner.

---

## Notes

- This tutorial‑style document replaces raw exploit output with structured steps
  and safe exercises suitable for classroom or lab notebooks.
- If you want, I can convert each lab _exercise_ into a printable worksheet with
  checkboxes and rubric guidance for assessment.
