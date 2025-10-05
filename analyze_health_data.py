#!/usr/bin/env python3
"""
Health Sensor Data Analysis Script

Complete the TODO sections to analyze health sensor data using NumPy.
This script demonstrates basic NumPy operations for data loading, statistics,
filtering, and report generation.
"""

import numpy as np


def load_data(filename):
    """Load CSV data using NumPy.
    
    Args:
        filename: Path to CSV file
        
    Returns:
        NumPy structured array with all columns
    """
    # This code is provided because np.genfromtxt() is not covered in the lecture
    dtype = [('patient_id', 'U10'), ('timestamp', 'U20'), 
             ('heart_rate', 'i4'), ('blood_pressure_systolic', 'i4'),
             ('blood_pressure_diastolic', 'i4'), ('temperature', 'f4'),
             ('glucose_level', 'i4'), ('sensor_id', 'U10')]
    
    data = np.genfromtxt(filename, delimiter=',', dtype=dtype, skip_header=1)
    return data


def calculate_statistics(data):
    """Calculate basic statistics for numeric columns.
    
    Args:
        data: NumPy structured array
        
    Returns:
        Dictionary with statistics
    """
    # Handle empty input
    if data.size == 0:
        return {'avg_heart_rate': 0.0, 'avg_systolic_bp': 0.0, 'avg_glucose': 0.0}

    # Use NumPy's mean on the structured array fields
    avg_heart_rate = float(np.mean(data['heart_rate']))
    avg_systolic_bp = float(np.mean(data['blood_pressure_systolic']))
    avg_glucose = float(np.mean(data['glucose_level']))

    return {
        'avg_heart_rate': avg_heart_rate,
        'avg_systolic_bp': avg_systolic_bp,
        'avg_glucose': avg_glucose,
    }


def find_abnormal_readings(data):
    """Find readings with abnormal values.
    
    Args:
        data: NumPy structured array
        
    Returns:
        Dictionary with counts
    """
    # Handle empty input
    if data.size == 0:
        return {'high_heart_rate': 0, 'high_blood_pressure': 0, 'high_glucose': 0}

    high_hr_count = int((data['heart_rate'] > 90).sum())
    high_bp_count = int((data['blood_pressure_systolic'] > 130).sum())
    high_glucose_count = int((data['glucose_level'] > 110).sum())

    return {
        'high_heart_rate': high_hr_count,
        'high_blood_pressure': high_bp_count,
        'high_glucose': high_glucose_count,
    }


def generate_report(stats, abnormal, total_readings):
    """Generate formatted analysis report.
    
    Args:
        stats: Dictionary of statistics
        abnormal: Dictionary of abnormal counts
        total_readings: Total number of readings
        
    Returns:
        Formatted string report
    """
    lines = []
    lines.append("Health Sensor Data Analysis Report")
    lines.append("=" * 40)
    lines.append(f"Total readings: {total_readings}")
    lines.append("")
    lines.append("Averages:")
    lines.append(f"  - Heart Rate (avg): {stats['avg_heart_rate']:.1f} bpm")
    lines.append(f"  - Systolic BP (avg): {stats['avg_systolic_bp']:.1f} mmHg")
    lines.append(f"  - Glucose (avg): {stats['avg_glucose']:.1f} mg/dL")
    lines.append("")
    lines.append("Abnormal reading counts:")
    lines.append(f"  - High heart rate (>90): {abnormal['high_heart_rate']}")
    lines.append(f"  - High systolic BP (>130): {abnormal['high_blood_pressure']}")
    lines.append(f"  - High glucose (>110): {abnormal['high_glucose']}")
    lines.append("=" * 40)

    return "\n".join(lines)


def save_report(report, filename):
    """Save report to file.
    
    Args:
        report: Report string
        filename: Output filename
    """
    # Ensure parent directory exists
    import os
    parent = os.path.dirname(filename)
    if parent and not os.path.exists(parent):
        os.makedirs(parent, exist_ok=True)

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(report)


def main():
    """Main execution function."""
    data_file = 'health_data.csv'
    out_file = 'output/analysis_report.txt'

    try:
        data = load_data(data_file)
    except Exception as e:
        print(f"Error loading data from {data_file}: {e}")
        return

    stats = calculate_statistics(data)
    abnormal = find_abnormal_readings(data)
    total = int(data.size)

    report = generate_report(stats, abnormal, total)
    save_report(report, out_file)

    print(f"Analysis complete. Report written to {out_file}")


if __name__ == "__main__":
    main()