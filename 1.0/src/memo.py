# =============================================================================
#      FileName: memo.py
#          Desc: 实现memo各个控件的功能
# =============================================================================
from PyQt5.QtWidgets import QWidget,QHBoxLayout,QSizePolicy
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
import css
from edit import Edit
from function import Button,Label
from dataIO import write

class Memo(QWidget):
    def __init__(self, parent=None, data=None):
        super(Memo, self).__init__(parent)
        self.initData(parent)
        self.initModule(data)
        self.setModule(data)
        # data
        self.loadInfo(data)
        #button
        self.doneBtn.clicked.connect(self.done)
        self.labelEdit.sureBtn.clicked.connect(self.save)

    def initData(self,parent):
        self.pw = parent
        self.data = parent.data

    def initModule(self, data):
        self.layout = QHBoxLayout()
        self.label = Label(data)
        self.labelEdit = Edit(self)
        self.labelEdit.hide()
        self.doneBtn = Button()

        self.layout.addWidget(self.label, 1, Qt.AlignLeft)
        self.layout.addSpacing(10)
        self.layout.addWidget(self.labelEdit, 1, Qt.AlignLeft)
        self.layout.addWidget(self.doneBtn, 1, Qt.AlignLeft)
        self.layout.setContentsMargins(1, 10, 1, 10)
        self.layout.setSpacing(1)
        self.setLayout(self.layout)

    def setModule(self, data):
        self.setMinimumWidth(400)
        #set size
        self.label.setMargin(2)
        self.label.setWordWrap(True)    #auto newline
        self.label.setMinimumWidth(340)
        self.label.setMaximumWidth(340)
        self.label.setMinimumHeight(50)
        self.labelEdit.setMinimumHeight(50)
        self.labelEdit.setMaximumHeight(50)
        self.doneBtn.setMinimumSize(45, 45)
        self.doneBtn.setMaximumSize(45, 45)
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        # set style
        self.doneBtn.setStyleSheet(css.memo_btn_no)
        self.no = True
        self.label.setStyleSheet(css.memo_label.replace('fc', data['font_color']).replace('bgc', data['background_color']))

    def loadInfo(self, data):
        self.id = data['id']
        if 'content' in data:
            content = data['content']
        else:
            content = 'It is empty!'
        self.label.setText(content)
        self.labelEdit.setText(content)
        if data['font_bold'] == 'Bold':
            font = QFont(data['font'], data['font_size'], QFont.Bold)
        else:
            font = QFont(data['font'], data['font_size'], 50)
        self.label.setFont(font)

    def done(self):
        if self.no:
            self.doneBtn.setStyleSheet(css.memo_btn_yes)
            self.no = False
        else:
            self.doneBtn.setStyleSheet(css.memo_btn_no)
            self.no = True

    def save(self):
        txt = self.labelEdit.document()
        self.label.setText(txt.toPlainText())
        self.label.show()
        self.doneBtn.show()
        self.labelEdit.hide()
        self.saveData(txt.toPlainText())

    def saveData(self, data):
        self.data['memo_data'][self.id-1]['content'] = data
        write(self.data)

    def deleteData(self, data):
        self.data['memo_data'].pop(data-1)
        self.data['memo_num'] -= 1
        write(self.data)

    def keyPressEvent(self, QKeyEvent):
        if QKeyEvent.key() == 0x01000004:
            self.save()
        # elif QKeyEvent.key() == 0x60:
        #     print(2)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self.moveFlag = True
            self.positon = event.globalPos() - self.pos()

    def mouseMoveEvent(self, event):
        self.move(event.globalPos() - self.positon)
        can = self.pw.getTrashPos()
        flag = self.Collide(can, self)
        if flag and self.moveFlag:
            self.deleteMemo(True)
        else:
            self.deleteMemo(False)

    def mouseReleaseEvent(self, event):
        can = self.pw.getTrashPos()
        flag = self.Collide(can, self)
        if flag and self.moveFlag:
            self.deleteMemo(False)
            self.moveFlag = False
            self.hide()
            self.deleteData(self.id)
        else:
            self.hide()
            self.show()

    def mouseDoubleClickEvent(self, QMouseEvent):
        if QMouseEvent.button() == Qt.LeftButton:
            self.label.hide()
            self.doneBtn.hide()
            self.labelEdit.show()
            self.grabKeyboard()

    def Collide(self, widgetp, widgetc):
        dict1 = {}
        dict1['size'] = widgetp.size()
        dict1['pos'] = widgetp.pos()

        dict2 = {}
        dict2['size'] = widgetc.size()
        dict2['pos'] = widgetc.pos()

        pTopLeftX = dict1['pos'].x()
        pTopLeftY = dict1['pos'].y()
        pBottomRightX = dict1['pos'].x() + dict1['size'].width()
        pBottomRightY = dict1['pos'].y() + dict1['size'].height()

        childX = dict2['pos'].x()
        childY = dict2['pos'].y()
        if childX < pBottomRightX and childX > pTopLeftX and childY < pBottomRightY and childY > pTopLeftY:
            return True
        else:
            return False

    def deleteMemo(self, flag):
        if flag:
            self.pw.mainpage.delatingIcon()
        else:
            self.pw.mainpage.normalIcon()

    def editFinish(self):
        self.EditFinish.emit()

    def editing(self):
        self.Editing.emit()

