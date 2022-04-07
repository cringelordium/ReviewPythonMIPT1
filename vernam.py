from global_var import alphabet_upper
import random


def vernam_encrypt(source_file_way, result_file_way, result_key_file_way, seed):
    """
    Шифрование методом Вернама.
    Генерирует случайный ключ из сида.
    result_key_file_way - файл куда будет сохранен ключ
    seed - сид из которого будет сгенерирован случайный ключ
    return - ничего не возвращает, но запысывает зашифрованный текст в result_file и ключ в result_key_file
    """

    result = ""
    result_key = ""
    with open(source_file_way, "r") as source_file:

        random.seed(seed)

        # encrypting file
        for line in source_file:
            # preparing keyword
            new_line = ""

            for i in line.upper():
                if i in alphabet_upper:
                    new_line += i
            line = new_line

            tmp = ""
            for i in range(len(line)):
                tmp += alphabet_upper[random.randint(0, 25)]
            keyword = tmp

            for let, klet in zip(line, keyword):
                found_let = alphabet_upper.find(let)
                found_key_let = alphabet_upper.find(klet)
                result += alphabet_upper[(found_let + found_key_let) % len(alphabet_upper)]

            result_key += keyword

    # writing result
    with open(result_file_way, "w") as source_file:
        source_file.write(result)
    with open(result_key_file_way, "w") as result_key_file:
        result_key_file.write(result_key)


def vernam_encrypt_interface():
    """
    Интерфейс для работы в консоли с функцией vernam_encrypt
    return - Ничего не возвращает
    """
    source_file_way = input("Enter the name of the file you want encrypt: ")
    result_file_way = input("Enter the name of the file you want to save the result to: ")
    new_key_file_way = input("Enter the name of the file with key name or absolute way: ")
    seed = input("Enter seed to generate random key: ")
    vernam_encrypt(source_file_way, result_file_way, new_key_file_way, seed)


def vernam_decrypt(source_file_way, result_file_way, key_file_way):
    """
    Дешифрование
    key_file_way - файл с ключом
    return - ничего не возвращает, но записывает результат дешифрования в result_file
    """
    result = ""

    with open(source_file_way, "r") as source_file:
        with open(key_file_way, "r") as key_file:

            # encrypting file
            for let, klet in zip(source_file.read(), key_file.read()):
                found_let = alphabet_upper.find(let)
                found_key_let = alphabet_upper.find(klet)
                result += alphabet_upper[(found_let - found_key_let) % len(alphabet_upper)]

    # writing result
    with open(result_file_way, "w") as result_file:
        result_file.write(result)


def vernam_decrypt_interface():
    """
    Интерфейс
    """
    source_file_way = input("Enter the name of the file you want decrypt: ")
    result_file_way = input("Enter the name of the file you want to save the result to: ")
    key_file_way = input("Enter the name of the file with key: ")
    vernam_decrypt(source_file_way, result_file_way, key_file_way)
