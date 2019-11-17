#!/usr/bin/env python3
#Crosslinker FM Copyright (c) 2017 JJ Posti <techtimejourney.net> Crosslinker is a python file manager.The program comes with ABSOLUTELY NO WARRANTY; for details see: http://www.gnu.org/copyleft/gpl.html. This is free software, and you are welcome to redistribute it under GPL Version 2, June 1991")
import gi
gi.require_version('Vte', '2.91')
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gdk, GObject, GLib, Gio, Vte
import os, sys, subprocess, shutil, errno, sys, getpass
from os.path import basename
class CrosslinkerFM(Gtk.ApplicationWindow):    
################################
#Keypress functions
################################
    def delete_event(self, widget, ev):
        key = Gdk.keyval_name(ev.keyval)
        if key == "Delete":
           self.trash(widget)
        else:
            pass

    def double_click_connect(self, widget, ev):
        key = Gdk.keyval_name(ev.keyval)
        if key == "F9":
            self.default_state=True
            self.indicator.set_text("Double-click mode enabled. Clear with Esc.")
        else:
            pass

    def esc_event(self, widget, ev):
        key = Gdk.keyval_name(ev.keyval)
        if key == "Escape":
            self.delete_list_of_files(widget)
            self.indicator.set_text("")
            self.labels.set_text('')
            self.default_state=False
  
        else:
            pass

    def permanent_deleting(self, widget, ev):
        modifier_mask = Gtk.accelerator_get_default_mod_mask()
        ev_state = ev.state & modifier_mask
        if ev.keyval == Gdk.KEY_F12 and ev_state == Gdk.ModifierType.CONTROL_MASK:
            self.foreverdelete(widget)
    
    def select_for(self, widget, ev):
        modifier_mask = Gtk.accelerator_get_default_mod_mask()
        ev_state = ev.state & modifier_mask
        if ev.keyval == Gdk.KEY_d and ev_state == Gdk.ModifierType.CONTROL_MASK:
            self.sourcemove2.extend(self.filea.get_filenames())
            print (self.sourcemove2)
            self.amount=len(self.sourcemove2) 
            self.indicator.set_text("Number of items waiting for actions: " + str(self.amount) + "   Clear with Esc.")
            basenamex=os.path.basename(str(self.sourcemove2))
            basenamey=basenamex.replace("]",'')
            basename=basenamey.replace("'",'')
            self.labels.set_text("Added: " + basename)
                      
    def paste_copy_to(self, widget, ev):
        modifier_mask = Gtk.accelerator_get_default_mod_mask()
        ev_state = ev.state & modifier_mask
        if ev.keyval == Gdk.KEY_x and ev_state == Gdk.ModifierType.CONTROL_MASK:
            self.copydestination(widget)
   
    def move_to(self, widget, ev):
        modifier_mask = Gtk.accelerator_get_default_mod_mask()
        ev_state = ev.state & modifier_mask
        if ev.keyval == Gdk.KEY_m and ev_state == Gdk.ModifierType.CONTROL_MASK:
            self.movedestination(widget)              
################## 
#RENAME FUNCTION
################## 
    def rename_selects(self,widget):
        sourcemove=self.filea.get_filename()
        self.renamer.set_text(sourcemove)
        print (sourcemove)
   	    
    def actual_rename (self, widget, data=None):
        msg=("If an object with the same name is found on the rename destination it will be overwritten. Are you sure you want to continue?")

        destroy_dialog = Gtk.MessageDialog (None, 0, Gtk.MessageType.INFO,
                                    Gtk.ButtonsType.OK_CANCEL, msg)
        destroy_dialog.set_title("Rename an object?")
        response = destroy_dialog.run()
        destroy_dialog.destroy()                            
        if response == Gtk.ResponseType.OK:			
                getsit1=self.renamer.get_text()
                sourcemove=self.filea.get_filename()
                done=shutil.move(sourcemove,getsit1)
                self.indicator.set_text("File renamed.")
                return False # returning False and make destroy-event
        else:
            return True # returning True and avoid "destroy-event" 
