#!/usr/bin/env python

import gtk
import subprocess

#TODO: Show the license agreement .rtf file
#The Steam installer doesn't do this for some reason, but we should.
#
#The .rtf is included in the SteamInstall.msi package.
#So perhaps we should distribute a plain text version because the .msi
#isn't downloaded until the user clicks Install

class MainWindow:
    def delete_event(self, widget, event, data=None):
        return False
        
    def destroy(self, widget, data=None):
        gtk.main_quit()

    def __init__(self):
        window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        window.set_position(gtk.WIN_POS_CENTER)
        
        window.set_title("Facepunch Linux Steam Installer.");
        # set an icon here
        # window.set_icon_from_file("icon.png")
        
        window.connect("delete_event", self.delete_event)
        window.connect("destroy", self.destroy)
        
        fixed = gtk.Fixed()
        
        window.set_default_size(450,550)
        
        button = gtk.Button("Install")
        button.connect("clicked", self.install);
        
        box1 = gtk.VBox(True,0)
        box1.pack_start(button)
        
        #set the button's size so we can center it better.
        fixed.put(box1, 215, 500)
        window.add(fixed)
        window.show_all()
    
    def install(self, widget):
        subprocess.Popen('./install.sh', shell=True)
    
    def main(self):
        gtk.main()
        

app = MainWindow()
app.main()
