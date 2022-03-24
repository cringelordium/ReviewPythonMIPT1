from caesar import caesar_encrypt_int

def hello():
    print("ENCRYPTOR v0.1 BY CRINGELORD (Aitimov Akezhan)")


def quit_program():
    quit()


def print_menu(menu_options):
    print("Start the Encryption:")
    for key in menu_options:
        print(key, ": ", menu_options[key]["text"], sep="")


if __name__ == "__main__":
    menu_options = {"q": {"function": quit_program, "text": "QUIT"},
                    "1": {"function": caesar_encrypt_int, "text": "Caesar encrypt"}}
    hello()
    keepWorking = True
    while keepWorking:
        menuSelection = ""
        while menuSelection not in menu_options.keys():
            print_menu(menu_options)
            menuSelection = input().lower()
        menu_options[menuSelection]["function"]()
