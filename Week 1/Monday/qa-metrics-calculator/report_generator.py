from dataclasses import dataclass

@dataclass
class Test:
    name: str
    duration: int
    status: bool

tests = [
    Test("test_login", 1200, True),
    Test("test_search", 850, True),
    Test("test_checkout", 2300, False),
    Test("test_profile", 450, True),
    Test("test_logout", 180, True)
]

print("-" * 47)
print(f"| {'Test Name':<15} | {'Duration':>12} | {'Status':<10} |")
print("-" * 47)

for test in tests:
    print(f"| {test.name:<15} | {test.duration:>9} ms | {"PASS" if test.status else "FAIL":<10} |")

print("-" * 47)
print(f"| {'TOTAL':<15} | {sum(t.duration for t in tests):>9} ms | {sum(1 for t in tests if t.status)}/{len(tests)} Pass   |")
print("-" * 47)