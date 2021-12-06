#!/usr/bin/python
# (c) 2021 Ton Smeele - Utrecht University
#
# MainWindow manages the application window 
# use the config() method to pass a dict with information

import gi
from gi.repository import Gtk, GdkPixbuf, Gdk
from IrodsChooserDialog import IrodsChooserDialog, IrodsChooserStore
from IrodsStore import IrodsStore
from LogWindow import LogWindow

LOGO_FILE = 'UU_logo_2021_EN_RGB_transparant.png'
CSS_FILE = 'guisync.css'
EMPTY_SELECTION = '-> Click to select '

# synctypes: 0 = save (to iRODS)  1 = retrieve (from iRODS)
SYNCTYPES = [
    '-> save ->',                
    '<- retrieve <-'          
    ]


class MainWindow(Gtk.Window):
   def __init__(self, data):
     super().__init__()
     self.data = data
     self.setup()

   def setup(self):
     self.props.title = self.data['program_name']

     vbox = Gtk.Box(orientation = Gtk.Orientation.VERTICAL)
     vbox.set_spacing(5)

     # show logo and instructions in top/header section of window
     header = Gtk.Box()
     logo = self.widget_logo()
     header.add(logo)
     label = Gtk.Label()
     label.set_markup('<i>Save valuable data to a Yoda server</i>')
     header.add(label)
     vbox.add(header)

     # show content in center section of window
     grid = Gtk.Grid()
     self.h_grid = grid
     self.h_grid_rows = 0
     self.add_grid_header()
     self.add_grid_row()
     vbox.add(grid)

     self.add(vbox)

     # set css style for window
     # see: https://docs.gtk.org/gtk3/css-overview.html
     css_provider = Gtk.CssProvider()
     dirname = self.data['program_directory']
     css_provider.load_from_path(dirname + '/' + CSS_FILE)
     Gtk.StyleContext.add_provider_for_screen(Gdk.Screen.get_default(),
             css_provider,
             Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION)

   def widget_logo(self):
     dirname = self.data['program_directory']
     pixbuf = GdkPixbuf.Pixbuf.new_from_file_at_scale(
             filename= dirname + '/' + LOGO_FILE, 
             width=200, height=200, 
             preserve_aspect_ratio=True)
     logo = Gtk.Image.new_from_pixbuf(pixbuf)
     return logo

   def widget_synctype_selector(self):
     combo = Gtk.ComboBoxText()
     for i in range(len(SYNCTYPES)):
         combo.insert(i, str(i), SYNCTYPES[i])
     combo.set_active(0)
     return combo
   
   def widget_clicklabel(self, location):
     button = Gtk.Button(label = EMPTY_SELECTION + location)
     return button


   def on_local_folder_clicked(self, widget):
     dialog = Gtk.FileChooserDialog(
             title = 'Select a directory to synchronize',
             parent = self,
             action = Gtk.FileChooserAction.SELECT_FOLDER)
     dialog.add_buttons(
             Gtk.STOCK_CANCEL, Gtk.ResponseType.CANCEL,
             Gtk.STOCK_OPEN, Gtk.ResponseType.OK)
     current_label = widget.get_label()
     if not current_label.startswith(EMPTY_SELECTION):
        dialog.set_filename(current_label)
     response = dialog.run()
     if response == Gtk.ResponseType.OK:
         widget.set_label(dialog.get_filename())
         widget.completed = True
     dialog.destroy()

   def on_irods_folder_clicked(self, widget):
     data = IrodsChooserStore()
     data.load_iRODS_collections()
     
     dialog = IrodsChooserDialog(data.get_store())
     response = dialog.run()
     if response == Gtk.ResponseType.OK:
         irods_path = dialog.get_selection()
         if irods_path is not None:
           widget.set_label(irods_path)
           widget.path_prefix = data.get_path_prefix()
           widget.completed = True
     dialog.destroy()

   def on_run_now_clicked(self, widget):
     # only act if both local and remote folders are known
     if widget.h_local_folder.completed and widget.h_remote_folder.completed:
#        print('local folder is :' + widget.h_local_folder.get_label())
#        print('remote folder is:' + widget.h_remote_folder.get_label())
        cmd = build_run_command(
                widget.h_local_folder.get_label(),
                widget.h_remote_folder.path_prefix + widget.h_remote_folder.get_label(),
                widget.h_sync_type.get_active()
                )
        log = LogWindow(cmd, 'Synchronization log')


   def add_grid_header(self):
     label_local = Gtk.Label()
     label_local.set_markup('<b>Workspace folder</b>')
     label_remote = Gtk.Label()
     irods_host = IrodsStore().get_hostname()
     label_remote.set_markup('<b>Server at ' + irods_host + '</b>')
     row = self.h_grid_rows
     self.h_grid.attach(label_local, 0, row, 1, 1)
     self.h_grid.attach(label_remote, 2, row, 1, 1)
     self.h_grid_rows = row + 1


   def add_grid_row(self):
     # create widgets for the 4 cells: local / sync / remote / run-now
     local_folder = self.widget_clicklabel('local folder')
     local_folder.completed = False
     local_folder.connect("clicked", self.on_local_folder_clicked)

     sync_type = self.widget_synctype_selector()

     remote_folder = self.widget_clicklabel('Yoda/iRODS folder')
     remote_folder.completed = False
     remote_folder.connect("clicked", self.on_irods_folder_clicked)

     run_now = Gtk.Button(label = 'Run!', border_width = 20)
     run_now.h_local_folder = local_folder
     run_now.h_remote_folder= remote_folder
     run_now.h_sync_type = sync_type
     run_now.connect("clicked", self.on_run_now_clicked)

     # place the created widgets in the grid cells of a new row
     row = self.h_grid_rows     # get current # of rows
     self.h_grid.attach(local_folder, 0, row, 1, 1)
     self.h_grid.attach(sync_type, 1, row, 1, 1)
     self.h_grid.attach(remote_folder, 2, row, 1, 1)
     self.h_grid.attach(run_now, 3, row, 1, 1)
     self.h_grid_rows = row + 1

     
def build_run_command(local, remote, sync):
     done = ';echo "-- END OF LOG --"'
     cmd = 'irsync -r -v '
     if sync == 0:
         cmd = cmd + local + '  i:' + remote
     if sync == 1:
         cmd = cmd + 'i:' + remote + '  ' + local
     return cmd + ';echo "DONE!"'
