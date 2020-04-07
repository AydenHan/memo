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
    }
}

jsonpath = './data/'
imgpath = './img/'

#dataIO.py
configPath = jsonpath + 'config.json'

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
    要是有朋友觉得我这款做的还不错想用一用的，可以自己换图（在img文件夹下），找png格式的然后要把背景扣掉变成透明，不然很丑~

    简单教程：
    1.主图标（默认为滑稽），按住可以随意拖动；
    2.上面的开关（灯泡），可以打开选项（按顺序：新建便笺，设置，关于），其中设置有待开发ing。。
    3.建立便笺后，右边默认显示×，表示未完成；单击变为√，表示完成；
    4.双击便笺进入编辑状态，按确认或回车完成编辑~
    5.鼠标按住便笺可以拖拽，便笺左上角与主图标接触时松开鼠标即可删除便笺~
    6.按~键可最小化至托盘（ESC下面那个）

    2.0版本过段时间抽空会弄一下~先凑合用=_=
'''
about_website = '个人小破站：<a href="www.hanhan0223.cn">hanhan0223.cn</a> ,欢迎来逛~ '