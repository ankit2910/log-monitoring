def analyze_logs(lines, rules):
    error_count = 0
    warning_count = 0

    for line in lines:
        if any(k in line for k in rules["error_keywords"]):
            error_count += 1
        elif any(k in line for k in rules["warning_keywords"]):
            warning_count += 1

    return error_count, warning_count
