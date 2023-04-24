class Letter:
    def __init__(self, string, place):
        self.string = string
        self.place = place
    
    def __init__(self, string):
        self.string = string
        self.place = 6
        
        
# import collections

class Word:
    def __init__(self, string, dict):
        self.string = string
        self.value = 0
        used_chars = []
        for i in range(5):
            if self.string[i] not in used_chars:
                self.value += dict[self.string[i]]
                used_chars.append(self.string[i])
        
    
    def __str__(self):
        return self._string
    
class Game:
    def __init__(self):
        self.grey = []
        self.yellow = []
        self.green = []
        try:
            with open("quordle-guess.txt", "r") as f:
                self.all_words = [Word(line.strip()) for line in f]
            self.possible = self.all_words[:]
        except Exception as e:
            print("failed to generate word list")
    
    def update_possible_list(self):
        # GREY
        for word in self.all_words:
            for string in self.grey:
                if string in word.string:
                    if word in self.possible:
                        self.possible.remove(word)
        # YELLOW
        for word in self.all_words:
            for letter in self.yellow:
                if letter.string not in word.string or word.string[letter.place] == letter.string:
                    if word in self.possible:
                        self.possible.remove(word)
        
        # GREEN
        for word in self.all_words:
            for letter in self.green:
                if word.string[letter.place] != letter.string:
                    if word in self.possible:
                        self.possible.remove(word)
        
        return self.possible
    
    def add_grey(self, string):
        if string is None or len(string) > 1:
            raise ValueError()
        self.grey.append(string)
        
    def add_yellow(self, letter):
        if letter is None or len(letter.string) > 1:
            raise ValueError()
        self.yellow.append(letter)
        
    def add_green(self, letter):
        if letter is None or len(letter.string) > 1:
            raise ValueError()
        self.green.append(letter)
    
    def get_best_guess(self):
        