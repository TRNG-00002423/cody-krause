test_results = [
    {"name": "test_login", "module": "auth", "duration_ms": 1200, "status": "pass"},
    {"name": "test_register", "module": "auth", "duration_ms": 2100, "status": "pass"},
    {"name": "test_logout", "module": "auth", "duration_ms": 300, "status": "pass"},
    {"name": "test_search", "module": "search", "duration_ms": 850, "status": "fail"},
    {"name": "test_filter", "module": "search", "duration_ms": 1800, "status": "fail"},
    {"name": "test_sort", "module": "search", "duration_ms": 670, "status": "pass"},
    {"name": "test_add_cart", "module": "checkout", "duration_ms": 2300, "status": "fail"},
    {"name": "test_payment", "module": "checkout", "duration_ms": 3100, "status": "pass"},
    {"name": "test_confirm", "module": "checkout", "duration_ms": 1900, "status": "pass"},
    {"name": "test_view_profile", "module": "profile", "duration_ms": 380, "status": "pass"},
    {"name": "test_edit_profile", "module": "profile", "duration_ms": 540, "status": "pass"},
    {"name": "test_settings", "module": "profile", "duration_ms": 420, "status": "fail"},
]

# Task 1
by_duration = sorted(test_results, key=lambda r : r["duration_ms"])

by_module_name = sorted(by_duration, key=lambda r : r["module"])

by_status = sorted(by_module_name, key=lambda r : r["status"])


# Task 2
just_names = list(map(lambda r : r["name"], test_results))

all_failures = list(filter(lambda r : r["status"] == "fail", test_results))

all_slow_tests = list(filter(lambda r : r["duration_ms"] > 1500, test_results))

summary_list = list(map(lambda r : f"{r["name"]} ({r["duration_ms"]})", test_results))

unique_module_names = set(map(lambda r : r["module"], test_results))


# Task 3
from functools import reduce

total_duration_ms = reduce(lambda acc, r : acc + r["duration_ms"], test_results, 0)

total_failure_time = reduce(lambda acc, r : acc + r["duration_ms"], 
                            filter(lambda r : r["status"] == "fail", test_results), 0)

longest_test_name = reduce(lambda acc, r : r["name"] if len(r["name"]) > len(acc) else acc, test_results, "")

module_summary_dict = reduce(lambda acc, r : {**acc, r["module"]: acc.get(r["module"], 0) + 1}, test_results, {})


# Task 4
endpoints = ["/login", "/search", "/checkout", "/profile"]
expected_codes = [200, 200, 201, 200]
actual_codes = [200, 500, 201, 403]
for i, (end, exp, act) in enumerate(zip(endpoints, expected_codes, actual_codes)):
    status = "PASS" if exp == act else "FAIL"
    print(f"{status}: {end}")

names, modules, durations, statuses = zip(*test_results)

name_to_dur_dict = dict(zip(names, durations))