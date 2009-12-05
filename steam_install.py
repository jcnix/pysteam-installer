#!/usr/bin/env python

import os
import gtk
import subprocess
import urllib2

#TODO: Show the license agreement .rtf file
#The Steam installer doesn't do this for some reason, but we should.
#
#The .rtf is included in the SteamInstall.msi package.
#So perhaps we should distribute a plain text version because the .msi
#isn't downloaded until the user clicks Install

class MainWindow:
    progressbar = gtk.ProgressBar(adjustment=None)

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
        
        self.progressbar.set_orientation(gtk.PROGRESS_LEFT_TO_RIGHT)
        
        button = gtk.Button("Install")
        button.connect("clicked", self.install);
        
        box1 = gtk.VBox(True,0)
        box1.pack_start(self.progressbar)
        box1.pack_end(button)
        
        #set the button's size so we can center it better.
        fixed.put(box1, 215, 500)
        window.add(fixed)
        window.show_all()
    
    def install(self, widget):
        block_size = 4096
        
        steam_url = "http://storefront.steampowered.com/download/SteamInstall.msi"
        local_file = "SteamInstall.msi"
        
        temp = urllib2.urlopen(steam_url);
        headers = temp.info()
        size = int(headers['Content-Length'])
        data = open(local_file, 'wb')
        
        i = 0
        count = 0
        while i < size:
            data.write(temp.read(block_size))
            i += block_size
            count += 1
            self.progressbar.set_fraction(i/size)
        
        data.close()
        temp.close()
        
        #subprocess.Popen('./install.sh', shell=True)
    
    def main(self):
        gtk.main()
        

app = MainWindow()
app.main()
