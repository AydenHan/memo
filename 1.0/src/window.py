# =============================================================================
#      FileName: window.py
#          Desc: 软件主窗口
# =============================================================================
from PyQt5 import QtGui,Qt
from PyQt5.QtWidgets import QWidget,QHBoxLayout,QVBoxLayout
import css
from aboutmemo import AboutMemo
from settingbar import SettingBar
from tray import TraySet
from memo import Memo
from sidebar import SideBar
from mainpage import MainPage
from dataIO import *


class Window(QWidget):
    def __init__(self, data=None):
        super(Window, self).__init__()
        self.initData(data)
        self.initUi()
        self.initModule()
        self.setModule()
        #hide menu bar
        self.setWindowFlags(Qt.Qt.FramelessWindowHint)
        self.setAttribute(Qt.Qt.WA_TranslucentBackground)
        #button
        self.mainpage.homeBtn.clicked.connect(self.flexSideBar)
        self.sidebar.newBtn.clicked.connect(self.addMemo)
        self.sidebar.setBtn.clicked.connect(self.settingMemo)
        self.sidebar.aboutBtn.clicked.connect(self.aboutMemo)
        #data
        self.dataLoad()

    def initData(self,data):
        self.data = read(data)
        self.memoSettings = readMemoSettings(data)

    def initUi(self):
        self.setWindowTitle('Memo')
        self.setMinimumWidth(600)
        self.setMaximumWidth(600)

        self.layout = QHBoxLayout()
        self.layoutl = QVBoxLayout()
        self.layoutr = QVBoxLayout()
        #self.layout.setMargin(0)
        self.layout.setSpacing(0)

    def initModule(self):
        self.mainpage = MainPage(self)
        self.sidebar = SideBar(self)
        self.sidebar.hide()
        self.tray = TraySet(self)
        self.tray.show()
        self.about = AboutMemo()
        self.about.hide()
        self.setting = SettingBar(self)
        self.setting.hide()

        self.windowIcon = QtGui.QIcon(css.AppIconPath)
        self.setWindowIcon(self.windowIcon)
        self.grabKeyboard()

    def setModule(self):
        self.layoutl.addWidget(self.mainpage)
        self.layoutl.addWidget(self.sidebar)
        self.layoutl.addStretch(1)
        #set main layout
        self.layout.addLayout(self.layoutl)
        self.layout.addLayout(self.layoutr)
        self.setLayout(self.layout)

    def dataLoad(self):
        content = readMemoContent(self.data)
        settings = readMemoSettings(self.data)
        if self.data['memo_num'] > 0:
            for i in range(self.data['memo_num']):
                info = {}
                info.update(id=i+1, content=content[i])
                info.update(settings)
                self.loadMemo(info)

    def loadMemo(self, data):
        label = Memo(self, data)
        allCount = self.layoutr.count()
        if allCount == 0:
            self.layoutr.addWidget(label)
        else:
            self.layoutr.insertWidget(allCount + 1, label)

    def addMemo(self):
        list = self.data['memo_data']
        numInfo = len(list) > 0 and list[-1]['id'] or 0
        info = {}
        info.update(id=numInfo+1)
        info.update(self.memoSettings)

        allCount = self.layoutr.count()
        label = Memo(self, info)
        if allCount == 0:
            self.layoutr.addWidget(label)
        else:
            self.layoutr.insertWidget(allCount + 1, label)

        memo_data = {}
        memo_data.update(id=numInfo+1, content='It is empty!', set_date='', if_done={})
        self.data['memo_data'].append(memo_data)
        self.data['memo_num'] = len(list)
        write(self.data)

    def aboutMemo(self):
        self.about.show()

    def settingMemo(self):
        self.setting.show()

    def getTrashPos(self):
        return self.mainpage.getTrashPos()

    def flexSideBar(self):
        if self.sidebar.isHidden():
            self.sidebar.show()
        else :
            self.sidebar.hide()

    #move without form
    def mousePressEvent(self, QMouseEvent):
        if QMouseEvent.button() == Qt.Qt.LeftButton:
            self.flag = True
            self.m_Position = QMouseEvent.globalPos() - self.pos()
            QMouseEvent.accept()
            self.setCursor(Qt.QCursor(Qt.Qt.OpenHandCursor))
    def mouseMoveEvent(self, QMouseEvent):
        if Qt.Qt.LeftButton and self.flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)
            QMouseEvent.accept()
    def mouseReleaseEvent(self, QMouseEvent):
        self.flag = False
        self.setCursor(Qt.QCursor(Qt.Qt.ArrowCursor))

    #keyboard answer
    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() == 0x60: #0x60 means `
            if self.isVisible():
                self.hide()