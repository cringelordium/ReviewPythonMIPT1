from global_var import alphabet_lower
from global_var import alphabet_upper


def encrypt_caesar_line(line, shift):
    """
    шифрование одной строки шифром цезаря
    line - строка для зашифровки
    shift - сдвиг 
    """
    result = ""
    for let in line:
        encrypt = alphabet_lower.find(let)
        if encrypt != -1:
            encrypt += shift
            encrypt %= len(alphabet_upper)
            result += alphabet_lower[encrypt]
        else:
            encrypt = alphabet_upper.find(let)
            if encrypt != -1:
                encrypt += shift
                encrypt %= len(alphabet_upper)
                result += alphabet_upper[encrypt]
            else:
                result += let
    return result
  

def caesar_encrypt(source_file_way, result_file_way, shift):
    """
    шифрование текста из файла шифром цезаря
    source_file_way - файл с исходным текстом
    result_file_way - файл куда будет сохранен результат 
    shift - сдвиг
    """
    result = ""

    # читаем
    source_file = open(source_file_way, "r")

    # encrypting file
    for line in source_file.readlines():
        result += encrypt_caesar_line(line, shift)
    source_file.close()

    # writing result
    result_file = open(result_file_way, "w")
    result_file.write(result)
    result_file.close()


def caesar_encrypt_interface():
    """
    Интерфейс (работает caesar_encrypt)
    return - ничего не возвращает
    """
    source_file_way = input("Enter the name of the file you want to encrypt: ")
    result_file_way = input("Enter the name of the file you want to save the result to: ")
    shift = int(input("Enter shift from 1 to 25: "))
    caesar_encrypt(source_file_way, result_file_way, shift)


def decrypt_caesar_line(line, shift):
    """
    расшифровка строки шифром цезаря
    return - расшифрованная строка
    """

    result = ""
    for let in line:
        find_res = alphabet_lower.find(let)
        if find_res != -1:
            find_res -= shift
            find_res %= len(alphabet_upper)
            result += alphabet_lower[find_res]
        else:
            find_res = alphabet_upper.find(let)
            if find_res != -1:
                find_res -= shift
                find_res %= len(alphabet_upper)
                result += alphabet_upper[find_res]
            else:
                result += let
    return result


def caesar_decrypt(source_file_way, result_file_way, shift):

    #дешифрование
    result = ""
    source_file = open(source_file_way, "r")

    # encrypting file
    for line in source_file.readlines():
        result += decrypt_caesar_line(line, shift)
    source_file.close()

    # writing result
    result_file = open(result_file_way, "w")
    result_file.write(result)


def caesar_decrypt_interface():
    """
    Интерфейс (caesar_decrypt)
    return - ничего не возвращает
    """
    source_file_way = input("Enter the name of the file you want to encrypt: ")
    result_file_way = input("Enter the name of the file you want to save the result to: ")
    shift = int(input("Enter shift from 1 to 25: "))
    caesar_decrypt(source_file_way, result_file_way, shift)


def caesar_hack(source_file_way, result_file_way):
    """
    Расшифровки шифра цезаря методом частотного анализа
    source_file_way - исходный файл с зашифрованным текстом
    result_file_way - файл куда будет сохранен декрипт
    """
    source_file = open(source_file_way, "r")

    # Подсчет количества букв
    counter = {}
    letters = 0
    for let in alphabet_lower:
        counter[let] = 0
    for line in source_file.readlines():
        for let in line.lower():
            if let in counter.keys():
                counter[let] += 1
                letters += 1

    # Находим самую часто входящую букву и считаем что в исходном тексте это была буква "e"
    counter = (list(counter.items()))
    counter.sort(key=lambda i: i[1], reverse=True)
    counter = list(map(lambda x: [x[0], x[1] / letters], counter))
    shift = alphabet_lower.find(counter[0][0]) - alphabet_lower.find("e")
    if shift < 0:
        shift = len(alphabet_upper) + shift

    caesar_decrypt(source_file_way, result_file_way, shift)


def caesar_hack_interface():
    """
    Интерфейс (caesar_hack)
    """
    source_file_way = input("Enter name of file you want decrypt: ")
    result_file_way = input("Enter name of file you want to save result to: ")
    caesar_hack(source_file_way, result_file_way)