################################							                   								                                  
#Moving for files and folders
################################		
    def movedestination(self, widget, data=None):
        msg=("Are you sure you want to continue? Object with a similar name might get overwritten.")
        
        destroy_dialog = Gtk.MessageDialog (None, 0, Gtk.MessageType.INFO,
                                    Gtk.ButtonsType.OK_CANCEL, msg)
        destroy_dialog.set_title("Move object(s)?")
        response = destroy_dialog.run()
        destroy_dialog.destroy()                            
        if response == Gtk.ResponseType.OK:
            try:			
                movedest=self.filea.get_current_folder()
                os.chdir(movedest)
                for files in self.sourcemove2:
                    shutil.move(files,movedest)
            except Exception as e:
                print("Error. Object with a similar name in path.")
                self.indicator.set_text("Error. Object with a similar name in path.")
                return False # returning False and make destroy-event
            else:
                return True # returning True and avoid "destroy-event"
            finally:
                self.delete_list_of_files(widget)
                self.labels.set_text('')                                              
#############################
#TRASH & DELETE FUNCTIONS
#############################
    def delete_list_of_files(self,widget):
        del self.sourcemove2[:]
    
    def maketrash(self,widget):
        name=getpass.getuser()
        uhome="/home/"
        trash="/trash"
        combine1=uhome + name
        os.chdir(combine1)
        if os.path.exists("trash"):
            pass
        else:                
            makefolder=os.makedirs('trash')            

#Multiple objects to trash	
    def trash(self, widget, data=None):
        self.maketrash(widget)	  
        msg=("This operation automatically creates a 'trash' folder to user's home if it does not exist. If an object with the same name is found within the trash It might get overwritten. Are you sure you want to continue?")
        
        destroy_dialog = Gtk.MessageDialog (None, 0, Gtk.MessageType.INFO,
                                    Gtk.ButtonsType.OK_CANCEL, msg)
        destroy_dialog.set_title("Trash an object?")
        response = destroy_dialog.run()
        destroy_dialog.destroy()                            
        if response == Gtk.ResponseType.OK:			
            try:
                name=getpass.getuser()
                uhome="/home/"
                trash="/trash"
                combine1=uhome + name 
                os.chdir(combine1)            
                combinex=uhome + name + trash
                sourcemovex=(self.filea.get_filenames())
                for files in sourcemovex:
                    shutil.move(files, combinex)
            except Exception as e:
                print("Error. Object with a similar name in trash.")
                self.indicator.set_text("Error. Object with a similar name in trash.")        
                return False # returning False and make destroy-event
        
        else:
            return True # returning True and avoid "destroy-event" 

##################################
#PASTE FUNCTION
##################################
    def copydestination(self, widget, data=None):
        msg=("If an object with the same name is found within the paste destination it will be overwritten. Are you sure you want to continue?")
        destroy_dialog = Gtk.MessageDialog (None, 0, Gtk.MessageType.INFO,
                                    Gtk.ButtonsType.OK_CANCEL, msg)
        destroy_dialog.set_title("Paste an object or objects?")
        response = destroy_dialog.run()
        destroy_dialog.destroy()                            
        if response == Gtk.ResponseType.OK:
            try:
                copydest=self.filea.get_current_folder()
                os.chdir(copydest)
                for folders in self.sourcemove2:
                    subprocess.Popen(['cp', '-r', folders , copydest])
            except OSError as e:
                if e.errno == errno.ENOTDIR:		
                    copydest=self.filea.get_current_folder()
                    os.chdir(copydest)
                    for files in self.sourcemove2:
                        shutil.copy(files,copydest)
                    return False # returning False and make destroy-event
            else:
                   return True # returning True and avoid "destroy-event"
            finally:
                self.delete_list_of_files(widget)
                self.indicator.set_text("")
                self.labels.set_text('')                                			              
#################################
#CREATE OBJECT FUNCTIONS
#################################
#Make new directory
    def newdir(self,widget):
        foldername=self.filea.get_current_folder()
        os.chdir(foldername)
        makefolder=os.makedirs('Newfolder')
        makefolder           

#Make new empty text file
    def newfile(self,widget):
        foldername=self.filea.get_current_folder()
        os.chdir(foldername)
        newtext=os.mknod('Newtext.txt')
        newtext
