# Definición de la clase Labyrinth
class Labyrinth:
    def __init__(self, grid):
        self.grid = grid

    # Método para verificar si un movimiento es válido
    def is_valid_move(self, row, col):
        return 0 <= row < len(self.grid) and 0 <= col < len(self.grid[0]) and self.grid[row][col] != '#'

# Definición de la clase Rod
class Rod:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.is_horizontal = True
        self.is_rotated = False

    # Método para mover la varilla
    def move(self, dr, dc):
        new_row, new_col = self.row + dr, self.col + dc
        return Rod(new_row, new_col) if labyrinth.is_valid_move(new_row, new_col) else None

    # Método para verificar si la varilla puede rotar
    def can_rotate(self, labyrinth):
        if self.is_rotated:
            return False

        if all(all(labyrinth.is_valid_move(self.row + i, self.col + j) for j in range(-1, 2)) for i in range(-1, 2)):
            return True

        return False

    # Método para rotar la varilla
    def rotate(self, labyrinth):
        if not self.can_rotate(labyrinth):
            return None

        new_rod = Rod(self.row, self.col)
        new_rod.is_horizontal = not self.is_horizontal
        new_rod.is_rotated = True
        return new_rod

# Función para recorrer el laberinto usando BFS
def bfs_labyrinth(labyrinth, start_rod):
    rows, cols = len(labyrinth.grid), len(labyrinth.grid[0])
    queue = [(start_rod, 0)]
    visited = set()

    while queue:
        rod, moves_taken = queue.pop(0)
        rod_key = (rod.row, rod.col, rod.is_horizontal, rod.is_rotated)

        if rod_key in visited:
            continue

        visited.add(rod_key)

        if labyrinth.grid[rod.row][rod.col] == '#':
            continue

        if (rod.row, rod.col) == (rows - 1, cols - 1) or (rod.row, rod.col) == (rows - 2, cols - 1) or (rod.row, rod.col) == (rows - 1, cols - 2):
            return moves_taken

        moves = [(0, -1), (0, 1), (-1, 0), (1, 0),(1,1),(-1,-1),(-1,1),(1,-1)]
        for dr, dc in moves:
            new_rod = rod.move(dr, dc)
            if new_rod:
                queue.append((new_rod, moves_taken + 1))

        new_rod = rod.rotate(labyrinth)
        if new_rod:
            queue.append((new_rod, moves_taken + 1))

    return -1

# Ejemplos de representación de cuadrículas para 4 laberintos distintos
grid1 = [
    ['.', '.', '.', '.','.','.','.','.','.'],
    ['#', '.', '.', '.','#','.','.','.','.'],
    ['.', '.', '.', '.','#','.','.','.','.'],
    ['.', '#', '.', '.','.','.','.','#','.'],
    ['.', '#', '.', '.','.','.','.','#','.']
]
labyrinth = Labyrinth(grid1)
start_rod = Rod(0, 0)
print(f"Laberinto 1: {bfs_labyrinth(labyrinth, start_rod)}")

grid2 =  [
    ['.', '.', '.', '.','.','.','.','.','.'],
    ['#', '.', '.', '.','#','.','.','#','.'],
    ['.', '.', '.', '.','#','.','.','.','.'],
    ['.', '#', '.', '.','.','.','.','#','.'],
    ['.', '#', '.', '.','.','.','.','#','.']
]
labyrinth = Labyrinth(grid2)
start_rod = Rod(0, 0)
print(f"Laberinto 2: {bfs_labyrinth(labyrinth, start_rod)}")

grid3 =[
    ['.', '.', '.'],
    ['.', '.', '.'],
    ['.', '.', '.']
]
labyrinth = Labyrinth(grid3)
start_rod = Rod(0, 0)
print(f"Laberinto 3: {bfs_labyrinth(labyrinth, start_rod)}")

grid4 = [
    ['.', '.', '.', '.','.','.','.','.','.','.'],
    ['.', '#', '.', '.','.','.','#','.','.','.'],
    ['.', '#', '.', '.','.','.','.','.','.','.'],
    ['.', '.', '.', '.','.','.','.','.','.','.'],
    ['.', '.', '.', '.','.','.','.','.','.','.'],
    ['.', '#', '.', '.','.','.','.','.','.','.'],
    ['.', '#', '.', '.','.','#','.','.','.','.'],
    ['.', '.', '.', '.','.','.','#','.','.','.'],
    ['.', '.', '.', '.','.','.','.','.','.','.'],
    ['.', '.', '.', '.','.','.','.','.','.','.']
]
labyrinth = Labyrinth(grid4)
start_rod = Rod(0, 0)
print(f"Laberinto 4: {bfs_labyrinth(labyrinth, start_rod)}")
