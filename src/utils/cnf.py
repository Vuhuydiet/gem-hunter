

def get_id(i: int, j: int, cols: int):
  return i * cols + j + 1

def neighbors(i, j, rows, cols):
  neighbors = []
  for dx in [-1, 0, 1]:
    for dy in [-1, 0, 1]:
      if dx == 0 and dy == 0:
        continue
      ni, nj = i + dx, j + dy
      if 0 <= ni < rows and 0 <= nj < cols:
        neighbors.append((ni, nj))
  return neighbors

def is_valid(model, cnf):
  for clause in cnf:
    if not any(lit in model for lit in clause):
      return False
  return True
