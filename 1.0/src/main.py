# =============================================================================
#      FileName: main.py
#          Desc: 主程序入口
#        Author: szh
#         Email: shen19710308@126.com
#      HomePage: www.hanhan0223.cn
#       Version: 1.0.0
#    LastChange:
# =============================================================================

import sys
from PyQt5 import QtWidgets
from window import Window
import css

def main():
    app = QtWidgets.QApplication(sys.argv)
    while True:
        w = Window(css.userdata)
        w.show()
        exit_code = app.exec_()
        if exit_code == 888:
            w.tray.exitApp()
            w.close()
        else:
            break

if __name__ == "__main__":
    main()
