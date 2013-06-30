#!/usr/bin/env python

import json

MONOOPS = '-'
LEFTOPS = "+-*/%"
QUOTE = 'quote'
TEXT = 'text'
IF = 'if'
FN = 'fn'
DEF = 'def'



class Translator:
    def translate(self, y):
        if isinstance(y, list):
            return self.translate_list(y)
        if isinstance(y, str):
            return self.translate_str(y)
        if isinstance(y, int):
            return self.translate_int(y)
        if isinstance(y, bool):
            return self.translate_bool(y)
        if isinstance(y, dict):
            return self.translate_dict(y)
        if y is None:
            return "none"
        raise

    def translate_list(self, y):
        n = len(y)
        if isinstance(y[0], str):
            if y[0] == DEF:
                #assert n == 3
                #return 'yamlisp[{0}] = {1};'.format(y[1], self.translate(y[2]))
                #return "function(){yamlisp[x] = '1'; return yamlisp[x];}()"
                pass
            if y[0] == QUOTE:
                assert n == 2
                return json.dumps(y[1])
            if y[0] == TEXT:
                assert n == 2
                return y[1]
            elif y[0] == IF:
                if n == 3:
                    return "function(){if(" + self.translate(y[1]) +") { return "+ self.translate(y[2]) + ";}}()"
                elif n == 4:
                    return "function(){if(" + self.translate(y[1]) + ")" + \
                        "{ return " + self.translate(y[2]) + ";}" + \
                        " else " +\
                        "{return " + self.translate(y[3]) + ";};}()"
                else:
                    assert False
            elif y[0] == FN:
                args = ','.join(y[1])
                body = self.translate(y[2])
                return "function(){return (function(" +  args + "){return " + body + ";})}()"
            elif y[0] in MONOOPS and n == 2:
                '''[-, 1] ==> -1'''
                return "function(){return " + y[0] + self.translate(y[1]) + ";}()"
            elif y[0] in LEFTOPS and n > 2:
                '''[+, 1, 2, 3, 4] ==> 10'''
                xs = [self.translate(y[i]) for i in range(1, n)]
                return "function(){return " + (' %s '%(y[0],)).join(xs) + ";}()"
            else:
                pass
        elif isinstance(y[0], list):
            '''apply'''
            args = ",".join([self.translate(a) for a in y[1]])
            return "function(){return " + self.translate_list(y[0]) + "("+ args + ");}()"

        else:
            pass
        print y
        raise 

    def translate_int(self, y):
        return str(y)

    def translate_dict(self, y):
        xs = [(self.translate(k), self.translate(v)) for k, v in y.iteritems()]
        xs = map(lambda x: '%s: %s'%(x[0], x[1]), xs)
        return "{" + ','.join(xs) + "}"

    def translate_bool(self, y):
        if y:
            return 'true'
        return 'false'

    def translate_str(self, y):
        #FIXME escape! '"
        return '%s'%(y,)


