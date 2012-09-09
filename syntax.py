from pyparsing import *
str =  '1.  Px->Ax\t\tPr'
#
#def Syntax():
#    linenumber = (Word(nums) + Suppress('.')).setParseAction(lambda t: int(t[0])).setResultsName("linenumber")
#    op = oneOf( '\/ -> *')
#    lpar  = Literal('(') .suppress()
#    rpar  = Literal( ')' ).suppress()
#    statement = Word(srange('[A-Z]'),srange('[a-z]'))
#    wff = Forward()
#    atom = statement | Group( lpar + wff + rpar )
#    wff << atom + ZeroOrMore( op + wff )
#    reasoning = Word(alphas) + Word(nums) + Suppress(',') + Word(nums)
#    line = linenumber + wff + reasoning
#    return line


#def Syntax():
#    period = Suppress('.')
#    comma = Suppress(',')
#    linenumber = (Word(nums) + period).setParseAction(lambda t: int(t[0])).setResultsName("linenumber")
#    op = oneOf( '\/ -> *').setResultsName('op')
#    expr = Word(alphas) + op + Word(alphas)
#    reason = Word(alphas) + Optional(Word(nums) + comma + Optional(Word(nums)))
#    line = linenumber + expr + reason
#    return line

def Syntax():
    period = Literal('.').suppress()
    comma = Literal(',').suppress()
    lpar  = Literal('(') .suppress()
    rpar  = Literal( ')' ).suppress()
    linenumber = (Word(nums) + period).setParseAction(lambda t: int(t[0])).setResultsName("linenumber")
    op = oneOf( '\/ -> *').setResultsName('op')
    variable = Word(srange('[a-z]'),max=1).setResultsName('variable')
    statement = (Optional(variable) + Word(srange('[A-Z]'), max = 1) + variable).setResultsName("statement")
    expr = Forward().setResultsName('expr')
    atom = statement | Group(lpar + expr + rpar)
    expr << atom + ZeroOrMore( op + expr )
    reason = Word(alphas) + Optional(Word(nums) + comma + Optional(Word(nums)))
    line = linenumber + expr + reason
    return line
    

number = Syntax()

results = number.parseString('1.  yPx + Ax -> yBx Pr')
print results.linenumber
print results.op
print results.variable
print results.statement
print results.expr
print results