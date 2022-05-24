import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc


class mainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        # set windowtitle
        self.setWindowTitle('This is my Title')
        self.setWindowIcon(qtg.QIcon('./qt_icon.png'))
        #self.setGeometry(100,100,1000,600)
        self.setFixedSize(1200,600)

        # QLabel
        self.label1 = qtw.QLabel('<h1>Welcome to PyQt Basic Programming</h1>',self)
        self.label2 = qtw.QLabel('This application demonstrate simple PyQt Programming',self)        
        self.label_img = qtw.QLabel('this is image',self)
        self.label_img.setPixmap(qtg.QPixmap('./sample.jpg'))
        self.label_img.setScaledContents(True)

        # QLineEdit
        self.line_edit = qtw.QLineEdit(self,placeholderText='Enter you Name',maxLength=20)

        # QPushButton
        self.button = qtw.QPushButton('Select',self,clicked=self.changeImage)

        # Combobox
        self.combobox = qtw.QComboBox(self)
        self.combobox.addItems(['Lemon','Peach','Strawberry','Raddish'])

        # Layout
        hlayout = qtw.QHBoxLayout() # this is horizontal layout
        vlayout = qtw.QVBoxLayout() # this is vertical layout

        vlayout.addWidget(self.label1)
        vlayout.addWidget(self.label2)
        vlayout.addWidget(self.line_edit)
        vlayout.addWidget(self.combobox)
        vlayout.addWidget(self.button)

        # horizontal layout left to righ
        hlayout.addLayout(vlayout)
        hlayout.addWidget(self.label_img)

        # end
        self.setLayout(hlayout)
        self.show()
    
    def changeImage(self):
        textLineEdit = self.line_edit.text()
        curretText = self.combobox.currentText()

        if curretText == 'Lemon':
            self.label_img.setPixmap(qtg.QPixmap('./images/lemon.jpg'))
        elif curretText =='Peach':
            self.label_img.setPixmap(qtg.QPixmap('./images/peach.jpg'))
        elif curretText == 'Strawberry':
            self.label_img.setPixmap(qtg.QPixmap('./images/strawberry.jpg'))
        elif curretText == 'Raddish':
            self.label_img.setPixmap(qtg.QPixmap('./images/raddish.jpeg'))


if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    mw = mainWindow()
    sys.exit(app.exec())