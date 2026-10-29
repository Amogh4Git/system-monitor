"""
tests/test_config.py - Unit tests for configuration and threshold validation.
"""

import unittest
import config


class TestConfigThresholds(unittest.TestCase):
    """Test suite to validate system health thresholds defined in config.py."""

    def test_sampling_interval_positive(self):
        """Verify sampling interval is a positive non-zero number."""
        self.assertIsInstance(config.SAMPLING_INTERVAL_SECONDS, (int, float))
        self.assertGreater(
            config.SAMPLING_INTERVAL_SECONDS,
            0,
            "Sampling interval must be greater than 0 seconds.",
        )

    def test_threshold_structure_keys(self):
        """Verify threshold dictionaries contain required 'warning' and 'critical' keys."""
        for name, threshold_dict in [
            ("CPU", config.CPU_THRESHOLDS),
            ("RAM", config.RAM_THRESHOLDS),
            ("DISK", config.DISK_THRESHOLDS),
        ]:
            with self.subTest(metric=name):
                self.assertIn("warning", threshold_dict)
                self.assertIn("critical", threshold_dict)

    def test_threshold_percentage_ranges(self):
        """Verify all threshold percentage values fall within 0.0 and 100.0."""
        all_thresholds = [
            config.CPU_THRESHOLDS,
            config.RAM_THRESHOLDS,
            config.DISK_THRESHOLDS,
        ]

        for threshold_dict in all_thresholds:
            for key, value in threshold_dict.items():
                self.assertIsInstance(value, (int, float))
                self.assertGreaterEqual(
                    value, 0.0, f"Threshold {key} cannot be negative."
                )
                self.assertLessEqual(
                    value, 100.0, f"Threshold {key} cannot exceed 100%."
                )

    def test_warning_less_than_critical(self):
        """Verify warning threshold is strictly less than critical threshold."""
        metrics = {
            "CPU": config.CPU_THRESHOLDS,
            "RAM": config.RAM_THRESHOLDS,
            "DISK": config.DISK_THRESHOLDS,
        }

        for metric_name, thresholds in metrics.items():
            with self.subTest(metric=metric_name):
                self.assertLess(
                    thresholds["warning"],
                    thresholds["critical"],
                    f"{metric_name} warning threshold must be lower than critical threshold.",
                )


if __name__ == "__main__":
    unittest.main()
