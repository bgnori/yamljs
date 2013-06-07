#!/usr/bin/env python

from selenium import webdriver

PAGE = "file:///home/nori/Desktop/study/yamljs/hoge.html"

class Executor:
    def __init__(self):
        self.driver = driver = webdriver.PhantomJS('phantomjs')     
        self.driver.get(PAGE)

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


