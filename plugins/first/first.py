#!/usr/bin/env python
# encoding: utf-8
from asdasd import ClassB
'''
    The plugin must have run() function, it will executed by the controller
'''
def run(str):
    print "%s this is from first" % str
    #print os.system("pwd")
    ax = ClassB()
    ax._mprint("test")

if __name__ == '__main__':
    run('asdasdsd')
