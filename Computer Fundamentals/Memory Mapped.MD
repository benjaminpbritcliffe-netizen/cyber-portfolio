# Memory Mapped

Created: 15 July 2025 13:15 Is Completed: No

## 🔧 **Key Terminology & Concepts**

### 🧠 1. **Memory-Mapped I/O (MMIO)**

- A method where **device registers** (e.g. for a keyboard, disk, or graphics
  card) are mapped to specific **memory addresses**.
- The **CPU interacts with I/O devices** using standard **load/store**
  instructions (e.g., `mov`, `lw`, `sw`) instead of special I/O instructions.

### ✅ **Advantages:**

- Simplifies the programming model—no need to switch between memory and I/O
  instruction sets.
- Makes device communication more consistent with regular memory access
  patterns.
- Enables use of standard compiler optimizations and C code.

### ⚠️ **Trade-Offs:**

- Portions of memory are reserved for device I/O, reducing usable RAM.
- Requires **cache management** (MMIO regions are often marked uncacheable to
  prevent stale reads).
- Can complicate virtual memory systems if MMIO regions are mapped incorrectly.

---

### 🖥️ 2. **Device Controllers**

- Hardware interfaces that manage communication between the CPU and specific I/O
  devices (e.g., **USB controller**, **GPU adapter**, **disk controller**).
- Controllers handle **registers** (for commands, statuses) and **buffers** (for
  data).
- Communicate with **main memory** via **Direct Memory Access (DMA)**.

---

### 🚍 3. **System Bus**

- The **data highway** that connects the CPU, memory, and I/O controllers.
- Includes three types of lines:
  - **Address Bus** – identifies memory/I/O locations.
  - **Data Bus** – transfers actual data.
  - **Control Bus** – sends commands like read/write.

---

### ⚙️ 4. **Programmed I/O vs. DMA**

- **Programmed I/O**: CPU manually reads/writes to MMIO addresses (inefficient
  for large data transfers).
- **DMA (Direct Memory Access)**:
  - Offloads data transfer to the controller.
  - Frees CPU for other tasks.
  - Essential for high-throughput devices like graphics cards or USB storage.

---

### 💡 **Questions Addressed**

---

### 🧩 _Q1: How does memory-mapped I/O simplify CPU-device communication?_

| Benefit                | Explanation                                                                             |
| ---------------------- | --------------------------------------------------------------------------------------- |
| Unified access         | CPU can use standard instructions (`mov`, `load`, `store`) to communicate with devices. |
| Compiler compatibility | Easier to manage in high-level code; no need for assembly-level I/O.                    |
| Flexible design        | Device registers can be treated as memory cells.                                        |

**Trade-offs**:

- You lose memory space to device registers.
- MMIO regions must be managed carefully in cache and VM systems.
- Bugs in device access can crash the system due to unrestricted memory access.

---

### 🎮 _Q2: How do USB and graphics devices use the system bus and memory architecture?_

| Device               | Use of System Bus                                                              | Role of Memory Architecture                                                              |
| -------------------- | ------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------- |
| **USB Controller**   | Transfers data via DMA over the system bus; CPU sends high-level instructions. | Uses memory buffers to read/write data from peripherals (e.g., keyboards, flash drives). |
| **Graphics Adapter** | Accesses GPU memory and framebuffer via bus or PCIe lanes.                     | Relies on fast memory for textures, framebuffers; often mapped into memory space.        |

**Key Point**: Devices rely on **DMA** and **bus bandwidth** to avoid
overloading the CPU and to maintain system responsiveness.

---

## 📝 **Summary**

- **Memory-Mapped I/O** allows devices to appear as memory, making programming
  easier and more uniform.
- Devices like USB controllers and GPUs interact with **RAM** and the **CPU**
  via the **system bus**, often using **DMA** to offload transfers.
- While MMIO simplifies access, it introduces **memory management and cache**
  challenges that require careful system design.
