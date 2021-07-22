import copy


class Data:
    def __init__(self, val):
        self.val = val


def generate(x, y):
    dimension_2d = []
    part = []
    for i in range(y):
        for j in range(x):
            part.append(Data(0))
        dimension_2d.append(part.copy())
        part.clear()
    return dimension_2d


def oscillator(width, height):
    cell = generate(width, height)
    for i in range(3, height, 5):
        for j in range(2, width, 5):
            for k in range(3):
                cell[i-k][j].val = 1
    return cell


def glider(width, height):
    cell = generate(width, height)
    cell[1][2].val = 1
    cell[1][3].val = 1
    cell[2][1].val = 1
    cell[2][2].val = 1
    cell[3][3].val = 1
    return cell


def stable(width, height):
    cell = generate(width, height)
    for i in range(3, height, 5):
        for j in range(4, width, 6):
            for k in range(2):
                cell[i][j-1-k].val = 1
                cell[i-2][j-1-k].val = 1
            cell[i-1][j].val = 1
            cell[i-1][j-3].val = 1
    return cell


def game(width, height, cell):
    cell_t = copy.deepcopy(cell)
    for y in range(height):
        for x in range(width):
            alive = 0
            for i in range(-1, 2):
                ny = y + i
                if ny < 0:
                    ny = height-1
                elif ny == height:
                    ny = 0
                for j in range(-1, 2):
                    nx = x + j
                    if nx < 0:
                        nx = width-1
                    elif nx == width:
                        nx = 0
                    if cell[ny][nx].val == 1:
                        alive += 1
            if cell[y][x].val == 1:
                alive -= 1
                if alive > 3 or alive < 2:
                    cell_t[y][x].val = 0
            else:
                if alive == 3:
                    cell_t[y][x].val = 1
    return cell_t
