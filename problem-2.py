def numCells(grid):
  n, m = len(grid), len(grid[0])
  count = 0
  for i in range(1, n - 1):
    for j in range(1, m - 1):
      if is_dominant(grid, i, j):
        count += 1
  return count

def is_dominant(grid, i, j):
  """
  Checks if a cell is dominant.

  Args:
    grid: A 2-dimensional list of integers representing the grid.
    i: The row index of the cell.
    j: The column index of the cell.

  Returns:
    True if the cell is dominant, False otherwise.
  """

  value = grid[i][j]
  for di in range(-1, 2):
    for dj in range(-1, 2):
      if di == 0 and dj == 0:
        continue
      ni, nj = i + di, j + dj
      if 0 <= ni < len(grid) and 0 <= nj < len(grid[0]) and grid[ni][nj] >= value:
        return False
  return True

# Example usage
grid = [
  [1, 3, 7],
  [4, 5, 6],
  [7, 8, 9],
]
count = numCells(grid)
print(count)  # Output: 1