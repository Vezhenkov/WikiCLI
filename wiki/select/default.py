import os
import time

import keyboard

from .display.default import DisplayDefault


class SelectDefault:
    def __init__(self, request):
        self.request = request
        self.response = []
        self.display = DisplayDefault(self)
        self.selected = 0
        self.prev_selected = 0
        self.prev_key = 0
        self.prev_time = 0

    def get(self):
        self.response = self.request.get()
        self.draw_initial()
        keyboard.on_press(self.on_press_key)
        keyboard.wait("enter")
        return self.response[self.selected]

    def draw_initial(self):
        os.system('cls')
        if not len(self.response):
            print('No results')
            exit()
        print(self.display.get())

    def on_press_key(self, e):
        if self.prev_key == e.name and time.time() - self.prev_time < 0.2:
            return
        self.prev_key = e.name
        self.prev_time = time.time()
        self.prev_selected = self.selected
        match e.name:
            case 'down':
                self.selected += 1
            case 'up':
                self.selected -= 1
            case _:
                return
        self.selected = min(max(self.selected, 0), len(self.response) - 1)
        if self.selected == self.prev_selected:
            return
        os.system('cls')
        print(self.display.get())
