# ----------------------Index Sub Cipher----------------------
from cgitb import text
from distutils import text_file
from operator import index
from platform import java_ver
from queue import Empty
from re import A, I
import string
from unittest import TextTestResult

def encryptIndexSubstitutionCipher(text):
    k = []
    lst = [i for i in range(ord('a'), ord('z') + 1)]
    for x in text:
        for y in lst:
            if x == chr(y):
                k.append(y)
    a = [x - 96 for x in k]
    stringA = []
    for i in a:
        if (i < 10):
            stringA.append("0" + str(i))
        else:
            stringA.append(str(i))
    new_list = (' '.join(stringA))

    return new_list


def decryptIndexSubstitutionCipher(text):
    k = 0
    t = []
    lst = [i for i in range(ord('a'), ord('z') + 1)]
    a = [x - 96 for x in lst]
    output = [str(x) for x in a]
    pt = []
    for i in output:
        if (int(i) < 10):
            pt.append('0' + i)
        else:
            pt.append(i)

    for x in text.split(' '):
        for y in pt:
            if x == y:
                k = int(x) + 96
                t.append(chr(k))
    new_list = (''.join(t))
    return new_list


# ----------------------Morse Code----------------------
morseCode = {
    'a': '._',
    'b': '_...',
    'c': '_._.',
    'd': '_..',
    'e': '.',
    'f': '.._.',
    'g': '__.',
    'h': '....',
    'i': '..',
    'j': '.___',
    'k': '_._',
    'l': '._..',
    'm': '__',
    'n': '_.',
    'o': '___',
    'p': '.__.',
    'q': '__._',
    'r': '._.',
    's': '...',
    't': '_',
    'u': '.._',
    'v': '..._',
    'w': '.__',
    'x': '_.._',
    'y': '_.__',
    'z': '__..'
}


def encryptMorseCode(text):
    k = []
    for x in text:
        for y in morseCode.keys():
            if x == y:
                k.append(morseCode[y])
    new_list = (' '.join(k))
    return new_list


def decryptMorseCode(text):
    k = []
    for x in text.split(' '):
        for key, value in morseCode.items():
            if x == value:
                k.append(key)
    new_list = (''.join(k))
    return new_list


# ----------------------Affine Cipher----------------------
def encryptAffineCipher(text, a, b):
    dict1 = {
        'a': '0',
        'b': '1',
        'c': '2',
        'd': '3',
        'e': '4',
        'f': '5',
        'g': '6',
        'h': '7',
        'i': '8',
        'j': '9',
        'k': '10',
        'l': '11',
        'm': '12',
        'n': '13',
        'o': '14',
        'p': '15',
        'q': '16',
        'r': '17',
        's': '18',
        't': '19',
        'u': '20',
        'v': '21',
        'w': '22',
        'x': '23',
        'y': '24',
        'z': '25'
    }
    k = []
    l = []
    for x in text:
        for key, value in dict1.items():
            if value == dict1[x]:
                formula = (a * int(dict1[x]) + b) % 26
                k.append(formula)
    for x in k:
        for a, b in dict1.items():
            if str(x) == b:
                l.append(a)
    m = (''.join(l))
    return m


def decryptAffineCipher(text, a, b, ):
    dict1 = {
        'a': '0',
        'b': '1',
        'c': '2',
        'd': '3',
        'e': '4',
        'f': '5',
        'g': '6',
        'h': '7',
        'i': '8',
        'j': '9',
        'k': '10',
        'l': '11',
        'm': '12',
        'n': '13',
        'o': '14',
        'p': '15',
        'q': '16',
        'r': '17',
        's': '18',
        't': '19',
        'u': '20',
        'v': '21',
        'w': '22',
        'x': '23',
        'y': '24',
        'z': '25'
    }
    k = []
    l = []
    for x in text:
        for key, value in dict1.items():
            if key == x:
                formula = ((pow(a, -1, 26)) * (int(dict1.get(key)) - b)) % 26
                k.append(formula)
    for x in k:
        for a, b in dict1.items():
            if str(x) == b:
                l.append(a)
    new_list = (''.join(l))
    return new_list


# ----------------------Caesar Cipher----------------------


