# 1. een functie maken die groupinfo() heet en info van de groep weergeeft
# 2. een functie maken die encrypt_ceasar(plaintext, shift) encrypted text returnen
# 3. een functie maken die decrypt_caesar(ciphertext , shift) decrypted text returnen als een string
# 4. een functie maken die quadgram_fitness (text) heet libary importeren (dit is een beetje vaag)
# 5. een functie maken die solve_ceasar(ciphertext) heet en die de tekst naar EN vertaald en return als een plaint text

import english_quadgrams as quadgrams

def groupinfo():
    '''
    # 1. een functie maken die groupinfo() heet en info van de groep weergeeft

    :return:
    '''
    groupinfo = [
        ('1014917', 'Thijs Verkade', 'DINF-1A'),
        ('099506', 'Darren Siriram', 'DINF-1A'),
    ]
    groupInfoPrint = print(groupinfo)
    return groupInfoPrint


def encrypt_ceasar(plaintext, shift):
    '''
    2. een functie maken die encrypt_ceasar(plaintext, shift) encrypted text returnen

    :param plaintext:
    :param shift:
    :return:
    '''


    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    encrypt_ceasar = ''

    for i in plaintext:
        if i in alphabet:
            position = alphabet.find(i)
            new_position = (position + shift) % 26
            new_character = alphabet[new_position]
            encrypt_ceasar += new_character
        else:
            encrypt_ceasar += i

    result = print(encrypt_ceasar)
    return result


encrypt_ceasar('I came, I saw, I conquered', 10)


def decrypt_caesar(plaintext, shift):
    '''
    # 3. een functie maken die decrypt_caesar(ciphertext , shift) decrypted text returnen als een string

    :param plaintext:
    :param shift:
    :return:
    '''
    alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    decrypt_caesar = ''

    for i in plaintext:
        if i in alphabet:
            position = alphabet.find(i)
            new_position = (position - shift) % 26
            new_character = alphabet[new_position]
            decrypt_caesar += new_character
        else:
            decrypt_caesar += i
    result = print(str(decrypt_caesar))
    return result


decrypt_caesar('s mkwo, s ckg, s myxaeobon', 10)

def quadgram_fitness(text):
    '''
    @todo 4. een functie maken die quadgram_fitness (text) heet libary importeren (dit is een beetje vaag)
    A function called quadgram_fitness(text)
    that returns the quadgram fitnessof a string must be implemented.
    Definition and examples of quadgram fitnessare given above.
    The function must make use of the dictionaryquadgram_score in the provided file english_quadgrams.py, which must beimported (not copied!).

    Example: quadgram_fitness("Wkh glh kdv ehhq fdvw!")
     must return anumber that coincides with 280.9567026 to at least 5 decimal places.
    '''
    return

def solve_caesar(ciphertext):
    '''
    @todo 5. een functie maken die solve_ceasar(ciphertext) heet en die de tekst naar EN vertaald en return als een plaint text
    A function called solve_caesar(ciphertext)
    that returns the plaintext for aCaesar-encrypted ciphertext must be implemented.
    You can use quadgramanalysis to find the shift used, but the shift should not be output (just theplaintext).

    Example: solve_caesar("Lqdqlm ivl Kwvycmz!")
    must return "Divide andConquer!".
    '''
    return

