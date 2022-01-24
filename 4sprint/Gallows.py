class Gallows:
    def __init__(self):
        self.words=[]
        self.game_over=False
    def play(self,word):
        if (len(self.words) == 0 or self.words[-1][-1] == word[0]) and word not in self.words:
            self.words.append(word)
            return self.words
        else:
            self.game_over=True
            return "game over"

    def restart(self):
        self.words = []
        self.game_over = False
        return "game restarted"


my_gallows = Gallows()
print(my_gallows.play('apple')) #➞ ['apple']
print(my_gallows.play('ear'))# ➞ ['apple', 'ear']
print(my_gallows.play('rhino'))# ➞ ['apple', 'ear', 'rhino']
print(my_gallows.words)# ➞ ['apple', 'ear', 'rhino']
# Words should be accessible.
print(my_gallows.restart()) #➞ "game restarted"
# Words list should be set back to empty.
print(my_gallows.play('hostess'))# ➞ ['hostess']
print(my_gallows.play('stash'))# ➞ ['hostess', 'stash']
print(my_gallows.play('hostess'))# ➞ "game over"
# Words cannot have already been said.
print(my_gallows.restart()) #➞ "game restarted"

print(my_gallows.play('apple'))# ➞ ['apple']
print(my_gallows.play('ear'))# ➞ ['apple', 'ear']
print(my_gallows.play('rhino'))# ➞ ['apple', 'ear', 'rhino']
# Corn does not start with an "o".
print(my_gallows.play('corn'))# ➞"game over"
print(my_gallows.words)# ➞ ['apple', 'ear', 'rhino']
print(my_gallows.restart())# ➞ "game restarted"
print(my_gallows.words)# ➞ []