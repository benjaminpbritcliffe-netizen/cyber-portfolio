\# OS Design

Created: 24 July 2025 10:57
Is Completed: No

| Term | Definition (In Your Own Words) |
| --- | --- |
| **Operating System (OS)** | The main software that manages all hardware and software on a computer, acting as a bridge between the user, applications, and hardware. |
| **Kernel** | The core part of the OS responsible for managing hardware, processes, memory, and system calls. |
| **System Call** | A request made by a program to the OS for a service, like accessing files or communicating with hardware. |
| **Scheduler** | A component that decides which processes run and when, to manage CPU time efficiently. |
| **Driver** | A specialized program that lets the OS communicate with specific hardware devices. |
| **Process** | A running instance of a program, including code, data, and system resources. |
| **Thread** | The smallest unit of execution within a process. |
| **Virtual Memory** | A memory abstraction that gives programs the illusion they have access to a large, continuous memory space. |

Abstraction in operating systems hides the complexity of hardware by offering a simplified interface. Instead of dealing with raw binary instructions or specific device protocols, users and programmers interact with files, applications, and graphical interfaces. For example, a programmer doesn’t need to know how a hard drive stores data — they just use file commands like “open” or “save.” This makes it much easier to develop software and allows users to work intuitively with complex machines.

A **general-purpose OS** (like Windows, macOS, Linux) needs to be flexible, capable of running many different applications, managing multiple users, and supporting a wide range of hardware. It prioritizes usability, compatibility, and multitasking.

An **embedded system OS**, on the other hand, is optimized for one specific task — such as controlling a washing machine or a medical device. It often has real-time constraints, must use minimal resources, and is tightly integrated with specific hardware. Security, speed, and reliability are more critical than user-friendly features.

| **Term** | **Definition (In Your Own Words)** |
| --- | --- |
| **System Call** | A controlled way for a user program to request services or resources from the OS kernel. |
| **Kernel Mode** | A CPU mode that allows execution of privileged instructions; used by the OS for full hardware access. |
| **User Mode** | A restricted CPU mode used by applications, preventing direct access to critical system resources. |
| **Trap** | A software-generated interrupt triggered by a system call or error, used to switch to kernel mode. |
| **Interrupt** | A signal from hardware to the processor, indicating an event like I/O completion or a timer expiry. |
| **Exception** | Any unexpected event that disrupts normal program flow, either from hardware or software. |
| **Context Switch** | Saving one process’s state and loading another's — used in multitasking and handling interrupts. |
| **File Descriptor** | An integer handle returned by the OS when a file or resource is opened; used for reading/writing. |

System calls act as a **controlled gateway** between a user program and the OS kernel. Since user-mode programs are restricted from directly accessing hardware (for safety and stability), they must use system calls to request services like:

- Reading/writing files
- Allocating memory
- Creating processes
- Accessing the network

When a program makes a system call (e.g., `read()` or `write()` in C), the CPU performs a **trap**, switching the processor from **user mode to kernel mode**. The OS then safely executes the requested operation on the program’s behalf and returns the result.

### 🔑 Why It's Important:

- Prevents bugs or malicious code from corrupting the system.
- Enforces privilege separation: programs can’t overwrite memory or kill other processes without permission.
- Provides a **consistent API** across hardware platforms.

> Example: When you open a file in C using open(), you’re not talking directly to the hard drive — you’re calling the OS to do it safely for you.
> 

### 🔷 **Hardware-Generated Exceptions (e.g., Interrupts & Faults):**

- Occur at the **CPU level** due to hardware events.
- Examples:
    - Timer interrupt
    - Keyboard input
    - Page fault (accessing non-resident memory)
- Handled by the OS through predefined interrupt/trap handlers.
- Often used for resource management, multitasking, and error handling at the system level.

### 🔷 **Software Exceptions (in languages like Java or Python):**

- Triggered **by code logic**, not the CPU.
- Examples:
    - Division by zero
    - Null pointer access
    - File not found
- Caught using constructs like `try...catch` or `try...except`.
- Handled within the application logic, **not by the OS kernel**.

### ✅ **Why This Distinction Matters:**

- **Level of handling**: Hardware exceptions are handled by the OS; software exceptions are handled by the application.
- **Purpose**: Hardware exceptions keep the system stable and responsive; software exceptions keep the application robust and user-friendly.
- **Control**: Programmers write code to handle software exceptions, but rely on the OS to manage hardware exceptions.

> Analogy:
> 
> 
> Think of hardware exceptions like a fire alarm (must be handled by firefighters — the OS), while software exceptions are like spelling errors in a document (you can fix those yourself — the program handles them).
> 

- **OS as Interface:** The lesson explains how operating systems serve as an essential layer managing the relationship between hardware and software to enable user interaction and resource management.
- **OS vs. Bare-metal:** It differentiates operating systems from bare-metal systems, where software runs directly on hardware without the use of abstraction layers, such as BIOS and the kernel.
- **Kernel Role:** The kernel is highlighted as the core control component responsible for managing processes, memory, and devices, acting as the system’s taskmaster.
- **System Calls:** The material covers how programs use system calls to interact with the OS kernel, requesting services and accessing hardware safely and efficiently.
- **Exceptional Control Flow:** Concepts such as interrupts, faults, traps, and aborts are introduced as special events that change normal execution flow to manage hardware and OS-level events.
- **OS Exceptions vs. Language Exceptions:** The reading clarifies the difference between OS-level exceptions and high-level language exceptions, using Linux examples to illustrate these system-level mechanisms.

