class Configuration:
    def __init__(self, positions):
        self.__size = len(positions)
        self.__positions = positions[:]

    def getsize(self):
        return self.__size

    def get_positions(self):
        return self.__positions

    def next_config(self):
        x, y = self.find('_')
        directions = [(x - 1, y), (x, y + 1), (x + 1, y), (x, y - 1)]
        children = []
        for i in directions:
            child = self.generate_puzzle(x, y, i[0], i[1])
            if child is not None:
                children.append(Configuration(child))
        return children

    def find(self, ch):
        for i in range(0, self.__size):
            for j in range(0, self.__size):
                if self.__positions[i][j] == ch:
                    return i, j

    def generate_puzzle(self, x1, y1, x2, y2):
        if 0 <= x2 < self.__size and 0 <= y2 < self.__size:
            new_puzzle = [row[:] for row in self.__positions]
            aux = new_puzzle[x1][y1]
            new_puzzle[x1][y1] = new_puzzle[x2][y2]
            new_puzzle[x2][y2] = aux
            return new_puzzle

    def __eq__(self, other):
        if not isinstance(other, Configuration):
            return False
        if self.__size != other.getsize():
            return False
        for i in range(self.__size):
            for j in range(self.__size):
                if self.__positions[i][j] != other.get_positions()[i][j]:
                    return False
        return True

    def __str__(self):
        s = ""
        for i in range(self.__size):
            for j in range(self.__size):
                s += self.__positions[i][j] + ' '
            s += '\n'
        return s
