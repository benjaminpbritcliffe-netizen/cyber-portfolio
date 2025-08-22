# Basic Concepts of Software and Hardware

Created: 3 July 2025 11:35 Class: 6 Is Completed: No

---

## 📘 Key Terms & Definitions

1. **Operating System (OS)**A system-level software layer that manages hardware
   resources and provides common services for applications
   [mebrahimii.github.io+1cs.hunter.cuny.edu+1](https://mebrahimii.github.io/comp322-fall2024/lecture/week_1/OS%20Services%20and%20Structures%20-%20Ch%202.pdf?utm_source=chatgpt.com)[en.wikipedia.org+10en.wikipedia.org+10drive.uqu.edu.sa+10](https://en.wikipedia.org/wiki/Operating_system?utm_source=chatgpt.com).
2. **Kernel**
   - The core part of an OS that runs in privileged mode ("kernel mode"),
     handling CPU scheduling, memory, I/O, and inter-process communication.
3. **User Mode vs Kernel Mode**
   - **Privilege separation**: Kernel mode has full access to system hardware;
     user mode is restricted and must use system calls
     [cs.hunter.cuny.edu+3en.wikipedia.org+3mebrahimii.github.io+3](https://en.wikipedia.org/wiki/CPU_modes?utm_source=chatgpt.com).
4. **System Call**
   - A controlled request from a user application to the kernel to perform
     privileged operations, like file access or I/O.
5. **Monolithic Kernel**

- A design where most OS services run inside a single kernel space—for speed,
  but at the cost of complexity.

1. **Microkernel**

- Minimal kernel design that runs most services in user space, communicating via
  message passing. Improves security and modularity, but may reduce performance
  [cs.hunter.cuny.edu+2cs.fsu.edu+2mebrahimii.github.io+2](https://www.cs.fsu.edu/~lacher/courses/COP4610/lectures_8e/ch02.pdf?utm_source=chatgpt.com)

.

1. **Layered Structure**

- An OS design organized into layers where higher layers depend only on lower
  ones—enabling modularity and easier maintenance
  [mebrahimii.github.io+5cs.fsu.edu+5cc.ee.ntu.edu.tw+5](https://www.cs.fsu.edu/~lacher/courses/COP4610/lectures_8e/ch02.pdf?utm_source=chatgpt.com).

1. **Virtual Machine (VM)**

- A complete OS environment emulated by another OS, making software believe it's
  running on real hardware
  [cps-cse.media.uconn.edu+3en.wikipedia.org+3en.wikipedia.org+3](https://en.wikipedia.org/wiki/Instruction_set_architecture?utm_source=chatgpt.com).

1. **Instruction Set Architecture (ISA)**

- Defines the CPU's supported instructions, registers, memory model, and control
  flow—serving as the interface between hardware and software
  [en.wikipedia.org+1en.wikipedia.org+1](https://en.wikipedia.org/wiki/Instruction_set_architecture?utm_source=chatgpt.com).

1. **RISC and CISC**
   - **RISC**: Simplified, fixed-length instructions optimized for speed and
     pipelining.
   - **CISC**: Richer, complex instructions that pack more work in each
     operation
     [en.wikipedia.org+1en.wikipedia.org+1](https://en.wikipedia.org/wiki/Reduced_instruction_set_computer?utm_source=chatgpt.com).

2. **Protection Ring**

- Hardware-enforced privilege levels (e.g., Ring 0 vs Ring 3) to isolate
  untrusted code from the kernel
  [eng.auburn.edu+11en.wikipedia.org+11en.wikipedia.org+11](https://en.wikipedia.org/wiki/Protection_ring?utm_source=chatgpt.com).

### 1. Von Neumann Model Influence & Its Limitations

- **Influence**: It laid the foundation for modern CPU design—shared memory,
  instruction/data registers, and sequential fetch-execute cycles.
- **Limitations**: The von Neumann bottleneck causes slowness due to shared bus
  for instructions and data. It doesn't natively support parallelism or
  protection mechanisms—architecture had to adapt (e.g., pipelining, caches,
  privilege modes).

---

### 2. Trade-offs Between Speed & Complexity

- **Monolithic kernels** offer fast operation but are complex and harder to
  secure or maintain.
- **Microkernels/layered designs** are more modular and secure, but
  inter-process messaging and context switching add overhead.
- **ISA design** balances complexity: RISC simplifies CPU but requires more
  instructions, while CISC reduces instruction count but complicates CPU design
  and pipelining.
