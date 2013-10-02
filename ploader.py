#!/usr/bin/env python

'''
    Copyleft 2013
    Written by Widnyana Putra. <widnyana.p@gmail.com>
    A __very__ simple plugin system build with python
'''

import os
import sys
import imp

PluginFolder = "./plugins"

plugins = {}

class PluginLoader():
    '''
        code was modified by widnyana
        original code taken from http://lkubuntu.wordpress.com/2012/10/02/writing-a-python-plugin-api/ 
    '''
    def getPlugins(self):
        plugins = []
        possibleplugins = os.listdir(PluginFolder)
        for i in possibleplugins:
            location = os.path.join(PluginFolder, i)
            sys.path.append(location)
            if not os.path.isdir(location) or not i + ".py" in os.listdir(location):
                continue
            info = imp.find_module(i, [location])
            plugins.append({"name": i, "info": info})
        return plugins

    def loadPlugin(self, plugin):
        return imp.load_module(plugin['name'], *plugin["info"])

    def load_all(self):
        for p in self.getPlugins():
            plugins[p['name']] = self.loadPlugin(p)

        return plugins