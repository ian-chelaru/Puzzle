from configuration import Configuration
from problem import Problem
from controller import Controller
from ui import UI
from reader import Reader


filename = "input.txt"
r = Reader(filename)
initial_puzzle, final_puzzle = r.read()

initial = Configuration(initial_puzzle)
final = Configuration(final_puzzle)

problem = Problem(initial, final)
controller = Controller(problem)

ui = UI(controller)
ui.run()
