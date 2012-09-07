#!/usr/bin/env python
"""
Main Methods
-----------------------------------

The following are all of the methods 
needed to apply logic rules and 
confirm that a Hilbert sle proof is correct.

----
"""

import sys
import re


def filetodict(nameoffile):
    file1 = open(nameoffile,'r')
    dict1 = {}
    for line in file1:
        lst1 = line.strip().split('//')
        dict1[lst1[0]] = filetodicthelper(lst1)
    file1.close()
    return dict1
    
        

def filetodicthelper(lst1):
    lst2 = []
    lst2.append(lst1[1])
    lst3 = lst1[2].split(' ')
    lst2.append(lst3[0])
    
    if len(lst3) > 1:
        lst4 = lst3[1].split(',')
        for element in lst4:
            lst2.append(element)
        return lst2
    else:
        if len(lst3) == 2:
            lst2.append(lst3[1])
        return lst2
    
    
def Pr(dict1,line):
    return True

def EI(dict1,line):
    line2 = dict1[line][-1]
    p = re.compile(dict1[line2][0][9])
    str1 = dict1[line2][0][12:-1]
    str1 = re.sub(p,'[a-z]',str1)
    str1 = re.sub(r'\*','\*',str1)
    p = re.compile(str1)
    return bool(p.match(dict1[line][0]))
    
def Simp(dict1,line):
    line2 = dict1[line][-1]
    return dict1[line][0] in dict1[line2][0].split('*')

def MP(dict1,line):
    line2 = dict1[line][-2]
    line3 = dict1[line][-1]
    str1 = dict1[line3][0] + '->' + dict1[line][0]
    return str1 == dict1[line2][0]

def EG(dict1,line):
    line2 = dict1[line][-1]
    p = re.compile(dict1[line][0][9])
    str1 = dict1[line][0][12:-1]
    str1 = re.sub(p,'[a-z]',str1)
    str1 = re.sub(r'\*','\*',str1)
    p = re.compile(str1)
    return bool(p.match(dict1[line2][0]))

def Conj(dict1,line):
    line2 = dict1[line][-2]
    line3 = dict1[line][-1]
    str1 = dict1[line2][0] + '*' + dict1[line3][0]
    return str1 == dict1[line][0]

def UI(dict1,line):
    line2 = dict1[line][-1]
    p = re.compile(dict1[line2][0][1])
    str1 = dict1[line2][0][4:-1]
    str1 = re.sub(p,'[a-z]',str1)
    str1 = re.sub(r'\*','\*',str1)
    p = re.compile(str1)
    return bool(p.match(dict1[line][0]))

    
def verifydict(dict1):
    lst = []
    for i in dict1:
        lst.append(eval(dict1[i][1] + '(dict1, i)'))
    return all(lst)



dict1 = filetodict('quacker.txt')
print dict1
print verifydict(dict1)