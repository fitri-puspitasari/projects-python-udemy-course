from pygame import mixer

class KeyboardManager():
    
    def __init__(self, root, keyboards, is_alphabet_active, board):
        self.keyboards = keyboards
        self.is_alphabet_active = is_alphabet_active
        self.board = board
        self.selected_key = None
        root.bind("<KeyPress>", self.key_pressed)
        self.sfx = mixer.Sound("assets/sfx/key_press.wav")

    def set_selected_key(self, event_keysym):
        key = None
        if event_keysym == 'space':
            # if self.is_alphabet_active:
            #     key = 'space'
            # else:
            #     key = '└─┘'
            key = 'space'
        elif event_keysym == 'BackSpace':
        # if event_keysym == 'BackSpace':
            if self.is_alphabet_active:
                key = 'backspace'
            else:
                key = '⇦'
        elif event_keysym == 'period':
            key = '.'
        elif event_keysym == 'minus':
            key = '_'
        elif event_keysym == 'slash':
            key = '/'
        elif event_keysym.isalpha():
            key = event_keysym.upper()
        elif event_keysym.isnumeric():
            key = event_keysym

        self.selected_key = key

    
    def key_pressed(self, event):
        # return if key is not expected
        if self.board.is_limit and event.keysym != 'BackSpace':
            return
        if self.is_alphabet_active:
            if event.keysym == 'period' or event.keysym == 'minus' or event.keysym == 'slash':
                return
        else:
            if event.keysym != 'period' and event.keysym != 'minus' and event.keysym != 'slash' and event.keysym != 'space' and event.keysym != 'BackSpace':
                return
        
        # key process
        self.sfx.play()
        self.set_selected_key(event.keysym)

        try:
            list(self.keyboards.keys()).index(self.selected_key)
        except ValueError:
            return
        
        self.keyboards[self.selected_key].press_physical_keyboard()
        return "break"