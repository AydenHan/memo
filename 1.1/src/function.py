# =============================================================================
#      FileName: function.py
#          Desc: 各种功能的封装
# =============================================================================
from PyQt5.QtWidgets import QPushButton,QGraphicsOpacityEffect,QLabel
from PyQt5.QtCore import Qt
from PIL import Image
import css


'''
@note: Make transparent background for PNG image .
'''
def transparent_back(address, filename):
    img = Image.open(address)
    img = img.convert('RGBA')
    L, H = img.size
    color_0 = img.getpixel((2,2))
    for h in range(H):
        for l in range(L):
            dot = (l,h)
            color_1 = img.getpixel(dot)
            if color_1 ==color_0 or l==0 or h==0:
                color_1 = color_1[:-1] + (0,)
                img.putpixel(dot,(0,0,0,0))
    img.save(css.imgpath + filename)

'''
@note: Get the longest continuous date.
'''
def getLongest(frame_list):
    tmp_list = []
    return_list = []
    for i in range(len(frame_list)):
        if len(tmp_list) == 0:
            tmp_list.append(frame_list[i])
        else:
            change = getDateDiffer(tmp_list[-1], frame_list[i])
            if change == 1:
                tmp_list.append(frame_list[i])
            else:
                if len(return_list) < len(tmp_list):
                    return_list = tmp_list
                tmp_list = []
                tmp_list.append(frame_list[i])
    if len(return_list) < len(tmp_list):
        return_list = tmp_list
    return return_list

'''
@note: Get the number between two date in ISODate.
'''
def getDateDiffer(first, current):
    f = list(map(int, first.split('-')))
    c = list(map(int, current.split('-')))
    if f[0] == c[0]:
        if f[1] == c[1]:
            if f[2] != c[2]:
                return c[2] - f[2]
            else:
                return 0
        else:
            return dayInYear(c[0],c[1],c[2]) - dayInYear(f[0],f[1],f[2])
    else:
        if isLeap(f[0]):
            day1 = 366 - dayInYear(f[0],f[1],f[2])
        else:
            day1 = 365 - dayInYear(f[0], f[1], f[2])
        day2 = dayInYear(c[0],c[1],c[2])
        day3 = 0
        for i in range(c[0] - f[0] - 1):
            if isLeap(f[0] + i + 1):
                day3 += 366
            else:
                day3 += 365
        return day1 + day2 + day3

def isLeap(year):
    return (year % 4 == 0 or year % 400 == 0) and (year % 100 != 0)
def dayInYear(y, m, d):
    mDay = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if isLeap(y):
        mDay[1] = 29
    for i in range(m-1):
        d += mDay[i]
    return d

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