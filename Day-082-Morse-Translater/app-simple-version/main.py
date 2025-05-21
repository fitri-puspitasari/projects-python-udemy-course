from pygame import mixer
from tkinter import Tk
from tkinter import *
from alphabet_keyboards import AlphabetKeyword
from morse_keyboard import MorseKeyword
from text_boards import TextBoars
from morse_translater import MorseTranslater
from keyboard_manager import KeyboardManager

# from keyboard_button import KeyboardButton
# from data import code_morse
# import ttkbootstrap as ttk
# from ttkbootstrap.constants import *
# from tkinter.ttk import *

# import os
# cwd = os.getcwd()
# print(cwd + '/images/bg.png')

WHITE = '#FCFFF9'
BROWN = '#BE7339'
DARK_BROWN = '#3D0D02'
LIGHT_BROWN = '#F5C896'

# from threading import Timer
 
# breaker_breaker = False
 
# def delayed_function (seconds_delayed) :
#     global breaker_breaker
#     breaker_breaker = True
#     print (f'This funciton was delayed for {seconds_delayed} seconds.')
 
# wait_for_it = Timer (3, delayed_function, '3')
# wait_for_it.start ()
 
# while breaker_breaker == False:
#     print ('Still waiting...')
#     for dummy in range (999999) : dummy =+ 1




def switch():
    pop = mixer.Sound("assets/sfx/pop.mp3")
    pop.play()

    global is_alphabet_active
    is_alphabet_active =  not is_alphabet_active
    if is_alphabet_active:
        # active_keyboard = 'alphabet'
        # active_keyboard.set('alphabet')
        translater.set_type('word')
        keyboard_manager.is_alphabet_active = is_alphabet_active
        alphabet_keyboard.show()
        morse_keyboard.hide()
    else:
        # active_keyboard = 'morse'
        # active_keyboard.set('morse')
        translater.set_type('code')
        keyboard_manager.is_alphabet_active = is_alphabet_active
        alphabet_keyboard.hide()
        morse_keyboard.show()

    left_str.set('alphabet' if is_alphabet_active else 'morse')
    right_str.set('morse' if is_alphabet_active else 'alphabet')
    # alphabet_keyboard.hide()

def main():
    mixer.init()
    # key_press_sfx = mixer.Sound("assets/sfx/key_press.wav")
    # key_press_sfx.play()

    # tkinter configuration
    root = Tk()
    root.title("Morse Game")
    root.geometry("800x600")
    # root.config(padx=50, pady=50)

    # bg
    canvas = Canvas(root, width=800, height=600)
    bg_img = PhotoImage(file="assets/images/bg.png")
    bg_img.img = bg_img
    canvas.create_image(400, 300, image=bg_img)
    canvas.pack()

    # switch button
    switch_button = Button(
        root,
        background=LIGHT_BROWN,
        foreground=DARK_BROWN,
        activebackground=BROWN,
        activeforeground=WHITE,
        highlightthickness=2,
        highlightbackground=LIGHT_BROWN,
        highlightcolor=WHITE,
        width=6,
        height=1,
        border=0,
        # cursor='hand1',
        text='switch',
        font=('Comic Sans MS', 16),
        command=switch
    )
    switch_btn_window = canvas.create_window(400, 302, window=switch_button, anchor=CENTER)

    # globe boolean variable
    global is_alphabet_active
    is_alphabet_active = True

    # text boards
    board = TextBoars(root, canvas)

    # translater
    global translater
    translater = MorseTranslater(board)


    # keyboard dict
    keyboards = {}
    # alphabet keyboard
    global alphabet_keyboard
    alphabet_keyboard = AlphabetKeyword(root, canvas, translater, keyboards)
    # morse keyword
    global morse_keyboard
    morse_keyboard = MorseKeyword(root, canvas, translater, keyboards)
    morse_keyboard.hide()

    # keyboard manager
    global keyboard_manager
    keyboard_manager = KeyboardManager(root, keyboards, is_alphabet_active, board)

    # labels    
    global left_str
    left_str = StringVar()
    left_str.set('alphabet')
    left_label = Label(
        root,
        textvariable=left_str,
        background=LIGHT_BROWN,
        foreground=DARK_BROWN,
        font=('Comic Sans MS', 14),
    )
    left_label_window = canvas.create_window(191, 242, window=left_label, anchor=CENTER)

    global right_str
    right_str = StringVar()
    right_str.set('morse')
    right_label = Label(
        root,
        textvariable=right_str,
        background=WHITE,
        foreground=DARK_BROWN,
        font=('Comic Sans MS', 14),
    )
    right_label_window = canvas.create_window(610, 242, window=right_label, anchor=CENTER)


    root.mainloop()

if __name__ == "__main__":
    main()
    # pass