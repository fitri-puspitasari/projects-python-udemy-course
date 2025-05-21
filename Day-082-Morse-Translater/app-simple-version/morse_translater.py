# from threading import Timer
from data import code_morse

class MorseTranslater:
    def __init__(self, board):
        # self.input_type = 'word'    # 'word' | 'code'
        # self.letters = ''
        self.board = board
        self.set_type('word')

        self._word_code_dict = code_morse
        
        keys = list(code_morse.values())
        values = list(code_morse.keys())
        self._code_word_dict = dict(zip(keys, values))

    def set_type(self, type):
        self.input_type = type
        self.letters = ''
        self.board.clear()

    def collect(self, key):
        # if self.board.is_limit:
        #     return

        # if key == 'space' or key == '└─┘':
        if key == 'space':
            # if self.input_type == 'word':
            #     key = ' '
            # elif self.input_type == 'code':
            #     key = '/'
            key = ' '
            self.letters += key
        elif key == 'backspace' or key == '⇦':
            self.letters = self.letters[:-1]
        elif key == '.':
            key = '•'
            self.letters += key
        elif key == '_':
            key = '-'
            self.letters += key
        else:
            self.letters += key
            
        # '▪ ─ - ⏺▀▀▀ ▬⦁'
        # '•--‧---.'


        
        # print(self.letters)
        # print('-----------------')

        # else:
        
        
        # wait_for_write = Timer(0.01, self.board.write, (self, self.letters))
        # wait_for_write.start()

        self.board.write(self, self.letters)
        # self.translate()

    def translate(self, letters_updated):
        self.letters = letters_updated
        if self.input_type == 'word':
            self.translate_word(self.letters)
        elif self.input_type == 'code':
            self.translate_codes(self.letters)

    def translate_word(self, word):
        # print(word)
        generated_code = ''
        for letter in word:
            if letter == ' ':
                generated_code += '/'
            else:
                code = self._word_code_dict[letter]
                generated_code += (code + ' ')
        # print(generated_code)
        self.board.post_result(generated_code)
    
    
    def translate_codes(self, codes):
        # print(codes)
        codes = codes.replace('/', ' / ')
        codes = codes.replace('•', '.')
        codes = codes.split(' ')
        codes = [c for c in codes if c != '']
        # print(codes)

        generated_word = []
        for c in codes:
            if c == '/':
                letter = ' '
            else:
                try:
                    letter = self._code_word_dict[c]
                except KeyError:
                    letter = '❔'
            generated_word.append(letter)

        generated_word = ''.join(generated_word)
        # print(generated_word)
        self.board.post_result(generated_word)

    
