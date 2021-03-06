from pyparsing import *


class Grammar:
    
    def __init__(self):
        pass

    def syntax(self):
        period = Literal('.').suppress()
        comma = Literal(',').suppress()
        lpar  = Literal('(') .suppress()
        rpar  = Literal( ')' ).suppress()
        linenumber = (Word(nums) + period).setResultsName("linenumber")
        op = oneOf( '\/ -> *').setResultsName('op')
        variable = Word(srange('[a-z]'),max=1).setResultsName('variable')
        opvariable = Word(srange('[a-z]'),max=1).setResultsName('opvariable')
        quant = (lpar + variable + rpar | lpar + '\exists' + variable + rpar).setResultsName('quant')
        statement = (Optional(variable) + Word(srange('[A-Z]'), max = 1) + variable).setResultsName("statement")
        expr = Forward().setResultsName('expr')
        atom = statement | Group(lpar + expr + rpar)
        expr << Optional(quant) + atom + ZeroOrMore( op + expr )
        reason = (Word(alphas) + Optional(Word(nums)) + Optional(comma) + Optional(Word(nums))).setResultsName("reason")
        line = linenumber + expr + reason
        return line
    
    
        