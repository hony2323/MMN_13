import json
import os

from max_min_heap import MaxMinHeap
from validation import validate_max_min_heap


class Menu:
    def __init__(self, root_dir):
        self.root_dir = root_dir or os.path.dirname(os.path.abspath(__file__))
        self.mmh = MaxMinHeap([])
        self.running = False
        self.menu = self._first_menu()

    def start(self):
        self.running = True
        while self.running:
            self.print_menu()
            try:
                print(self.handle_selection() or "")
            except Exception as e:
                print("an error as occurred, try again...")

    def handle_selection(self):

        i = str(input("choose option: "))
        try:
            func, msg, *no_params = self.menu[i]
        except KeyError as e:
            print(f"\n {i} is not an option \n")
            raise e
        if no_params:
            return func()
        i = str(input("write your input: "))
        return func(i)

    # Menu initializations
    def _first_menu(self):
        return {
            "1": (self._file_replace_heap, "write file path (relative to src/)"),
            "2": (self._string_replace_heap, "write you heap in this format [x,x,x,x,x,x,x,....] (including [])"),
            "s": (lambda: self._switch_menu(self._second_menu()), "skip menu", True),
            "v": (lambda: str(validate_max_min_heap(self.mmh, 0, 0)),
                  "(for dev but feel free to use) validate the algorithm of the build_heap", True),
            "p": (lambda: print(self.mmh.array), "print current heap", True),
            "x": (self.end_loop, "exit the application", True)
        }

    def _second_menu(self):
        return {
            "1": (self.mmh.build_heap, "build heap", True),
            "2": (self.mmh.heapify, "heapify"),
            "3": (self.mmh.heap_insert, "insert"),
            "4": (self.mmh.heap_extract_min, "extract min"),
            "5": (self.mmh.heap_extract_max, "extract max"),
            "6": (self.mmh.heap_delete, "delete"),
            "b": (lambda: self._switch_menu(self._first_menu()), "go back to first menu", True),
            "p": (lambda: print(self.mmh.array), "print current heap", True),
            "v": (lambda: str(validate_max_min_heap(self.mmh, 0, 0)),
                  "(for dev but feel free to use) validate the algorithm of the build_heap", True),
            "x": (self.end_loop, "exit the application", True)
        }

    def end_loop(self):
        self.running = False

    def _switch_menu(self, menu):
        self.menu = menu

    # ------ PART OF FIRST MENU ---------
    def _file_replace_heap(self, path_to_file):
        try:
            with open(os.path.join(self.root_dir, path_to_file), 'r') as f:
                self.mmh = MaxMinHeap(json.load(f))
        except FileNotFoundError as e:
            print(f"\n file {path_to_file} not found \n")
            raise e
        self.menu = self._second_menu()

    def _string_replace_heap(self, s):
        ls = json.loads(s)
        if not type(ls) == list:
            print("\n the input is not a list \n")
            raise Exception()
        self.mmh = MaxMinHeap(json.loads(s))
        self.menu = self._second_menu()

    def print_menu(self):
        for key in self.menu.keys():
            func, msg, *no_params = self.menu[key]
            print(f"{key} - {msg}")
