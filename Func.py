from Main import *
import pandas as pd
import sqlite3
global df1
def FromDate(self):
    dt = self.ui.FromDate.dateTime()
    dt_string = dt.toString(self.ui.FromDate.displayFormat())
    self.ui.FromMonth = dt_string.replace("-","")

def ToDate(self):
    dt = self.ui.ToDate.dateTime()
    dt_string = dt.toString(self.ui.ToDate.displayFormat())
    self.ui.ToMonth = dt_string.replace("-","")

def OK1(self):
    dt = self.ui1.Month.dateTime()
    dt_string = dt.toString(self.ui1.Month.displayFormat())
    label_text = self.ui1.Status.text()
    self.ui1.SetMonth = dt_string.replace("-","")
    self.ui1.Status.setText(label_text+" "+dt_string)
    return dt_string

def FileBrowser(self):
        FilePath = QtWidgets.QFileDialog.getOpenFileName(None,'ADD EXCEL','C:\Program Files')
        self.ui1.FilePath1 = str(FilePath[0])
        self.ui1.Status.setText("Status: File Path "+str(FilePath[0]))
        try:
            xl = pd.ExcelFile(str(FilePath[0]))
            ExcelSheets = xl.sheet_names
            CorrectExcel = False
            for i in ExcelSheets:
                df1 = pd.read_excel(FilePath[0],i)
                self.ui1.df1 = df1
                self.SheetName = str(i)
                #df1_str = self.df1.to_string(index = False)
                df1_str = df1.to_string(index = False).lower()
                df1_str = df1_str.replace(" ","")
                if (("transactionamount(rs.)" in df1_str) and ("accountnumber" in df1_str)):
                    print("Excel Contains the reqired details")
                    CorrectExcel = True
                    self.ui1.Error = "Read Excel successfull"
                    break
            if  not CorrectExcel:
                self.ui1.Error = "Excel is not in correct format"
                raise Exception("Excel is not in correct format")
            return
        except:
            self.ui1.Error = "Read Excel failed"
            print("Read Excel failed ")



class AppDemo(QtWidgets.QWidget):
    def __init__(self,df,Month_Date):
        super().__init__()
        #self.ui.resize(1600, 600)
        #df1 = self.df1
        #Unnamed: 0
        df2 = df
        df1 = df2.fillna(0)
        for row in range(0,20):
            HeadereList1 = ""
            HeadereList = list(df1.loc[row])
            HeadereList1 = (','.join([str(elem) for elem in HeadereList])).lower()
            HeadereList1 = HeadereList1.replace(" ","")
            if 'accountnumber' in HeadereList1:
                row1 = row
                break
        df1.columns = df1.iloc[row1]
        df1 = df1[(row1+1):]
        df1.columns = df1.columns.str.replace(" ","")
        df1.columns = df1.columns.str.lower()
        Main_df = df1
        print(df1)
        df1["transactionamount(rs.)"] = df1["transactionamount(rs.)"].astype("float")
        tracid = df1['accountnumber'].unique
        print(df1.columns)
        df1 = df1.pivot_table(index = ['accountnumber'],values = ['transactionamount(rs.)'], aggfunc ='sum')
        #df1 = df1.pivot_table(index = ['accountnumber'],values = ['transactionamount(rs.)'], aggfunc ='sum')
        df1 = df1.sort_values(by=["transactionamount(rs.)"], ascending=False)
        df1.reset_index(inplace=True)
        #df1.columns = ["Account Name","Transaction Amount (Rs.)"]
        #df1["Month/Year"] = str(Month_Date)
        df1.insert(loc=0, column='MonthYear', value=str(Month_Date))
        df1.rename(columns=str.upper, inplace=True)
        
        mainLayout = QtWidgets.QVBoxLayout()
        table = TableWidget1(df1,list(df1.columns))
        table.setStyleSheet(u"QTableWidget {	\n"
"	background-color: rgb(250, 250, 250);\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(0, 0, 0);\n"
"	border-bottom: 1px solid rgb(102, 204, 255);\n"
"   font: 9pt \"Segoe UI\";"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(102, 204, 255);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(102, 204, 255);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"	Background-color: rgb(102, 204, 255);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(32, 34, 42);\n"
"   border-bottom: 1px solid rgb(102, 204, 255);\n"
"   border-right: 1px solid rgb(102, 204, 255);\n"
"}\n"
""
                        "QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"	background-color: rgb(102, 204, 255);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 0px;\n"
"    border-top-right-radius: 0px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(102, 204, 255);\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"	background-color: rgb(102, 204, 255);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 0px;\n"
"   border-top-right-radius: 0px;\n"
"}\n"
"")
        button = QtWidgets.QPushButton()
        '''
        for i in range(df1.rowCount()):
            button = QtWidgets.QPushButton()
            table.setCellWidget(i, 2, button)
        '''
        button.clicked.connect(lambda:table.buttonpush())

        mainLayout.addWidget(table)
        buttonLayout = QtWidgets.QVBoxLayout()

        button_new = QtWidgets.QPushButton('Export')
        button_new.clicked.connect(lambda:table._copyRow(df1))
        buttonLayout.addWidget(button_new)
        mainLayout.addLayout(buttonLayout)
        self.setLayout(mainLayout)
        #writing Data to DataBase
        conn = sqlite3.connect('master.db')
        c = conn.cursor()
        listOfTables = c.execute(
    """SELECT name FROM sqlite_master WHERE type='table'
    AND name='UserDB'; """).fetchall()
        #Users DataFrame to UsersDB
        DB_list = ' '.join(map(str, listOfTables))
        Main_df.insert(loc=0, column='MonthYear', value=str(Month_Date))
        if 'UserDB' in DB_list:
        
            #df_UserDB = pd.read_sql("SELECT * FROM UserDB WHERE instr(column, {}) > 0;".format(Month_Date), con=conn)
            #Main_df.to_sql('UserDB', conn, if_exists='append')
            Main_df.to_sql('UserDB', conn, if_exists='append', index = False)
            
        else:
            
            Main_df.to_sql('UserDB', conn, if_exists='replace', index = False)
    
        #MonthData to Month DataBase
        if Month_Date in DB_list:
            print("{} Exist".format(Month_Date))
            df1.to_sql(Month_Date, conn, if_exists='replace', index = False)
        else:
            print("{} Creating New Datatable".format(Month_Date))
            df1.to_sql(Month_Date, conn, if_exists='replace', index = False)
           
        '''
        except Exception as e:
            print("Exit")
            mainLayout = QtWidgets.QVBoxLayout()
            self.label = QtWidgets.QLabel()
            self.label.setObjectName("label")
            self.label.setText(f'No TDS1 data foundfoundfound')
            mainLayout.addWidget(self.label)
            self.setLayout(mainLayout)
        '''
      
