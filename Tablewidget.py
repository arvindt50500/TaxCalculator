from Main import *
import pandas as pd
import sqlite3

class TableAdd(QtWidgets.QWidget):
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