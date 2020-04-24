# =============================================================================
#      FileName: css.py
#          Desc: 软件的css样式和路径集合
# =============================================================================

#------------------PATH-----------------
#data
userdata = {
    'memo_num': 0,
    'memo_data': [
    ],
    'set_data': {
        'font': '微软雅黑',
        'font_size': 13,
        'font_color': 'black',
        'font_bold': 'Bold',
        'background_color': '#CCCCCC',
        'label_opacity': 0.9,
        'touch_opacity': 0.65
    },
    'ui_data':{
        'is_up': False,
        'auto_hide':True
    },
    'login_date':''
}

statistics = {
    'date':{
        'finished':[],
        'unfinished':[]
    }
}
#-----------!! project中为../ , 打包时需改为./
jsonpath = './data/'
imgpath = './img/'

#dataIO.py
configPath = jsonpath + 'config.json'
statisticsPath = jsonpath + 'statistics.json'

#windows.py
AppIconPath = imgpath + 'icon.png'
#mainpage.py
homeBtnPath = imgpath + 'homeBtn.png'
homeBtn_chgPath = imgpath + 'homeBtn_chg.png'
homeLabelPath = imgpath + 'huaji.png'
homeLabel_chgPath = imgpath + 'huaji_chg.png'
#sidebar.py
newBtnPath = imgpath + 'newBtn.png'
setBtnPath = imgpath + 'setBtn.png'
dataBtnPath = imgpath + 'dataBtn.png'
aboutBtnPath = imgpath + 'aboutBtn.png'
#memo.py
yesBtnPath = imgpath + 'yesBtn.png'
noBtnPath = imgpath + 'noBtn.png'
#tray.py
trayIconPath = imgpath + 'icon.png'
#aboutmemo.py
aboutBGPath = imgpath + 'aboutBG.png'
#------------------CSS-----------------
#windows.py

#mainpage.py
mainpage_btn = '''
    QPushButton{
        border-image: url(%s);
    }
    QPushButton:Pressed{
        border-image: url(%s);
    }
''' %(homeBtnPath, homeBtn_chgPath)

mainpage_label = '''
    QLabel{
        background-image: url(%s);
    }
''' %(homeLabelPath)

mainpage_label_chg = '''
    QLabel{
        background-image: url(%s);
    }
''' %(homeLabel_chgPath)

#sidebar.py
sidebar_new = '''
    QPushButton{
        border-image: url(%s);
    }
''' %(newBtnPath)

sidebar_set = '''
    QPushButton{
        border-image: url(%s);
    }
''' %(setBtnPath)

sidebar_data = '''
    QPushButton{
        border-image: url(%s);
    }
''' %(dataBtnPath)

sidebar_about = '''
    QPushButton{
         border-image: url(%s);
    }
''' %(aboutBtnPath)

#memo.py
memo_label = '''
    QLabel{
        color:fc;
        border-radius: 6px;
        background-color: bgc;

    } '''

memo_btn_yes = '''
    QPushButton{
        border-image: url(%s);
    }
''' % (yesBtnPath)

memo_btn_no = '''
    QPushButton{
        border-image: url(%s);
    }
''' % (noBtnPath)

#edit.py
edit_text = '''
    QTextEdit{
        border-top-left-radius: 4px;
        border-bottom-left-radius: 4px;
        background-color: #CCCCCC;
        selection-color: #CCCCCC;
        selection-background-color: #222222;
        color: black;
    } '''
edit_btn = '''
    QPushButton{
        color: #003300;
        border-top-right-radius: 4px;
        border-bottom-right-radius: 4px;
        background-color: #CCCC99;
        font-size: 15px;
        font-family: '';
    }
    QPushButton:Hover{
        background-color: #009966;
        color: white;
    } '''

#settingbar.py
restart_btn = '''
    QPushButton{
        color:black;
        font-size: 32px;
    }
    QPushButton:Hover{
        background-color: #32cd99;
        color: white;
    } '''

#aboutmemo.py
aboutmemo_label = '''
    QLabel{
        border-radius: 4px;
        background-image: url(%s);
        font-size:22px;
    }
''' %(aboutBGPath)
aboutmemo_btn = '''
    QPushButton{
        border-radius: 4px;
        border-image: url(%s);
    }
'''%(noBtnPath)

about = '''
Author: 沈子涵
Version: 1.0.0

一个简单的windows便笺小软件~
因为是做出来给自己用的，所以选择的图标按钮都是按本人的喜好来的（逗比风格）。
要是有朋友觉得我这款做的还不错想用一用的，可以自己换图（在img文件夹下），找png格式的然后要把背景扣掉变成透明~

使用教程如下：
1.双击可以修改内容（目前无法使用删除键，修改方式为鼠标全选后直接输入文本，待debug）
2.右边按钮为当日完成情况，初始化为X，点击表示完成√
3.删除：拖动单条便笺到主图标滑稽上，松开鼠标即可删除
4.按~键（ESC下面）即可最小化至托盘
5.拖动主图标即可拖动整个便笺软件移动
6.对便笺样式以及内容的修改信息均会保存，在下次启动时直接调用~
7.主图标以及各种按钮的图标均可找自己喜欢的图片修改（要求：png图片、背景透明（怎么弄透明百度有教程，可网站上在线生成也可ps自己弄）、将处理好的图片与想改的图标做替换（文件名要相同））

1.1版本更新如下：

1.优化了设置和关于界面的UI
2.添加了主图标右键可以打开菜单栏操作功能
3.新增部分设置选项（设置置顶、勾选重启以创建桌面快捷方式、边缘自动隐藏）
4.完善了每个便笺个体的信息保存，软件在下一天启动时所有便笺状态归于未完成
5.删除了任务栏图标，只保留托盘图标了
6.更新了数据统计功能，从整体和个体角度分析完成情况
7.新增简单的一键换肤功能（不提倡，建议ps手动修图手动在img文件夹下替换）

8.关于与个人网站的联动，会做一个内测版本，将我每日的学习进度展示在我的个人网站上~暂时不打算封装起来
'''
about_website = '个人小破站：<a href="www.hanhan0223.cn">hanhan0223.cn</a> ,欢迎来逛~ '

#datastatistics.py
label_style = '''
    QLabel{
        font-size:22px;
    }
'''

combobox_style = '''
    QComboBox{
        font-size:22px;
    }
'''