class TableWidget1(QtWidgets.QTableWidget):
    def __init__(self, df,header_name):
        super().__init__()
        self.df = df
        self.setStyleSheet('background-color: rgb(102, 204, 255);font-size: 20px;')
        nRows, nColumns = self.df.shape
        self.setColumnCount(nColumns)
        self.setRowCount(nRows)
        QtWidgets.QHeaderView
        self.setHorizontalHeaderLabels((header_name))
        self.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.horizontalHeader().setSectionResizeMode(2,QtWidgets.QHeaderView.Stretch)
        self.horizontalHeader().setFixedHeight(30)
        self.setItemDelegateForColumn(1, FloatDelegate())
        # data insertion/
    

        for i in range(self.rowCount()):
            for j in range(self.columnCount()):
                if j == 1:
                    button = QtWidgets.QPushButton()
                    button.setAutoFillBackground(False)
                    button.setText("")
                    icon = QtGui.QIcon()
                    icon.addPixmap(QtGui.QPixmap("icons/feather/x.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
                    button.setIcon(icon)
                    button.setIconSize(QtCore.QSize(32, 32))
                    button.clicked.connect(lambda:self.buttonpush())
                    self.setCellWidget(i, 1, button)
                else:
                    self.setItem(i, j,QtWidgets.QTableWidgetItem(str(self.df.iloc[i, j])))
                                  
                #self.setItem(0, j,QtWidgets.QTableWidgetItem(QtWidgets.QPushButton()))
                
        self.cellChanged[int, int].connect(self.updateDF)   
        self.doubleClicked.connect(lambda:self.buttonpush())
        self.clicked.connect(lambda:self.buttonpush())
    def buttonpush(self):
        print(str(self.currentRow())+"="+str(self.currentColumn()))
    def updateDF(self, row, column):
        text = self.item(row, column).text()
        self.df.iloc[row, column] = text
    def updateDF1(self, row, column):
        text = self.item(row, column).text()
        self.df.iloc[row, column] = text
        df1 = self.df
    def _addRow(self,df):
        rowCount = self.rowCount()
        currentRow = self.currentRow()
        self.insertRow((rowCount-1)+1)
        self.df.loc[rowCount] = ['1', "1", "1", "1"]
        df1 = self.df
    def _removeRow(self,df):
        global df1
        if self.rowCount() > 0:
            print("before remove",self.df)
            currentRow = self.currentRow()
            self.removeRow(currentRow)
            df1 = self.df.drop(index=currentRow)
            df1 = df1.reset_index(drop=True)
            self.df = df1
    def _copyRow(self,df1):
        file = str(QtWidgets.QFileDialog.getExistingDirectory(self, "Select Directory"))+"/TDS1.xlsx"
        df1.to_excel(file, index = False, header=True)  

class FloatDelegate(QtWidgets.QItemDelegate):
    def __init__(self, parent=None):
        super().__init__()

    def createEditor(self, parent, option, index):
        editor = QtWidgets.QLineEdit(parent)
        editor.setValidator(QDoubleValidator())
        return editor


class UserTable(QtWidgets.QWidget):
    def __init__(self,Userdf):
            super().__init__()
            #self.resize(1200, 800)
            print("AppDemo")
            mainLayout = QtWidgets.QVBoxLayout()
            stylesheet = """
            QHeaderView::section{background-color: rgb(98, 102, 244);}
            """       
            self.table = TableWidget4(Userdf,list(Userdf.columns))
            self.table.setStyleSheet(u"QTableWidget {	\n"
"	background-color: rgb(250, 250, 250);\n"
"	padding: 10px;\n"
"	border-radius: 5px;\n"
"	gridline-color: rgb(0, 0, 0);\n"
"	border-bottom: 1px solid rgb(102, 204, 255);\n"
"   font: 9pt \"Segoe UI\";"
"}\n"
"QTableWidget::item{\n"
"	border-color: rgb(102, 204, 255);\n"
"	padding-left: 5px;\n"
"	padding-right: 5px;\n"
"	gridline-color: rgb(102, 204, 255);\n"
"}\n"
"QTableWidget::item:selected{\n"
"	background-color: rgb(85, 170, 255);\n"
"}\n"
"QScrollBar:horizontal {\n"
"    border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    height: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
"}\n"
" QScrollBar:vertical {\n"
"	border: none;\n"
"    background: rgb(52, 59, 72);\n"
"    width: 14px;\n"
"    margin: 0px 21px 0 21px;\n"
"	border-radius: 0px;\n"
" }\n"
"QHeaderView::section{\n"
"	Background-color: rgb(102, 204, 255);\n"
"	max-width: 30px;\n"
"	border: 1px solid rgb(32, 34, 42);\n"
"   border-bottom: 1px solid rgb(102, 204, 255);\n"
"   border-right: 1px solid rgb(102, 204, 255);\n"
"}\n"
""
                        "QTableWidget::horizontalHeader {	\n"
"	background-color: rgb(81, 255, 0);\n"
"}\n"
"QHeaderView::section:horizontal\n"
"{\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"	background-color: rgb(102, 204, 255);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 0px;\n"
"    border-top-right-radius: 0px;\n"
"}\n"
"QHeaderView::section:vertical\n"
"{\n"
"    border: 1px solid rgb(102, 204, 255);\n"
"    border: 1px solid rgb(32, 34, 42);\n"
"	background-color: rgb(102, 204, 255);\n"
"	padding: 3px;\n"
"	border-top-left-radius: 0px;\n"
"   border-top-right-radius: 0px;\n"
"}\n"
"")
            mainLayout.addWidget(self.table)
            self.setLayout(mainLayout)

class FloatDelegate(QtWidgets.QItemDelegate):
    def __init__(self, parent=None):
        super().__init__()

    def createEditor(self, parent, option, index):
        editor = QLineEdit(parent)
        editor.setValidator(QDoubleValidator())
        return editor
class TableWidget4(QtWidgets.QTableWidget):
    def __init__(self, df,header):
        super().__init__()
        self.df = df
        self.setStyleSheet('color:black;font-size: 20px;')
        nRows, nColumns = self.df.shape
        self.setColumnCount(nColumns)
        self.setRowCount(nRows)
        QtWidgets.QHeaderView
        self.setHorizontalHeaderLabels((header))
        self.verticalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.verticalHeader().hide()
        self.horizontalHeader().setSectionResizeMode(QtWidgets.QHeaderView.Stretch)
        self.horizontalHeader().setFixedHeight(30)

        self.setItemDelegateForColumn(1, FloatDelegate())
        # data insertion/
        for i in range(self.rowCount()):
            for j in range(self.columnCount()):
                self.setItem(i, j,
                             QtWidgets.QTableWidgetItem(str(self.df.iloc[i, j])))

        self.cellChanged[int, int].connect(self.updateDF)   
    QtWidgets.QTableWidgetItem
    def updateDF(self, row, column):
        text = self.item(row, column).text()
        self.df.iloc[row, column] = text