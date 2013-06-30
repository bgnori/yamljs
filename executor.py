#!/usr/bin/env python

from selenium import webdriver

import os

PAGE =  "html/eval.html"
scheme = "file:///"

class Executor:
    def __init__(self):
        self.driver = driver = webdriver.PhantomJS('phantomjs')     
        p = os.path.join(os.getcwd(), PAGE)
        self.driver.get(scheme + p)

    def execute(self, script):
        self.driver.execute_script(r'''$(document).ready(function(){
    $("#output").replaceWith('<div id="output">' + %s + '</div>');
    });'''%(script,))
        return self.output()

    def output(self):
        element = self.driver.find_element_by_id("output")
        #for t in t.xpath('//div[@id="output"]'):
        return element.text

    def quit(self):
        self.driver.quie()


