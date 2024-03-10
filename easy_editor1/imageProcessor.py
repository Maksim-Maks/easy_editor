from PIL import Image , ImageFilter
import os
from PyQt5.QtGui import QPixmap 
from PyQt5.QtCore import Qt
class ImageProcessor:
    def __init__(self, ui):
        self.current_image: Image = None
        self.filename: str = None
        self.modified_folder = "modified"
        self.workdir = ""
        self.ui = ui

    def open(self, dir ,fn):
        self.workdir = dir
        self.filename = fn
        self.path = os.path.join(self.workdir, self.filename)
        self.current_image  = Image.open(self.path)
    def show(self):
        self.ui.photo_lb.hide()

        pixmapimage = QPixmap(self.path)
        w,h = self.ui.photo_lb.width(), self.ui.photo_lb.height()
        pixmapimage.scaled(w,h, Qt.KeepAspectRatio)
        self.ui.photo_lb.setPixmap(pixmapimage)







        self.ui.photo_lb.show()
        
