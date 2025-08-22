# Perhiperal Devices

Created: 15 July 2025 13:21 Is Completed: No

## ✳️ **Key Concepts and Terminology**

| Term                                 | Definition (in your own words)                                                                                       |
| ------------------------------------ | -------------------------------------------------------------------------------------------------------------------- |
| **Peripheral Interface**             | The method by which input/output devices (e.g., keyboard, mouse, touch screen) connect and communicate with the CPU. |
| **Device Driver**                    | Software that allows the operating system to communicate with hardware peripherals.                                  |
| **Human-Computer Interaction (HCI)** | The study and design of how humans interact with computers using interfaces like GUIs, touch, and voice.             |
| **Communication Protocol**           | A set of rules for transmitting data between devices over a network.                                                 |
| **Overhead**                         | Extra time or resources needed to manage communication and coordination in a system.                                 |
| **Latency**                          | Delay between a user action and a system’s response or between sending and receiving data.                           |
| **Bandwidth**                        | The amount of data that can be transmitted over a network connection in a fixed period.                              |

---

## 📌 Peripheral Interfaces: Evolution and Impact

### 💡 **Emerging Peripheral Interfaces**

- **Touchscreens**, **voice control**, **gesture recognition**, and **eye
  tracking** are examples of modern input methods.
- Devices are becoming more **natural**, **intuitive**, and **adaptive**,
  reducing barriers for users.

### 🧠 **Impact on Accessibility**

- Improved **usability for people with disabilities** (e.g., screen readers,
  braille interfaces, speech-to-text).
- Enables **multi-modal interaction**—users can combine voice, touch, and visual
  feedback.

### 🔄 **Impact on Productivity**

- Faster and more fluid interaction increases efficiency (e.g., touchscreens for
  quick tasks).
- Customizable input for different user needs (e.g., CAD users vs. gamers vs.
  voice users).

---

## 🔌 Wired vs. Wireless Communication

### 📡 **Network Protocols and Overhead**

| Type                 | Impact                                                                |
| -------------------- | --------------------------------------------------------------------- |
| **TCP/IP**           | Reliable but has more overhead due to error-checking and ordering.    |
| **UDP**              | Faster, less overhead, but no delivery guarantees—good for streaming. |
| **Bluetooth/Wi-Fi**  | Wireless convenience but prone to interference and speed variability. |
| **Ethernet (Wired)** | Low latency, high bandwidth, better for high-performance tasks.       |

### ⚖️ **Trade-Offs: Wired vs Wireless**

| Feature         | Wired            | Wireless                                                 |
| --------------- | ---------------- | -------------------------------------------------------- |
| **Speed**       | Typically faster | More variable                                            |
| **Latency**     | Lower            | Higher (can be significant for gaming or real-time data) |
| **Reliability** | Stable           | Susceptible to dropouts/interference                     |
| **Mobility**    | Limited          | High                                                     |

### 🎯 **Design Considerations**

- Use **wired connections** for:
  - Servers, real-time processing, or applications requiring large data
    transfers.
- Use **wireless** for:
  - Flexibility, mobile devices, or when physical cabling is impractical.
- Design systems to **balance overhead and convenience** depending on the use
  case.

---

## 💬 Summary: Big Picture Thinking

### ✅ How emerging interfaces improve computing

- Shift towards **user-centered design**.
- **Accessibility** becomes an integrated part of UI/UX strategy.
- More inclusive technology = wider reach and better user satisfaction.

### ✅ How network protocol overhead affects system performance

- High overhead = **better reliability**, but slower speeds.
- Protocols and infrastructure must be tailored to the application:
  - **High-speed media streaming?** → UDP
  - **Banking transactions?** → TCP
  - **IoT sensors?** → Lightweight protocols like MQTT over Wi-Fi/Bluetooth
