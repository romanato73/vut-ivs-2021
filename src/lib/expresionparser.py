from __future__ import division
from pyparsing import (Literal, CaselessLiteral, Word, Combine, Group, Optional,
                       ZeroOrMore, Forward, nums, alphas, oneOf, CaselessKeyword, Suppress,Regex )
import operator
import sys
import re

from .mathstuck import mathcore


class MathExpresionParser():
    def __init__(self, ):

        floatnumber = Regex(r"[+-]?\d+(?:\.\d*)?(?:[eE][+-]?\d+)?!*")
        ident = Word(alphas, alphas + nums + '!'+ "_$")

        plus, minus, mult, div, factorial = map(Literal, "+-*/!")
        lpar, rpar = map(Suppress, "()")
        addop = plus | minus
        multop = mult | div
        expop = Literal("^")
        pi = CaselessKeyword("π")

        expr = Forward()
        atom = (Optional(addop) + (ident + lpar + expr + rpar | pi | floatnumber | factorial).setParseAction(
            self.pushFirst)) | Optional(oneOf("- +")) + Group(lpar + expr + rpar).setParseAction(self.pushUMinus)
        # Definuje jak může vypadát číslo:
        # 

        factor = Forward()
        factor << atom + ZeroOrMore((expop + factor).setParseAction(self.pushFirst))

        # factorialc = Forward()
        # factorialc << factor + ZeroOrMore((floatnumber + factorial).setParseAction(self.pushFirst))

        term = factor + ZeroOrMore((multop + factor).setParseAction(self.pushFirst))

        expr << term + ZeroOrMore((addop + term).setParseAction(self.pushFirst))

        self.bnf = expr

        """ expresion = infixNotation(
        operand,
        [
            (sinus, 1, opAssoc.RIGHT),
            (cosinus, 1, opAssoc.RIGHT),
            ("!", 1, opAssoc.LEFT),
            ("^", 2, opAssoc.RIGHT),
            (signop, 1, opAssoc.RIGHT),
            (multop, 2, opAssoc.LEFT),
            (plusop, 2, opAssoc.LEFT),
        ])
        self.bnf = expresion
        """
        epsilon = 1e-12
        self.opn = {"+": mathcore.add,
                    "-": mathcore.sub,
                    "*": mathcore.mul,
                    "/": operator.truediv,
                    "^": operator.pow,
                    "!": mathcore.fact
                    }
        self.fn = {"sin": mathcore.sin,
                   "cos": mathcore.cos,
                   "exp": mathcore.exp,
                   }

    def pushFirst(self, strg, loc, toks):
        self.exprStack.append(toks[0])

    def pushUMinus(self, strg, loc, toks):
        if toks and toks[0] == '-':
            self.exprStack.append('unary -')

    def eval(self, num_string, parseAll=True):
        self.exprStack = []
        results = self.bnf.parseString(num_string, parseAll)
        print(results)
        val = self.evaluateStack(self.exprStack[:])
        return val

    def evaluateStack(self, s):
        # print(s)
        op = s.pop()
        if op == 'unary -':
            return -1 * (self.evaluateStack(s))
        if op in "+-*/^":
            op2 = self.evaluateStack(s)
            op1 = self.evaluateStack(s)
            return self.opn[op](op1, op2)
        elif op == "π":
            return mathcore.pi()  # 3.1415926535
        elif re.match('([+-]?\d*)!$', op):
            rematch = re.match('([+-]?\d*)!$', op)
            return mathcore.fact(int(rematch.group(1)))
        elif op in self.fn:
            return self.fn[op](self.evaluateStack(s))
        elif op[0].isalpha():
            return 0
        else:
            return float(op)


"""test = [
    "sin(10)+10*5-10",
    "10+20+30+40",
    "10!",
    "sin(90)-sin(90)",
    "10!-5"
]
for t in test:
    nsp = MathExpresionParser()
    result = nsp.eval(t)
    print(result)
    # 16.0
    """
