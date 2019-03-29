from problem import Problem


class Controller:
    def __init__(self, problem):
        self.__problem = problem

    def get_problem(self):
        return self.__problem

    def bfs(self, root):
        queue = [root]
        while len(queue) > 0:
            current_state = queue.pop(0)
            if current_state.get_values()[-1] == self.__problem.get_final_config():
                return current_state
            queue += Problem.expand(current_state)

    # def bfs(self, root):
    #     queue = [root]
    #     visited = []
    #     while len(queue) > 0:
    #         current_state = queue.pop(0)
    #         current_config = current_state.get_values()[-1]
    #         visited.append(current_config)
    #         if current_config == self.__problem.get_final_config():
    #             return current_state
    #         aux = []
    #         for state in Problem.expand(current_state):
    #             if state.get_values()[-1] not in visited:
    #                 aux.append(state)
    #         queue += aux[:]

    def gbfs(self, root):
        # states to visit
        to_visit = [root]
        # configurations visited
        visited = []
        while len(to_visit) > 0:
            current_state = to_visit.pop(0)
            current_config = current_state.get_values()[-1]
            visited.append(current_config)
            if current_config == self.__problem.get_final_config():
                return current_state
            aux = []
            for state in Problem.expand(current_state):
                if state.get_values()[-1] not in visited:
                    aux.append(state)
            aux.sort(key=lambda x: self.__problem.heuristics(x))
            to_visit = aux[:] + to_visit
