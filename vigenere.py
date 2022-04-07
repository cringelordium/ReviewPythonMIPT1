from global_var import alphabet_upper
from itertools import cycle


def vigenere_encrypt(source_file_way, result_file_way, key_word):
    """
    Шифрование шифром Виженера.
    (все буквы будут переведены в верхний регистр, а остальные символы удалены)
    source_file_way - файл с исходным текстом
    result_file_way - файл с результатом шифрования
    key_word - ключевое слово шифра Виженера
    ретерн ничего не возвращает, но запысывает зашифрованный текст в result_file
    """
    result = ""
    with open(source_file_way, "r") as source_file:

        new_text = ""
        # подготовка файла
        for line in source_file.readlines():
            for i in line.upper():
                if i in alphabet_upper:
                    new_text += i

    # подготовка ключевого слова
    tmp = ""
    for i in key_word.upper():
        if i in alphabet_upper:
            tmp += i
    key_word = tmp

    #основной шифратор
    encryptor = lambda arg: alphabet_upper[(alphabet_upper.index(arg[0]) + alphabet_upper.index(arg[1]) % 26) % 26]
    result += ''.join(map(encryptor, zip(new_text, cycle(key_word))))

    # пишем результат
    with open(result_file_way, "w") as result_file:
        result_file.write(result)


def vigenere_encrypt_interface():
    """
    интерфейс шифровальщика (vigenere_encrypt)
    :return: Ничего не возвращает
    """
    print("Enter the name of file you want decrypt: i took the file. Interface check")
    source_file_way = input("Enter the name of file you want encrypt: ")
    result_file_way = input("Enter the name of file you want to save the result to: ")
    key_word = input("Enter keyword: ")
    vigenere_encrypt(source_file_way, result_file_way, key_word)


def vigenere_decrypt(source_file_way, result_file_way, key_word):
    """
    расшифровкg шифра Виженера.
    source_file_way - файл с исходным текстом
    result_file_way - файл с результатом
    key_word - ключевое слово
    return - ничего не возвращает, но запысывает расшифрованный текст в result_file
    """
    result = ""

    with open(source_file_way, "r") as source_file:

        new_text = ""
        # подготовка файла
        for line in source_file.readlines():
            for i in line.upper():
                if i in alphabet_upper:
                    new_text += i

    # подготовка ключевого слова
    tmp = ""
    for i in key_word.upper():
        if i in alphabet_upper:
            tmp += i
    key_word = tmp

    # дешифрование
    for i in range(len(new_text)):
        result += alphabet_upper[alphabet_upper.find(new_text[i]) - alphabet_upper.find(key_word[i % len(key_word)])]

    # пишем результат
    with open(result_file_way, "w") as result_file:
        result_file.write(result)


def vigenere_decrypt_interface():
    """
    интерфейс расшифровщика (vigenere_decrypt)
    (ретерн ничего не возвращает)
    """
    source_file_way = input("Enter the name of file you want decrypt: ")
    result_file_way = input("Enter the name of file you want to save the result to: ")
    key_word = input("Enter keyword: ")
    vigenere_decrypt(source_file_way, result_file_way, key_word)
