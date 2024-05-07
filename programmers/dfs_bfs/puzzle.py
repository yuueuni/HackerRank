

# game_board table result
inputs = [
    [[[1,1,0,0,1,0],[0,0,1,0,1,0],[0,1,1,0,0,1],[1,1,0,1,1,1],[1,0,0,0,1,0],[0,1,1,1,0,0]], [[1,0,0,1,1,0],[1,0,1,0,1,0],[0,1,1,0,1,1],[0,0,1,0,0,0],[1,1,0,1,1,0],[0,1,0,0,0,0]], 14],
    [[[0,0,0],[1,1,0],[1,1,1]], [[1,1,1],[1,0,0],[0,0,0]], 0],
]


class Puzzle:

    def __init__(self, board, check_value):
        self.board = board
        self.length = len(board)
        self.visited = [[False] * self.length for _ in range(self.length)]
        self.check_value = check_value
        self.rotate_puzzle = None

    def check_pieces(self):
        size_index = {}

        for i in range(self.length):
            for j in range(self.length):
                if self.board[i][j] == self.check_value and not self.visited[i][j]:
                    self.visited[i][j] = True
                    size = self.check_piece(i, j, 1)
                    if size in size_index:
                        size_index[size].append([i, j])
                    else:
                        size_index[size] = [[i, j]]
        return size_index

    def check_piece(self, x, y, size):

        dxs = [0, 0, 1, -1]
        dys = [1, -1, 0, 0]

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.length and 0 <= ny < self.length and self.board[nx][ny] == self.check_value and not self.visited[nx][ny]:
                self.visited[nx][ny] = True
                size = self.check_piece(nx, ny, size + 1)
        return size

    def rotate(self):
        pass

    def find_piece(self, bx, by):
        return 0


def solution(game_board, table):

    pieces_puzzle = Puzzle(table, 1)
    pieces = pieces_puzzle.check_pieces()

    blank_puzzle = Puzzle(game_board, 0)
    blank_pieces = blank_puzzle.check_pieces()

    answer = 0
    for size in blank_pieces.keys():
        if size not in pieces.keys():
            continue
        for x, y in blank_pieces[size]:
            answer += find_piece(x, y) * size

    return answer


if __name__ == "__main__":
    for inp in inputs:
        game_board, table, result = inp[0], inp[1], inp[2]
        res = solution(game_board, table)
        print(res == result, res, result)
