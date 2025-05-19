from pysat.formula import CNF
from itertools import product

from utils.cnf import is_valid
from utils.cnf import get_id

def solve(cnf: CNF, grid: list[list[int]]) -> list[int]:
  rows, cols = len(grid), len(grid[0])
  empty_cells_ids = [get_id(i, j, cols) for i in range(rows) for j in range(cols) if grid[i][j] == '_']
  
  for assignment in product([True, False], repeat=len(empty_cells_ids)):
    model = [empty_cells_ids[i] if val else -empty_cells_ids[i] for i, val in enumerate(assignment)]
    if is_valid(model, cnf):
      return model
  
  raise Exception("No solution found")