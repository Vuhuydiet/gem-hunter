import random
from file import display
from cnf import neighbors

T = int(input("The number of traps: "))
G = int(input("The number of golds: "))

rows = int(input("The number of rows: "))
cols = int(input("The number of columns: "))

cells = [(i, j) for i in range(rows) for j in range(cols)]
random.shuffle(cells)

grid = [['_' for _ in range(cols)] for _ in range(rows)]
for i in range(T):
  x, y = cells[i]
  grid[x][y] = 'T'
for i in range(T, T + G):
  x, y = cells[i]
  grid[x][y] = 'G'
  
print("Trap and gold positions:")
display(grid)

for i in range(rows):
  for j in range(cols):
    if grid[i][j] == '_':
      surrounding_cells = neighbors(i, j, rows, cols)
      trap_count = sum(1 for (x, y) in surrounding_cells if grid[x][y] == 'T')
      grid[i][j] = trap_count

for i in range(rows):
  for j in range(cols):
    if grid[i][j] == 'G' or grid[i][j] == 'T':
      grid[i][j] = '_'
      
print("Final grid:")
display(grid)