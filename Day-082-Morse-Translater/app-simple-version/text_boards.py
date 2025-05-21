from tkinter import *
from data import code_morse

WHITE = '#FCFFF9'
BROWN = '#BE7339'
DARK_BROWN = '#3D0D02'
LIGHT_BROWN = '#F5C896'

class TextBoars():

    def __init__(self, root, canvas):
        self.canvas = canvas
        self.is_limit = False
        self.num_letters = 0

        self.material_str = StringVar()
        # material_str.set('LOREM IPSUM DOLOR SIT AMET, CONSECTETUR ADIPISCING ELIT. FUSCE CURSUS, TELLUS SED GRAVIDA PHARETRA, ANTE RISUS SODALES LECTUS, ID ORNARE DIAM TELLUS UT SEM. NULLA LUCTUS ENIM ET ERAT EFFICITUR, ID EFFICITUR AUGUE LACINIA. PELLENTESQUE IN LEO EFFICITUR, COMMODO IPSUM SIT AMET, FERMENTUM MAGNA. NULLA AC MOLESTIE DUI. MORBI ET PURUS NUNC.')
        self.material_str.set('|')

        self.material_label = Label(
            root,
            textvariable=self.material_str,
            background=LIGHT_BROWN,
            # background=WHITE,
            foreground=DARK_BROWN,
            font=('Comic Sans MS', 12),
            anchor='w',
            justify=LEFT,
            wraplength=250
        )
        self.material_label_window = canvas.create_window(191 - 125, 260, window=self.material_label, anchor='nw')
        # print(self.material_label.winfo_reqheight())


        self.result_str = StringVar()
        # self.result_str.set('.-.. --- .-. . -- / .. .--. ... ..- -- / -.. --- .-.. --- .-. / ... .. - / .- -- . - --..-- / -.-. --- -. ... . -.-. - . - ..- .-. / .- -.. .. .--. .. ... -.-. .. -. --. / . .-.. .. - .-.-.- / ..-. ..- ... -.-. . / -.-. ..- .-. ... ..- ... --..-- / - . .-.. .-.. ..- ... / ... . -.. / --. .-. .- ...- .. -.. .-')
        self.result_str.set('')
        self.result_label = Label(
            root,
            textvariable=self.result_str,
            # background=LIGHT_BROWN,
            background=WHITE,
            foreground=DARK_BROWN,
            font=('Comic Sans MS', 12),
            anchor='w',
            justify=LEFT,
            wraplength=250
        )
        self.result_label_window = canvas.create_window(610 - 125, 260, window=self.result_label, anchor='nw')
        # print(self.result_label.winfo_reqheight())

    def write(self, translater, letters):
        self.letters = letters + '|'
        self.material_str.set(self.letters)
        self.check_limit('write')
        self.check_limit('write')        
        self.letters = self.letters.replace('|', '')

        # normalize color of labels
        if len(self.letters) < self.num_letters:
            self.material_label.config(foreground=DARK_BROWN)
            self.result_label.config(foreground=DARK_BROWN)
        self.num_letters = len(self.letters)

        # translate
        try:
            self.translater.translate(self.letters)
        except AttributeError:
            self.translater = translater
            self.translater.translate(self.letters)
        
    
    def check_limit(self, type):
        # print(self.material_label.winfo_reqheight())
        # print(self.result_label.winfo_reqheight())
        self.is_limit = self.material_label.winfo_reqheight() > 121 or self.result_label.winfo_reqheight() > 121
        
        if self.is_limit:
            # print(self.material_label.winfo_reqheight())
            self.material_label.config(foreground='red' if self.material_label.winfo_reqheight() > 121 else DARK_BROWN)
            self.result_label.config(foreground='red' if self.result_label.winfo_reqheight() > 121 else DARK_BROWN)
        
            self.letters = self.letters[:-1]
            self.material_str.set(self.letters)

            

    def clear(self):
        self.material_str.set('|')
        self.result_str.set('')
        self.is_limit = False

    def post_result(self, text):
        self.result_str.set(text)
        self.check_limit('post')
        if self.is_limit:
            self.translater.translate(self.letters)

