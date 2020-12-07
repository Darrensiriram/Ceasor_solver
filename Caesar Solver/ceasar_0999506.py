# 1. een functie maken die groupinfo() heet en info van de groep weergeeft 
# 2. een functie maken die encrypt_ceasar(plaintext, shift) encrypted text returnen 
# 3. een functie maken die decrypt_caesar(ciphertext , shift) decrypted text returnen als een string
# 4. een functie maken die quadgram_fitness (text) heet libary importeren (dit is een beetje vaag)
# 5. een functie maken die solve_ceasar(ciphertext) heet en die de tekst naar EN vertaald en return als een plaint text 

def groupinfo():
    groupinfo = ('099506', 'Darren Siriram' , 'DINF-1A', )
    groupInfoPrint = print(groupinfo)
    return groupInfoPrint

def encrypt_ceasar(plaintext , shift):
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
decrypt_caesar('s mkwo, s ckg, s myxaeobon' , 10)