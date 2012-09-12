#!/usr/bin/env python
"""
Main Methods
-----------------------------------

The following are all of the methods 
needed to apply logic rules and 
confirm that a Hilbert style proof is correct.

Arguments given to each method are the line
number of the statement and any line numbers
needed to check for validity.

----
"""

import sys
import re
from syntax import Grammar


def file_to_list_of_parsed(nameoffile):
    """
    Takes a file and returns a list of parsed lines.
    This can then be used to verify the proof.
    """
    a = Grammar()
    b = a.syntax()
    file1 = open(nameoffile,'r')
    parsed = []
    for line in file1:
        parsed.append(b.parseString(line))
    return parsed
    
    
def pr(line_number):
    return True

def ei(line_number1, line_number2):
    dict1 = {}
    compare1 = parsed[int(line_number1) - 1].expr[2]
    compare2 = parsed[int(line_number2) - 1].expr
    for i in range(len(compare1)):
        try:
            if not compare1[i].islower():
                if not compare1[i] == compare2[i]:
                    return False
            else:
                if compare1[i] in dict1:
                    if not dict1[compare1[i]] == compare2[i]:
                        return False
                else:
                    dict1[compare1[i]] = compare2[i]
        except:
            return False
    return True
    
def simp(line1, line2):
    str1 = ''.join(list(parsed[int(line2) - 1].expr))
    str2 = ''.join(list(parsed[int(line1) - 1].expr))
    lst1 = str2.split('*')
    return str1 in lst1

def mp(line1, line2, line3):
    lst1 = list(parsed[int(line3)-1].expr)
    lst2 = list(parsed[int(line2)-1].expr)
    str1 = ''.join(lst2) + '->' + ''.join(lst1)
    str2 = ''.join(list(parsed[int(line1)-1].expr))
    return str1 == str2
    

def eg(line1, line2):
    """
    The inverse of EI.
    """

def conj(line1, line2, line3):
    str1 = ''.join(list(parsed[int(line1)-1].expr))
    str1 += '*' + ''.join(list(parsed[int(line2)-1].expr))
    str2 = ''.join(list(parsed[int(line3)-1].expr))
    return str1 == str2

def ui(line_number1, line_number2):
    dict1 = {}
    compare1 = parsed[int(line_number1) - 1].expr[1]
    compare2 = parsed[int(line_number2) - 1].expr
    for i in range(len(compare1)):
        try:
            if not compare1[i].islower():
                if not compare1[i] == compare2[i]:
                    return False
            else:
                if compare1[i] in dict1:
                    if not dict1[compare1[i]] == compare2[i]:
                        return False
                else:
                    dict1[compare1[i]] = compare2[i]
        except:
            return False
    return True


def verify(nameoffile):
    global parsed
    parsed = file_to_list_of_parsed(nameoffile)
    for line in parsed:
        if not line.reason[0] == 'Pr':
            str1 = str(line.reason[0].lower())
            str1 += '(*'
            args = line.reason[1:] + list(line.linenumber)
            str1 += str(args)
            str1 += ')'
            print eval(str1)
        
    


verify('quacker2.txt')

