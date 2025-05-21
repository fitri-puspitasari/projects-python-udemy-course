from keyboard_button import KeyboardButton

class MorseKeyword:
    def __init__(self, root, canvas, translater, keyboards):
        self.canvas = canvas
        self.children = []
        
        # dot
        dot = KeyboardButton(root, canvas, '.', 350, 444, translater=translater, isBold=True, keyboards=keyboards)
        self.children.append(dot)
        dot.button.config(anchor='n')
        # dash
        dash = KeyboardButton(root, canvas, '_', 400, 444, translater=translater, isBold=True, keyboards=keyboards)
        self.children.append(dash)
        dash.button.config(anchor='n')
        # slash
        self.children.append(
            KeyboardButton(root, canvas, '/', 450, 444, translater=translater, isBold=True, keyboards=keyboards)
            )
        # space
        space = KeyboardButton(root, canvas, 'space', 376, 494, translater=translater, width=8, isBold=False, keyboards=keyboards)
        self.children.append(space)
        # space.button.config(anchor='s')
        # backspace
        self.children.append(
            KeyboardButton(root, canvas, '⇦', 450, 494, translater=translater, isBold=True, keyboards=keyboards)
            )

        
    def show(self):
        for btn in self.children:
            btn.show()

    def hide(self):
        for btn in self.children:
            btn.hide()