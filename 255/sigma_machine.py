import keyboard

# keylamp is a list of letters
keylamp = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z']

# plugboard is a list of letters that will be swapped
plugboard = []
user_input = ''

# get the plugboard configuration from the user
while user_input != 'exit' and len(plugboard) < 26:
    if user_input in plugboard:
        print("Already in plugboard")
        user_input = ''
    else:
        user_input = input(
            f"Enter a letter to add to the plugboard for letter {keylamp[len(plugboard)]} (or type 'exit' to finish): ")
        if user_input in keylamp and user_input not in plugboard:
            plugboard.append(user_input)
            user_input = ''
        elif user_input == 'exit':
            break
        else:
            print("Invalid input.")

# fill the rest of the plugboard with letters
for letter in keylamp:
    if letter not in plugboard:
        plugboard.append(letter)

# right shift
right_shift_factor = 6
right_shift = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z']
for i in range(right_shift_factor):
    # get the last letter and move it to the front
    letter = right_shift.pop()
    right_shift.insert(0, letter)

# left shift
left_shift_factor = 15
left_shift = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
              'v', 'w', 'x', 'y', 'z']
for i in range(left_shift_factor):
    # get the first letter and move it to the end
    letter = left_shift.pop(0)
    left_shift.append(letter)

print("Plugboard configuration:", plugboard)
print("Right shift configuration:", right_shift)
print("Left shift configuration:", left_shift)

original_word = ""
shifted_word = ""
print("Press backspace to exit.")
while True:
    encrypt_mode = False
    # check if the user wants to exit
    if keyboard.read_key() == 'backspace':
        break

    # get the letter from the user
    letter = keyboard.read_key()

    # check if spacebar is pressed
    if letter == 'space':
        original_word += " "
        shifted_word += " "
        continue

    original_word += letter
    print(original_word)

    if letter == 'space':
        original_word += " "
        shifted_word += " "
        continue

    if encrypt_mode:
        # Encryption
        plugboard_index = plugboard.index(letter)
        right_shift_letter = right_shift[plugboard_index]   # get the letter from the right shift
        right_shift_index = right_shift.index(right_shift_letter)   # get the index of the letter in the right shift
        left_shift_letter = left_shift[right_shift_index]   # get the letter from the left shift
        left_shift_index = left_shift.index(left_shift_letter)  # get the index of the letter in the left shift
        keylamp_letter = keylamp[keylamp.index(left_shift_letter)]  # get the letter from the keylamp
        shifted_word += keylamp_letter  # add the letter to the shifted word
        print("Encrypted so far:", shifted_word)

    else:
        # Decryption
        keylamp_index = keylamp.index(letter)
        left_shift_letter = keylamp[keylamp_index]  # this is the encrypted letter
        left_shift_index = left_shift.index(left_shift_letter)  # find its position in left shift
        right_shift_letter = right_shift[left_shift_index]  # use same index to get from right shift
        right_shift_index = right_shift.index(right_shift_letter)  # find this letter's position in right shift
        plugboard_letter = plugboard[right_shift_index]  # map back through plugboard
        shifted_word += plugboard_letter  # append decrypted letter
        print("Decrypted so far:", shifted_word)

