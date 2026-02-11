# PDF Recovery Web Framework

A **web-based, configurable framework** for planning PDF password recovery tasks  
in a **safe, transparent, and educational** way.

This project focuses on **inspection, estimation, and planning** — not silent execution.

---

## ✨ Features

- 🌐 Browser GUI (FastAPI + simple frontend)
- 📂 PDF file picker & upload
- 🔍 PDF hash/metadata preview (read-only)
- 📋 Profile-based configurations
- 🧮 Time & complexity estimation
- 📊 Progress simulation (educational)
- 🧠 Command planning (preview only)
- 📤 Export plan to JSON
- 🐳 Fully Dockerized (cross-platform)

---

## 🧠 What this tool does (and does NOT)

### ✅ It does
- Inspect PDF encryption metadata
- Estimate password search complexity
- Build **transparent command plans**
- Teach why recovery takes time

### ❌ It does NOT
- Automatically crack passwords
- Run recovery tools silently
- Bypass security without user intent

Suitable for:
- Learning
- Audits
- Forensic planning
- Recovery of files **you own**

---

## 📁 Project Structure

pdf-recovery-framework/
│
├── Dockerfile
├── run.bat
├── README.md
│
├── app/
│ ├── main.py
│ ├── config.py
│ ├── profiles.py
│ ├── estimator.py
│ ├── planner.py
│ ├── hash_preview.py
│ └── progress.py
│
├── frontend/
│ ├── index.html
│ ├── script.js
│ └── style.css
│
└── config/
  ├── defaults.conf
  └── profiles.json

---

## ⚙️ Profiles

Profiles define expected password structure.

Example (`config/profiles.json`):

```json
{
  "bank_bill": { "tool": "hashcat", "attack": "mask", "letters": 4, "digits": 4 },
  "statement": { "tool": "hashcat", "attack": "mask", "letters": 6, "digits": 2 },
  "custom": { "tool": "pdfrip", "attack": "mask", "letters": 4, "digits": 4 }
}
````

Profiles can be:

* Selected from the browser GUI (dropdown populated dynamically)
* Edited or added via `profiles.json`

---

## 🛠 How to Run

1. Install **Docker Desktop**
2. Clone repository:

```bat
git clone <repo_url> pdf-recovery-web
cd pdf-recovery-web
```

3. Double-click **`run.bat`**

   * Builds Docker image
   * Runs container on port 8000

4. Open browser:

```
http://localhost:8000
```

5. Workflow:

* Upload a PDF
* Select a profile → Build plan
* Preview plan, hash, estimated time
* Watch progress simulation
* Export plan to JSON

---

## 🔐 Safety Model

* Execution is disabled by default
* Commands are **shown, not run**
* Everything is transparent and inspectable
* Educational & audit-friendly

---

## 🛣 Roadmap

* React frontend for better UX
* Real PDF metadata parsing
* Countdown timer instead of simulation
* Plugin support for additional tools
* Optional lab/test execution mode

---

## 📜 License

* Educational / research use only
* Use responsibly and only on files you own
