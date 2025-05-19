

from itertools import combinations
from pysat.formula import CNF

from utils.cnf import get_id, neighbors

def exactly_k(vars_list: list[int], k: int) -> list[tuple]:
  cnf = []
  # At least k (one of these must be True)
  if k > 0:
    for combo in combinations(vars_list, len(vars_list) - k + 1):
      cnf.append(sorted(list(combo)))

  # At most k (no k+1 can be True together)
  for combo in combinations(vars_list, k + 1):
    cnf.append(sorted([-v for v in combo]))

  return cnf

def gen_cnf(grid: list[list[any]]) -> CNF:
  rows, cols = len(grid), len(grid[0])
  clause_set = set()

  for i in range(rows):
    for j in range(cols):
      val = grid[i][j]
      if val == '_':
        continue
      
      surrounding_cells = neighbors(i, j, rows, cols)
      vars = [get_id(x, y, cols) for (x, y) in surrounding_cells]

      cnf_list = exactly_k(vars, val)
      for clause in cnf_list:
        clause_set.add(tuple(clause))

  cnf = CNF()
  for clause in clause_set:
    cnf.append(list(clause))
  return cnf