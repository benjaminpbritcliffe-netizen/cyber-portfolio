# Security Engineering Models

Created: 21 May 2025 14:32
Is Completed: Yes

## 📘 1. **Bell-LaPadula Model (Confidentiality Focused)**

- **Goal**: Protect **secrets** — primarily used in military and government.
- **Rules**:
    - **No Read Up**: Users cannot read data above their security level.
    - **No Write Down**: Users cannot write data to lower levels (prevents secret leaks).
- **Think**: "Keep confidential data from leaking."

---

## 📗 2. **Biba Model (Integrity Focused)**

- **Goal**: Protect **accuracy and trustworthiness** of data.
- **Rules**:
    - **No Read Down**: Users cannot read data from lower integrity levels.
    - **No Write Up**: Users cannot write data to higher integrity levels.
- **Think**: "Keep data clean and reliable."

---

## 📙 3. **Clark-Wilson Model (Commercial Integrity)**

- **Goal**: Ensure **data is modified properly** and only by authorized users.
- **Key Ideas**:
    - Uses **well-formed transactions** (controlled steps) to enforce rules.
    - Uses **programs** to separate users from data and verify rules.
- **Think**: "Only the right people can make the right changes the right way."

---

## 📕 4. **Brewer-Nash Model (The 'Coca-Cola' Model)**

- **Goal**: Prevent **conflicts of interest** (used in consulting firms).
- **Key Idea**:
    - Access to one company's data blocks access to competitors' data.
- **Think**: "No spying on competitors."

---

## 📒 5. **Graham-Denning Model**

- **Goal**: Manage **secure rights and permissions** in a system.
- **Key Components**:
    - Defines **8 rules** for creating/deleting users and objects and managing access.
- **Think**: "Who can do what, to which data, and how?"

---

## 🧠 Summary Table:

| Model | Focus | Common Use |
| --- | --- | --- |
| Bell-LaPadula | Confidentiality | Military/Government |
| Biba | Integrity | Medical, Banking |
| Clark-Wilson | Commercial Integrity | Business Systems |
| Brewer-Nash | Conflict of Interest | Consulting Firms |
| Graham-Denning | Access Control | Operating Systems |