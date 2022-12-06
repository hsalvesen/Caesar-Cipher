# Import functions
import cipher
import decrypt

# Key
key = str(input("Enter key: "))

# Check if input is valid
try : 
    if key.isnumeric() and int(key) >= 0 and int(key) <= 26:
        # Convert key to an integer
        key = int(key)
        # Textline
        line = str(input("Enter line: "))

        # Check that the textline is valid
        if line.isspace() :
            # If textline is whitespace
            raise Exception("\nInvalid text!")

        # Key and textline are valid
        else :
            # Convert line to a list
            line = list(line)
            # Call the encrypt function to encrypt a given message
            encrypt = cipher.cipher(key, line)
            # Print the message to the terminal
            print("\n" + encrypt)

    # If key is not valid
    else :
        raise Exception("\nInvalid key!")
        
# Check if the input is invalid
except Exception as e :
    print(e)
                       
                       
                       
                       
                       
                        # # Call the decrypt function to decrypt a given message
                        # decryption = decrypt.decrypt(int(input("Enter key: ")), list(encrypt))
                        # # Print the message to the terminal
                        # print(decryption)
