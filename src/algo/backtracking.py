from pysat.formula import CNF
from utils.cnf import get_id, is_valid, neighbors

def ok_assignment(grid, model, cell_id):
  rows, cols = len(grid), len(grid[0])
  row, col = divmod(cell_id - 1, cols)
  
  assigned = [abs(x) for x in model]
  
  for neighbor in neighbors(row, col, rows, cols):
    if grid[neighbor[0]][neighbor[1]] == '_':
      continue
    expected_traps = grid[neighbor[0]][neighbor[1]]
    traps = 0
    unknowns = 0
    for sur in neighbors(neighbor[0], neighbor[1], rows, cols):
      if grid[sur[0]][sur[1]] != '_':
        continue
      if get_id(sur[0], sur[1], cols) in model:
        traps += 1
      elif get_id(sur[0], sur[1], cols) not in assigned:
        unknowns += 1
    if traps > expected_traps or traps + unknowns < expected_traps:
      return False
  return True

def backtrack(grid, cnf, model, empty_cells_ids, i):
  if i == len(empty_cells_ids):
    if is_valid(model, cnf):
      return model
    return None

  for val in [True, False]:
    new_assignment = model + [empty_cells_ids[i] if val else -empty_cells_ids[i]]
    if not ok_assignment(grid, new_assignment, empty_cells_ids[i]):
      continue
    result = backtrack(grid, cnf, new_assignment, empty_cells_ids, i + 1)
    if result:
      return result
  return None

def solve(cnf: CNF, grid: list[list[any]]) -> list[int]:
  rows, cols = len(grid), len(grid[0])

  empty_cells_ids = [get_id(i, j, cols) for i in range(rows) for j in range(cols) if grid[i][j] == '_']
  
  model = backtrack(grid, cnf, [], empty_cells_ids, 0)
  if model is None:
    raise Exception("No solution found")
  return model