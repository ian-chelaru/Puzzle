from time import time


class UI:
    def __init__(self, controller):
        self.__controller = controller

    @staticmethod
    def show_commands():
        s = "\n"
        s += "1 - Find a path with BFS\n"
        s += "2 - Find a path with Greedy best-first search\n"
        s += "0 - Exit"
        print(s)

    def bfs_path(self):
        start_clock = time()
        state = self.__controller.bfs(self.__controller.get_problem().get_initial_state())
        print(str(state))
        print("Execution time: ", time() - start_clock, "seconds")
        print("Number of moves: ", len(state) - 1)

    def gbfs_path(self):
        start_clock = time()
        state = self.__controller.gbfs(self.__controller.get_problem().get_initial_state())
        print(str(state))
        print("Execution time: ", time() - start_clock, "seconds")
        print("Number of moves: ", len(state) - 1)

    def run(self):
        ok = True
        while ok:
            UI.show_commands()
            try:
                command = int(input(">> "))
                if command == 1:
                    self.bfs_path()
                elif command == 2:
                    self.gbfs_path()
                elif command == 0:
                    ok = False
                else:
                    print("Invalid command")
            except ValueError:
                print("Invalid command")
