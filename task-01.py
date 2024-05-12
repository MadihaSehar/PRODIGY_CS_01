def caesar_cipher(text, shift, mode):
    encrypted_text = ''
    for char in text:
        if char.isalpha():  # check if the character is an alphabet
            shifted = ord(char) + shift if mode == 'encrypt' else ord(char) - shift
            if char.islower():
                if shifted > ord('z'):
                    shifted -= 26
                elif shifted < ord('a'):
                    shifted += 26
            elif char.isupper():
                if shifted > ord('Z'):
                    shifted -= 26
                elif shifted < ord('A'):
                    shifted += 26
            encrypted_text += chr(shifted)
        else:
            encrypted_text += char
    return encrypted_text

def main():
    while True:
        print("Choose an option:")
        print("1. Encrypt text")
        print("2. Decrypt text")
        print("3. Quit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            plaintext = input("Enter the text to encrypt: ")
            shift = int(input("Enter the shift value: "))
            encrypted_text = caesar_cipher(plaintext, shift, 'encrypt')
            print("Encrypted text:", encrypted_text)
        elif choice == '2':
            ciphertext = input("Enter the text to decrypt: ")
            shift = int(input("Enter the shift value: "))
            decrypted_text = caesar_cipher(ciphertext, shift, 'decrypt')
            print("Decrypted text:", decrypted_text)
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    main()