| **Term** | **Your Own Definition** |
| --- | --- |

| **Workload Management** | The way an OS organizes and prioritizes the execution of tasks to balance performance and fairness. |
| --- | --- |

| **Scheduling** | The process of deciding which task (process or thread) runs on the CPU at any given time. |
| --- | --- |

| **Preemptive Scheduling** | A strategy where the OS can interrupt a running task to give the CPU to another, usually higher-priority, task. |
| --- | --- |

| **Non-preemptive Scheduling** | Tasks run until completion or voluntarily yield the CPU; the OS doesn't interrupt them mid-execution. |
| --- | --- |

| **Round-Robin Scheduling** | Each process gets an equal time slice in a rotating order, promoting fairness. |
| --- | --- |

| **Priority Scheduling** | Tasks are scheduled based on assigned priority levels; higher-priority tasks run first. |
| --- | --- |

| **Interrupt** | A signal that pauses current execution to let the CPU respond to an external or internal event. |
| --- | --- |

| **Polling** | A method where the CPU repeatedly checks a device or condition to see if it needs attention. |
| --- | --- |

| **Context Switch** | The act of saving the state of one process and loading the state of another during a CPU switch. |
| --- | --- |

| **Real-Time Operating System (RTOS)** | An OS designed to handle tasks within strict timing constraints, often used in embedded systems. |  |
| --- | --- | --- |
- **Process and Thread Management:** The operating system uses Process IDs (PIDs) and maintains essential data structures to manage and distinguish between concurrently running tasks (processes).
- **Scheduling and Prioritisation:** Tasks are scheduled using algorithms such as preemptive scheduling and multiple priority queues to ensure performance, fairness, and responsiveness.
- **Thread Models and Execution:** Threads are managed as lightweight execution units within processes using different threading models, enabling parallelism and resource sharing.
- **Event Handling:** Interrupts and polling mechanisms enable the CPU to respond to external events in real-time, which is particularly crucial in real-time systems.
- **Concurrency and Thread Safety:** The chapter emphasises thread safety and reentrancy to prevent issues like race conditions when multiple threads access shared resources.

| **Term** | **Definition (In Your Own Words)** |
| --- | --- |
| **Multicore Processor** | A single CPU chip with multiple cores that can independently execute tasks, improving parallelism. |
| **Hyperthreading (Simultaneous Multithreading - SMT)** | A technology allowing a single physical core to handle multiple threads by sharing its resources more efficiently. |
| **Task Switching** | Switching the CPU from one task to another, which involves saving and loading process state (context). |
| **CPU Affinity** | Binding a process or thread to a specific CPU core to reduce overhead and improve performance. |
| **Uniprocessor System** | A computer with only one CPU, executing one instruction stream at a time. |
| **Multiprocessor System** | A system with more than one processor (or core) working together to handle tasks concurrently. |
| **Load Balancing** | Distributing work evenly across CPUs or cores to maximize resource use and minimize idle time. |

### 🔷 Traditional Uniprocessor Systems:

- Can run only **one task at a time**.
- Frequent **context switches** are needed to simulate multitasking.
- Each switch involves saving/restoring CPU state — an **expensive operation** in terms of time and performance.

### 🔷 How Multicore Systems Help:

- Multiple cores can run **multiple tasks simultaneously**, reducing the need to switch between tasks as often.
- **True parallelism**: One core handles user input, another processes data, etc.
- Reduces overhead of **task switching**, since fewer switches are required overall.

### 🔷 How Hyperthreading Helps:

- Allows a single core to process **two threads concurrently** by sharing execution units.
- If one thread stalls (e.g., waiting on memory), the other can continue using the core.
- Increases **utilization of idle CPU resources** and smooths out performance.

> Bottom Line: Both multicore and hyperthreading reduce idle time and context-switching costs, improving system responsiveness and throughput.
> 

### 🔷 OS Design for Uniprocessor:

- Simpler scheduling — only one CPU to manage.
- No need for load balancing or thread migration.
- Less concern about concurrency and shared resource conflicts.
- Easier debugging, but limited performance scalability.

### 🔷 OS Design for Multiprocessor:

- Requires **advanced scheduling** to assign tasks across CPUs efficiently.
- Needs **synchronization mechanisms** to prevent race conditions (e.g., mutexes, semaphores).
- Includes **load balancing algorithms** to ensure all CPUs are utilized fairly.
- May implement **processor affinity** to minimize cache misses and memory latency.

### 🔷 Performance Implications:

- **Multiprocessor systems** can offer major performance gains, especially for multithreaded or parallel workloads.
- However, performance depends on how well the OS handles:
    - Thread scheduling across cores
    - Synchronization
    - Memory access patterns (NUMA-aware systems)
- Poor design can lead to **CPU contention**, **idle cores**, or **cache thrashing**.