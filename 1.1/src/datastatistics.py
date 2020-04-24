# =============================================================================
#      FileName: datastatistics.py
#          Desc: 数据分析
# =============================================================================
from PyQt5.QtWidgets import QDialog,QFrame,QWidget,QLabel,QComboBox,QButtonGroup,QStackedLayout,QVBoxLayout,QToolButton,QMainWindow,QStatusBar
from PyQt5.QtGui import QIcon,QColor
from PyQt5.QtCore import QDate,Qt
import pyqtgraph as pg
from dataIO import *
from function import getDateDiffer,getLongest
import css

class DataStatistics(QDialog):
    def __init__(self,parent=None):
        super(DataStatistics, self).__init__(parent)
        self.initData()
        self.initModule()
        self.setModule()
        self.funcLink()
        self.drawGraph()
        self.analyzeSingleMemo()

    def initModule(self):
        self.setWindowTitle(u'数据统计')
        self.setWindowIcon(QIcon(css.dataBtnPath))
        self.resize(500, 500)
        pg.setConfigOptions(foreground=QColor(113, 148, 116), antialias=True)

        self.btnframe = QFrame(self)
        self.mainframe = QFrame(self)
        self.btngroup = QButtonGroup(self.btnframe)
        self.stacklayout = QStackedLayout(self.mainframe)

        self.btn1 = QToolButton(self.btnframe)
        self.btn2 = QToolButton(self.btnframe)
        self.btngroup.addButton(self.btn1, 1)
        self.btngroup.addButton(self.btn2, 2)

        self.frame1 = QMainWindow()
        self.frame1_bar = QStatusBar()
        self.frame1.setStatusBar(self.frame1_bar)
        self.frame1_bar.showMessage(self.date + ':  ' + str(readFinishRate(self.date)[2]*100) + '%')

        self.frame2 = QMainWindow()
        self.frame2_bar = QStatusBar()
        self.frame2.setStatusBar(self.frame2_bar)
        self.frame2_bar.showMessage("坚持，就是每一天很难，可一年一年越来越容易。")

        self.stacklayout.addWidget(self.frame1)
        self.stacklayout.addWidget(self.frame2)

    def setModule(self):
        self.btnframe.setGeometry(0, 0, self.width(), 35)
        self.btnframe.setStyleSheet("border-color: rgb(0, 0, 0);")
        self.btnframe.setFrameShape(QFrame.Panel)
        self.btnframe.setFrameShadow(QFrame.Raised)
        self.mainframe.setGeometry(0, 35, self.width(), self.height() - self.btnframe.height())

        self.btn1.setCheckable(True)
        self.btn1.setText("整体完成率")
        self.btn1.resize(100, 35)
        self.btn2.setCheckable(True)
        self.btn2.setText("单条完成情况")
        self.btn2.resize(100, 35)
        self.btn2.move(self.btn1.width(), 0)

    def funcLink(self):
        self.btn1.clicked.connect(self.showFrame1)
        self.btn2.clicked.connect(self.showFrame2)

    def initData(self):
        date = QDate.currentDate()
        self.date = date.toString(Qt.ISODate)
        self.statistics = readStatistics(css.statistics, self.date)

    def drawGraph(self):
        self.myplot = pg.PlotWidget(self.frame1, title='每日任务完成率')
        self.frame1.setCentralWidget(self.myplot)

        x = []
        for key in self.statistics.keys():
            x.append(key)
        points = []
        for key in x:
            points.append(readFinishRate(key)[2])

        tick_b = [list(zip(range(len(x)), x))]
        bottom = self.myplot.getAxis('bottom')
        bottom.setTicks(tick_b)

        self.myplot.setBackground((210, 240, 240))  # 背景色
        self.myplot.showGrid(y=True)

        pen = pg.mkPen({'color': (155, 200, 160), 'width': 4})  # 画笔设置
        self.myplot.plot(points[0:], clear=True, pen=pen, symbol='o', symbolBrush=QColor(113, 148, 116))

    def analyzeSingleMemo(self):
        #data extract
        data = read(css.userdata)
        self.content=[]
        self.set_date=[]
        self.if_done=[]
        if data['memo_data']:
            for memo in data['memo_data']:
                self.content.append(memo['content'])
                self.set_date.append(memo['set_date'])
                self.if_done.append(memo['if_done'])
        #UI init
        self.ui = QWidget(self.frame2)
        self.option = QComboBox(self.ui)
        self.label0 = QLabel(self.ui)
        self.label1 = QLabel(self.ui)
        self.label2 = QLabel(self.ui)
        self.label3 = QLabel(self.ui)
        self.frame2.setCentralWidget(self.ui)
        #UI set
        self.option.setGeometry(10, 95, self.width()-100, 40)
        self.option.setStyleSheet(css.combobox_style)
        self.option.addItems(self.content)
        self.option.currentIndexChanged.connect(self.getMemoMessage)

        self.label0.setGeometry(10, 5, self.width()-100, 80)
        self.label1.setGeometry(10, 145, self.width()-100, 80)
        self.label2.setGeometry(10, 235, self.width()-100, 80)
        self.label3.setGeometry(10, 325, self.width()-100, 80)
        self.label0.setStyleSheet(css.label_style)
        self.label1.setStyleSheet(css.label_style)
        self.label2.setStyleSheet(css.label_style)
        self.label3.setStyleSheet(css.label_style)
        self.label0.setText('选择需要查看的memo：')
        self.label1.setText('设立已 ' + str(getDateDiffer(self.set_date[0], self.date)) + ' 天')
        self.label2.setText('已完成 ' + str(len(self.if_done[0])) + ' 天')
        self.label3.setText('最大连续完成 ' + str(len(getLongest(self.if_done[0]))) + ' 天')

    def getMemoMessage(self):
        self.label1.setText('设立已 ' + str(getDateDiffer(self.set_date[self.option.currentIndex()], self.date)) + ' 天')
        self.label2.setText('已完成 ' + str(len(self.if_done[self.option.currentIndex()])) + ' 天')
        self.label3.setText('最大连续完成 ' + str(len(getLongest(self.if_done[self.option.currentIndex()]))) + ' 天')

    def showFrame1(self):
        if self.stacklayout.currentIndex() != 0:
            self.stacklayout.setCurrentIndex(0)

    def showFrame2(self):
        if self.stacklayout.currentIndex() != 1:
            self.stacklayout.setCurrentIndex(1)

