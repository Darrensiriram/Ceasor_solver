# 1. een functie maken die groupinfo() heet en info van de groep weergeeft
# 2. een functie maken die encrypt_ceasar(plaintext, shift) encrypted text returnen
# 3. een functie maken die decrypt_caesar(ciphertext , shift) decrypted text returnen als een string
# 4. een functie maken die quadgram_fitness (text) heet libary importeren (dit is een beetje vaag)
# 5. een functie maken die solve_ceasar(ciphertext) heet en die de tekst naar EN vertaald en return als een plaint text

import english_quadgrams as quadgrams
import sys

alphabet = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

def groupinfo():
    '''
    # 1. een functie maken die groupinfo() heet en info van de groep weergeeft
    :return:
    '''
    groupinfo = [
        ('1014917', 'Thijs Verkade', 'DINF-1A'),
        ('099506', 'Darren Siriram', 'DINF-1A'),
    ]
    
    result = groupinfo
    
    return result

def encrypt_ceasar(plaintext, shift):
    '''
    2. een functie maken die encrypt_ceasar(plaintext, shift) encrypted text returnen

    :param plaintext:
    :param shift:
    :return:
    '''
    encrypt_ceasar = ''

    for i in plaintext:
        if i in alphabet:
            position = alphabet.find(i)
            new_position = (position + shift) % 26
            new_character = alphabet[new_position]
            if i.isupper():
                new_character = new_character.upper()
            encrypt_ceasar += new_character
        else:
            encrypt_ceasar += i

    result = encrypt_ceasar

    return result


def decrypt_caesar(plaintext, shift):
    '''
    # 3. een functie maken die decrypt_caesar(ciphertext , shift) decrypted text returnen als een string
    :param plaintext:
    :param shift:
    :return:
    '''

    decrypt_caesar = ''

    for i in plaintext:
        if i in alphabet:
            position = alphabet.find(i)
            new_position = (position - shift) % 26
            new_character = alphabet[new_position]
            if i.isupper():
                new_character = new_character.upper()
            decrypt_caesar += new_character
        else:
            decrypt_caesar += i
    result = str(decrypt_caesar)

    return result


def quadgram_fitness(text):
    '''
    @todo 4. een functie maken die quadgram_fitness (text) heet libary importeren (dit is een beetje vaag)
    A function called quadgram_fitness(text)
    that returns the quadgram fitness of a string must be implemented.
    Definition and examples of quadgram fitnessare given above.
    The function must make use of the dictionaryquadgram_score in the provided file english_quadgrams.py, which must beimported (not copied!).

    Example: quadgram_fitness("Wkh glh kdv ehhq fdvw!")
     must return anumber that coincides with 280.9567026 to at least 5 decimal places.

    :param text:
    :return:
    '''

    newtext = ''
    score = 0

    for i in range(len(text)):
        count = 0
        if text[i] in alphabet:
            while len(newtext) < 4:
                newIndex = i + count
                if newIndex in range(len(text)):
                    newVal = text[newIndex]
                    if newVal in alphabet:
                        newtext += newVal.lower()
                    count += 1
                else:
                    # score = format(round(score, 7))
                    return score
            if newtext in quadgrams.quadgram_score:
                score = score + quadgrams.quadgram_score[newtext]
            else:
                score = score + 23
            newtext = ''


def solve_caesar(ciphertext):
    '''
    @todo 5. een functie maken die solve_ceasar(ciphertext) heet en die de tekst naar EN vertaald en return als een plaint text
    A function called solve_caesar(ciphertext)
    that returns the plaintext for aCaesar-encrypted ciphertext must be implemented.
    You can use quadgramanalysis to find the shift used, but the shift should not be output (just theplaintext).

    Example: solve_caesar("Lqdqlm ivl Kwvycmz!")
    must return "Divide and Conquer!".
    '''
    list = []

    for shift in range(len(alphabet)):
        translated = ''
        for symbol in ciphertext:
            if symbol in alphabet:
                num = alphabet.find(symbol)
                num -= shift
                if num < 0:
                    num += len(alphabet)
                new_character = alphabet[num].lower()
                if symbol.isupper():
                    new_character = new_character.upper()
                translated += new_character
            else:
                translated += symbol
        info = {'text': translated, 'code': quadgram_fitness(translated), 'shift': shift}
        list.append(info)

    return min(list, key=lambda x:x['code'])['text']

