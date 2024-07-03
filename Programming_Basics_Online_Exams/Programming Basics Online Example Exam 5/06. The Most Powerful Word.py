command = input()
winning_first_letters = "aeiouyAEIOUY"
most_powerful_word = ""
max_result = 0

while command != "End of words":
    current_word = command
    current_result = 0
    for letter in current_word:
        ascii_value = ord(letter)
        current_result += ascii_value

    if current_word[0] in winning_first_letters:
        current_result *= len(current_word)
    else:
        current_result /= len(current_word)
        current_result = int(current_result)

    if current_result > max_result:
        max_result = current_result
        most_powerful_word = current_word
    command = input()

print(f"The most powerful word is {most_powerful_word} - {max_result}")

# test inputs:

# The
# Most
# Powerful
# Word
# Is
# Experience
# End of words

# But
# Some
# People
# Say
# It's
# LOVE
# End of words
