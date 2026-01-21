# Log Monitoring & Incident Detection System

This project implements a Python-based log monitoring and incident detection system designed to
simulate how platform and reliability teams analyze logs and detect system instability
early in the delivery lifecycle.

The system is integrated with CI/CD and automatically fails the pipeline when critical error
thresholds are exceeded.

---

## Overview

Modern production systems generate logs across multiple services such as application, database,
and authentication layers. Manual log inspection is error-prone and does not scale.

This project automates log analysis by:
- Scanning logs from multiple services
- Applying configurable detection rules
- Classifying errors and warnings
- Generating a consolidated incident report
- Failing CI execution when critical conditions are met

---

## How It Works

1. Log files are read from multiple services
2. Detection rules are loaded from a configuration file
3. Logs are analyzed for errors and warnings
4. A consolidated report is generated per service
5. The pipeline fails if critical thresholds are exceeded

