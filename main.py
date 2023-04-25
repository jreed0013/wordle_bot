import string


class Letter:
    def __init__(self, string, place):
        self.string = string
        self.place = place
        
        
# import collections

class Word:
    def __init__(self, string):
        self.string = string
        self.value = None  
    
    def set_value(self, dictionary):
        used_chars = []
        self.value = 0
        i = 0
        for i in range(len(self.string)):
            if (self.string[i] not in used_chars):
                self.value += dictionary[self.string[i]]
                used_chars.append(self.string[i])
    
    def __str__(self):
        return self._string
    
class Game:
    def __init__(self):
        self.grey = []
        self.yellow = []
        self.green = []
        self.char_vals = {}
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
        if len(self.possible) == 0:
            print("No possible words")
            return None
        
        self.update_char_vals()
        
        self.possible[0].set_value(self.char_vals)
        best_word = self.possible[0]
        
        for word in self.possible:
            word.set_value(self.char_vals)
            if (word.value > best_word.value):
                best_word = word
        return best_word
        
    def update_char_vals(self):
        lower = list(string.ascii_lowercase)
        for l in lower:
            value = 0
            for word in self.possible:
                value += word.string.count(l)
            self.char_vals[l] = value
            
    def check_lists_for_duplicates(self):
        for letter in self.yellow:
            if letter.string in self.grey:
                self.grey.remove(letter.string)
        for letter in self.green:
            if letter.string in self.grey:
                self.grey.remove(letter.string)
    
    def play(self, answer):
        # Initializing the game
        guess_count = 1
        print("Wordle Bot solution to : " + answer)
        
        # Starting the guess loop
        while guess_count < 7:
            guess = self.get_best_guess().string
            print(f"Guess {guess_count}: {guess}")
            
            green_count = 0
            for i in range(len(answer)):
                if answer[i] == guess[i]:
                    self.add_green(Letter(guess[i], i))
                    green_count += 1
                elif guess[i] in answer:
                    self.add_yellow(Letter(guess[i], i))
                else:
                    self.add_grey(guess[i])
            
            if green_count == 5:
                print(f"Puzzle solved in {guess_count} guesses")
                return
            else:
                self.check_lists_for_duplicates()
                self.update_possible_list()
            guess_count += 1
        print(f"Wordle bot failed to solve for {answer}")
        return

                
def main():
    answer = input("Wordle Answer: ")
    game = Game()
    input_error = True
    for word in game.all_words:
        if word.string == answer:
            input_error = False
    if input_error:
        print("Not a valid answer to Wordle")
        return
    else:
        game.play(answer)
    
if __name__ == "__main__":
    main()