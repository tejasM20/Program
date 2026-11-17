import java.util.Scanner;

public class Knapsack04 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter number of items: ");
        int n = sc.nextInt();

        int[] weight = new int[n];
        int[] value = new int[n];

        System.out.println("Enter weight and value of each item:");
        for (int i = 0; i < n; i++) {
            weight[i] = sc.nextInt();
            value[i] = sc.nextInt();
        }

        System.out.print("Enter knapsack capacity: ");
        int capacity = sc.nextInt();

        // Step 1: Create the DP table
        // Rows = number of items + 1, Columns = knapsack capacity + 1
        int[][] dp = new int[n + 1][capacity + 1];

        // Step 2: Fill the table bottom-up
        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= capacity; j++) {
                // If the current item's weight is less than or equal to the current capacity 'j'
                if (weight[i - 1] <= j) {
                    // Take the maximum of:
                    // 1. Not including the item (value from the row above)
                    // 2. Including the item (item's value + value of remaining capacity from the row above)
                    dp[i][j] = Math.max(
                            dp[i - 1][j],
                            value[i - 1] + dp[i - 1][j - weight[i - 1]]
                    );
                } else {
                    // If it's too heavy, we can't include it. Just copy the value from above.
                    dp[i][j] = dp[i - 1][j];
                }
            }
        }

        System.out.println("Maximum value = " + dp[n][capacity]);

        // Step 3: Find which specific items were selected
        int j = capacity;
        System.out.print("Selected items: ");
        for (int i = n; i > 0; i--) {
            // If the value is different from the one directly above it, it means this item was selected
            if (dp[i][j] != dp[i - 1][j]) {
                System.out.print(i + " ");
                // Subtract the item's weight from our tracking capacity
                j = j - weight[i - 1];
            }
        }
        sc.close();
    }
}