# SpellingBeeSolver
Finds solutions to the NY Times word game Spelling Bee.

Outputs a text file containing valid words, sorted from longest to shortest, then alphabetically. It works fine, however NYT doesn't say where they get their word list from. This solver uses a tournament Scrabble list by default (twl06.txt) which is more broad than Spelling Bee. Unfortunately, until I prune the list or find a better way there are going to be some false positives.
