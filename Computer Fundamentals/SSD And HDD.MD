# SSD and HDD

Created: 15 July 2025 13:19
Is Completed: No

## 📚 **Chapter 7 Summary: Storage Technologies and Data Access**

### 🔑 Key Concepts & Terms

| Term | Definition (in your own words) |
| --- | --- |
| **Storage Hierarchy** | The layered structure of memory, from fastest/smallest (registers, cache) to slowest/largest (HDDs, cloud). |
| **Latency** | The delay between a request and its response. SSDs have much lower latency than magnetic disks. |
| **Throughput** | The amount of data transferred per unit time. Crucial for big data workloads. |
| **Block Device** | Storage device (like a hard disk) that reads/writes data in blocks. |
| **Fragmentation** | When data is scattered across the disk, reducing read performance. |
| **Wear Levelling** | Technique in SSDs that spreads writes evenly to extend lifespan. |
| **TRIM Command** | SSD command that clears deleted data blocks to prevent slowdowns. |
| **RAID** | Redundant Array of Independent Disks – combines multiple drives for redundancy and performance. |
| **NAS vs. SAN** | Network-Attached Storage (file-level access) vs. Storage Area Network (block-level access). |

---

## 🚀 From Tapes to SSDs: The Evolution of Storage

### 🧱 1. **Magnetic Tapes and Disks**

- Used **sequential access**: you had to read in order.
- **Cheap, durable**, and still used for archival backups.
- **Slow seek times** and mechanical failures were common.

### ⚙️ 2. **Hard Disk Drives (HDDs)**

- Introduced **random access**.
- Faster than tapes, but mechanical parts (platters, arms) make them **prone to wear**.
- Still good for large, low-cost storage.

### ⚡ 3. **Solid State Drives (SSDs)**

- Use flash memory, no moving parts → **faster** and more **reliable**.
- Handle **random reads/writes** efficiently.
- Require **wear leveling** and **TRIM** to manage memory health and performance.

### 🧠 4. **Impact on System Design**

- Faster boot times and application loads.
- OS file systems adapted to optimize for SSDs.
- Enabled new computing models (e.g. ultra-thin laptops, real-time analytics).

---

## 💡 Key Takeaways: Modern Storage Considerations

### 🏁 1. **Access Speed**

- SSDs outperform HDDs in speed and reliability.
- NVMe SSDs (connected via PCIe) are even faster.

### 🧰 2. **Reliability and Wear**

- SSDs have limited write cycles → require wear leveling.
- HDDs suffer from head crashes and magnetic degradation over time.

### 🧹 3. **Fragmentation**

- Major issue for HDDs (slows read times).
- Less critical for SSDs but still relevant to file system design.

### ☁️ 4. **Remote Storage / Cloud**

- Adds **network latency** but provides **scalability** and **redundancy**.
- Good for backups and distributed applications, but may not suit real-time workloads.

---

## 🎯 Choosing Storage for High-Performance Environments

When selecting a data storage solution for performance-critical applications,
**prioritize these factors**:

| Priority | Why it Matters |
| --- | --- |
| **Speed (Latency + Throughput)** | Critical for real-time analytics, AI/ML workloads. |
| **Durability / MTBF** | Mean Time Between Failure affects uptime in production systems. |
| **Scalability** | System must grow with data. Consider RAID/NAS/SAN or cloud hybrids. |
| **Write Endurance** | Especially important for SSDs under heavy write loads. |
| **Fragmentation Resistance** | Affects long-term performance stability. |
| **Cost Efficiency** | Balance between high-speed SSDs and cheaper HDDs or cloud cold storage. |

---

## 🧠 Final Thoughts

Storage technology has evolved from **slow, sequential access**
models to **ultra-fast, resilient, and scalable** systems.

SSDs revolutionized expectations around latency and reliability,
while cloud and network storage brought new flexibility.

**When designing high-performance systems**, think holistically:

- Match storage type to workload.
- Monitor performance over time (e.g., wear indicators).
- Consider hybrid setups (SSD for cache, HDD for bulk, cloud for archival).

## 🔹 Section 6.2 — **RAID: Redundant Array of Independent Disks**

RAID is a **data storage virtualization** technique that combines
multiple physical disks into one logical unit,
to improve **performance**, **fault tolerance**, or both.

### 🔑 Key RAID Terminology

