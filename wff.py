from pyparsing import *



def Syntax():
    op = oneOf( '\/ -> *')
    lpar  = Literal('(') .suppress()
    rpar  = Literal( ')' ).suppress()
    statement = Word(srange('[A-Z]'),srange('[a-z]'))
    expr = Forward()
    atom = statement | Group( lpar + expr + rpar )
    expr << atom + ZeroOrMore( op + expr )
    return expr


if __name__ == "__main__":
    expr = Syntax()
    def test(s):
        results = expr.parseString( s )
        print s,'->', results
        
        
test( "(Ax * Bz) -> Cg")