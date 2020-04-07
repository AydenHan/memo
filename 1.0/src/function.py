# =============================================================================
#      FileName: function.py
#          Desc: 各种功能的封装
# =============================================================================
from PyQt5.QtWidgets import QPushButton,QGraphicsOpacityEffect,QLabel
from PyQt5.QtCore import Qt

'''
@note: Effect occurs when the mouse moves over the button.
'''
class Button(QPushButton):
    def __init__(self, parent=None):
        super(Button, self).__init__(parent)
        self.opacity = QGraphicsOpacityEffect()
        self.setEffects()

    def enterEvent(self, event):
        self.setCursor(Qt.PointingHandCursor)
        self.changeEffects()

    def leaveEvent(self, event):
        self.setCursor(Qt.ArrowCursor)
        self.setEffects()

    def setEffects(self):
        self.opacity.setOpacity(0.5)
        self.setGraphicsEffect(self.opacity)
    def changeEffects(self):
        self.opacity.setOpacity(0.9)
        self.setGraphicsEffect(self.opacity)

'''
@note: Effect occurs when the mouse moves over the Label.
'''
class Label(QLabel):
    def __init__(self, data=None, parent=None):
        super(Label, self).__init__(parent)
        self.opacity = QGraphicsOpacityEffect()
        self.opacityInfo(data)
        self.setEffects()

    def opacityInfo(self, data):
        if 'label_opacity' in data:
            self.label_opacity = data['label_opacity']
            self.touch_opacity = data['touch_opacity']
        else:
            self.label_opacity = 0.9
            self.touch_opacity = 0.65

    def enterEvent(self, event):
        self.changeEffects()
    def leaveEvent(self, event):
        self.setEffects()

    def setEffects(self):
        self.changeOpacity(self.label_opacity)
    def changeEffects(self):
        self.changeOpacity(self.touch_opacity)

    def changeOpacity(self, data):
        self.opacity.setOpacity(data)
        self.setGraphicsEffect(self.opacity)