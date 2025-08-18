# OS Hierarchies

Created: 22 July 2025 09:52
Is Completed: No

## **1. Operating System Models and Hierarchies**

**Models of Operating Systems:**

- **Monolithic Kernel** (e.g., Linux): All OS services run in kernel space for performance. Modular but not always fault-tolerant.
- **Microkernel** (e.g., QNX, Minix): Only essential services run in kernel space. More secure and stable, but slower due to inter-process communication.
- **Layered OS**: Hierarchical design where each layer builds upon the one below. Easier to debug and maintain.
- **Exokernel**: Minimal abstraction, giving applications direct access to hardware.
- **Hybrid Kernel** (e.g., Windows, macOS): Combines monolithic and microkernel approaches for balance between performance and stability.

**Hierarchy:**

1. **Hardware Layer** – CPUs, memory, I/O devices
2. **Kernel** – Core functions (scheduling, memory management)
3. **System Calls / APIs**
4. **User-Level Programs & Shells**
5. **Graphical User Interface (GUI)**

---

## **2. Types and Standards of OS**

- **Linux**: Open-source, Unix-like OS. Features multitasking, multithreading, and supports many architectures. Has strong server and developer community.
- **DOS (Disk Operating System)**: Early command-line OS with limited multitasking and no memory protection. Used in legacy systems.
- **macOS**: Unix-based graphical OS with a hybrid kernel (XNU). Emphasizes usability and tight hardware integration.
- **Graphical OS**: Includes a GUI (e.g., Windows, macOS, GNOME on Linux). Enables user interaction through visual elements.
- **Specialized OS:**
    - **RTOS (Real-Time OS)**: Provides deterministic responses to events, used in embedded systems (e.g., FreeRTOS, VxWorks).
    - **Embedded OS**: Small-footprint OS tailored for specific hardware (e.g., IoT devices).
    - **Mobile OS**: Android, iOS, optimized for touchscreen, power efficiency, and app sandboxing.

---

## **3. Program Execution, Scheduling, and User Contexts**

**Key Concepts:**

- **User/Superuser**: Regular users have limited permissions. Superuser (root/admin) has full system control.
- **Kernel**: Core of the OS. Manages hardware, scheduling, memory, and I/O.
- **Multitasking**: Running multiple processes concurrently.
- **Multithreading**: Single process with multiple threads sharing resources. More efficient than multiple processes.
- **Scheduling**: Determines which process/thread gets CPU time.
    - Types: Round Robin, Priority Scheduling, Multilevel Queue, Real-Time Scheduling.
- **Priority**: Higher-priority processes get preference. System prevents starvation via aging or priority inheritance.

**Measurement Characteristics:**

- **CPU Burst Time**, **Waiting Time**, **Turnaround Time**, **Throughput**, **Response Time**

---

## **4. Resource Utilization and Memory Management**

- **Virtual Memory**: Abstracts physical memory using paging. Allows large programs to run and supports memory isolation.
- **Memory Management**: Handles allocation/deallocation, segmentation, paging, and swapping.
- **Interprocess Communication (IPC)**: Mechanisms include shared memory, pipes, message queues, and sockets.
- **Virtualization**: Running multiple OS instances on a single host using a hypervisor (e.g., VMware, KVM).
- **Multiprocessor Systems**: Systems with multiple CPUs/cores. Require thread synchronization and load balancing.
- **Performance Issues:**
    - **Disk Swapping**: Moving data between RAM and disk when memory is full. Can cause performance bottlenecks.
    - **Thrashing**: Excessive swapping that severely degrades system performance.

---

## **5. Key Processor & OS Developments Supporting Modern Demands**

- **Multicore CPUs**: Improve concurrency and performance, essential for modern OS multitasking.
- **Hardware Virtualization Support**: Intel VT-x, AMD-V enable efficient hypervisors.
- **Security Enhancements**: Secure Boot, TPM integration, and kernel-level exploit protection.
- **Energy Efficiency**: Advanced Power Management (e.g., ACPI), especially important for mobile OS.
- **Containerization Support**: OS-level virtualization (e.g., Linux namespaces and cgroups used in Docker).
- **Parallel & Distributed Systems Support**: Integration with cloud and big data systems.

---

## **Learning Outcome Mapping**

| **Learning Outcome** | **How This Summary Supports It** |
| --- | --- |
| Identify OS components and behavior | Explained kernel, scheduling, memory, IPC, multitasking, threads |
| Resource management & concurrency | Detailed memory, CPU, IPC, and scheduling models |
| Analyze modern OS solutions | Compared Linux, RTOS, macOS, and virtualization trends |

### 🔷 **1. Hierarchical Structure of an Operating System**

Understanding the layered structure of an OS reveals how control flows from hardware to user software:

**OS Layers (Bottom to Top):**

1. **Firmware** – Low-level code stored in ROM (e.g., BIOS/UEFI) that initializes hardware.
2. **Kernel** – Core of the OS that manages CPU, memory, I/O, and processes.
3. **System Libraries & Drivers** – Enable communication between kernel and hardware/software.
4. **System Utilities** – Tools for system management (e.g., file explorers, terminal).
5. **User Interface (CLI/GUI)** – What users directly interact with.
6. **User Applications** – Web browsers, games, productivity software, etc.

Each layer depends on the one below it—firmware boots the system, the kernel allocates resources, and everything else builds upon this foundation.

---

### 🔷 **2. Diversity of Operating Systems**

Operating systems are **designed to meet the needs of specific environments**:

| Type | Example OS | Environment | Key Traits |
| --- | --- | --- | --- |
| **Embedded OS** | FreeRTOS, Zephyr | IoT, appliances | Lightweight, real-time constraints |
| **Mobile OS** | Android, iOS | Phones, tablets | Touch UI, battery-focused, app sandboxing |
| **Desktop OS** | Windows, macOS | PCs, laptops | GUI-focused, multitasking, full hardware use |
| **Server OS** | Linux, Windows Server | Data centers | High-performance, security, virtualization |
| **Real-Time OS (RTOS)** | VxWorks, RTEMS | Robotics, aerospace | Predictable timing, low latency |

---

### 🔷 **3. Core Functions of the Operating System**

These essential **backbone services** form the foundation of any OS:

### 🧠 **Process Management**

- Controls which programs run, when, and for how long.
- Uses **scheduling algorithms** (e.g., Round Robin, Priority Scheduling).
- Enables **multitasking** and **multithreading**.

### 💾 **Memory Management**

- Allocates RAM to processes.
- Uses **virtual memory** and **paging** to extend usable memory.
- Prevents programs from corrupting each other's memory.

### 📂 **File System Management**

- Organizes data on storage devices.
- Controls access rights (read, write, execute).
- Examples: FAT32, NTFS, ext4.

### 🖨️ **Device Management**

- Interfaces with hardware through **drivers**.
- Manages input/output operations (printers, disk drives, etc.).
- Handles **interrupts** and prioritizes device requests.

### 🔗 **Interprocess Communication (IPC)**

- Allows processes to exchange data and coordinate tasks.
- Methods include pipes, message queues, and shared memory.

---

### 🔷 **Key Takeaway: Software ↔ Hardware Bridge**

At its core, the OS functions as a **mediator**:

- **Software** (apps) requests services.
- **OS** manages hardware and allocates resources.
- **Hardware** executes tasks efficiently and securely.

This layered approach provides **stability, security, and abstraction**—allowing users and developers to focus on applications without dealing with hardware complexities.