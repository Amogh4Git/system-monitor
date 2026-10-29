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
```bash
git clone [https://github.com/YOUR-USERNAME/system-monitor.git](https://github.com/YOUR-USERNAME/system-monitor.git)
cd system-monitor
