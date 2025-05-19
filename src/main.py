import random
import time
from utils.cnf_generator import gen_cnf
from utils.file import input_grid, output_result, display
from utils.cnf import get_id
from algo import pysat_solver, bruteforce, backtracking

algos = [pysat_solver.solve, bruteforce.solve, backtracking.solve]

def main():
  test = (input("Choose input test case (1, 2, 3): "))
  input_file = f"testcases/input_{test}.txt"
  output_file = f"testcases/output_{test}.txt"
  print(f"Input file: {input_file}")
  print(f"Output file: {output_file}")
  print()
  
  grid = input_grid(input_file)
  cnf = gen_cnf(grid)
  vars = [get_id(i, j, len(grid[0])) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == '_']

  models = []
  for algorithm in algos:
    print(f"Running algorithm: {algorithm.__module__}")
    start_time = time.time()

    model = sorted(algorithm(cnf, grid), key=lambda x: abs(x))
    # print(f"Model: {model}")
  
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Algorithm: {algorithm.__module__}, Time taken: {elapsed_time:.4f} seconds")
    print()
    
    model = [x for x in model if x in vars]
    models.append(model)
  
  if models[1] != models[0] or models[2] != models[0]:
    print("Warning: Different models found!")
    print(f"PySAT model: {models[0]}")
    print(f"Brute force model: {models[1]}")
    print(f"Backtracking model: {models[2]}")
  
  rows, cols = len(grid), len(grid[0])
  result = [row[:] for row in grid]
  _s = [(i, j) for i in range(rows) for j in range(cols) if grid[i][j] == '_']
  for (i, j) in _s:
    v = get_id(i, j, cols)
    result[i][j] = 'T' if v in models[0] else 'G'
  
  print("Result:")
  display(result)
  output_result(output_file, result)

if __name__ == "__main__":
  main()