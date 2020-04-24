# =============================================================================
#      FileName: window.py
#          Desc: 软件主窗口
# =============================================================================
from PyQt5.QtGui import QCursor,QIcon
from PyQt5.QtWidgets import QWidget,QHBoxLayout,QVBoxLayout,QApplication
from PyQt5.QtCore import pyqtSignal,Qt,QDate
from aboutmemo import AboutMemo
from settingbar import SettingBar
from datastatistics import DataStatistics
from tray import TraySet
from memo import Memo
from sidebar import SideBar
from mainpage import MainPage
from dataIO import *


class Window(QWidget):
    showMemo = pyqtSignal(bool)

    def __init__(self, data=None):
        super(Window, self).__init__()
        self.initData(data)
        self.initUi()
        self.initModule()
        self.setModule()
        self.funcLink()
        #data
        self.dataLoad()

    def initData(self,data):
        self.autohide = False
        self.data = read(data)
        self.memoSettings = readMemoSettings(data)
        self.uiSettings = readMemoUi(data)
        date = QDate.currentDate()
        date = date.toString(Qt.ISODate)
        if self.data['login_date'] != date:
            self.data['login_date'] = date
            write(self.data)

    def funcLink(self):
        # button
        self.mainpage.homeBtn.clicked.connect(self.flexSideBar)
        self.sidebar.newBtn.clicked.connect(self.addMemo)
        self.sidebar.setBtn.clicked.connect(self.settingMemo)
        self.sidebar.dataBtn.clicked.connect(self.dataStatistics)
        self.sidebar.aboutBtn.clicked.connect(self.aboutMemo)

    def initUi(self):
        self.setMinimumWidth(600)
        self.setMaximumWidth(600)

        self.layout = QHBoxLayout()
        self.layoutl = QVBoxLayout()
        self.layoutr = QVBoxLayout()
        #self.layout.setMargin(0)
        self.layout.setSpacing(0)
        # hide menu bar
        if self.uiSettings['is_up']:
            self.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool | Qt.WindowStaysOnTopHint)
        else:
            self.setWindowFlags(Qt.FramelessWindowHint | Qt.Tool)
        self.setAttribute(Qt.WA_TranslucentBackground)

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
        self.statistics = DataStatistics(self)
        self.statistics.hide()

        self.windowIcon = QIcon(css.AppIconPath)
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
        if_done = readMemoPerformance(self.data)
        if self.data['memo_num'] > 0:
            for i in range(self.data['memo_num']):
                info = {}
                info.update(id=i+1, content=content[i], if_done=if_done[i])
                info.update(self.memoSettings)
                self.loadMemo(info)

    def loadMemo(self, data):
        label = Memo(self, data)
        allCount = self.layoutr.count()
        if allCount == 0:
            self.layoutr.addWidget(label)
        else:
            self.layoutr.insertWidget(allCount + 1, label)

    def addMemo(self):
        #set dict message about single memo
        list = self.data['memo_data']
        numInfo = len(list) > 0 and list[-1]['id'] or 0
        info = {}
        info.update(id=numInfo+1)
        info.update(self.memoSettings)
        #get the time of creating memo
        date = QDate.currentDate()
        date = date.toString(Qt.ISODate)
        #initialize memo object
        allCount = self.layoutr.count()
        label = Memo(self, info)
        if allCount == 0:
            self.layoutr.addWidget(label)
        else:
            self.layoutr.insertWidget(allCount + 1, label)
        #save new memo's message
        memo_data = {}
        memo_data.update(id=numInfo+1, content='It is empty!', set_date=date, if_done=[])
        self.data['memo_data'].append(memo_data)
        self.data['memo_num'] = len(list)
        write(self.data)

    def aboutMemo(self):
        self.about.show()

    def settingMemo(self):
        self.setting.show()

    def dataStatistics(self):
        self.statistics.show()

    def getTrashPos(self):
        return self.mainpage.getTrashPos()

    def flexSideBar(self):
        if self.sidebar.isHidden():
            self.sidebar.show()
            self.showMemo.emit(True)
        else :
            self.sidebar.hide()
            self.showMemo.emit(False)

        if self.mainpage.homeLabel.isHidden():
            self.mainpage.homeLabel.show()

    def autoHide(self):
        x = self.pos().x()
        y = self.pos().y()
        desk = QApplication.desktop()
        if x < -40:
            self.sidebar.hide()
            self.showMemo.emit(False)
            self.move(-65, y)
            self.autohide = True
        elif y < -40:
            self.sidebar.hide()
            self.showMemo.emit(False)
            self.move(x, -125)
            self.autohide = True
        elif x > desk.width() - 99:
            self.sidebar.hide()
            self.showMemo.emit(False)
            self.move(desk.width() - 65, y)
            self.autohide = True
        elif self.autohide:
            self.sidebar.show()
            self.showMemo.emit(True)
            self.autohide = False

    #move without form
    def mousePressEvent(self, QMouseEvent):
        if QMouseEvent.button() == Qt.LeftButton:
            self.flag = True
            self.m_Position = QMouseEvent.globalPos() - self.pos()
            QMouseEvent.accept()
            self.setCursor(QCursor(Qt.OpenHandCursor))
    def mouseMoveEvent(self, QMouseEvent):
        if Qt.LeftButton and self.flag:
            self.move(QMouseEvent.globalPos() - self.m_Position)
            QMouseEvent.accept()
    def mouseReleaseEvent(self, QMouseEvent):
        self.flag = False
        self.setCursor(QCursor(Qt.ArrowCursor))
        self.autoHide()

    #keyboard answer
    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() == 0x60: #0x60 means `
            if self.isVisible():
                self.hide()