"""
config.py - Shared Application Configuration & Threshold Parameters
"""

# Sampling Settings
SAMPLING_INTERVAL_SECONDS = 2  # Time delay between resource metric collections

# Health Classification Thresholds
# Rules:
# - NORMAL: All metrics < WARNING thresholds
# - WARNING: At least one metric >= WARNING threshold, but none >= CRITICAL threshold
# - CRITICAL: At least one metric >= CRITICAL threshold

CPU_THRESHOLDS = {
    "warning": 70.0,   # 70% utilization triggers warning
    "critical": 90.0   # 90% utilization triggers critical alert
}

RAM_THRESHOLDS = {
    "warning": 75.0,   # 75% memory utilization triggers warning
    "critical": 90.0   # 90% memory utilization triggers critical alert
}

DISK_THRESHOLDS = {
    "warning": 80.0,   # 80% storage capacity occupied triggers warning
    "critical": 95.0   # 95% storage capacity occupied triggers critical alert
}

# Logging Configuration
DEFAULT_LOG_FILEPATH = "logs/system_health.csv"