##########################
#DELETE FUNCTIONS
##########################   
    def foreverdelete (self, widget, data=None):
        msg=("PERMANENT Delete!")
        destroy_dialog = Gtk.MessageDialog (None, 0, Gtk.MessageType.INFO,
                                    Gtk.ButtonsType.OK_CANCEL, msg)
        destroy_dialog.set_title("DELETE")
        response = destroy_dialog.run()
        destroy_dialog.destroy()                            
        if response == Gtk.ResponseType.OK:
            try:
                foldername=self.filea.get_filename()
                shutil.rmtree(foldername)
            except OSError as e:
                if e.errno == errno.ENOTDIR:
                    filename=self.filea.get_filename()
                    os.remove(filename)
            return False # returning False and make destroy-event

        else:
            return True # returning True and avoid "destroy-event"
################################
#About dialog function
################################
    def about1 (self, widget):
        about1 = Gtk.AboutDialog()
        about1.set_name('about')
        about1.set_program_name("Crosslinker FM")
        about1.set_version("2017 Reboot v.1")
        about1.set_copyright(" Copyright (c) 2015 JJ Posti <techtimejourney.net>")
        about1.set_comments("Crosslinker is a python file-manager.The program comes with ABSOLUTELY NO WARRANTY; for details see: http://www.gnu.org/copyleft/gpl.html. This is free software, and you are welcome to redistribute it under GPL Version 2, June 1991. \nCopyright (C) 2015 JJ Posti.")
        about1.set_website("www.techtimejourney.net")
        about1.run()
        about1.destroy()
################################
#Info dialog function
################################
    def info(self, widget):
        dialog = Gtk.MessageDialog(self, 0, Gtk.MessageType.INFO,
            Gtk.ButtonsType.OK, "Supported shortkeys:")
        dialog.format_secondary_text(
            "\n Control+d=Select for actions(copy or move). \n \n Control+h=Show/Hide hidden objects. \n \n Control+x=Copy to location.\n \n Control+m=Move to location.\n \n F9=Enable double-click mode.\n \n Escape=Key clear actions buffer and/or disable double-click mode.\n \n Delete key=Move to trash(trash folder is in user's home).\n \n Control+F12=Delete permanently.")
        dialog.set_name('info')
        dialog.run()
        dialog.destroy()
###################################################
#Navigation functionalities for NAVBAR/RENAMER-BAR.
###################################################
    def address_path(self,widget):
        self.pathway=self.renamer.get_text()
        self.renamer.set_editable(self.pathway)
        self.filea.set_current_folder(self.pathway)
###########################################################
#WHEN LOCATION CHANGES IN FILEA UPDATE NAVBAR/RENAMER-BAR.
###########################################################    
    def addressnow(self,widget):    
        current=self.filea.get_current_folder()
        print (current)
        self.renamer.set_text(current)
###########################################################
#TERMINAL FUNCTIONS.
###########################################################            
    def copy(self, widget):
        self.vte.copy_clipboard()
        self.vte.grab_focus()
        
    def paste(self, widget):
        self.vte.paste_clipboard()
        self.vte.grab_focus()

    def right_click_menu(self, widget, event):
        if event.button == 3:
            self.right_menu.show_all()            
            self.right_menu.popup(None, None, None, None, 0, Gtk.get_current_event_time())                        
####################################
#STARTING WINDOW DEFINITIONS
###################################  
#Notice that this is the parent window.
    def __init__(self, *args, **kwargs):
        super(CrosslinkerFM, self).__init__(*args, **kwargs)   
#Create THE WINDOW
        self.window1=Gtk.Window()
        self.window1.set_position(Gtk.WindowPosition.CENTER)
        self.window1.set_title("Crosslinker FM")
        self.window1.connect("key-press-event", self.delete_event)
        self.window1.connect("key-press-event", self.permanent_deleting)
        self.window1.connect("key-press-event", self.select_for)
        self.window1.connect("key-press-event", self.paste_copy_to)
        self.window1.connect("key-press-event", self.move_to)
        self.window1.connect("key-press-event", self.esc_event)
        self.window1.connect("key-press-event", self.double_click_connect)
        self.window1.connect("button-press-event", self.double_click)

