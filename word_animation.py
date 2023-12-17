import string
import time
lowercase_alphabets = list(string.ascii_lowercase)

text_to_animate = input().lower()
animated_text = ""
for character in text_to_animate:
    if character not in lowercase_alphabets:
        animated_text = animated_text + character
        print(animated_text)
    else:
        for alphabet in lowercase_alphabets:
            animated_text = animated_text + alphabet
            print(animated_text)
            if alphabet == character:
                break
            else:
                animated_text = animated_text[:len(animated_text)-1]
    time.sleep(0.1)