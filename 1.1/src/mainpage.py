# =============================================================================
#      FileName: mainpage.py
#          Desc: 便笺主体部分
# =============================================================================
from PyQt5.QtGui import QCursor,QIcon
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLabel,QVBoxLayout,QWidget,QAction,QMenu,qApp,QDialog,QFileDialog,QLineEdit,QComboBox
import css
from function import Button,transparent_back

class MainPage(QWidget):
    def __init__(self, parent=None):
        super(MainPage, self).__init__(parent)
        self.parent = parent
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
        self.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.skinDialog()

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

    def restartMemo(self):
        qApp.exit(888)

    def contextMenuEvent(self, QContextMenuEvent):
        self.menu = QMenu()
        self.hideAction = QAction(u'隐藏', self)
        self.hideAction.triggered.connect(self.homeLabel.hide)
        self.skinAction = QAction(u'一键换肤', self)
        self.skinAction.triggered.connect(self.skinChange)
        self.restartAction = QAction(u'重启', self)
        self.restartAction.triggered.connect(self.restartMemo)
        self.trayAction = QAction(u'最小化', self)
        self.trayAction.triggered.connect(self.parent.hide)
        self.quitAction = QAction(u"退出", self)
        self.quitAction.triggered.connect(qApp.quit)
        self.menu.addAction(self.hideAction)
        self.menu.addAction(self.skinAction)
        self.menu.addAction(self.restartAction)
        self.menu.addAction(self.trayAction)
        self.menu.addAction(self.quitAction)
        self.menu.exec_(QCursor.pos())
        self.menu.show()

    def skinDialog(self):
        self.skin = QDialog()
        self.skin.setWindowTitle('一键换肤简单版')
        self.skin.setWindowIcon(QIcon(css.AppIconPath))
        self.skin.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.skin.resize(300,200)

        self.path = QLineEdit()
        self.selBtn = Button('选取图片')
        self.combobox = QComboBox()
        self.sureBtn = Button('一键更换')
        self.aboutlabel = QLabel('换肤前建议将img文件夹备份，换肤后文件直接覆盖无法复原。。懒得整复原程序了。。')
        self.skinl = QVBoxLayout()
        self.skinl.addWidget(self.path)
        self.skinl.addWidget(self.selBtn)
        self.skinl.addWidget(self.combobox)
        self.skinl.addWidget(self.sureBtn)
        self.skinl.addWidget(self.aboutlabel)
        self.skin.setLayout(self.skinl)
        self.skin.hide()

        self.selBtn.clicked.connect(self.openImage)
        self.sureBtn.clicked.connect(self.skinChangeFinished)
        self.combobox.addItems(['主图标', '主控按钮', '添加memo按钮', '设置按钮', '数据统计按钮', '关于按钮', '完成按钮', '未完成按钮'])

    def skinChange(self):
        self.skin.show()

    def skinChangeFinished(self):
        index = self.combobox.currentIndex()
        fname = '1.png'
        if index == 0:
            fname = 'huaji.png'
            transparent_back(self.pathIn, 'huaji_chg.png')
        elif index == 1:
            fname = 'homeBtn.png'
            transparent_back(self.pathIn, 'homeBtn_chg.png')
        elif index == 2:
            fname = 'newBtn.png'
        elif index == 3:
            fname = 'setBtn.png'
        elif index == 4:
            fname = 'dataBtn.png'
        elif index == 5:
            fname = 'aboutBtn.png'
        elif index == 6:
            fname = 'yesBtn.png'
        elif index == 7:
            fname = 'noBtn.png'
        transparent_back(self.pathIn, fname)
        self.restartMemo()

    def openImage(self):
        filename, filetype = QFileDialog.getOpenFileName(self, "选取文件", "D:/", "All Files(*);;PNG Files(*.png)")
        self.path.setText(filename)
        self.pathIn = filename