###############################
#TERMINAL
################################# 
        self.vte = Vte.Terminal()
        self.vte.set_size(90,10)
        self.vte.spawn_sync(
            Vte.PtyFlags.DEFAULT,
            os.environ['HOME'],
            ["/bin/bash"],
            [],
            GLib.SpawnFlags.DO_NOT_REAP_CHILD,
            None,
            None,
            )
#Make a clipboard for copy and paste
        self.clipboard = Gtk.Clipboard.get(Gdk.SELECTION_CLIPBOARD)            
###############################
#FILE MANAGER
#################################       
#Creating scrolled window, which will hold filemanager.        
        self.scrolled_window = Gtk.ScrolledWindow()
        self.scrolled_window.set_border_width(10)
        self.scrolled_window.set_policy(
            Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.AUTOMATIC)
        self.scrolled_window.set_size_request(400, 320)
    
# Create a new file selection widget        
        self.filea = Gtk.FileChooserWidget()
        self.filea.set_name('filea')
        self.scrolled_window.add(self.filea)

#List for moving and copying files and folders(selecting items.)
        self.sourcemove2=self.filea.get_filenames()
#Additional features
        name=getpass.getuser()
        uhome="/home/"
        combine=uhome + name
        self.filea.set_current_folder(combine)
        self.filea.set_select_multiple(True)
        
#Labels for showing items(for moving and copying files and folders(selecting items.))
        self.indicator=Gtk.Label()
        self.labels=Gtk.Label()                
#################################
####NAVBAR/RENAMER-BAR+BUTTONS
#################################
#Renamer-Bar
        self.renamer=Gtk.Entry()
        self.renamer.set_name('renamer')        
        self.renamer.set_alignment(xalign = 0.5)
#Select for rename - button
        self.rbutton1=Gtk.Button("Select for rename ")
        self.rbutton1.set_name('button1')
        self.rbutton1.connect("clicked", self.rename_selects)
#Rename to - button
        self.rbutton2=Gtk.Button("Rename selected")        
        self.rbutton2.set_name('button2')
        self.rbutton2.connect("clicked", self.actual_rename)             
#Connecting Bar to functions
        name=getpass.getuser()
        uhome="/home/"
        combine=uhome + name
        self.renamer.connect("activate", self.address_path)
        self.filea.connect("current-folder-changed", self.addressnow)

#################################              
#FILE MENU & DOUBLE-CLICK STATE
#################################
#Create menu items for File menu
        self.menu=Gtk.Menu()
        self.menu.set_name('menu')
        self.filemenu=Gtk.MenuItem("File")
        self.filemenu.set_name('filemenu')
        self.filemenu.set_submenu(self.menu)
#Close button for file menu
        self.away=Gtk.MenuItem("Close")
        self.away.connect("activate", Gtk.main_quit)

#About button for file menu
        self.about=Gtk.MenuItem("About")
        self.about.connect("activate", self.about1)

#Info button for file menu
        self.infoe=Gtk.MenuItem("Shortkeys")
        self.infoe.connect("activate", self.info)

#New Folder
        self.newfolder1=Gtk.MenuItem("New folder")
        self.newfolder1.connect("activate", self.newdir)

#New text file
        self.newfile1=Gtk.MenuItem("New text file")
        self.newfile1.connect("activate", self.newfile)        

#Double_click mode (default state)
        self.default_state=False

#Appending things to menu        
        self.menu.append(self.newfolder1)
        self.menu.append(self.newfile1)
        self.menu.append(Gtk.SeparatorMenuItem())
        self.menu.append(self.infoe)
        self.menu.append(self.about)
        self.menu.append(self.away)
#Appending items to menubar
        self.menubar=Gtk.MenuBar()
        self.menubar.append(self.filemenu)
        
#################################              
#TERMINAL RIGHT-CLICK MENU
#################################
        self.right_menu=Gtk.Menu()
#Menu buttons
        #Copy&Paste
        self.copy_it = Gtk.MenuItem("Copy")
        self.copy_it.connect("activate", self.copy)

        self.paste_it = Gtk.MenuItem("Paste")
        self.paste_it.connect("activate", self.paste)
#Appending to menu        
        self.right_menu.append(self.copy_it)
        self.right_menu.append(self.paste_it)
#Connecting
        self.vte.connect("button_press_event", self.right_click_menu)
                
