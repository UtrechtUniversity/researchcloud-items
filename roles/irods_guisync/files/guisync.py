#!/usr/bin/python3
# (C) 2021 Ton Smeele - Utrecht University
# 
# guisync is a wrapper around irsync to provide for a graphical user interface
#
# For using Gtk3 please see: 
# https://python-gtk-3-tutorial.readthedocs.io/en/latest/layout.html

PROGRAM_NAME = 'Yoda-sync'
PROGRAM_VERSION = '0.2'

import gi
import os
from os.path import realpath, dirname
import sys
import getopt

# GUI related imports, first check if user interface is compatible
if not 'DISPLAY' in os.environ:
    print('Error: This program requires a graphical user interface')
    exit(1)
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
from MainWindow import *


def main(opts, args):
    program_dir = os.path.dirname(os.path.realpath(__file__))
    data = { 
          'program_name'     : PROGRAM_NAME,
          'program_version'  : PROGRAM_VERSION,
          'program_directory': program_dir,
          'opts' : opts,
          'args' : args
          }
    try:
       win = MainWindow(data)
       win.connect("destroy", Gtk.main_quit)
       win.show_all()
       Gtk.main()
    except:
       print('Error: Could not initiate GUI')
       exit(2)


def help():
    text = '''
    Usage: guisync [-hv]
    
    Options:
     -h  show this help
     -v  show program version
    '''
    print(text)


# main program
if __name__ == "__main__":

    try:
        opts, args = getopt.getopt(sys.argv[1:], 'hv')
    except:
        print('Error: Invalid program arguments specified. Use -h for help.')
        exit(1)

    quit = False
    for opt, arg in opts:
        opt = opt.lower()
        if opt == '-v':
            print(PROGRAM_NAME + ' release ' + PROGRAM_VERSION)
            quit = True
        if opt == '-h':
            help()
            quit = True
    if quit:
        exit(0)

    main(opts, args)

