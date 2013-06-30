#!/usr/bin/env python

import unittest

import yaml

import executor 
import translator


class CoreTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # For Speed
        cls.ex = executor.Executor() 
        cls.trans = translator.Translator()

    def test_num(self):
        line = "[+, 1, 2]"
        y = yaml.load(line)
        js = self.trans.translate(y)
        r = self.ex.execute(js)
        self.assertEqual('3', r)

    def test_fn(self):
        line = "[[fn, [x, y], [+, x, y]], [1, 2]]"
        y = yaml.load(line)
        js = self.trans.translate(y)
        r = self.ex.execute(js)
        self.assertEqual('3', r)

    def test_high_order(self):
        line = "[[[fn, [y], [fn, [x], [+, x, y]]], [1]], [2]]"
        y = yaml.load(line)
        js = self.trans.translate(y)
        r = self.ex.execute(js)
        self.assertEqual('3', r)

    def test_if(self): 
        line = "[if, 1, 2]"
        y = yaml.load(line)
        js = self.trans.translate(y)
        r = self.ex.execute(js)
        self.assertEqual('2', r)

    def test_if_else(self): 
        line = "[if, 0, 3, 2]"
        y = yaml.load(line)
        js = self.trans.translate(y)
        r = self.ex.execute(js)
        self.assertEqual('2', r)

    def test_quote(self):
        line = "[quote, [1, 2, 3]]"
        y = yaml.load(line)
        js = self.trans.translate(y)
        r = self.ex.execute(js)
        self.assertEqual('[1, 2, 3]', r)

    def test_text(self):
        line = """[+, '"Hello,"', '"World!"']"""
        y = yaml.load(line)
        js = self.trans.translate(y)
        r = self.ex.execute(js)
        self.assertEqual("Hello,World!", r)

    def test_def(self):
        line = """[def, '"x"', 1]"""
        y = yaml.load(line)
        js = self.trans.translate(y)
        print js
        r = self.ex.execute(js)
        self.assertEqual("1", r)


if __name__ == "__main__":
    unittest.main()

