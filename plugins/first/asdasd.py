#!/usr/bin/env python

class Abc():
    def __init__(self):
        print "im from class Abc"

    def tes(self):
        print "just test"

class ClassB():
    """docstring for ClassB"""
    def __init__(self):
        print "im initiated from classA"

    def _mprint(self, msg):
        print msg
        pass
