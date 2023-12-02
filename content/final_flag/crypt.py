def crypt1(character, shift):
    if character.isupper():
        return chr((ord(character) + shift - 65) % 26 + 65)
    elif character.islower():
        return chr((ord(character) + shift - 97) % 26 + 97)
    return character

def crypt1_inv(character, shift):
    if character.isupper():
        return chr((ord(character) - shift + 65) % 26 + 65)
    elif character.islower():
        return chr((ord(character) - shift + 97) % 26 + 97)
    
    return character

def crypt2_and_crypt1(text, crypted2, crypted1):
    result = ""
    for char in text:
        if char.isalpha():
            crypted = ord(char) + crypted2
            if char.islower():
                if crypted > ord('z'):
                    crypted -= 26
                elif crypted < ord('a'):
                    crypted += 26
            elif char.isupper():
                if crypted > ord('Z'):
                    crypted -= 26
                elif crypted < ord('A'):
                    crypted += 26

            ciphered_char = crypt1(chr(crypted), crypted1)
            result += ciphered_char
        else:
            result += char
    return result

def crypt2_and_crypt1_inv(char, crypted2, crypted1):
    result = ""
    crypted = ord(char)
    if char.isalpha():
        crypted = ord(char) - crypted2
        if char.islower():
            if crypted > ord('z'):
                crypted -= 26
            elif crypted < ord('a'):
                crypted += 26
        elif char.isupper():
            if crypted > ord('Z'):
                crypted -= 26
            elif crypted < ord('A'):
                crypted += 26

        
    return chr(crypted)


def encrypt_file(file_path, crypted2, crypted1):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()

        encrypted_content = crypt2_and_crypt1(content, crypted2, crypted1)

        with open(file_path + '.encrypted', 'w', encoding='utf-8') as encrypted_file:
            encrypted_file.write(encrypted_content)

        print("File encrypted successfully.")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("An error occurred:", e)

def decrypt_file(text, crypted2, crypted1):
    result = ""
    for char in text:
    
        a = crypt1_inv(char, crypted1)
        b = crypt2_and_crypt1_inv(a , crypted2, crypted1)
        result += b

    print(result)

file_path = 'farewell'
crypted2 =  2 # Fake number, the real number is between 1-5
crypted1 =  5 # Fake number, the real number is between 1-5
cyphertext = """Op Sbjf, pa'z Khcpk.
Dl ohcl zohylk thuf aopunz avnlaoly, pujsbkpun aol nvhs vm ahrpun kvdu Hyhzhrh.
Pu aol luk, pa hss klwlukz vu tl zhjypmpjpun tfzlsm bzpun h klclsvwpun tpspahyf aljouvsvnf aoha P't wyvihisf uva ylhkf mvy.
P ovwl aoha hmaly hss, fvb dpss il hisl av ylhjo aol tvvu huk mbsmps fvby kylht.
P dvu'a il aolyl av zll pa, iba P dpss ohcl kvul lclyfaopun P jhu av zll fvb nla aolyl, huk aoha'z nvvk luvbno mvy tl.
Pm fvb ohcl ayvbisl dpao aol shza whya vm aol tpzzpvu, bzl aopz: UBDL{15j099hl678222h8m9l416jk5m250466}

Vul shza yltpukly: oaawz://ddd.fvbabil.jvt/dhajo?c=f57hCTLc8v4"""
#encrypt_file(file_path, crypted2, crypted1)
#print(crypt1_inv('U', 4))
#print(crypt2_and_crypt1_inv('Q', crypted2, crypted1))
print(decrypt_file(cyphertext, crypted2, crypted1))
# print(crypt1('Q', crypted1))
