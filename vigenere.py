"""
student:shani dihorker
Assigment no.1
program:vigener
"""
import addlaters as add

def main():
    while True:
        try:
            user_input = input("Enter 'e' to encrypt or 'd' to decrypt: ")
            if user_input == 'e':
                key = input("Enter encryption key: ")
                file_name = input("Enter file name to encrypt: ")
                with open(file_name, 'r') as f:
                    plaintext = ''.join(c for c in f.read() if c.isalpha() or c == ' ')
                ciphertext = add.vigenere_encrypt(plaintext, key)

                with open('vig' + file_name, 'w') as f:
                    f.write(ciphertext)
                print("Encryption complete, saved to 'vig" + file_name + "'")
                break
            elif user_input == 'd':
                key = input("Enter decryption key: ")
                file_name = input("Enter file name to decrypt: ")
                with open(file_name, 'r') as f:
                    ciphertext = f.read()
                plaintext = add.vigenere_encrypt(ciphertext, key)
                with open('dec' + file_name, 'w') as f:
                    f.write(plaintext)
                print("Decryption complete, saved to 'dec" + file_name + "'")
                break
            else:
                print("Invalid input, try again")
        except Exception as e:
            print("An error occurred: ", e)
            break

if __name__ == '__main__':
    main()
