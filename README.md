# wordle_bot
Wordle Bot Backend Code

This is a bot that uses a static algorithm to solve Wordle puzzles given a case insensitive answer input by the user in terminal. Here is an example of the terminal output from a user inputting "crane":

Wordle Answer: crane
Wordle Bot solution to : crane
Guess 1: alert
Guess 2: grace
Guess 3: crane
Puzzle solved in 3 guesses

There is bounds checking such that if an answer is input that is not a valid word on the wordle answers list, it will be rejected and the algorithm will not run. Here is an example of this:

Wordle Answer: invalid_input
Not a valid answer to Wordle

The written efficiency test shows the following output: (note the average guesses only averages the puzzles that were solved)

Average number of guesses: 3.6476232010466636
Number of words solved in one guess: 1
Number of words solved in two guesses: 130
Number of words solved in three guesses: 920
Number of words solved in four guesses: 921
Number of words solved in five guesses: 267
Number of words solved in six guesses: 54
Number of failed words: 22
Failed words: ['catch', 'daddy', 'foyer', 'gully', 'hatch', 'holly', 'joker', 'jolly', 'kitty', 'pound', 'rarer', 'shave', 'stash', 'taste', 'tatty', 'taunt', 'tight', 'vaunt', 'willy', 'witty', 'wooly', 'wound']