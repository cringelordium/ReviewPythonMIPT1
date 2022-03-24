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
    return - ничего не возвращает, но записывает зашифрованный текст в result_file
    """
    result = ""
    source_file = open(source_file_way, "r") #читаем

    # encrypting file
    for line in source_file.readlines():
        result += encrypt_caesar_line(line, shift)
    source_file.close()

    # writing result
    result_file = open(result_file_way, "w") #пишем
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
