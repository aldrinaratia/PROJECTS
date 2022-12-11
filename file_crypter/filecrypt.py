#!/usr/bin/python
# -*- coding: UTF-8 -*-

from cryptography.fernet import Fernet


def menu():
    test = """
    Description : filecrypt
    Author : AL Drin
    Version: v1.0
        
    File Extension: ALL TYPE OF FILE
    NOTE: extension i already test
        exe,elf, txt,png,jpg,py,java,c,h,ps1,vbs,vba,cpp,sh,go,rb,lua
    
    ENCRYPTION 
    file auto generate key after select encrypt
    keep your key "encryptionkey.key" and file "secret.txt" 
    away in this directory after encryption done
    
    DECRYPTION 
    To decyrpt your file add in this directory the key 
    "encryptionkey.key" and filename "secret.txt"
    
    !!! NOTE !!! 
    Make sure your key and filename correct path or else you endup 'InvalidToken'
    
    """
    return test
print(menu())

def main():
    option = input("Encrypt = 'e' or Decrypt = 'd' file? (e/d): ")

    if option.lower() == "e" or option == "Encrypt" or option == "encrypt" or option == "E" or option == option.upper():
        key = Fernet.generate_key()
        with open('encryptkey.key', 'wb') as encryptkey:
           encryptkey.write(key)

        fernet = Fernet(key)

        user_file_encp = input("Enter file name: ")

        try:
            with open(user_file_encp, 'rb') as file:
                original_file = file.read()
        except FileNotFoundError:
            speak8 = " FILE NOT FOUND "
            print(speak8)

        encrypt = fernet.encrypt(original_file)

        with open(user_file_encp, 'wb') as encp_file:
            encp_file.write(encrypt)
            speak1 = " Your file is encrypted "
            speak2 = " Move file, key from this directory after encryption "
            print(speak1)
            print(speak2)

    elif option.lower() == "d" or option == "Decrypt" or option == "decrypt" or option == "D" or option == option.upper() :
        speak6 = "\nFILE AND KEY MUST BE UPLOADED IN THIS DIRECTORY BEFORE DECRYPTION "
        print(speak6)
        user_file_decp = input("Enter file name: ")

        with open('encryptkey.key', 'rb') as encp_key:
            read_enc_key = encp_key.read()

        fernet = Fernet(read_enc_key)

        try:
            with open(user_file_decp, 'rb') as read_encp_file:
                encrypted_file  = read_encp_file.read()
        except FileNotFoundError:
            speak7 = " FILE AND KEY NOT FOUND "
            print(speak7)

        decrypt = fernet.decrypt(encrypted_file)

        with open(user_file_decp, 'wb') as decp_file:
            decp_file.write(decrypt)
            speak10 = " Your file is decrypted "
            speak11 = " Move file, key from this directory after decryption "
            print(speak10)
            print(speak11)

    else:
        speak12 = " INVALID OPTION "
        print(speak12)

if __name__ == "__main__": 
    main()