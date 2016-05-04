﻿import matplotlib 
import matplotlib.pyplot as plt 



M=set(['TV', 'phone', 'camera', 'fridger', 'mixer', 'audio', 'cd player', 'light', 'computer', 'notebook', 'recorder']) 
F=set(['coffee machine', 'radio', 'camera', 'running machine', 'ramp', 'computer', 'notebook', 'recorder']) 
M1=['TV', 'phone', 'camera', 'fridger', 'mixer', 'audio', 'cd player', 'light', 'computer', 'notebook', 'recorder'] 
F1=['coffee machine', 'radio', 'camera', 'running machine', 'ramp', 'computer', 'notebook', 'recorder'] 
sentence = "sangmyung university" 
word = "sangmyung university, 20, honggimun 2-gil, jongno-gu, seoul, republic of korea" 

 
def charCount(sentence): 
   d=dict() 
   for c in sentence: 
      if c not in d: 
         d[c]=1 
             else: 
                   d[c]=d[c]+1 
       print d 
        plt.bar(range(0,len(d)),d.values(), align='center') 
        plt.xticks(range(0,len(d)),list(d.keys())) 
        plt.show() 
def countDigitsLetters(word): 
   d={"number":0, "word":0} 
      for c in word: 
      if c.isdigit()==True: 
         d["number"]=d["number"]+1 
      elif c.isdigit()==False: 
         d["word"]=d["word"]+1 
        print d 
        plt.bar(range(0,len(d)),d.values(), align='center') 
        plt.xticks(range(0,len(d)),list(d.keys())) 
        plt.show() 
 
def myhome(): 
    print M.difference(F) 

 
def friendhome(): 
    print F.difference(M) 
 
 
def myhomeOrfriendhome(): 
    print M.intersection(F) 
 
 
def myhomeAndfriendhome(): 
    print M1+F1 
    for c in F1: 
        M1.append(c) 
    d=dict() 
    for e in M1: 
       if e not in d: 
            d[e]=1 
       else: 
            d[e]=d[e]+1 
    print d 
 
 
 
 
 
 
def lab9(): 
     charCount(sentence) 
     countDigitsLetters(word) 
     myhome() 
     friendhome() 
     myhomeOrfriendhome() 
     myhomeAndfriendhom() 
 
 
def main(): 
   lab9() 
      
 
 
if __name__=="__main__": 
   main() 