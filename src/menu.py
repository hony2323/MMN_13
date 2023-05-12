import json
import os

from max_min_heap import MaxMinHeap


class Menu:
    def __init__(self, root_dir):
        root_dir = root_dir or os.path.dirname(os.path.abspath(__file__))
        self.first_running = False
        self.second_running = False

        self.mmh = MaxMinHeap([])

    def start(self):
        pass

    # def handle_input(self, ):
    #     pass

    def handle_selection(self, menu):
        pass

    # Menu initializations
    def _first_menu(self):
        return {
            "1": (self._replace_heap_file, "write file path (relative to src/)"),
            "2": (self._replace_heap_string, "write you heap in this format [x,x,x,x,x,x,x,....] (including [])"),
        }

    def _second_menu(self):
        pass

    # Helpers
    def _replace_heap_file(self, path_to_file):
        try:
            with open(path_to_file, 'r') as f:
                self.mmh = MaxMinHeap(json.load(f))
        except FileNotFoundError as e:
            print(f"\n file {path_to_file} not found \n")
            raise e

    def _replace_heap_string(self, s):
        ls = json.loads(s)
        if not type(ls) == list:
            print("\nthe input is not a list\n")
            raise Exception()
        self.mmh = MaxMinHeap(json.loads(s))

    def print_menu(self, menu: dict):
        for key in menu.keys():
            , msg = menu[key]
            print(f"{key} - {msg}")
