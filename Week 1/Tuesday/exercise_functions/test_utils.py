import re

def format_test_name(name : str):
    name = name.strip().lower()
    name = name.replace(" ", "_")
    name = "test_" + name
    return name

def is_valid_test_name(name : str):
    if not name.startswith("test_"):
        return False
    if not re.fullmatch(r"^test_[a-z0-9_]+$", name):
        return False
    if not len(name) > 5:
        return False
    return True

def create_test_result(name, status="pass", duration_ms=0, error=None):
    return {
        "name": name,
        "status": status,
        "duration_ms": duration_ms,
        "error": error
    }

def format_duration(ms : int, unit="ms"):
    if unit == "ms":
        return f"{ms:,}{unit}"
    elif unit == "s":
        return f"{ms/1000:,.2f}{unit}"
    elif unit == "min":
        return f"{ms/60000:,.2f}{unit}"
    else:
        raise ValueError("Unsupported unit")

def calculate_stats(*scores):
    if not scores:
        raise ValueError("At least one score is required")
    average = sum(scores) / len(scores)
    minimum = min(scores)
    maximum = max(scores)
    total = sum(scores)
    count = len(scores)
    return {"count": count, "total": total, "average": average, "min": minimum, "max": maximum}

def build_test_config(**settings):
    default_config = {
        "browser" : "chrome",
        "headless" : False,
        "timeout" : 30,
        "retries" : 0,
        "base_url" : "http://localhost:3000"
    }
    default_config.update(settings)
    return default_config

def analyze_results(*results):
    passed_count = sum(1 for r in results if r["status"] == "pass")
    failed_count = sum(1 for r in results if r["status"] == "fail")
    pass_rate = (passed_count / len(results)) * 100 if results else 0
    avg_duration = sum(r["duration_ms"] for r in results) / len(results) if results else 0
    return (passed_count, failed_count, pass_rate, avg_duration)

def generate_report(*results):
    summary = analyze_results(*results)
    report = f"Test Report:\nTotal: {summary[0] + summary[1]}\nPassed: {summary[0]}\nFailed: {summary[1]}\nPass Rate: {summary[2]:.2f}%\nAverage Duration: {format_duration(summary[3])}"
    return report

def run_assertions():
    # Test format_test_name and is_valid_test_name
    assert format_test_name("Valid Login") == "test_valid_login"
    assert format_test_name("  Search Results  ") == "test_search_results"
    assert is_valid_test_name("test_login") == True
    assert is_valid_test_name("login_test") == False
    assert is_valid_test_name("test_") == False
    
    
    # Test create_test_result and format_duration
    r1 = create_test_result("test_login")
    assert r1 == {"name": "test_login", "status": "pass", "duration_ms": 0, "error": None}

    r2 = create_test_result("test_checkout", status="fail", duration_ms=2300, error="Timeout")
    assert r2["status"] == "fail"
    assert r2["error"] == "Timeout"

    
    assert format_duration(1200) == "1,200ms"
    assert format_duration(1200, "s") == "1.20s"
    
    
    # Test calculate_stats and build_test_config
    stats = calculate_stats(85, 92, 78, 95, 88)
    assert stats["count"] == 5
    assert stats["average"] == 87.6
    assert stats["min"] == 78
    assert stats["max"] == 95

    config = build_test_config(headless=True, timeout=60)
    assert config["browser"] == "chrome"  # default
    assert config["headless"] == True     # overridden
    assert config["timeout"] == 60       # overridden
    
    
    # Test analyze_results and generate_report
    results = [
        create_test_result("test_login", "pass", 1200),
        create_test_result("test_search", "pass", 850),
        create_test_result("test_checkout", "fail", 2300, "Timeout"),
        create_test_result("test_profile", "pass", 450),
    ]

    passed, failed, rate, avg = analyze_results(*results)
    assert passed == 3
    assert failed == 1
    assert rate == 75.0
    
    print(generate_report(*results))

if __name__ == "__main__":
    run_assertions()