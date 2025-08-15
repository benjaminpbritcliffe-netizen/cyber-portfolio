# Computer Circuits

Created: 4 July 2025 15:58
Is Completed: No

## 1. **Binary and Hexadecimal Numbers** 🧮

- **Binary (base‑2)** uses two symbols, `0` and `1`. Each position represents a power of 2 (e.g., 1, 2, 4, 8…). Computers operate in binary.
- **Hexadecimal (base‑16)** uses `0–9` and `A–F` (where A=10, B=11, … F=15). Each hex digit represents four binary bits, making it a more compact way to display binary data [youtube.com+6lifewire.com+6simplicable.com+6](https://www.lifewire.com/what-is-hexadecimal-2625897?utm_source=chatgpt.com).

**Why use hex?**

- More human‑readable than long binary strings.
- Widely used in programming, debugging, and color codes (e.g., `#FF0000` for red) [lifewire.com](https://www.lifewire.com/what-is-hexadecimal-2625897?utm_source=chatgpt.com).

---

## 2. **Half Adder and Full Adder Circuits**

### 🔹 Half Adder

- Adds two single-bit inputs (A, B).
- Outputs a **Sum (S = A ⊕ B)** and a **Carry (C = A · B)** [eecs.umich.edu+14electronicsforu.com+14theorycircuit.com+14](https://www.electronicsforu.com/technology-trends/learn-electronics/half-adder-full-adder-truth-table-circuit-working-kmap?utm_source=chatgpt.com).
- Typical circuit: one XOR gate and one AND gate, as shown in the image above.

| A | B | Sum | Carry |
| --- | --- | --- | --- |
| 0 | 0 | 0 | 0 |
| 0 | 1 | 1 | 0 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 1 |

### 🔹 Full Adder

- Extends the half adder by including a **carry-in (Cₙ)** from a previous bit.
- Inputs: A, B, and Cₙ.
- Sum = A ⊕ B ⊕ Cₙ; Carry-out = (A·B) + (Cₙ·(A⊕B)) [theorycircuit.com+4en.wikipedia.org+4tutorialspoint.com+4](https://en.wikipedia.org/wiki/Adder_%28electronics%29?utm_source=chatgpt.com)[electroniclinic.com+13geeksforgeeks.org+13tutorialspoint.com+13](https://www.geeksforgeeks.org/difference-between-half-adder-and-full-adder/?utm_source=chatgpt.com).
- Built using two half adders plus one OR gate.

**Why it matters:**

- Full adders can be cascaded into multi-bit **ripple-carry adders**, enabling binary addition in CPUs [geeksforgeeks.org+14en.wikipedia.org+14circuitdiagram.co+14](https://en.wikipedia.org/wiki/Adder_%28electronics%29?utm_source=chatgpt.com).

---

## 3. **Optional: Sequential Logic – Flip-Flops, Registers, Counters**

### 🔸 RS Flip-Flop

- Basic memory element with **Set (S)** and **Reset (R)** inputs.
- Maintains (latches) a 0 or 1 output (Q) until inputs change [manualboudek7wd.z14.web.core.windows.net+7geeksforgeeks.org+7slideshare.net+7](https://www.geeksforgeeks.org/electronics-engineering/rs-flip-flop/?utm_source=chatgpt.com)[slideshare.net+2ece.mcmaster.ca+2en.wikipedia.org+2](https://www.ece.mcmaster.ca/~xwu/2di4/chapter7.pdf?utm_source=chatgpt.com).

### 🔸 D-Type Flip-Flop

- Data latch triggered on a clock edge.
- Captures the input (D) on a clock transition, making it ideal for synchronous storage [en.wikipedia.org](https://en.wikipedia.org/wiki/Flip-flop_%28electronics%29?utm_source=chatgpt.com).

### 🔸 Registers

- Formed by combining multiple D flip-flops.
- Used to hold binary words (e.g., 8-bit or 16-bit data) within CPUs or digital devices.

### 🔸 Digital Counters

- Built from flip-flops, often D or T types.
- Can increment binary counts each clock pulse.
- Useful in timers, clocks, and for dividing clock frequencies [circuitdataoverlabour.z21.web.core.windows.net+5en.wikipedia.org+5slideshare.net+5](https://en.wikipedia.org/wiki/Flip-flop_%28electronics%29?utm_source=chatgpt.com)[slideshare.net+1lifewire.com+1](https://www.slideshare.net/slideshow/flip-flop-counters-registers-computer-fundamental-and-organization/89797191?utm_source=chatgpt.com).

---

## ✅ Forward-Thinking Takeaways

- **Binary/Hex** foundations are essential for understanding digital systems.
- **Half/full adders** are the digital arithmetic building blocks.
- **Flip-flops and counters** form the basis of sequential, time-dependent logic—critical in memory, timing, and registers.
- These fundamentals underpin everything in digital electronics—from calculators to CPUs.