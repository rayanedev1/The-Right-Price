# 🏛️ The Right Price: Restaurant Tribunal

<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=FF4B4B&height=220&section=header&text=THE%20RIGHT%20PRICE&fontSize=50&animation=fadeIn" width="100%" />
</p>

## 📖 Project Overview
**The Right Price** is an "algorithmic justice" application designed to end disputes when settling the bill at a restaurant. Leveraging the power of **Python** and **Streamlit**, this system transforms a moment of tension into a humorous and precise judicial procedure.

> "Justice is served. Settle your accounts without the drama."

---

## 🛠️ System Architecture

### 📊 Data Structure (Pandas Engine)
The application relies on a dynamic DataFrame that serves as the "Registry of Evidence."

| Component | Technology | Logical Function |
| :--- | :--- | :--- |
| **UI Interface** | `Streamlit` | Interactive tribunal and input widgets |
| **Calculation Engine** | `Pandas` | Price aggregation and grouped calculations |
| **State Management** | `Session State` | Data persistence during reruns |
| **Export** | `Standard IO` | Generation of the "Peace Treaty" (.txt) |

### 🔍 Specialized Features Analysis

#### ⚖️ The Redistribution Algorithm
The system integrates logic for handling specific edge cases, notably for the defendant **"Wallet Forgetter 🪙"**:
1. **Detection:** The script identifies if the "forgetter" has a debt.
2. **Transfer:** Their debt is reset to zero.
3. **Redistribution:** The amount is split equally and automatically added to the bills of the other participants.

#### 🧾 Service Charge Calculation
A dynamic slider allows for the application of a service charge percentage (0% to 20%). The calculation follows the formula:  
`Total = Price_Excl_Tax * (1 + Service_Rate)`

---

## 🧠 Development Logic

The software is built modularly, following the Streamlit execution lifecycle:

### 1. Initialization (`st.session_state`)
Unlike a standard Python script, Streamlit runs from top to bottom on every interaction. We use `session_state` to ensure the tribunal does not lose its "evidence" whenever the table is modified.

### 2. The Registry of Evidence (`st.data_editor`)
The use of `st.data_editor` allows for seamless data entry. Columns are strictly typed (Number for price, Dropdown for defendants) to prevent manual entry errors.

### 3. The Verdict Engine
When the **"Render Verdict"** button is clicked, the system executes:
* A `groupby('defendant')` to isolate individual expenses.
* A visual rendering using columns (`st.columns`) for immediate, clear reading.

---

## 🚀 Quick Start Guide

To transform your script into an interactive web application, follow these steps:

1. **Install dependencies:**
   ```bash
   pip install streamlit pandas
