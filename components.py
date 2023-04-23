class Letter:
    def __init__(self, character, place):
        self.char = character
        self.place = place
    
    def __init__(self, character):
        self.char = character
        self.place = 6
        
        
# import collections

class Word:
    def __init__(self, string):
        self.string = string
        self.value = 0
        char_values = {'a': 4467, 'e': 4255, 'r': 3043, 'o': 2801, 'i': 2581, 's': 2383, 't': 2381, 'l': 2368,
                       'n': 2214, 'u': 1881, 'y': 1605, 'c': 1546, 'd': 1399, 'h': 1323, 'm': 1301, 'p': 1293,
                       'b': 1162, 'g': 1102, 'k': 882, 'w': 685, 'f': 661, 'v': 466, 'z': 250, 'x': 189, 'j': 163,
                       'q': 84}
        used_chars = set()
        for i in range(5):
            if self._string[i] not in used_chars:
                self._value += char_values[self._string[i]]
                used_chars.add(self._string[i])
    
    def __str__(self):
        return self._string