| Term | Meaning (in your own words) |
| --- | --- |
| **Striping** | Splitting data across multiple disks to increase read/write speed. |
| **Mirroring** | Copying identical data to two or more disks for redundancy. |
| **Parity** | Extra data used to reconstruct information in case of disk failure. |
| **RAID Controller** | Hardware or software that manages RAID logic. |

### 🔢 RAID Levels Overview

| RAID | Description | Pros | Cons | Use Case |
| --- | --- | --- | --- | --- |
| **RAID 0** | Striping only (no redundancy) | Fast performance | No fault tolerance | Video editing, gaming |
| **RAID 1** | Mirroring | High redundancy | 50% storage loss | OS drives, critical systems |
| **RAID 5** | Striping + distributed parity | Balanced performance & fault tolerance | Slower writes | Web servers, databases |
| **RAID 6** | Like RAID 5, but double parity | Can survive 2 disk failures | Even slower writes | High-availability systems |
| **RAID 10 (1+0)** | Mirroring + striping | High performance + redundancy | High cost | High-transaction systems |

---

## 🧠 RAID Strategy Takeaways

- **Redundancy priority?** → Use **RAID 1**, **RAID 5**, or **RAID 6**.
- **Performance priority?** → Use **RAID 0** or **RAID 10**.
- **Mission-critical with budget?** → **RAID 10** (best of both, but expensive).
- **Space efficiency + redundancy?** → **RAID 5** is a solid balance.

---

## 🔹 Section 6.3 — **Solid State Drives (SSDs)**

SSDs use **non-volatile flash memory** instead of spinning disks,
meaning no moving parts, faster speeds, and less power usage.

### 🔑 SSD Concepts & Terms

| Term | Meaning (in your own words) |
| --- | --- |
| **Flash Memory** | Type of memory that keeps data without power. |
| **Wear Leveling** | Spreads out writes evenly to prevent early cell failure. |
| **TRIM Command** | Helps the OS inform the SSD of unused data blocks to clean up. |
| **Garbage Collection** | Background process to clear and prepare memory blocks for writing. |
| **Endurance** | Number of write/erase cycles before memory cells fail. |

---

## 🔧 SSD Challenges and Design Implications

| Challenge | How It Affects Storage Design |
| --- | --- |
| **Write Wear** | Drives need **wear leveling** to ensure long-term health. |
| **Write Amplification** | SSDs may write more data than requested → impacts lifespan. |
| **No In-Place Updates** | Entire blocks must be erased before rewriting → requires buffer management. |
| **Data Recovery** | Recovery is more complex than HDDs; often requires special tools. |

**Design Adjustments Include:**

- Using **over-provisioning** (extra hidden space).
- Integrating **TRIM** and **garbage collection**.
- Choosing **RAID levels that minimize write amplification**.

---

## 🔄 RAID with SSDs vs. HDDs

| Feature | HDDs | SSDs |
| --- | --- | --- |
| Wear Concern | Low | High |
| Performance Gain from RAID | Significant | Already high without RAID |
| RAID 5/6 Viability | OK | Can increase wear without proper TRIM support |
| Best Practice | RAID 10 or 1 | Avoid parity-heavy setups like RAID 5 unless wear handled |

---

## 🧠 Final Analysis: Choosing the Right Setup

### 🎯 For Redundancy (e.g., critical financial data)

- **RAID 1 or 6 (HDDs)** – safer against disk failure.
- **RAID 10 (SSDs)** – combines speed + redundancy + lower wear.

### 🚀 For Performance (e.g., real-time data pipelines)

- **RAID 0 or RAID 10 (SSDs)** – SSDs already reduce latency; striping boosts throughput.
- Avoid RAID 5/6 with SSDs unless wear-leveling and TRIM are explicitly supported.

---

## ✅ Summary

- SSDs **excel in speed**, but require smarter wear handling and garbage collection.
- RAID provides **tailored solutions** for redundancy, speed,
  or both—choose based on workload and failure tolerance.
- For modern high-performance systems, combining **SSDs with RAID 10**
  offers both reliability and throughput—with proper management of SSD-specific constraints

## 🔹 Section 6.4 — **Optical Memory (CDs, DVDs, Blu-ray)**

### 📚 Key Terms & Definitions

