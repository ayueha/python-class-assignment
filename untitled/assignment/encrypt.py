
def getMode():
    while True:
        print('Choose mode e(encrypt) or d(decrypt)')
        mode = input().lower()
        if mode == 'e' or mode =='d':
            return mode

def getTranslatedMessage(mode):
    if mode == 'd':
        key = -5
        fileName = 'encrypted.txt'
        outputfile = 'target-decrypted.txt'
    else:
        key = 5
        fileName ='target-encryption.txt'
        outputfile = 'encrypted.txt'

    targetFile = open(fileName, 'r')
    translated = ''
    for line in targetFile:
        for letter in line:
            if letter.isalpha():
                if letter.isupper():
                    letter = letter.lower();

                num = ord(letter)
                num += key

                if num > ord('z'):
                    num -= 26
                elif num < ord('a'):
                    num += 26

                translated += chr(num)
            else:
                translated += letter

    targetFile.close();

    writeFile = open(outputfile, 'w')
    writeFile.write(translated)
    writeFile.close();
    #writeFile = open(translated, 'w')


mode = getMode()
getTranslatedMessage(mode)
