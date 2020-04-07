# =============================================================================
#      FileName: mainpage.py
#          Desc: 便笺主体部分
# =============================================================================
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel,QVBoxLayout,QWidget
import css
from function import Button

class MainPage(QWidget):
    def __init__(self, parent=None):
        super(MainPage, self).__init__(parent)
        self.initModule()
        self.setModule()

    def initModule(self):
        #create widget
        self.homeBtn = Button()
        self.homeLabel = QLabel()
        self.layout = QVBoxLayout()
        #add to layout
        self.layout.addWidget(self.homeBtn, 1, Qt.AlignCenter)
        self.layout.addWidget(self.homeLabel, 1, Qt.AlignCenter)
        self.setContentsMargins(0,0,0,0)
        self.setLayout(self.layout)

    def setModule(self):
        self.setContentsMargins(0,0,0,0)
        #set widgets's size
        self.homeLabel.setMinimumSize(75,75)
        self.homeLabel.setMaximumSize(75,75)
        self.homeBtn.setMinimumSize(37,45)
        self.homeBtn.setMaximumSize(37,45)
        #set style
        self.homeBtn.setStyleSheet(css.mainpage_btn)
        self.normalIcon()

    def delatingIcon(self):
        self.homeLabel.setStyleSheet(css.mainpage_label_chg)

    def normalIcon(self):
        self.homeLabel.setStyleSheet(css.mainpage_label)

    def getTrashPos(self):
        return self.homeLabel


