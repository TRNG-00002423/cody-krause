/**
 * Pair exercise — build sorted array, pick target, time both searches.
 */

import java.util.Scanner;

public class SearchBenchmark {

    public static void main(String[] args) {
        System.out.println("Implement benchmark");

        Scanner sc = new Scanner(System.in);
        System.out.print("How large of an array? : ");
        int n = sc.nextInt();

        int[] arr = buildSortedEvens(n);

        System.out.print("Target value (between 0 and " + (n - 1) * 2 + "): ");
        int target = sc.nextInt();

        System.out.println("Benchmarking linear search now...");
        long start = System.nanoTime();
        int index = SearchLib.linearSearch(arr, target);
        long stop = System.nanoTime();

        long difference = stop - start;
        System.out.println("Linear Search Time: " + difference);

        System.out.println("Benchmarking binary search now...");
        start = System.nanoTime();
        index = SearchLib.binarySearch(arr, target);
        stop = System.nanoTime();

        difference = stop - start;
        System.out.println("Binary Search Time: " + difference);
    }

    static int[] buildSortedEvens(int n) {
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = i * 2;
        }
        return arr;
    }
}
