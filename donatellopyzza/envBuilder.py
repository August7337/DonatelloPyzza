import os, sys, inspect
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent / "grid"))

from grid import Grid
from mazeParser import Parser


class EnvBuilder:
    def __init__(self, name: str, gui: bool):
        self.name = name
        self.gui = gui

    def get_data_path(self, path):
        return str(Path(__file__).resolve().parent / (path + self.name))

    def build_grid(self):
        data_path = self.get_data_path("data/environments/")
        parser = Parser(data_path)
        gui, map, agents = parser.parse()
        # for simplicity matters, we only use one agent in this package
        return agents[0], Grid(gui, map, agents, self.gui, self.name)
