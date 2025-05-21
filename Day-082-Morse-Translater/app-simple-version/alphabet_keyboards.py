from keyboard_button import KeyboardButton
from data import code_morse


class AlphabetKeyword:
    def __init__(self, root, canvas, translater, keyboards):
        self.canvas = canvas
        self.children = []
        
        # alphabet
        keys = code_morse.keys()
        spawn = { 'x': 75, 'y': 444 }
        offset = 50
        counter = { 'x': 0, 'y': 0 }
        num_column = 14
        alphabet_keyboards = []
        for key in code_morse.keys():
            self.children.append(
                KeyboardButton(
                    root, 
                    canvas, 
                    key, 
                    spawn['x'] + (counter['x'] * offset), 
                    spawn['y']  + (counter['y'] * offset),
                    translater=translater,
                    keyboards=keyboards
                    )
            )
            alphabet_keyboards
            counter['x'] += 1
            if counter['x'] % num_column == 0:
                counter['x'] = 0
                counter['y'] += 1
        # space
        self.children.append(
            KeyboardButton(root, canvas, 'space', 541, 544, translater=translater, width=15, keyboards=keyboards)
            )
        # backspace
        self.children.append(
            KeyboardButton(root, canvas, 'backspace', 692, 544, translater=translater, width=9, keyboards=keyboards)
            )

        
    def show(self):
        for btn in self.children:
            btn.show()

    def hide(self):
        for btn in self.children:
            btn.hide()