# Crosslinker-FM-Reboot
Gtk file manager for Linux/Unix 

![clfm-reboot_main x66479](https://user-images.githubusercontent.com/29865797/31883268-f82cee90-b7f1-11e7-9641-3cc564bf84c8.jpg)
<p>Crosslinker FM Reboot version brings new features and new outlook. File manager remains lightweight and contains about 535 lines of mostly redesigned code.</p>

____________________
<b>License</b>

<p>Crosslinker FM Copyright (c) 2015 JJ Posti <techtimejourney.net> Crosslinker is a python file manager.The program comes with ABSOLUTELY NO WARRANTY; for details see: http://www.gnu.org/copyleft/gpl.html. This is free software, and you are welcome to redistribute it under GPL Version 2, June 1991″)</p>

____________________
<b>Dependencies & Install</b>

<p>python3 python-gi python3-gi gir1.2-vte-2.91

Note that the packages listed above might be different depending on your distribution.

<b>To install:</b>

Download Crosslinker FM Reboot_v1.zip. Then decompress the archive. Now, make sure that the files are executable by opening a terminal and doing;

chmod +x /home/someuser/somefolder/Clfm/*

Next, move the Clfm folder to /usr/share by doing:

sudo mv /home/someuser/somefolder/Clfm /usr/share

You can execute Clfm with the command python /usr/share/Clfm/clfm.py

OR

you can create file called clfm to /usr/local/bin with the command below:

touch clfm && echo “python /usr/share/Clfm/clfm.py” >> clfm && chmod ugo-w clfm && chmod ugo+x clfm && sudo mv clfm /usr/local/bin/clfm

Now, the clfm command should open the file manager. </p>

______________________

<b>Outlook, Navbar & Scroll area</b>
<p>Crosslinker FM has a new outlook. It also has a navbar, which you can use for navigation or for

renaming an object. Outlook is done via CSS, which gives you an ability to customize the appearance by changing the CSS entries.

To rename an object: choose it (yellow colour means chosen) and then click select for rename – button. Now, the full pathway of file/folder gets printed to navbar, change the filename and click rename selected – button. Do not touch the file extension(like mp3). For example, /home/user/sample.mp3 can be changed to /home/user/myfile.mp3 </p>

![scrollarea x66479](https://user-images.githubusercontent.com/29865797/31883475-b0e3ed26-b7f2-11e7-91a6-260004c7e668.jpg)
<p>When mouse arrives to the scroll area there is no visible scrollbar. You can still press mouse button and start moving your mouse up and down to scroll. Alternatively, you can press page up or page down keys, after an object has been selected from the file manager. </p>

_______________
<b> Crosslinker FM´s file menu has the following entries: </b>

-New folder → Create a new folder.

-New text file → Create a new text file.

-Shortkeys → Supported shortkeys.

-About → About the program.

Close → Quit the program.

________________________
<b>Integrated terminal</b>

<p>Crosslinker FM has an integrated terminal in it. The terminal also supports copy and paste from a clipboard, which means you can copy and paste object locations easily into it.</p>

_____________________
<b>Crosslinker FM´s Escape key and indicator section </b>

<p> By default, when you select objects for moving and copying, or do anything else, you can always clear the buffer by pressing the Escape key. So, if things go wrong, the Escape key is your friend. Crosslinker also clears buffer by default on some operations but the use of Escape key comes in handy. </p>

![indicator x66479](https://user-images.githubusercontent.com/29865797/31883708-66f162e2-b7f3-11e7-99cf-631f77472797.jpg)
<p>Crosslinker FM´s indicator section is there to tell what is going on. Here I have chosen 5 objects for actions by pressing Control+d. Every object was first selected. If I made a mistake upon selection, then I will press Escape key to clear the buffer.</p>
________________________

<b>Crosslinker Fm´s double-click mode (F9 key)</b>
<p>By default Crosslinker FM will not open anything when you double-click. You have to tell Crosslinker to go in to double-click mode by pressing the F9 key. After the mode is enabled a message will get printed to the indicator sections stating the action. Now, when you double-click a file, after pressing F9, Crosslinker will try to open it with its predefined defaults. Currently, the default programs and file-types associated are as follows: </p>

Gimp → xcf files.

Vlc → ogg, mp3, mp4, mpg, mp2, flw, swf, m4v, avi and midi files.

Qpdfview → pdf files.

File-roller → zip, gz, bz and bz2 files.

Feh → gif, png and jpg files.

Abiword → abw files.

Libreoffice → odp and odt files.

Geany → txt files.

_____________________
<b>Other notable features </b>

<p> Crosslinker FM has bookmarks support and it also has error handling coded into it, which means that the common usage exceptions should be handled without a Gui crash. Crosslinker FM supports Gnome icons, which means that when you change the icon theme on the overall system Crosslinker will notice the change and start using the new icon theme. The file manager in question also has search capabilities in it. First, click the file/folder section and choose any object. Now, you can start typing and Crosslinker will start an effort to locate your object. </p>

__________________
Original post is at: https://www.techtimejourney.net/crosslinker-fm-2017-rebootversion-1/
