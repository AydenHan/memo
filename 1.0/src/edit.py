# =============================================================================
#      FileName: edit.py
#          Desc: 实现memo编辑状态
# =============================================================================
from PyQt5.QtWidgets import QWidget,QTextEdit,QHBoxLayout,QSizePolicy
from PyQt5.QtCore import Qt
import css
from function import Button

class Edit(QWidget):
    def __init__(self, parent=None):
        super(Edit, self).__init__(parent)
        self.initModule()
        self.setModule()

    def initModule(self):
        self.textEdit = QTextEdit()
        self.sureBtn = Button()
        self.layout = QHBoxLayout()

        self.layout.addWidget(self.textEdit, 1, Qt.AlignLeft)
        self.layout.addWidget(self.sureBtn, 1, Qt.AlignLeft)
        self.setLayout(self.layout)

    def setModule(self):
        self.layout.setContentsMargins(0,0,0,0) #设置四边距
        self.layout.setSpacing(1)   #设置控件之间的距离
        self.sureBtn.setText(u'确定')
        self.textEdit.setMinimumWidth(340)
        self.textEdit.setMaximumWidth(340)
        self.textEdit.setMinimumHeight(50)  #文本框最小高度
        self.sureBtn.setMinimumWidth(60)
        self.sureBtn.setMaximumWidth(60)
        self.sureBtn.setMinimumHeight(50)

        self.textEdit.setStyleSheet(css.edit_text)
        self.sureBtn.setStyleSheet(css.edit_btn)

    def setText(self, text):
        self.textEdit.setText(text)

    def document(self):
        return self.textEdit.document()

    def saveText(self):
        self.textEdit.setDocument(self.textEdit.document())

    def focusInEvent(self, event):
        self.Editing.emit()

    def focusOutEvent(self, event):
        if event.reason() == 4: # popup focus
            event.ignore()
        if self.textEdit.hasFocus():
            event.ignore()
        else:
            self.EditFinish.emit()

    def setFocus(self):
        self.textEdit.setFocus()