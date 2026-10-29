# Local System Resource Monitor & Health Classifier

A lightweight Python application that monitors local CPU, RAM, disk usage, and I/O metrics in real time. It evaluates resource readings against configurable thresholds, classifies system health (NORMAL, WARNING, CRITICAL), presents a live terminal dashboard, and logs measurements to CSV.

Developed as a System Programming group project.

---

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

### 1. Clone the Repository
Replace `<YOUR-USERNAME>`, `<FEATURE>`, `<FOLDER>` with your own values.

**1. Fork** the repository on GitHub (click **Fork**).

**2. Clone** your fork:
```bash
git clone https://github.com/<YOUR-USERNAME>/system-monitor.git
cd system-monitor
```

**3. Create your branch:**
```bash
git checkout -b feature/<FEATURE>
```

**5. Add only your folder:**
```bash
git add <FOLDER>
```
❌ Never use `git add .`

**6. Commit and push:**
```bash
git commit -m "feat: Added feature by <YOUR-USERNAME>"
git push origin feature/<FEATURE>
```

**7. Open a Pull Request** from your branch to the `main` branch of the original repo. Open the **Files changed** tab and confirm only your folder is listed.
