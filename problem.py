from state import State


class Problem:
    def __init__(self, initial, final):
        self.__initialConfig = initial
        self.__finalConfig = final
        self.__initialState = State([initial])

    def get_initial_config(self):
        return self.__initialConfig

    def get_final_config(self):
        return self.__finalConfig

    def get_initial_state(self):
        return self.__initialState

    @staticmethod
    def expand(current_state):
        my_list = []
        current_config = current_state.get_values()[-1]
        next_config = current_config.next_config()
        for i in next_config:
            my_list.append(current_state + i)
        return my_list

    def heuristics(self, state):
        config = state.get_values()[-1]
        size = config.getsize()
        count = 0
        for i in range(size):
            for j in range(size):
                if config.get_positions()[i][j] != '_' and config.get_positions()[i][j] != \
                        self.__finalConfig.get_positions()[i][j]:
                    count += 1
        return count
