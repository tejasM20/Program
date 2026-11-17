import java.util.Scanner;

public class Nqueen5 {
    static int n;
    static int[][] board;

    // Check whether a queen can be safely placed at board[row][col]
    static boolean isSafe(int row, int col) {
        // Check column directly above
        for (int i = 0; i < row; i++) {
            if (board[i][col] == 1)
                return false;
        }

        // Check upper-left diagonal
        for (int i = row - 1, j = col - 1; i >= 0 && j >= 0; i--, j--) {
            if (board[i][j] == 1)
                return false;
        }

        // Check upper-right diagonal
        for (int i = row - 1, j = col + 1; i >= 0 && j < n; i--, j++) {
            if (board[i][j] == 1)
                return false;
        }

        return true;
    }

    // Backtracking method
    static boolean solve(int row) {
        // Base case: If all queens are placed, we found a valid solution
        if (row == n)
            return true;

        // Try placing the queen in all columns of the current row one by one
        for (int col = 0; col < n; col++) {
            if (isSafe(row, col)) {
                // Place the queen
                board[row][col] = 1;

                // Recursively try to place the rest of the queens
                if (solve(row + 1))
                    return true;

                // BACKTRACK: If placing the queen here leads to no solution, remove it
                board[row][col] = 0;
            }
        }
        return false;
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter number of queens: ");
        n = sc.nextInt();
        board = new int[n][n];

        // Start solving from the 0th row
        if (solve(0)) {
            System.out.println("Solution:");
            for (int i = 0; i < n; i++) {
                for (int j = 0; j < n; j++) {
                    System.out.print(board[i][j] + " ");
                }
                System.out.println();
            }
        } else {
            System.out.println("No solution exists.");
        }
        sc.close();
    }
}