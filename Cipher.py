from string import *
code_pair=[]
global loop1
loop1=False
global num
num=0



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







