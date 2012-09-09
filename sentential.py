#!/usr/bin/env python
"""
Main Methods
-----------------------------------

The following are all of the methods 
needed to apply logic rules and 
confirm that a Hilbert style proof is correct.

----
"""

import sys
import re
from syntax import Grammar


def fileToListOfParse(nameoffile):
    a = Grammar()
    b = a.syntax()
    file1 = open(nameoffile,'r')
    lst1 = []
    for line in file1:
        lst1.append(b.parseString(line))
    return lst1    
    
    
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



lst1 = fileToListOfParse('quacker2.txt')
print lst1[1].linenumber
print lst1[5].reason