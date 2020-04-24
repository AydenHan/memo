# =============================================================================
#      FileName: about.py
#          Desc: 最小化设置
# =============================================================================
from PyQt5.QtWidgets import QWidget,QLabel,QVBoxLayout,QDesktopWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt,QPoint,QUrl
import css
from function import Button

class AboutMemo(QWidget):
    def __init__(self,parent=None):
        super(AboutMemo, self).__init__(parent)
        self.initModule()
        self.setModule()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)
        self.move(QPoint(0,0))

        self.btn.clicked.connect(self.hide)

    def initModule(self):
        self.setWindowTitle(u'关于')
        self.setWindowIcon(QIcon(css.AppIconPath))

        self.layout = QVBoxLayout()
        self.label1 = QLabel()
        self.label2 = QLabel()
        self.btn = Button()
        self.layout.addWidget(self.label1, 2, Qt.AlignCenter)
        self.layout.addSpacing(6)
        self.layout.addWidget(self.label2, 2, Qt.AlignCenter)
        self.layout.addSpacing(3)
        self.layout.addWidget(self.btn, 2, Qt.AlignCenter)
        self.setLayout(self.layout)

    def setModule(self):
        self.label1.setMinimumWidth(800)
        self.label1.setMaximumWidth(800)
        self.label1.setWordWrap(True)
        self.label1.setText(css.about)
        self.label1.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.label1.setOpenExternalLinks(True)
        self.label1.setStyleSheet(css.aboutmemo_label)

        self.label2.setMinimumWidth(800)
        self.label2.setMaximumWidth(800)
        self.label2.setText(css.about_website)
        self.label2.setOpenExternalLinks(True)
        self.label2.setStyleSheet(css.aboutmemo_label)

        self.btn.setMinimumSize(45,45)
        self.btn.setMaximumSize(45,45)
        self.btn.setStyleSheet(css.aboutmemo_btn)



