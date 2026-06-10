/** Basic calculator class that can add, subtract, multiply, and divide. */
public class Calculator {
    /** Used to demonstrate all functionality. */
    public static void main(String [] args) {
        System.out.println("3 + 2 = " +  add(3, 2));
        System.out.println("4 + 5 + 6 = " + add(4,5,6));
        System.out.println("9 * 8 = " + multiply(9,8));
        System.out.println("10 / 2 = " + divide(10, 2));
        System.out.println("9 / 0 = " + divide(9, 0));
    }

    /** Adds and returns the sum of two doubles. */
    public static double add(double x, double y) {
        return x + y;
    }

    /** Adds and returns the sum of three doubles. */
    public static double add(double x, double y, double z) {
        return x + y + z;
    }

    /** Subtracts and returns the difference of two doubles. */
    public static double subtract(double x, double y) {
        return x - y;
    }

    /** Multiplies and returns the product of two doubles. */
    public static double multiply(double x, double y) {
        return x * y;
    }

    /** Divides and returns the quotient of two doubles. Returns zero and warns the user if division by zero is attempted. */
    public static double divide(double x, double y) {
        if (y == 0) {
            System.out.println("Error: Cannot divide by zero. Returning 0...");
            return 0;
        } else {
            return x / y;
        }
    }
}
