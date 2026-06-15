import java.util.Arrays;

/**
 * Lab 1 — Arrays & loops. Implement the bodies.
 * See ../README.md
 */
public class ArrayLoopsLab {

    /** Reverse array in place. */
    public static void reverse(int[] data) {
        int low = 0;
        int hi = data.length-1;

        while (low < hi) {
            int temp = data[low];
            data[low] = data[hi];
            data[hi] = temp;

            low++;
            hi--;
        }
    }

    /** Smallest element; illegal if null or empty. */
    public static int min(int[] data) {
        if (data == null || data.length <= 0) {
            throw new IllegalArgumentException("int[] is either null or empty");
        }

        int smallestIndex = -1;
        int smallestValue = Integer.MAX_VALUE;
        for(int i = 0; i < data.length; i++) {
            if (data[i] < smallestValue) {
                smallestValue = data[i];
                smallestIndex = i;
            }
        }

        return smallestIndex;
    }

    /** Largest element; illegal if null or empty. */
    public static int max(int[] data) {
        if (data == null || data.length <= 0) {
            throw new IllegalArgumentException("int[] is either null or empty");
        }

        int largestIndex = -1;
        int largestValue = Integer.MIN_VALUE;
        for(int i = 0; i < data.length; i++) {
            if (data[i] > largestValue) {
                largestValue = data[i];
                largestIndex = i;
            }
        }

        return largestIndex;
    }

    /** In-place ascending sort using nested loops only (no Arrays.sort). */
    public static void sortAscending(int[] data) {
        for(int i = 0; i < data.length; i++) {
            int minIndex = min(Arrays.copyOfRange(data, i, data.length)) + i;
            if(minIndex != i) {
                int temp = data[i];
                data[i] = data[minIndex];
                data[minIndex] = temp;
            }
        }
    }

    public static void main(String[] args) {
        int[] data = {23,63,53,92,21,34,22,54,19,67,42,25,99,12,8,3,17,60};

        System.out.println("Before Reverse\n------------");
        displayData(data);
        System.out.println("\nAfter Reverse\n------------");
        reverse(data);
        displayData(data);

        int[] data2 = {54,72,78,35,11,73,52,98,57,66,48,22,1,6,98,43,21,64};

        System.out.println("\nBefore Sort\n------------");
        displayData(data2);
        System.out.println("\nAfter Sort\n------------");
        sortAscending(data2);
        displayData(data2);
    }

    private static void displayData(int[] data) {
        System.out.print("Data: ");
        for(int i = 0; i < data.length-1; i++) {
            System.out.print(data[i] + ", ");
        }
        System.out.println(data[data.length-1]);
    }
}
