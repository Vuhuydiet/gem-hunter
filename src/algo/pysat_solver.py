from pysat.formula import CNF
from pysat.solvers import Minisat22

def solve(cnf: CNF, grid: list[list[int]]) -> list[int]:
  solver = Minisat22()
  solver.append_formula(cnf.clauses)

  if not solver.solve():
    solver.delete()
    raise Exception("No solution found")
  
  model = solver.get_model()
  solver.delete()

  return model