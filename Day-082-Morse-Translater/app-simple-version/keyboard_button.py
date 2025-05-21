from tkinter import *
from pygame import mixer
from threading import Timer

WHITE = '#FCFFF9'
BROWN = '#BE7339'
DARK_BROWN = '#3D0D02'
LIGHT_BROWN = '#F5C896'

class KeyboardButton():

    def __init__(self, root, canvas, key, x, y, translater, width=3, isBold=False, keyboards=None):
        self.key = key
        self.canvas = canvas
        self.translater = translater
        self.sfx = mixer.Sound("assets/sfx/key_press.wav")

        self.button = Button(
            root,
            background=LIGHT_BROWN,
            foreground=DARK_BROWN,
            activebackground=BROWN,
            activeforeground=WHITE,
            highlightthickness=2,
            highlightbackground=LIGHT_BROWN,
            highlightcolor=WHITE,
            width=width,
            height=1,
            border=0,
            # cursor='hand1',
            text=key,
            font=('Comic Sans MS', 14),
            command=self.press
        )
        if isBold:
            self.button.config(font=('Comic Sans MS', 14, 'bold'))
        self.btn_window = canvas.create_window(x, y, window=self.button, anchor=CENTER)

        keyboards[key] = self
        
    def show(self):
        self.canvas.itemconfigure(self.btn_window, state='normal')

    def hide(self):
        self.canvas.itemconfigure(self.btn_window, state='hidden')

    def press(self):
        self.sfx.play()
        self.translater.collect(self.key)

    def press_physical_keyboard(self):
        self.sfx.play()
        self.button.config(background=BROWN, foreground=WHITE)
        self.translater.collect(self.key)
        wait_for_release = Timer(0.1, self.release_physical_keyboard)
        wait_for_release.start()

    def release_physical_keyboard(self):
        self.button.config(background=LIGHT_BROWN, foreground=DARK_BROWN)

        
    # translater = MorseTranslater()
    # print(translater.translate_word('bangun tidur ku terus mandi'))
    # print(translater.translate_codes('-... .- -. --. ..- -.  - .. -.. ..- .-.  -.- ..-  - . .-. ..- ...  -- .- -. -.. ..'))


# -------- bermasalah di keyboard yang berbarengan ditekan
# -------- time.sleep tidak cocok
# -------- coba uji fungsi ini!

"""
from threading import Timer
 
breaker_breaker = False
 
def delayed_function (seconds_delayed) :
    global breaker_breaker
    breaker_breaker = True
    print (f'This funciton was delayed for {seconds_delayed} seconds.')
 
wait_for_it = Timer (3, delayed_function, '3')
wait_for_it.start ()
 
while breaker_breaker == False:
    print ('Still waiting...')
    for dummy in range (999999) : dummy =+ 1
"""