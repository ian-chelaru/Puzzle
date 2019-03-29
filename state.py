from configuration import Configuration


class State:
    def __init__(self, values):
        self.__values = values

    def get_values(self):
        return self.__values

    def set_values(self, values):
        self.__values = values

    def __len__(self):
        return len(self.__values)

    def __str__(self):
        s = ""
        for x in self.__values:
            s += str(x) + '\n'
        return s

    def __add__(self, other):
        aux = State(self.__values)
        if isinstance(other, Configuration):
            aux.set_values(aux.get_values() + [other])
        return aux