| Term | Meaning (in your own words) |
| --- | --- |
| **Pits and Lands** | Physical indentations (pits) and flat areas (lands) on optical discs that represent binary data when read by a laser. |
| **Track Spiral** | Data on an optical disc is stored in a single long spiral track, unlike circular tracks on magnetic disks. |
| **Laser Beam Reading** | A laser reflects off the disc; differences in reflection (pit vs land) are interpreted as binary data. |
| **Write Once, Read Many (WORM)** | Optical media types that can be written to once (e.g., CD-R), but read repeatedly. |
| **Phase Change Technology** | Used in rewritable discs (e.g., CD-RW, DVD-RW), which change state between crystalline and amorphous to store data. |

### 💡 Characteristics of Optical Memory

- **Cheap and portable** — good for media distribution and archival.
- **Relatively slow** — poor random access speed compared to SSDs/HDDs.
- **Durable** — less susceptible to magnetic interference or mechanical shocks.
- **Low capacity** compared to modern flash or hard drives.
- Mostly **read-oriented** today (movies, backups, installations).

---

## 🔹 Section 6.5 — **Magnetic Tape**

### Terms & Definitions

| Term | Meaning |
| --- | --- |
| **Sequential Access** | Data is read in the order it was written, not randomly accessible like a disk. |
| **Reel-to-Reel Storage** | Tape is wound between spools during reading/writing. |
| **Data Density** | The amount of data that can be stored per inch of tape. |
| **Tape Library** | Automated system with robotic arms to retrieve and load tapes. Often used for archival data. |
| **LTO (Linear Tape-Open)** | A modern magnetic tape storage standard used in enterprises. |

### 💡 Magnetic Tape Advantages

- Extremely **high capacity** (now into hundreds of TBs per cartridge).
- **Inexpensive** per gigabyte — great for **archival and backup**.
- Excellent for **cold storage** (data that’s rarely accessed).
- Drawback: **Very slow access time**.

---

## 📰 Related Articles — Key Insights

### 🧠 **ITPro: Tape Storage’s Comeback**

- In 2023, **152.9 exabytes** of tape shipped — the highest ever.
- **AI and compliance** (e.g., GDPR) are driving demand for long-term storage.
- Tapes are being embraced again for their cost, longevity, and security benefits.

### 📊 **ACM: The Data Storage Crisis**

- The **volume of data is outpacing current storage density growth**.
- Researchers are exploring **new materials, physics, and optical tricks**
  to expand data storage (e.g., using phase transitions or atomic-scale bits).
- Suggests the need for **hybrid storage strategies**—not just speed,
  but lifespan and cost must be balanced.

### ⚙️ **TechXplore: Wafer-Scale Accelerators**

- AI workloads are driving the adoption of **wafer-scale chips** (like Cerebras WSE-3).
- These require **massive, fast-access memory bandwidth**—highlighting limits
  of traditional storage when used for AI training.
- Suggests a **clear divide between “hot” and “cold” data**: fast RAM/SSD for real-time,
  massive tapes for bulk retention.

---

## 🔄 Modern Implications: Key Questions Answered

### 🔍 **How have advancements (tapes → SSDs) changed our thinking?**

| Factor | Then (Tapes) | Now (SSDs, Flash) |
| --- | --- | --- |
| **Speed** | Sequential, slow | Instant random access |
| **Reliability** | Good for archiving | Wear-out risk (SSDs) |
| **Storage Management** | Manual, mechanical | Software-controlled, smart caching |
| **Access Model** | Archival | Real-time & mobile |

Modern systems now **tier** storage:

- SSDs/DRAM for real-time processing
- HDDs for bulk/active data
- Tapes/cloud cold storage for rarely-used backups

---

### ⚖️ **How should storage be chosen for HPC (High Performance Computing)?**

**Priorities for HPC:**

- **Latency and IOPS** (SSDs)
- **Concurrent read/write** (RAID or NVMe SSD arrays)
- **Durability of writes** (SSDs with wear-leveling)
- **Cheap backup/archiving** (tapes, cloud blob)

So you'd balance **performance, cost, redundancy, and lifespan** depending on:

- Volume
- Access frequency
- Failure impact

---

## ✅ Final Thoughts

- Optical media is declining but still **relevant for distribution and backups**.
- Magnetic tape is **back in demand** for its role in **cheap, high-capacity archival**.
- Storage now involves **strategic layering**—
  using the right medium for the right use case.
- New AI hardware (like wafer-scale accelerators) emphasizes the growing gap -
  between compute speed and storage throughput.
