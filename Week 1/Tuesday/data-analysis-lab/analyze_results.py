#The pandas library has 3 dependencies for other libraries: numpy, python-dateutil, and tzdata.

import pandas as pd
import numpy as np

df = pd.read_csv('test_data.csv')

print("=" * 40)
print("    Test Results Analysis")
print("=" * 40)

# First five rows
print("\nFirst 5 Tests:")
print(df.head())


# Total tests
print(f"\n{'Total Tests:':<20} {len(df)}")

pass_rate = df['status'].value_counts(normalize=True)['pass']
print(f"{'Pass Rate:':<20} {pass_rate:.1%}")

mean_duration = np.ceil(df['duration_ms'].mean())
print(f"{'Avg Duration:':<20} {mean_duration:,.0f} ms ({mean_duration/1000:.2f}s)")

slowest_test = df.loc[df['duration_ms'].idxmax()]
print(f"{'Slowest:':<20} {slowest_test['test_name']} ({slowest_test['duration_ms']} ms)")

fastest_test = df.loc[df['duration_ms'].idxmin()]
print(f"{'Fastest:':<20} {fastest_test['test_name']} ({fastest_test['duration_ms']} ms)")


# By Module
print("\n--- By Module ---")
print(f"{'Module':<20} {'Tests':<10} {'Pass Rate':<15} {'Avg Duration (ms)':<20}")
for module in df['module'].unique():
    module_df = df[df['module'] == module]
    module_pass_rate = module_df['status'].value_counts(normalize=True).get('pass', 0)
    module_mean_duration = np.ceil(module_df['duration_ms'].mean())
    print(f"{module:<20} {len(module_df):<10} {module_pass_rate:<15.1%} {module_mean_duration:,.0f}ms")


# Failed tests
print("\n--- Failed Tests ---")
failed_tests = df[df['status'] == 'fail']
for _, test in failed_tests.iterrows():
    print(f"{test['test_name']:<20} {test['module']:<10} ({test['duration_ms']} ms)")
    
    
# Adding a computed column
df['duration_sec'] = df['duration_ms'] / 1000


# Sorted and exported
df = df.sort_values(by='duration_ms', ascending=False)
df.to_csv('output/results_sorted.csv', index=False)