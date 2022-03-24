#!/bin/python
# (c) 2021 Ton Smeele - Utrecht University
#
# manages a window that shows (and updates) data read from a textfile 
# 

from subprocess import Popen, PIPE
import fcntl
import gi
from gi.repository import Gtk, GLib
import os

class LogWindow(Gtk.Window):
   def __init__(self, shell_command, title):
      super().__init__()
      self.shell_command = shell_command
      if title is not None:
        self.props.title = title
      self.setup()

   def setup(self):
      self.set_default_size(600,400)
      self.set_destroy_with_parent(True)

      textview = Gtk.TextView()
      self.textview = textview

      scroll = Gtk.ScrolledWindow()
      scroll.add(textview)
      self.add(scroll)
      self.show_all()
    
      # execute the shell command and collect its output via pipe 
      sub_process = Popen(self.shell_command, stdout= PIPE, shell= True)
      self.sub_process = sub_process
      self.timeout_id = GLib.timeout_add(100,self.update_terminal, None)
      self.activity_mode = False

   def non_block_read(self, output):
      fd = output.fileno()
      flags = fcntl.fcntl(fd, fcntl.F_GETFL)
      fcntl.fcntl(fd, fcntl.F_SETFL, flags | os.O_NONBLOCK)
      try:
         return output.read().decode("utf-8")
      except:
         return ''

   def update_terminal(self, user_data):
      self.textview.get_buffer().insert_at_cursor(
            self.non_block_read(self.sub_process.stdout))
      return self.sub_process.poll() is None

