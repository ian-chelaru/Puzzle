class Reader:
    def __init__(self, filename):
        self.__filename = filename

    def read(self):
        puzzle1 = []
        puzzle2 = []
        first = True
        with open(self.__filename, 'r') as f:
            for line in f:
                if line == '\n':
                    first = False
                else:
                    row = line.split()
                    if first:
                        puzzle1.append(row)
                    else:
                        puzzle2.append(row)
        return puzzle1, puzzle2
