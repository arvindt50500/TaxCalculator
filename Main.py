
import sys
import os
import pandas as pd
from PyQt5 import QtCore,QtWidgets
from PyQt5.QtGui import *
from tkinter import filedialog,messagebox
from win32com.client import Dispatch
from os.path import exists
import sqlite3
from datetime import date
#from app_modules import *
from ui_main1 import *
from ui_functions import *
from AddData import *
from Func import *
import pandas as pd
from UsersWindow import *
from Tablewidget import *
class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.FromMonth = "Nill"
        self.ui.ToMonth = "Nill"
        self.ui.MenuButton.clicked.connect(lambda: self.toggleMenu(55, True))
        self.ui.FILTER.clicked.connect(self.hide_unhide)
        self.ui.ADD.clicked.connect(lambda:self.OpenAdd())
        self.ui.FilterButton.clicked.connect(lambda:self.Filter())
        #self.ui.LIST.clicked.connect(lambda:PandasModel())
        self.ui.FromDate.dateChanged.connect(lambda:FromDate(self))
        self.ui.ToDate.dateChanged.connect(lambda:ToDate(self))
        self.ui.LIST.clicked.connect(lambda:self.List())
        #self.ui.LIST.clicked.connect(lambda:self.OpenUsers())
        self.show()

    def List(self):
        conn = sqlite3.connect('master.db')
        c = conn.cursor()
        listOfTables = c.execute(
        """SELECT name FROM sqlite_master  
        WHERE type='table';""").fetchall()
        DB_list = (list(map(lambda x:x[0],listOfTables)))[1:]
        df = pd.DataFrame(DB_list,columns =['Month'])
        df.reset_index(drop=True, inplace=True)
        
        print(df)
        self.Window=QtWidgets.QMainWindow()
        self.ui3 = Ui_UserWindow()
        self.ui3.setupUi(self.Window)
        #UserDf = UserDf[df.columns]
        #self.ui3.Window.addWidget(TableAdd(df))
        self.ui3.verticalLayout_7.addWidget(TableAdd(df))
        self.ui3.TITLEBAR.hide()
        self.Window.show()

    def Filter(self):
        if ("Nill" in self.ui.FromMonth) or ("Nill" in self.ui.ToMonth):
            print(" Month is Null")
        else:
            self.ui.FromDate.clear()
            self.ui.ToDate.clear()
            print("From "+self.ui.FromMonth)
            print("To "+self.ui.FromMonth)
            self.ui.FromMonth = "Nill"
            self.ui.ToMonth = "Nill"
        '''
        FromDate = self.ui.FromDate.dateTime()
        FromDate_string = FromDate.toString(self.ui.FromDate.displayFormat())
        '''
    def OpenUsers(self):
        self.Window=QtWidgets.QMainWindow()
        self.ui3 = Ui_UserWindow()
        self.ui3.setupUi(self.Window)
        GLOBAL_TITLE_BAR = True
        #self.verticalLayout_7.addWidget(self.TableUserInformation)
        conn = sqlite3.connect('master.db')
        c = conn.cursor()
        UserDf = pd.read_sql("SELECT * FROM UserDB", con=conn)
        print(UserDf.columns)
        Column_list = ['MonthYear', 'slno','accountnumber','transactionamount(rs.)']
        UserDf = UserDf[Column_list]
        self.ui3.verticalLayout_7.addWidget(UserTable(UserDf))
        self.Window.show()
    
    def OpenAdd(self):
        self.Window=QtWidgets.QMainWindow()
        self.ui1 = Ui_AddWindow()
        self.ui1.setupUi(self.Window)
        self.ui1.SetMonth = "Nill"
        self.ui1.Error = "Nill"
        GLOBAL_TITLE_BAR = True
        self.ui1.close.clicked.connect(lambda:self.Window.close())
        self.ui1.FilePath.clicked.connect(lambda:FileBrowser(self))
        self.ui1.OK.clicked.connect(lambda:self.add_tab())
        self.ui1.Month.dateChanged.connect(lambda:OK1(self))
        self.ui1.Month.clear()
        self.Window.show()
    
    def add_tab(self):
        if ("Nill" in (self.ui1.SetMonth)) or ("success" not in (self.ui1.Error)):
            print(self.ui1.SetMonth)
            self.ui1.Status.setText("Error:Set Date to Add "+ self.ui1.Error)
        else:
            self.ui.tabWidget.addTab(AppDemo(self.ui1.df1,self.ui1.SetMonth),self.ui1.SetMonth)
            self.Window.close()
        #self.tabwidget.addTab(AppDemo(),"Test")
    def toggleMenu(self, maxWidth, enable):
        print ("clicked")
        if enable:
            # GET WIDTH
            print(self.ui.LeftMenu.width())
            width = self.ui.LeftMenu.width()
            maxExtend = maxWidth
            standard = 138

            # SET MAX WIDTH
            if width == 138:
                widthExtended = maxExtend
                self.ui.Home.setText("")
                self.ui.LIST.setText("")
                self.ui.ADD.setText("")
                self.ui.SETTINGS.setText("")
                self.ui.HELP.setText("")
                self.ui.FILTER.setText("")
            else:
                widthExtended = standard
                self.ui.Home.setText("  HOME")
                self.ui.LIST.setText("   LIST")
                self.ui.ADD.setText("  ADD")
                self.ui.SETTINGS.setText("  SETTINGS")
                self.ui.FILTER.setText("  FILTER")
                self.ui.HELP.setText("  HELP")
            self.animation = QtCore.QPropertyAnimation(self.ui.LeftMenu, b"maximumWidth")
            self.animation.setDuration(300)
            self.animation.setStartValue(width)
            self.animation.setEndValue(widthExtended)
            self.animation.setEasingCurve(QtCore.QEasingCurve.InOutQuart)
            self.animation.start()

    def hide_unhide(self):
        if self.ui.FILTERWINDOW.isHidden():
            self.ui.FILTERWINDOW.show()           
        else:
            self.ui.FILTERWINDOW.hide()
            

    def maximize_restore(self):
        global GLOBAL_STATE
        status = GLOBAL_STATE
        if status == 0:
            self.showMaximized()
            GLOBAL_STATE = 1
            self.ui.horizontalLayout.setContentsMargins(0, 0, 0, 0)
            self.ui.MaximizeButtton.setToolTip("Restore")
            self.ui.MaximizeButtton.setIcon(QtGui.QIcon(u":/16x16/icons/16x16/cil-window-restore.png"))
            self.ui.MaximizeButtton.setStyleSheet("background-color: rgb(27, 29, 35)")
            self.ui.frame_size_grip.hide()
        else:
            GLOBAL_STATE = 0
            self.showNormal()
            self.resize(self.width()+1, self.height()+1)
            self.ui.horizontalLayout.setContentsMargins(10, 10, 10, 10)
            self.ui.btn_maximize_restore.setToolTip("Maximize")
            #self.ui.btn_maximize_restore.setIcon(QtGui.QIcon(u":/16x16/icons/16x16/cil-window-maximize.png"))
            self.ui.frame_top_btns.setStyleSheet("background-color: rgba(27, 29, 35, 200)")
            self.ui.frame_size_grip.show()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())