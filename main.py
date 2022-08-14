from Cipher import *
Inp = input("Enter the text to be converted: ").upper().replace(" ","/")
Key = input("Enter the key: ")
Initialize(len(Inp))
pair(Inp, Key)

for i in code_pair: print(i)