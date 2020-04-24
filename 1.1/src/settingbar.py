# =============================================================================
#      FileName: settingbar.py
#          Desc: 最小化设置
# =============================================================================
from PyQt5.QtWidgets import qApp,QLabel,QVBoxLayout,QHBoxLayout,QGridLayout,QTextEdit,QFontDialog,QDialog,QColorDialog,QCheckBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt,QFile,QStandardPaths
import sys, os
import css
from function import Button
from dataIO import write

class SettingBar(QDialog):
    def __init__(self,parent=None):
        super(SettingBar, self).__init__(parent)
        # data
        self.pw = parent
        self.data = parent.data
        self.isDesk = False
        #init
        self.initModule()
        self.setModule()
        self.funcLink()
        # self.setWindowFlags(Qt.FramelessWindowHint)
        # self.setAttribute(Qt.WA_TranslucentBackground)

    def funcLink(self):
        self.btn1.clicked.connect(self.fontSetting)
        self.btn2.clicked.connect(self.colorSetting)
        self.btn3.clicked.connect(self.bgcolorSetting)
        self.settingBtn.clicked.connect(self.updateSetting)
        self.isup_checkbox.stateChanged.connect(self.upstateSetting)
        self.shortcut_checkbox.stateChanged.connect(self.createDeskIcon)
        self.autohide_checkbox.stateChanged.connect(self.autohideSetting)

    def initModule(self):
        self.setWindowTitle(u'设置')
        self.setWindowIcon(QIcon(css.setBtnPath))

        self.layout = QVBoxLayout()

        self.fontlayout = QHBoxLayout()
        self.label1 = QLabel(u'字体设置')
        self.btn1 = Button(u'设置')
        self.fontlayout.addWidget(self.label1)
        self.fontlayout.addSpacing(6)
        self.fontlayout.addWidget(self.btn1)

        self.colorlayout = QHBoxLayout()
        self.label2 = QLabel(u'字体颜色')
        self.btn2 = Button(u'设置')
        self.colorlayout.addWidget(self.label2)
        self.colorlayout.addSpacing(6)
        self.colorlayout.addWidget(self.btn2)

        self.bgcolorlayout = QHBoxLayout()
        self.label5 = QLabel(u'背景颜色')
        self.btn3 = Button(u'设置')
        self.bgcolorlayout.addWidget(self.label5)
        self.bgcolorlayout.addSpacing(6)
        self.bgcolorlayout.addWidget(self.btn3)

        self.opacitylayout1 = QHBoxLayout()
        self.label3 = QLabel(u'透明度设置:')
        self.text1 = QTextEdit(str(self.data['set_data']['label_opacity']))
        self.opacitylayout1.addWidget(self.label3)
        self.opacitylayout1.addWidget(self.text1)

        self.opacitylayout2 = QHBoxLayout()
        self.label4 = QLabel(u'触碰透明度:')
        self.text2 = QTextEdit(str(self.data['set_data']['touch_opacity']))
        self.opacitylayout2.addWidget(self.label4)
        self.opacitylayout2.addWidget(self.text2)

        self.setuplayout = QGridLayout()
        self.isup_checkbox = QCheckBox(u'悬浮窗置顶')
        self.setuplayout.addWidget(self.isup_checkbox,0,0)
        self.shortcut_checkbox = QCheckBox(u'快捷方式')
        self.setuplayout.addWidget(self.shortcut_checkbox,0,1)
        self.autohide_checkbox = QCheckBox(u'边缘自动隐藏')
        self.setuplayout.addWidget(self.autohide_checkbox,1,0)

        self.settingBtn = Button(u'重启生效哦!')
        self.layout.addLayout(self.fontlayout)
        self.layout.addLayout(self.colorlayout)
        self.layout.addLayout(self.bgcolorlayout)
        self.layout.addLayout(self.opacitylayout1)
        self.layout.addLayout(self.opacitylayout2)
        self.layout.addLayout(self.setuplayout)
        self.layout.addWidget(self.settingBtn, 1, Qt.AlignCenter)
        self.setLayout(self.layout)

    def setModule(self):
        self.text1.setMaximumSize(55, 30)
        self.text2.setMaximumSize(55, 30)
        self.btn1.setMaximumSize(55, 30)
        self.btn2.setMaximumSize(55, 30)
        self.btn3.setMaximumSize(55, 30)
        self.settingBtn.setStyleSheet(css.restart_btn)
        #read setting record
        if self.data['ui_data']['is_up']:
            self.isup_checkbox.setChecked(True)
        if self.data['ui_data']['auto_hide']:
            self.autohide_checkbox.setChecked(True)

    def updateSetting(self):
        if self.isDesk:
            self.createIcon()
        #opacity set
        self.data['set_data']['label_opacity'] = float(self.text1.toPlainText())
        self.data['set_data']['touch_opacity'] = float(self.text2.toPlainText())
        write(self.data)
        self.close()
        qApp.exit(888)

    def createDeskIcon(self):
        if self.shortcut_checkbox.isChecked():
            self.shortcut_checkbox.setChecked(True)
            self.isDesk = True
        else:
            self.shortcut_checkbox.setChecked(False)

    def createIcon(self):
        pathExe = sys.executable
        pathIcon = QStandardPaths.writableLocation(QStandardPaths.DesktopLocation) + "/" + "Memo.lnk"
        if not os.path.exists(pathIcon):
            QFile.link(pathExe, pathIcon)

    def upstateSetting(self):
        if self.isup_checkbox.isChecked():
            self.isup_checkbox.setChecked(True)
            self.data['ui_data']['is_up'] = True
        else:
            self.isup_checkbox.setChecked(False)
            self.data['ui_data']['is_up'] = False

    def autohideSetting(self):
        if self.autohide_checkbox.isChecked():
            self.autohide_checkbox.setChecked(True)
            self.data['ui_data']['auto_hide'] = True
        else:
            self.autohide_checkbox.setChecked(False)
            self.data['ui_data']['auto_hide'] = False

    def fontSetting(self):
        font, ok = QFontDialog.getFont()
        info = font.toString().split(',')  # QFont Object  =>  list
        if ok:
            self.data['set_data']['font'] = info[0]
            self.data['set_data']['font_size'] = int(info[1])
            self.data['set_data']['font_bold'] = info[10]

    def colorSetting(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.data['set_data']['font_color'] = color.name()

    def bgcolorSetting(self):
        color = QColorDialog.getColor()
        if color.isValid():
            self.data['set_data']['background_color'] = color.name()


