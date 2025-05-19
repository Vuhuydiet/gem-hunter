def input_grid(filepath: str) -> list[list[any]]:
  grid = []
  with open(filepath) as f:
    for line in f:
      row = []
      for val in line.strip().split(','):
        val = val.strip()
        if val.isdigit():
          row.append(int(val))
        else:
          row.append(val)
      grid.append(row)
  return grid


def output_result(filepath: str, grid: list[list[any]]) -> None:
  with open(filepath, 'w') as f:
    for row in grid:
      line = ', '.join(str(cell) if cell != '_' else '_' for cell in row) + '\n'
      f.write(line)


def display(grid: list[list[any]]) -> None:
  for row in grid:
    print(', '.join(str(cell) if cell != '_' else '_' for cell in row))