def encryptCaesarCipher(text, key1, key2):
    string1 = ""
    x = string.ascii_lowercase
    k = string.ascii_uppercase
    converted = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')
    integer = 0
    for ch in text: 
        if ch in x:
         for y in x: 
            if y == ch and integer == 0:      
                key = key1%26
                if (ord(ch) + key) > ord('z'):
                    ch = chr(ord(ch)- (26 - key))
                    string1+=ch
                    integer+=1 
                    break
                else:
                    ch = chr(ord(y) + key) 
                    string1+=ch
                    integer+=1      
                    break
            elif ch == y and integer == 1:
                key = key2%26
                if (ord(ch) + key) > ord('z'):
                    ch = chr(ord(ch)- (26 - key))
                    integer-=1
                    string1 += ch
                    break          
                else:
                    ch = chr(ord(y)+ key)
                    integer-=1
                    string1 += ch
                    break
        elif ch in k:
            for i in k:
                if i == ch and integer == 0:        
                    key = key1%26
                    if (ord(ch) + key) > ord('Z'):
                        ch = chr(ord(ch)- (26 - key))
                        string1+=ch
                        integer+=1 
                        break
                    else:
                        ch = chr(ord(i) + key) 
                        string1+=ch
                        integer+=1      
                        break
                elif ch == i and integer == 1:
                    key = key2
                    if (ord(ch) + key) > ord('Z'):
                        ch = chr(ord(ch)- (26 - key))
                        integer-=1
                        string1 += ch
                        break               
                    else:
                        ch = chr(ord(i)+ key)
                        integer-=1
                        string1 += ch
                        break
        elif ch in converted:
            for l in converted:
                if l == ch and integer == 0: #'a'       
                    key = key1%10
                    if int(ch) + key > 9:
                        ch = str(int(ch) - (10 - key))
                        string1+=ch
                        integer+=1 
                        break
                    else:
                        ch = str(int(ch) + key) 
                        string1+=ch
                        integer+=1      
                        break
                elif ch == l and integer == 1:
                    key = key2%10
                    if int(ch)+ key > 9:
                        ch = str(int(ch) - (10 - key))
                        integer-=1
                        string1 += ch
                        break               
                    else:
                        ch = str(int(ch) + key)
                        integer-=1
                        string1 += ch
                        break                            
        elif ch not in x and ch not in k and ch not in converted:
            if integer == 0:
                integer+=1
                string1 += ch
            else:
                integer-=1
                string1 += ch  
    return string1


def decryptCaesarCipher(text, key1, key2):
    string1 = ""
    x = string.ascii_lowercase
    k = string.ascii_uppercase
    converted = ('0', '1', '2','3','4','5','6','7','8','9')
    integer = 0
    for ch in text: 
        if ch in x:
         for y in x: 
            if y == ch and integer == 0: #'a'       
                key = key1%26
                if (ord(ch) - key) < ord('a'):
                    ch = chr(ord(ch)+ (26 - key))
                    string1+=ch
                    integer+=1 
                    break
                else:
                    ch = chr(ord(y) - key) 
                    string1+=ch
                    integer+=1      
                    break
            elif ch == y and integer == 1:
                key = key2%26
                if (ord(ch) - key) < ord('a'):
                    ch = chr(ord(ch)+ (26 - key))
                    integer-=1
                    string1 += ch
                    break          
                else:
                    ch = chr(ord(y)- key)
                    integer-=1
                    string1 += ch
                    break
        elif ch in k:
            for i in k:
                if i == ch and integer == 0:        
                    key = key1%26
                    if (ord(ch) - key) < ord('A'):
                        ch = chr(ord(ch)+ (26 - key))
                        string1+=ch
                        integer+=1 
                        break
                    else:
                        ch = chr(ord(i) - key) 
                        string1+=ch
                        integer+=1      
                        break
                elif ch == i and integer == 1:
                    key = key2
                    if (ord(ch) - key) < ord('A'):
                        ch = chr(ord(ch)+ (26 - key))
                        integer-=1
                        string1 += ch
                        break               
                    else:
                        ch = chr(ord(i)- key)
                        integer-=1
                        string1 += ch
                        break
        elif ch in converted:
            for l in converted:
                if l == ch and integer == 0: #'a'       
                    key = key1%10
                    if int(ch) - key < 0:
                        ch = str(int(ch) + (10 - key))
                        string1+=ch
                        integer+=1 
                        break
                    else:
                        ch = str(int(ch) - key) 
                        string1+=ch
                        integer+=1      
                        break
                elif ch == l and integer == 1:
                    key = key2%10
                    if int(ch)- key < 0:
                        ch = str(int(ch) + (10 - key))
                        integer-=1
                        string1 += ch
                        break               
                    else:
                        ch = str(int(ch) - key)
                        integer-=1
                        string1 += ch
                        break                            
        elif ch not in x and ch not in k and ch not in converted:
            if integer == 0:
                integer+=1
                string1 += ch
            else:
                integer-=1
                string1 += ch  
    return string1
# ----------------------Transposition Cipher----------------------
def encryptTranspositionCipher(text, key):
    textList = []
    valueOfKey = key
    for i in range(0,len(text),key):
        textList.append(text[i:valueOfKey])
        valueOfKey += key
    count = 0
    string = ""
    for k in range(len(textList[0])):
        for i in textList: 
            if(count < len(i)) :
                string += i[count] 
        count += 1 
    return string
    
   

def decryptTranspositionCipher(text, key):
    x = int(len(text)/key) + 1 
    y = len(text)%key 
    
    arr = []
    count = 0
    jumping = x
    while(y != 0):
        arr.append(text[count:jumping])
        count = jumping
        jumping += x
        y -= 1
    
    new =  []
    loop = 0
    jumping = jumping -1
    while(loop <= len(text) - len("".join(arr))):
        arr.append(text[count:jumping])
        count = jumping
        jumping += x-1
        loop += 1
    count = 0
    lst = []
    string = ""
    for k in range(len(arr[0])):
        for i in arr: 
            if(count < len(i)) :

                lst.append(i[count])
        count += 1 
    new = (''.join(lst))
    return new