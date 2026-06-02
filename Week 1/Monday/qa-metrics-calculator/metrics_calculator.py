"""
QA Test Metrics Calculator
"""

def main():
    print("═" * 40)
    print("  QA Test Metrics Calculator")
    print("═" * 40)

    total_tests = int(input("Enter total test cases: "))
    passed_tests = int(input("Enter passed tests: "))
    total_time = float(input("Enter total execution time (seconds): "))


    failed_tests = total_tests - passed_tests
    pass_rate = (passed_tests / total_tests) * 100 if total_tests > 0 else 0
    fail_rate = 100 - pass_rate
    avg_time = total_time / total_tests if total_tests > 0 else 0


    print("\n" + "-" * 40)
    print("  Results Summary")
    print("-" * 40)
    print(f"{'Total Tests:':<20}{total_tests}")
    print(f"{'Passed:':<20}{passed_tests}")
    print(f"{'Failed:':<20}{failed_tests}")
    print(f"{'Pass Rate:':<20}{pass_rate:.1f}%")
    print(f"{'Fail Rate:':<20}{fail_rate:.1f}%")
    print(f"{'Avg Time/Test:':<20}{avg_time:.2f}s")
    print(f"{'Total Time:':<20}{total_time:.2f}s")


    if pass_rate >= 95:
        verdict = "RELEASE APPROVED"
    elif pass_rate >= 80:
        verdict = "CONDITIONAL RELEASE"
    else:
        verdict = "RELEASE BLOCKED"
        
    print(f"\nVerdict: {verdict}")


if __name__ == "__main__":
    main()