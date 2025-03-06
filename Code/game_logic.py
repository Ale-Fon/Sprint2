import random

class gameplay:
    def __init__(self, size, mode= 'Simple game'):
        self.size = size
        self.mode = mode
        self.board = [['' for _ in range(size)] for _ in range(size)]
        self.current_turn = random.choice(['Blue', 'Red'])
        self.moves = []
        print(f"Game initialized: Size {size}, Mode {mode}")
        print(f"Start player: {self.current_turn}")
    
    def letterPlace(self, row, col, letter):
        if self.board[row][col] == '':
            self.board[row][col] = letter
            self.moves.append((row, col, letter, self.current_turn))
        return None, None

    def switch_turn(self):
        self.current_turn = 'Red' if self.current_turn == 'Blue' else 'Blue'
        print(f"Turn is now {self.current_turn}")

    def sets_up_sos(self, row, col, letter):
        directions = [(-1,0), (1,0), (0, -1), (0,1), (-1,-1), (1,1), (-1,1), (1,-1)]
        for dr, dc in directions:
            if letter == 'S':
                if(0 <= row + 2*dr < self.size and 0 <= col + 2*dc < self.size and
                   self.board[row + dr][col + dc] == 'O' and
                   self.board[row +2*dr][col + 2*dc] == ''):
                    return True
                if(0 <= row + 2*dr < self.size and 0 <= col + 2*dc < self.size and
                   self.board[row + dr][col + dc] == '' and
                   self.board[row +2*dr][col + 2*dc] == 'S'):
                    return True
            elif letter == 'O':
                if (0 <= row + dr < self.size and 0 <= col + dc <self.size and
                     0 <= row - dr < self.size and 0 <= col - dc < self.size and
                     ((self.board[row + dr][col + dc] == 'S' and self.board[row - dr][col - dc] == '') or
                      self.board[row + dr][col + dc] == '' and self.board[row - dr][col - dc] == 'S')):
                    return True
        return False
    
    def complete_sos(self, row, col, letter):
        directions = [(-1,0), (1,0), (0, -1), (0,1), (-1,-1), (1,1), (-1,1), (1,-1)]
        for dr, dc in directions:
            if letter == 'S':
                if(0 <= row + 2*dr < self.size and 0 <= col + 2*dc < self.size and
                   self.board[row + dr][col + dc] == 'O' and
                   self.board[row +2*dr][col + 2*dc] == 'S'):
                    return True
            elif letter == 'O':
                if (0 <= row + dr < self.size and 0 <= col + dc <self.size and
                     0 <= row - dr < self.size and 0 <= col - dc < self.size and
                     ((self.board[row + dr][col + dc] == 'S' and self.board[row - dr][col - dc] == '') or
                      self.board[row + dr][col + dc] == '' and self.board[row - dr][col - dc] == 'S')):
                    return True
        return False