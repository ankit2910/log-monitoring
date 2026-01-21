import json
import sys
from scripts.log_reader import read_logs
from scripts.analyzer import analyze_logs
from scripts.reporter import generate_report

SERVICES = {
    "application": "logs/app.log",
    "database": "logs/db.log",
    "auth": "logs/auth.log"
}

with open("config/rules.json") as f:
    rules = json.load(f)

critical = False

for service, path in SERVICES.items():
    lines = read_logs(path)
    errors, warnings = analyze_logs(lines, rules)
    generate_report(service, errors, warnings)

    if errors > rules["critical_threshold"]:
        critical = True

if critical:
    print("\nCritical issues detected. Incident raised.")
    sys.exit(1)

print("\nSystem is stable. No critical incidents.")
