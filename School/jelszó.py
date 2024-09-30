import random

def safe(jelszo):
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", " ", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "!", "?", ".", ",", ";", ":", "\"", "'", "-", "_", "/", "\\", "@", "#", "$", "%", "^", "&", "*", "(", ")", "{", "}", "[", "]"]
  
    próbált_jelszo = ""
    probálkozások = 0
  
    while jelszo != próbált_jelszo:
        próbált_jelszo = ""
        probálkozások += 1
        for i in range(len(jelszo)):
            próbált_jelszo += random.choice(letters)
    
    print(f"Próbálkozások száma: {probálkozások}")
    print(f"A jelszó: {próbált_jelszo}")


password = input("Adj meg egy jelszót: ")
safe(password)
