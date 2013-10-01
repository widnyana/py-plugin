#!/usr/bin/env python
# encoding: utf-8

'''
    The plugin must have run() function, it will executed by the controller
'''


def add():
    return 4 + 6


def run(str):

    print "%s second was here" % str
    print "%i this is from another function" % add()