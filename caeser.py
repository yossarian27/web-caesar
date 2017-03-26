def alphabet_position(letter):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    letter = letter.lower()
    position = alphabet.find(letter)
    return position
    #returns 0-based numerical position of letter in alphabet


def rotate_character(char, rot):
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    if char not in alphabet:
        return char
    else:
        newposition = alphabet_position(char) + rot
        newchar = ""
        if newposition < 26:
            newchar += alphabet[newposition]
            if char == char.upper():
                return newchar.upper()
            else:
                return newchar
        else:
            newchar += alphabet[newposition % 26]
            if char == char.upper():
                return newchar.upper()
            else:
                return newchar

def encrypt(text, rot):
    newtext = ""
    for i in text:
        newchar = rotate_character(i, rot)
        newtext = newtext + newchar
    return newtext
