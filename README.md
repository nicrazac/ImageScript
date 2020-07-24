# ImageScript
A small Kivy GUI for Steganography

Hi, ImageScript is a small project I orginally created for a larger YouTube project (@nicrazac).  I decided to add the source code to github to assure those who are concerned of malicous intent or malware that there is none of that and that they are welcome to download the source code for themselves to build or change however thay want.

The stegano module is used to encode and decode a user provided image with user provided text.  From my research on Stegano, it uses the LSB (Least Significant Bit) technique to slightly modify the RGB values (up or down a maximum of 1 value) of the pixels.  When decoded, the last digit of the binary equivalents to the RGB values are concatenated to form the originally encoded message, which is displayed in regular ASCii text.

Kivy is used simply to make the reusable and repeatable GUI.

To build the executable on Windows, I (basically verbatum besides some name changes) followed the 'Simple App' instructions at this link:

https://kivy.org/doc/stable/guide/packaging-windows.html
