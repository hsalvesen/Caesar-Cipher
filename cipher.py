# Encryption Function
def cipher(key, line) :
    # Initialise a string to hold encrypted message
    encrypted = ""
    # For each character
    for char in line:
        # Check if the current character an uppercase letter
        if char.isupper(): 
            # Check current character's index, from [0:A to 25:Z) range
            char_index = ord(char) - ord('A')
            # Shift the current character index right by given key position
            char_shift = (char_index + key) % 26 + ord('A')
            # Define what the new character is
            char_new = chr(char_shift)
            # Add character to encryption message
            encrypted += char_new
        # Check if current character is a lowercase letter
        elif char.islower():
             # Check current character's index, from [0:a to 25:) range
            char_index = ord(char) - ord('a') 
            # Shift the current character index right by given key position
            char_shift = (char_index + key) % 26 + ord('a')
            # Define what the new character is
            char_new = chr(char_shift)
            # Add character to encryption message
            encrypted += char_new
                        # # Check if the character is a digit
                        # elif char.isdigit():
                        #     # If it's a number, shift its actual value 
                        #     char_new = (int(char) + key) % 10
                        #     # Add character to encryption message
                        #     encrypted += str(char_new)
        # If the current character is non-alphabetical
        else:
            # Add it, as is
            encrypted += char
    # Return the new expression to the function call
    return encrypted
