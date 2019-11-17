# Crosslinker-FM-Reboot
Gtk file manager for Linux/Unix

![screen](https://user-images.githubusercontent.com/29865797/69012725-9d237800-0981-11ea-98a0-1502bc545768.jpg)
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


__________________
Original post is at: https://www.techtimejourney.net/crosslinker-fm-2017-rebootversion-1/
