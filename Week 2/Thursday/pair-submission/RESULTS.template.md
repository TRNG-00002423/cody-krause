# Linear vs binary — results (rename to RESULTS.md)

## Contributors
- Driver / Navigator Round 1:
- Driver / Navigator Round 2:

## Round 1 (N = 2000)

| Algorithm | Time (nanos) | Notes |
|-----------|-----------|-------|
| Linear | 964700 | slower |
| Binary | 6200 | faster |

## Round 2 (N = 30000)

| Algorithm | Time (nanos) | Notes |
|-----------|-----------|-------|
| Linear | 3149300 | slower |
| Binary | 5900 | faster |

## Big-O discussion
logarithmic searches are significantly faster than linear searches. The O(log(n)) nature of 
the binary search makes it much better suited for larger datasets than its linear search counterpart with
an O(n) nature. However, both are fairly quick for the small datasets.

## Caveats (JVM, cache, warmup)
The linear search may have been slowed down marginally by startup or initializing of the start/stop variables. This
does not change the fact that the linear search is slower, it just may not be as slow as demonstrated. 