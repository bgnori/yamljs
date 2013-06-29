#!/usr/bin/env python


import yaml

from executor import Executor
import translator
from translator import Translator

from cmd import Cmd

class REPL(Cmd):
    prompt = 'repl:>> '

    def __init__(self):
        Cmd.__init__(self)
        self.ex = Executor()
        self.trans = Translator()

    def default(self, line):
        try:
            y = yaml.load(line)
            print 'yaml:', y
            js = self.trans.translate(y)
            print 'generated js:', js
            print self.ex.execute(js)
        except Exception as e:
            print e

    def do_EOF(self, line):
        return True
    def do_quit(self, line):
        return True

    def do_reload(self, line):
        reload(translator)#, Translator)
        return False


repl = REPL()

repl.cmdloop()

