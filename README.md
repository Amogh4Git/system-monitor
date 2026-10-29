# Local System Resource Monitor & Health Classifier

A lightweight Python application that monitors local CPU, RAM, disk usage, and I/O metrics in real time. It evaluates resource readings against configurable thresholds, classifies system health (NORMAL, WARNING, CRITICAL), presents a live terminal dashboard, and logs measurements to CSV.

Developed as a System Programming group project.

---

## Directory Structure
```
system-monitor/
├── main.py                  # Main execution loop and orchestrator
├── config.py                # Configuration and threshold definitions
├── requirements.txt         # External dependencies (psutil)
├── README.md                # Project documentation
├── .gitignore               # Git ignore pattern rules
├── src/                     # Core application source modules
│   ├── metrics/             # Resource metrics collection modules
│   ├── health/              # Threshold evaluation and classification
│   ├── ui/                  # Live terminal dashboard rendering
│   └── logging_utils/       # CSV timestamped data logger
├── tests/                   # Module unit tests
└── logs/                    # Output directory for system_health.csv
```

## 👥 Team Work Breakdown Structure

| Person | Role & Module | Primary Deliverable |
|---|---|---|
| **Person 1** | Integration & Architecture Lead | `main.py`, Git Repo, Architecture |
| **Person 2** | CPU Metrics Specialist | `src/metrics/cpu_metrics.py` |
| **Person 3** | RAM Metrics Specialist | `src/metrics/ram_metrics.py` |
| **Person 4** | Disk & I/O Specialist | `src/metrics/io_metrics.py` |
| **Person 5** | State Classification Engineer | `src/health/classifier.py` |
| **Person 6** | UI & Logging Designer | `src/ui/dashboard.py`, `src/logging_utils/csv_logger.py` |

---

## 🚀 Quickstart Guide

### A. Clone the Repository (FOR FIRST TIME USE ONLY)
Replace `<YOUR-USERNAME>`, `<FEATURE>`, `<FOLDER>` with your own values.

**1. Fork** the repository on GitHub (click **Fork**).

**2. Clone** your fork:
```bash
git clone https://github.com/<YOUR-USERNAME>/system-monitor.git
cd system-monitor
```
### B. Test the Project

**1. Set Up Virtual Environment**
```bash
#Type in VS Code terminal while in ".../system-monitor/" directory

# Create environment
python -m venv venv

# Activate (for Windows Command Prompt)
venv\Scripts\activate

# Activate (for macOS / Linux)
source venv/bin/activate
```
**2. Install Dependencies**
```bash
pip install -r requirements.txt
```

**3. Run the Application**
```bash
python main.py
```

### C. Add your new feature 
**1. Sync with latest features:**
```bash
git checkout main
git pull origin main
```

**2. Create a new branch:**
```bash
git checkout -b feature/<FEATURE>
```

**3. Add only your folder:**
```bash
git add <FOLDER>
```
❌ Never use `git add .`

**4. Commit and push:**
```bash
git commit -m "feat: Added feature by <YOUR-USERNAME>"
git push -u origin feature/<FEATURE>
```

**5. Open a Pull Request** from your branch to the `main` branch of the original repo. Click Compare & pull request on the banner that appears. Select main as the base branch and feature/cpu-metrics as the compare branch. Assign Amogh4Git as a reviewer and submit the PR.
