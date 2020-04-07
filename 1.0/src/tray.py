# =============================================================================
#      FileName: tray.py
#          Desc: 最小化设置
# =============================================================================
from PyQt5.QtWidgets import QSystemTrayIcon,QAction,QMenu,qApp
from PyQt5.QtGui import QIcon
import sys
import css

class TraySet(QSystemTrayIcon):
    def __init__(self,parent=None):
        super(TraySet, self).__init__(parent)
        self.parent = parent
        self.initModule()
        self.setModule()
        self.activated.connect(self.iconClicked)

    def initModule(self):
        self.menu = QMenu()
        self.showAction = QAction(u'显示', self)
        self.showAction.triggered.connect(self.parent.show)
        self.quitAction = QAction(u"退出", self)
        self.quitAction.triggered.connect(self.exitApp)
        self.icon = QIcon(css.trayIconPath)

    def setModule(self):
        self.menu.addAction(self.showAction)
        self.menu.addAction(self.quitAction)
        self.setIcon(self.icon)
        self.setContextMenu(self.menu)

    def iconClicked(self, reason):
        if reason == 2 or reason == 3:
            if self.parent.isVisible():
                self.parent.hide()
            else:
                self.parent.show()

    def exitApp(self):
        self.parent.show()
        self.setVisible(False)
        qApp.quit()
