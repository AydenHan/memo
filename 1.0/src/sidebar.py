# =============================================================================
#      FileName: sidebar.py
#          Desc: 便笺侧边栏部分
# =============================================================================
from PyQt5.QtWidgets import QVBoxLayout,QWidget
from PyQt5.QtCore import Qt
import css
from function import Button

class SideBar(QWidget):
    def __init__(self, parent=None):
        super(SideBar, self).__init__(parent)
        self.initModule()
        self.setModule()

    def initModule(self):
        self.newBtn = Button()
        self.setBtn = Button()
        self.aboutBtn = Button()
        self.layout = QVBoxLayout()

        self.layout.addWidget(self.newBtn, 1, Qt.AlignCenter)
        self.layout.addWidget(self.setBtn, 1, Qt.AlignCenter)
        self.layout.addWidget(self.aboutBtn, 1, Qt.AlignCenter)
        self.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(20)
        self.setLayout(self.layout)

    def setModule(self):
        self.newBtn.setMinimumSize(30, 30)
        self.newBtn.setMaximumSize(30, 30)
        self.setBtn.setMinimumSize(30, 30)
        self.setBtn.setMaximumSize(30, 30)
        self.aboutBtn.setMinimumSize(30, 30)
        self.aboutBtn.setMaximumSize(30, 30)

        self.newBtn.setStyleSheet(css.sidebar_new)
        self.setBtn.setStyleSheet(css.sidebar_set)
        self.aboutBtn.setStyleSheet(css.sidebar_about)

