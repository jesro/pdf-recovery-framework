---

# PDF Recovery Framework

A **GUI-based, configurable framework** for planning PDF password recovery tasks
in a **safe, transparent, and educational** way.

This project focuses on **inspection, estimation, and planning** — not silent execution.

---

## ✨ Features

* 🖥 GUI (Tkinter)
* 📂 PDF file picker
* 🔍 PDF encryption preview (read-only)
* 📋 Profile-based configurations
* 🧮 Time & complexity estimation
* 📊 Progress simulation (educational)
* 🧠 Command planning (preview only)
* 📤 Export plan to JSON
* 🐳 Dockerized (Windows-friendly)

---

## 🧠 What this tool does (and does NOT)

### ✅ It does

* Inspect PDF encryption metadata
* Estimate password search complexity
* Build **transparent command plans**
* Teach why recovery takes time

### ❌ It does NOT

* Automatically crack passwords
* Run recovery tools silently
* Bypass security without user intent

This makes it suitable for:

* Learning
* Audits
* Forensic planning
* Recovery of files **you own**

---

## 📁 Project Structure

```
pdf-recovery-framework/
│
├── Dockerfile
├── run.bat
├── README.md
│
├── app/
│   ├── main.py
│   ├── config.py
│   ├── profiles.py
│   ├── estimator.py
│   ├── planner.py
│   ├── executor.py
│   ├── hash_preview.py
│   └── progress.py
│
└── config/
    ├── defaults.conf
    └── profiles.json
```

---

## ⚙️ Profiles

Profiles define expected password structure.

Example (`config/profiles.json`):

```json
{
  "bank_bill": {
    "tool": "hashcat",
    "attack": "mask",
    "letters": 4,
    "digits": 4
  }
}
```

Profiles can be:

* Selected from the GUI
* Edited or added via **Profile Editor**

---

## ▶️ How to Run (Windows)

### Prerequisites

* Docker Desktop installed
* Docker running

### Steps

1. Clone or extract this repository
2. Double-click `run.bat`
3. Docker builds the image (first run may take a few minutes)
4. GUI window opens

### Typical Workflow

1. Pick a PDF
2. Preview PDF encryption
3. Choose or edit a profile
4. Build plan
5. Simulate progress
6. Export plan to JSON

---

## 🔐 Safety Model

* Execution is **disabled by default**
* Commands are **shown, not run**
* Everything is explicit and inspectable

This is intentional and by design.

---

## 🛣 Roadmap

* Real PDF metadata parsing
* Estimated time countdown (instead of simulation)
* Web-based GUI (FastAPI + React)
* Plugin support for additional tools
* Optional lab/test execution mode

---

## 📜 License

Educational / research use only.
Use responsibly and **only on files you own**.

---

## ✅ Quick Run Summary

1️⃣ Install **Docker Desktop**
2️⃣ Place all files in `pdf-recovery-framework/`
3️⃣ Double-click **`run.bat`**
4️⃣ Use the GUI 🎉

---

This version fixes:

* ✅ Proper fenced code blocks
* ✅ All headings display correctly
* ✅ Lists render properly
* ✅ Workflow & safety notes clearly separated

---