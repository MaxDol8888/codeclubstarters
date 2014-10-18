secret = ''
correct_letters = []
missed_letters = []


def check_letter(letter):
    in_word = letter.upper() in secret
    if in_word:
        correct_letters.append(letter)
    else:
        missed_letters.append(letter)
    return in_word


def hide_word():
    display = []
    for letter in secret:
        if letter in correct_letters or letter == ' ':
            display.append(letter)
        else:
            display.append('-')

    return ' '.join(display)