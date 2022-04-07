from caesar import caesar_encrypt_interface, caesar_decrypt_interface, caesar_hack_interface
from vigenere import vigenere_encrypt_interface, vigenere_decrypt_interface
from vernam import vernam_encrypt_interface, vernam_decrypt_interface

def hello():
    print("ENCRYPTOR v1.0 BY CRINGELORD (Aitimov Akezhan)")


def quit_program():
    quit()


def print_interface(menu_options):
    print("Start the Encryption:")
    for key in menu_options:
        print(key, ": ", menu_options[key]["text"], sep="")


print('-----------------------------------------------')


if __name__ == "__main__":
    menu_options = {"q": {"function": quit_program, "text": "QUIT"},
                    "1": {"function": caesar_encrypt_interface, "text": "Caesar encryption"},
                    "2": {"function": caesar_decrypt_interface, "text": "Caesar decryption"},
                    "3": {"function": caesar_hack_interface, "text": "Caesar Hack"},
                    "4": {"function": vigenere_encrypt_interface, "text": "Vigenere encryption"},
                    "5": {"function": vigenere_decrypt_interface, "text": "Vigenere decryption"},
                    "6": {"function": vernam_encrypt_interface, "text": "Vernam encryption"},
                    "7": {"function": vernam_decrypt_interface, "text": "Vernam decryption"}}
    hello()
    keepWorking = True
    while keepWorking:
        menuSelection = ""
        while menuSelection not in menu_options.keys():
            print_interface(menu_options)
            menuSelection = input().lower()
        menu_options[menuSelection]["function"]()
