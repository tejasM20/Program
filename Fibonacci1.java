
import java.util.Scanner;

public class Fibonacci1 {

    // Non-recursive (Iterative) method
    static long fibonacciNonRecursive(int n) {
        if (n <= 1) {
            return n;
        }
        long first = 0;
        long second = 1;
        long result = 0;

        // Loop builds the sequence from the bottom up
        for (int i = 2; i <= n; i++) {
            result = first + second;
            first = second;
            second = result;
        }
        return result;
    }

    // Recursive method
    static long fibonacciRecursive(int n) {
        // Base case to stop recursion
        if (n <= 1) {
            return n;
        }
        // Top-down approach breaking into two smaller sub-problems
        return fibonacciRecursive(n - 1) + fibonacciRecursive(n - 2);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the value of n: ");
        int n = sc.nextInt();

        if (n < 0) {
            System.out.println("Please enter a non-negative number.");
        } else if (n > 40) {
            System.out.println("Please enter n between 0 and 40 for faster execution.");
        } else {
            System.out.println("\nFibonacci Series:");
            for (int i = 0; i <= n; i++) {
                System.out.print(fibonacciNonRecursive(i) + " ");
            }
            System.out.println("\n");
            System.out.println("Non-recursive Fibonacci number: " + fibonacciNonRecursive(n));
            System.out.println("Recursive Fibonacci number: " + fibonacciRecursive(n));
        }
        sc.close();
    }
}