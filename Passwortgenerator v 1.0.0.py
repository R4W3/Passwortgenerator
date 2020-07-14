print("Passwortgenerator v 1.0.0")
print("Ein Service der RE IT Dienstleistungen")
print("https://github.com/R4W3/Passwortgenerator")
import random
x = ["a", "b", "d", "c", "e", "f", "g", "h", "j", "i", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "y", "x", "z", "A", "B", "D", "C", "E", "F", "G", "H", "J", "I", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "Y", "X", "Z","1", "2", "3", "4", "5", "6", "7", "8", "9", "#", "§", "$", "!", "%", "&", "/", "(", ")", "=", "?"]
random.shuffle(x)
random.shuffle(x)
length = input("Passwortlänge (ganzzahlig): ")
y = random.sample(x, int(length))
str1 = ''.join(y)
print("Dein Passwort lautet:" , str1)
