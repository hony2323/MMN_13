import json
import os

from max_min_heap import MaxMinHeap


class Menu:
    def __init__(self, root_dir):
        root_dir = root_dir or os.path.dirname(os.path.abspath(__file__))
        self.mmh = MaxMinHeap([])
        self.running = False
        self.menu = self._first_menu()

    def start(self):
        self.running = True
        while self.running:
            self.print_menu()
            self.handle_selection()

    # def handle_input(self, ):
    #     pass

    def handle_selection(self):
        a = input()

    # Menu initializations
    def _first_menu(self):
        return {
            "1": (self._file_replace_heap, "write file path (relative to src/)"),
            "2": (self._string_replace_heap, "write you heap in this format [x,x,x,x,x,x,x,....] (including [])"),
        }

    def _second_menu(self):
        return {}

    # ------ PART OF FIRST MENU ---------
    def _file_replace_heap(self, path_to_file):
        try:
            with open(path_to_file, 'r') as f:
                self.mmh = MaxMinHeap(json.load(f))
        except FileNotFoundError as e:
            print(f"\n file {path_to_file} not found \n")
            raise e
        self.menu = self._second_menu()

    def _string_replace_heap(self, s):
        ls = json.loads(s)
        if not type(ls) == list:
            print("\nthe input is not a list\n")
            raise Exception()
        self.mmh = MaxMinHeap(json.loads(s))
        self.menu = self._second_menu()

    def print_menu(self):
        for key in self.menu.keys():
            func, msg = self.menu[key]
            print(f"{key} - {msg}")
