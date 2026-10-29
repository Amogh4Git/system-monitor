"""
main.py - Application Orchestrator & Monitoring Loop
Lead Developer: Person 1 (Integration Lead)
"""

import time
import sys

# Configuration settings
SAMPLING_INTERVAL = 2  # Sampling delay in seconds


def mock_get_cpu_metrics():
    """Temporary mock for Person 2's module until integration."""
    return {
        "cpu_percent": 18.5,
        "per_core_percent": [15.0, 22.0],
        "cpu_count": 2,
        "frequency_mhz": 2100.0,
    }


def mock_get_ram_metrics():
    """Temporary mock for Person 3's module until integration."""
    return {
        "total_bytes": 8589934592,
        "available_bytes": 4294967296,
        "used_bytes": 4294967296,
        "percent": 50.0,
    }


def mock_get_io_metrics():
    """Temporary mock for Person 4's module until integration."""
    return {
        "partitions": [],
        "primary_disk_percent": 40.0,
        "bytes_read": 102400,
        "bytes_written": 204800,
        "read_count": 100,
        "write_count": 150,
    }


def mock_evaluate_health(cpu, ram, io):
    """Temporary mock for Person 5's module until integration."""
    return {
        "state": "NORMAL",
        "reasons": ["All parameters within acceptable thresholds."],
    }


def mock_render_dashboard(cpu, ram, io, health):
    """Temporary mock for Person 6's dashboard module."""
    print("=" * 45)
    print(f" SYSTEM HEALTH MONITOR | Status: [{health['state']}]")
    print("=" * 45)
    print(f" CPU Usage: {cpu['cpu_percent']}% ({cpu['cpu_count']} cores)")
    print(f" RAM Usage: {ram['percent']}% ({ram['used_bytes'] // (1024**2)} MB used)")
    print(f" Disk Usage: {io['primary_disk_percent']}%")
    if health["reasons"]:
        print(f" Notes: {', '.join(health['reasons'])}")
    print("=" * 45)


def mock_log_to_csv(cpu, ram, io, health):
    """Temporary mock for Person 6's CSV logger module."""
    # TODO: Person 6 will implement writing timestamped rows to CSV
    pass


def main():
    """Main execution loop for system resource monitoring."""
    print("Starting System Resource Monitor...")
    print(f"Sampling every {SAMPLING_INTERVAL} seconds. Press Ctrl+C to stop.\n")

    # TODO: Replace mock functions with real imports once team members complete their modules:
    # from src.metrics.cpu_metrics import get_cpu_metrics
    # from src.metrics.ram_metrics import get_ram_metrics
    # from src.metrics.io_metrics import get_io_metrics
    # from src.health.classifier import evaluate_health
    # from src.ui.dashboard import render_dashboard
    # from src.logging_utils.csv_logger import log_to_csv

    try:
        while True:
            # 1. Collect Metrics
            cpu_data = mock_get_cpu_metrics()
            ram_data = mock_get_ram_metrics()
            io_data = mock_get_io_metrics()

            # 2. Evaluate Health State
            health_data = mock_evaluate_health(cpu_data, ram_data, io_data)

            # 3. Output to Terminal Dashboard
            mock_render_dashboard(cpu_data, ram_data, io_data, health_data)

            # 4. Log to CSV File
            mock_log_to_csv(cpu_data, ram_data, io_data, health_data)

            # 5. Wait for the next sampling cycle
            time.sleep(SAMPLING_INTERVAL)

    except KeyboardInterrupt:
        print("\n[INFO] Monitoring process stopped cleanly by user (Ctrl+C). Exiting.")
        sys.exit(0)
    except Exception as e:
        print(f"\n[ERROR] An unexpected error occurred during monitoring: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
