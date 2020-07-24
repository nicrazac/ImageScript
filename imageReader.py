from PIL import Image as PILImg
from stegano import lsb

import kivy
kivy.require('1.11.1')
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.image import Image
from kivy.uix.tabbedpanel import TabbedPanel
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty


kv = Builder.load_file("imageReader.kv")

class MainClass(TabbedPanel):
    path = ObjectProperty(None)
    btnLoad = ObjectProperty(None)
    image = ObjectProperty(None)
    imageEnc = ObjectProperty(None)
    encode = ObjectProperty(None)
    filename = ObjectProperty(None)
    btnDecode = ObjectProperty(None)
    labelDecode = ObjectProperty(None)
    imageDec = ObjectProperty(None)
    loadMessage = ObjectProperty(None)
    decodeMessage = ObjectProperty(None)
    encodeMessage = ObjectProperty(None)
    
    def getImage(self):
        self.image.source = self.path.text
        self.imageEnc.source = self.path.text
        self.imageDec.source = self.path.text

    def encodeImage(self):
        try:
            secret = lsb.hide(self.path.text, message=self.encode.text).save(self.filename.text)
            message = "Msg:  Successfully encoded and saved image."
            self.encodeMessage.text = message
        except:
            message = "Msg:  Something went wrong - Check path and filename and make sure the message is not empty."
            self.encodeMessage.text = message

    def decodeImage(self):
        try:
            message = lsb.reveal(self.path.text)
            self.labelDecode.text = message
            message = "Msg:  Successfully decoded message."
            self.decodeMessage.text = message
        except:
            message = "Msg:  Something went wrong - This image may not have an encoded message."
            self.decodeMessage.text = message
        
        

class MyApp(App):
    def build(self):
        self.title = "ImageScript - LSB Steganography"
        return MainClass()
    

if __name__ == '__main__':
    MyApp().run()
