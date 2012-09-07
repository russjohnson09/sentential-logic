from pyparsing import Literal,Word,ZeroOrMore,Forward,nums,oneOf,Group,srange


def Syntax():
    op = oneOf( '+ - / *')
    lpar  = Literal('(') .suppress()
    rpar  = Literal( ')' ).suppress()
    num = Word(srange('[1-9]'),nums)
    expr = Forward()
    atom = num | Group( lpar + expr + rpar )
    expr << atom + ZeroOrMore( op + expr )
    return expr


if __name__ == "__main__":
    expr = Syntax()
    def test(s):
        results = expr.parseString( s )
        print s,'->', results


test( "(9 + 3)" )
test( "(9 + 3) * (4 / 5)" )
test( "(69 + 3) * (4 / 5)" )
test("5 + 6 * 5 + 7")
