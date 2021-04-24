from __future__ import division
from pyparsing import (Literal, Word, Group, Optional, ZeroOrMore, Forward, nums, alphas, oneOf, CaselessKeyword,
                       Suppress, Regex)

import re

import mathcore

"""Class for parsing math expresion

"""


class MathExpresionParser():
    def __init__(self, ):
        """Initial function. Prepare Literals and other expresion
            """
        floatnumber = Regex(r"[+-]?\d+(?:\,\d*)?(?:[eE][+-]?\d+)?!*")
        ident = Word(alphas, alphas + nums + '!' + "_$")

        plus, minus, mult, div, factorial = map(Literal, "+-*/!")
        lpar, rpar = map(Suppress, "()")
        addop = plus | minus
        multop = mult | div
        expop = Literal("^")
        sqrtop = Literal('√')
        sqrex = expop | sqrtop
        pi = CaselessKeyword("π")

        expr = Forward()
        atom = (Optional(addop) + (ident + lpar + expr + rpar | pi | floatnumber | factorial).setParseAction(
            self.pushFirst)) | Optional(oneOf("- +")) + Group(lpar + expr + rpar).setParseAction(self.pushUMinus)

        factor = Forward()
        factor << atom + ZeroOrMore((sqrex + factor).setParseAction(self.pushFirst))

        term = factor + ZeroOrMore((multop + factor).setParseAction(self.pushFirst))

        expr << term + ZeroOrMore((addop + term).setParseAction(self.pushFirst))

        self.bnf = expr

        epsilon = 1e-12
        self.opn = {"+": mathcore.add,
                    "-": mathcore.sub,
                    "*": mathcore.mul,
                    "/": mathcore.div,
                    "^": mathcore.exp,
                    "√": mathcore.sqrt
                    }
        self.fn = {"sin": mathcore.sin,
                   "cos": mathcore.cos,
                   "exp": mathcore.exp,
                   }

    def pushFirst(self, strg, loc, toks):
        """Append exprStack for 1st element from toks.

        :param toks: elements for parse
        :param strg: string witch is now parsed
        :param loc: parser options
        """
        self.exprStack.append(toks[0])

    def pushUMinus(self, strg, loc, toks):
        """Append exprStack for minus if number is negative.

        :param toks: number for parse
        :param strg: string witch is now parsed
        :param loc: parser options
        """

        if toks and toks[0] == '-':
            self.exprStack.append('unary -')

    def eval(self, num_string, parseAll=True):
        """Quantification of num_string.

        :param num_string: string with parsed numbers

        :return quantification number
        """
        self.exprStack = []
        results = self.bnf.parseString(num_string, parseAll)
        print(results)
        val = self.evaluateStack(self.exprStack[:])
        return val

    def evaluateStack(self, s):
        """Quantification of s by declared operation.

        :param s: string witch is parsed

        :return quantification number
        """
        print(s)
        op = s.pop()
        if op == 'unary -':
            return -1 * (self.evaluateStack(s))
        if op in "+-*/^":
            op2 = self.evaluateStack(s)
            op1 = self.evaluateStack(s)
            return self.opn[op](op1, op2)
        if op in '√^':
            op2 = self.evaluateStack(s)
            op1 = self.evaluateStack(s)
            return self.opn[op](op2, op1)
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
            return float(op.replace(',', '.'))
