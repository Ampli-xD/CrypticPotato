from string import *
B_Map=[]
B_Key=[]
code_pair=[]
global loop1
loop1=False
global num
num=0
#def Initialize(length):
#  x=0
#  while x!=10000:
#    for i in ascii_uppercase+digits:
#      B_Map.append(i)
#    x+=1
#  return B_Map


def pair(Inp, Key):
  global loop1

  global num
  for i in Inp:
    if i == "/":
      code_pair.append(("*",i))
    else:
      
      if num != len(Key):
        loop1=True
        while loop1 is True:
          code_pair.append((Key[num],i))
          num=num+1
          loop1 = False
      else:
        num=0
        loop1=True
        while loop1 is True:
          code_pair.append((Key[num],i))
          num=num+1
          loop1 = False
        
  return code_pair







