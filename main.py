from Cipher import *
TempList=[]
CheckList=[]
AlphaList=[]
Inp = input("Enter the text to be converted: ").upper().replace(" ","/")
Key = input("Enter the key: ")
pair(Inp, Key)

#for i in code_pair: print(i)

for i in ascii_uppercase+digits:
  AlphaList.append(i)

for i in code_pair:
  TempList.extend(AlphaList[code_pair[i][1]-1,len(code_pair)])
  for j in TempList:
    for k in AlphaList:
      CheckList.append(j,k)
  for l in CheckList:
    if code_pair[i][0] == l[0]:
      print (l[1])