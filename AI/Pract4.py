def solve_n_queens(n):
    board = [-1] * n

    def is_safe(row, col):
        for i in range(row):
            # Check column and diagonal conflicts
            if board[i] == col or abs(board[i] - col) == row - i:
                return False
        return True

    def solve(row):
        if row == n:
            print("Solution:", board)
            return
        
        for col in range(n):
            if is_safe(row, col):
                board[row] = col
                solve(row + 1)
                board[row] = -1  # Backtrack

    solve(0)


# -------- Multiple Test Cases --------
test_values = [4, 5, 6]

for n in test_values:
    print(f"\nSolving {n}-Queens Problem:")
    solve_n_queens(n)
    print("-" * 40)