###########################
#BOX CONTAINERS 
############################
        self.hbox=Gtk.HBox()
        self.hbox.pack_start(self.menubar,False, False, False)
        self.hbox2=Gtk.HBox()
        self.hbox2.pack_start(self.rbutton1, False, False, False)
        self.hbox2.pack_start(self.renamer, True, True, True)
        self.hbox2.pack_start(self.rbutton2, False, False, False)     
# Vertical box2 for toolbar2      
        self.vbox=Gtk.VBox(False)
        self.vbox.set_name('vbox')
        self.vbox.pack_start(self.hbox, False, False, False)
        self.vbox.pack_start(self.hbox2, False, False, False)
        self.vbox.pack_start(self.vte, False, False, True)
        self.vbox.pack_start(self.scrolled_window, True, True, True)
        self.vbox.pack_start(self.indicator, False, False, False)
        self.vbox.pack_start(self.labels, False, False, False)                       
#Show everything		
        self.window1.add(self.vbox)
        self.window1.show_all()         
#Making window resizable and enabling the close window connector        
        self.window1.set_resizable(True)
        self.window1.connect("destroy", Gtk.main_quit)
###################################################################################################
class Double_Clicks(CrosslinkerFM):
#Capturing clicks (Replaces Open file button)
    def double_click(self, widget, event):
        if self.default_state == False:
            pass			
        else:
            if event.type == Gdk.EventType._2BUTTON_PRESS:
                filename=self.filea.get_filename()
                try:    
                    if filename.endswith("pdf"):
                        subprocess.Popen(['qpdfview', filename])
                    elif filename.endswith("zip"):
                        subprocess.Popen(['file-roller', filename])
                    elif filename.endswith("gz"):
                        subprocess.Popen(['file-roller', filename])
                    elif filename.endswith("bz2"):
                        subprocess.Popen(['file-roller', filename])
                    elif filename.endswith("bz"):
                        subprocess.Popen(['file-roller', filename])        
                    elif filename.endswith("gif"):
                        subprocess.Popen(['feh', filename])
                    elif filename.endswith("abw"):
                        subprocess.Popen(['abiword', filename])
                    elif filename.endswith("odt"):
                        subprocess.Popen(['libreoffice', filename])
                    elif filename.endswith("odp"):
                        subprocess.Popen(['libreoffice', filename])    
                    elif filename.endswith("txt"):
                        subprocess.Popen(['geany', filename])
                    elif filename.endswith("png"):
                        subprocess.Popen(['feh', filename])
                    elif filename.endswith("jpg"):
                        subprocess.Popen(['feh', filename])
                    elif filename.endswith("ogg"):
                        subprocess.Popen(['vlc', filename])
                    elif filename.endswith("mp3"):
                        subprocess.Popen(['vlc', filename])
                    elif filename.endswith("mp4"):
                       subprocess.Popen(['vlc', filename])
                    elif filename.endswith("avi"):
                        subprocess.Popen(['vlc', filename])
                    elif filename.endswith("midi"):
                        subprocess.Popen(['vlc', filename])
                    elif filename.endswith("xcf"):
                        subprocess.Popen(['gimp', filename])
                    elif filename.endswith("mpg"):
                        subprocess.Popen(['vlc', filename])
                    elif filename.endswith("mp2"):
                        subprocess.Popen(['vlc', filename])
                    elif filename.endswith("flw"):
                        subprocess.Popen(['vlc', filename])
                    elif filename.endswith("swf"):
                        subprocess.Popen(['vlc', filename])
                    elif filename.endswith("m4v"):
                        subprocess.Popen(['vlc', filename])
                except Exception as e:
                    print("Crosslinker FM encountered an error.")
            else:
                print("Trying to launch.")
		
######################################################################################################
class CSS():
#CSS Styles
        style_provider = Gtk.CssProvider()
        css = open('/usr/share/Clfm/style.css', 'rb')
        css_data = css.read()
        css.close()
        style_provider.load_from_data(css_data)
        Gtk.StyleContext.add_provider_for_screen(
            Gdk.Screen.get_default(),
            style_provider,
            Gtk.STYLE_PROVIDER_PRIORITY_APPLICATION) 
###################################################################################################
def main():
    Gtk.main()
    return 0
if __name__ == "__main__":
    Double_Clicks()
    main()
