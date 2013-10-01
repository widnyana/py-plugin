#!/usr/bin/env python
'''
    Copyleft 2013
    Written by Widnyana Putra. <widnyana.p@gmail.com>
    Demo of simple python plugin system
'''

from ploader import PluginLoader

if __name__ == '__main__':
    pl = PluginLoader()
    lists = pl.load_all()

    avail = "Available Commands: "
    for key, val in enumerate(lists):
        avail+="%s, " % val

    # print available command    
    print avail[:-2]


    # executor part
    # pass command as string, the code will run it on a 'switch-case' style
    cmd = raw_input("Enter Command: ").strip()
    args = raw_input("Enter parameter: ").strip()
    try:
        lists[cmd].run(args)
    except Exception, ex:
        msg = "%s" % ex
        if msg.startswith('run()'):
            # parameter is missing or not enough
            print "command " + msg[6:]
        else:
            print "command Not found"
            print ex
    