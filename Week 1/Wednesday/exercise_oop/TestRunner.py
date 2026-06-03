from TestSuite import TestSuite
from TestResult import TestResult
import time
import random

class TestRunner:
    """Executes a TestSuite and collects results.

    Methods:
        run(suite): Run all tests in a suite, return list of TestResult
        summary(results): Print a formatted summary
    """
    # TODO: Implement

    @staticmethod
    def run(suite : TestSuite):
        """Run each test in the suite and return a list of TestResults."""
        
        results = []
        for test in suite.tests:
            start = time.time()
            passed = test.run()
            duration = (time.time() - start) * 1000
            # Simulate varying duration
            duration += random.uniform(50, 500)
            result = TestResult(
                test.name,
                "pass" if passed else "fail",
                round(duration, 1),
                None if passed else f"{test.name} assertion failed"
            )
            results.append(result)
        return results
    
    @staticmethod
    def summary(results : list[TestResult]):
        print("=" * 40)
        print("   Test Summary")
        print("=" * 40)
        
        for result in results:
            print(result.summary())
        
        