# -*- coding: utf-8 -*-
from PyQt4 import QtCore,QtGui,QtSql
import sys
import StockGUI

from selenium import webdriver

from bs4 import BeautifulSoup
import pandas as pd

import MySQLdb

import pyqtgraph as pg
from pyqtgraph import QtCore, QtGui

class graphicsItem(QtGui.QGraphicsItem):
    def __init__ (self, parent=None):
        super(graphicsScene, self).__init__ (parent)


class graphicsScene(QtGui.QGraphicsScene):
    setDateAndPoint = QtCore.pyqtSignal(int,int)
    def __init__ (self, parent=None):
        super(graphicsScene, self).__init__ (parent)
        #self.signal1.connect(self.SignalSuccess)

    def mousePressEvent(self, event):
        position = QtCore.QPointF(event.scenePos())
        #print "pressed here: " + str(position.x()) + ", " + str(position.y())
        self.setDateAndPoint.emit(position.x(), position.y())
        self.update()

    def mouseMoveEvent(self, event):
        position = QtCore.QPointF(event.scenePos())
        #print "moved here: " + str(position.x()) + ", " + str(position.y())
        self.setDateAndPoint.emit(position.x(),position.y())
        self.update()

    def mouseReleaseEvent(self, event):
        position = QtCore.QPointF(event.scenePos())
        #print "released here: " + str(position.x()) + ", " + str(position.y())
        self.setDateAndPoint.emit(position.x(), position.y())
        self.update()


## Create a subclass of GraphicsObject.
## The only required methods are paint() and boundingRect()
## (see QGraphicsItem documentation)
class Mainwindow(QtGui.QMainWindow,StockGUI.Ui_MainWindow):
    def __init__(self,parent=None):
        super(Mainwindow, self).__init__(parent)
        self.setupUi(self)

        #Style
        self.setStyleSheet("color : blue;")

        #DataBaseSet&Connect
        self.db = QtSql.QSqlDatabase.addDatabase("QMYSQL")
        self.db.setHostName("")
        self.db.setUserName("")
        self.db.setPassword("")
        self.db.setDatabaseName("")
        if (self.db.open()):
            QtCore.qDebug("connected ")
        else:
            QtCore.qDebug("Connection FAILED.")
        self.ID_Name_Table  = []

        # 此支股票 year1 ~ year2 的資料
        self.data           = []

        # Initial button table
        self.model          = QtSql.QSqlTableModel()
        self.tableView      = QtGui.QTableView()

        #Set ComBox
        self.InitComboBoxData()
        self.ComboBoxData_Change_Handler()

        #Function Connect
        self.showbutton.clicked.connect(self.showStockTable)
        self.yearText1.textChanged.connect(self.YearText_Change_Handler)
        self.yearText2.textChanged.connect(self.YearText_Change_Handler)
        self.StockCB.currentIndexChanged.connect(self.ComboBoxData_Change_Handler)
        self.MA3.clicked.connect(self.CheckBox_Change_Handler)
        self.MA5.clicked.connect(self.CheckBox_Change_Handler)
        self.MA10.clicked.connect(self.CheckBox_Change_Handler)
        self.MA20.clicked.connect(self.CheckBox_Change_Handler)
        self.MA60.clicked.connect(self.CheckBox_Change_Handler)
        self.MA240.clicked.connect(self.CheckBox_Change_Handler)

    def InitComboBoxData(self):
        query   = QtSql.QSqlQuery()
        query.exec_("SELECT ID,Name FROM Stock_ID_Name")
        i = 0
        while query.next():
            Stock_ID        = query.value(0).toString()
            Stock_Name      = query.value(1).toString()
            Stock_ID + "_" + Stock_Name
            self.ID_Name_Table.append(Stock_ID + "_" + Stock_Name)
            self.StockCB.addItem(self.ID_Name_Table[i])
            i = i + 1

    #Signal
    def ComboBoxData_Change_Handler(self):
        self.setHLPrice()
        self.setStockData()

        self.DrawGrid(QtCore.Qt.darkGray)
        self.DrawAllLine()
        self.DrawCandlestick()

        self.graphicsView.setAlignment(QtCore.Qt.AlignRight)
        self.graphicsView.setAlignment(QtCore.Qt.AlignHCenter)
        self.graphicsView.setScene(self.scene)

    def YearText_Change_Handler(self):
        self.setHLPrice()
        self.setStockData()

        self.DrawGrid(QtCore.Qt.darkGray)
        self.DrawAllLine()
        self.DrawCandlestick()

        self.graphicsView.setAlignment(QtCore.Qt.AlignRight)
        self.graphicsView.setAlignment(QtCore.Qt.AlignHCenter)
        self.graphicsView.setScene(self.scene)

    def CheckBox_Change_Handler(self):
        self.DrawAllLine()
        self.DrawCandlestick()

        self.graphicsView.setAlignment(QtCore.Qt.AlignRight)
        self.graphicsView.setAlignment(QtCore.Qt.AlignHCenter)
        self.graphicsView.setScene(self.scene)

    def setDateAndPoint(self,posx,posy):
        nthItem = 0
        point   = 0
        nthItem = (posx + 5) / 15
        point = float( (-posy + self.minh) / float(self.ntime) )
        #print("%f point:%f" % (self.minh,point) )
        self.dateText.setText(self.datearr[nthItem])
        self.pointText.setText(str(point))
        optext      = str(self.o_p[nthItem]/float(self.ntime))
        cltext      = str(self.c_p[nthItem] / float(self.ntime))
        hptext      = str(self.h_p[nthItem] / float(self.ntime))
        fptext      = str(self.f_p[nthItem] / float(self.ntime))
        ma3text     = str(self.dataMA3[nthItem] / float(self.ntime))
        ma5text     = str(self.dataMA5[nthItem] / float(self.ntime))
        ma10text    = str(self.dataMA10[nthItem] / float(self.ntime))
        ma20text    = str(self.dataMA20[nthItem] / float(self.ntime))
        ma60text    = str(self.dataMA60[nthItem] / float(self.ntime))
        ma240text   = str(self.dataMA240[nthItem] / float(self.ntime))

        self.opText.setText(optext)
        self.clText.setText(cltext)
        self.hpText.setText(hptext)
        self.fpText.setText(fptext)
        self.MA3Text.setText(ma3text)
        self.MA5Text.setText(ma5text)
        self.MA10Text.setText(ma10text)
        self.MA20Text.setText(ma20text)
        self.MA60Text.setText(ma60text)
        self.MA240Text.setText(ma240text)

    def showStockTable(self,i):
        self.model.setTable(self.Stock.currentText())
        self.model.select()
        self.tableView.setWindowTitle(self.Stock.currentText())
        self.tableView.setModel(self.model)
        self.tableView.resize(600, 600)
        self.tableView.show()

    #Data Function
    def setHLPrice(self):
        query = QtSql.QSqlQuery()
        sql  = "SELECT * FROM " + self.StockCB.currentText()
        query.exec_(sql)
        earliest_y  = ""
        last_y      = ""
        n=0
        while query.next():
            self.data.append((float(n+1),query.value(1).toFloat(),query.value(2).toFloat(),query.value(3).toFloat(),query.value(4).toFloat()))
            tempstring = query.value(0).toString()
            if n == 0:
                for ei in range(len(tempstring)):
                    if tempstring[ei] == '/':
                        earliest_y  = tempstring[:ei]
                        break
            for li in range(len(tempstring)):
                if tempstring[li] == '/':
                    last_y = tempstring[:li]
                    break
            n = n + 1

        stockcbtext = self.StockCB.currentText()
        fyear1text  = float(str(self.yearText1.text()))
        fyear2text  = float(str(self.yearText2.text()))
        year1text   = self.yearText1.text()
        year2text   = self.yearText2.text()
        sqlMax = "SELECT MAX(HighestPrice) FROM "   + stockcbtext
        sqlMin = "SELECT MIN(FloorPrice) FROM "     + stockcbtext

        #判斷範圍
        if float(earliest_y) >= fyear1text and  float(last_y) <= fyear2text :
            sqlMax  = "SELECT MAX(HighestPrice) FROM "  + stockcbtext \
                    + " WHERE Date BETWEEN "            + earliest_y                + " and "       + last_y
            sqlMin  = "SELECT MIN(FloorPrice) FROM "    + stockcbtext \
                    + " WHERE Date BETWEEN "            + earliest_y                + " and "       + last_y
        elif float(earliest_y) >= fyear1text and  float(last_y) > fyear2text :
            sqlMax  = "SELECT MAX(HighestPrice) FROM "  + stockcbtext \
                    + " WHERE Date BETWEEN "            + earliest_y                + " and "       + year2text
            sqlMin  = "SELECT MIN(FloorPrice) FROM "    + stockcbtext \
                    + " WHERE Date BETWEEN "            + earliest_y                + " and "       + year2text
        elif float(earliest_y) < fyear1text and  float(last_y) <= fyear2text :
            sqlMax  = "SELECT MAX(HighestPrice) FROM "  + stockcbtext \
                    + " WHERE Date BETWEEN "            + year1text         + " and "       + last_y
            sqlMin  = "SELECT MIN(FloorPrice) FROM "    + stockcbtext \
                    + " WHERE Date BETWEEN "            + year1text         + " and "       + last_y
        elif float(earliest_y) < fyear1text and  float(last_y) > fyear2text :
            sqlMax  = "SELECT MAX(HighestPrice) FROM "  + stockcbtext \
                    + " WHERE Date BETWEEN "            + year1text         + " and "       + year2text
            sqlMin  = "SELECT MIN(FloorPrice) FROM "    + stockcbtext \
                    + " WHERE Date BETWEEN "            + year1text         + " and "       + year2text
        query.exec_(sqlMax)
        while query.next():
            string      = query.value(0).toString()
            new_val     = "%.2f" % float(string)
            self.h_p_Text.setText(str(new_val))
        query.exec_(sqlMin)
        while query.next():
            string      = query.value(0).toString()
            new_val     = "%.2f" % float(string)
            self.l_p_Text.setText(str(new_val))
        #QtCore.qDebug(sqlMax)
        #QtCore.qDebug(sqlMin)

    def setStockData(self):
        self.scene = graphicsScene(self)
        # 連接到 signal
        self.scene.setDateAndPoint.connect(self.setDateAndPoint)
        # 背景黑色
        self.scene.setBackgroundBrush(QtCore.Qt.black)

        stockcbtext = self.StockCB.currentText()
        fyear1text = float(str(self.yearText1.text()))
        fyear2text = float(str(self.yearText2.text()))
        year1text = self.yearText1.text()
        year2text = self.yearText2.text()
        self.xScale = 1.0
        self.yScale = 1.0

        # 讀取資料
        query = QtSql.QSqlQuery()
        sql = "SELECT * FROM " + stockcbtext
        query.exec_(sql)
        earliest_y = ""
        last_y = ""
        n = 0
        while query.next():
            tempstring = query.value(0).toString()
            if n == 0:
                for ei in range(len(tempstring)):
                    if tempstring[ei] == '/':
                        earliest_y = tempstring[:ei]
                        break
            for li in range(len(tempstring)):
                if tempstring[li] == '/':
                    last_y = tempstring[:li]
                    break
            n = n + 1

        query = QtSql.QSqlQuery()
        sql = "SELECT * FROM " + stockcbtext
        if float(earliest_y) >= fyear1text and float(last_y) <= fyear2text:
            sql = "SELECT * FROM " + stockcbtext \
                  + " WHERE Date BETWEEN " + earliest_y + " and " + last_y
        elif float(earliest_y) >= fyear1text and float(last_y) > fyear2text:
            sql = "SELECT * FROM " + stockcbtext \
                  + " WHERE Date BETWEEN " + earliest_y + " and " + year2text
        elif float(earliest_y) < fyear1text and float(last_y) <= fyear2text:
            sql = "SELECT * FROM " + stockcbtext \
                  + " WHERE Date BETWEEN " + year1text + " and " + last_y
        elif float(earliest_y) < fyear1text and float(last_y) > fyear2text:
            sql = "SELECT * FROM " + stockcbtext \
                  + " WHERE Date BETWEEN " + year1text + " and " + year2text
        query.exec_(sql)
        nth = 0
        self.maxh = 0
        self.maxw = 0
        self.minh = 100000
        self.datearr = []
        self.o_p = []
        self.c_p = []
        self.h_p = []
        self.f_p = []
        self.rec_h = []
        self.line_h = []
        self.dataMA3 = []
        self.dataMA5 = []
        self.dataMA10 = []
        self.dataMA20 = []
        self.dataMA60 = []
        self.dataMA240 = []

        while query.next():
            nth = nth + 1
            self.ntime = 100
            self.datearr.append(query.value(0).toString())
            self.o_p.append(int(float(query.value(1).toString()) * self.ntime))
            self.c_p.append(int(float(query.value(2).toString()) * self.ntime))
            self.h_p.append(int(float(query.value(4).toString()) * self.ntime))
            self.f_p.append(int(float(query.value(3).toString()) * self.ntime))
            self.dataMA3.append(int(float(query.value(5).toString()) * self.ntime))
            self.dataMA5.append(int(float(query.value(6).toString()) * self.ntime))
            self.dataMA10.append(int(float(query.value(7).toString()) * self.ntime))
            self.dataMA20.append(int(float(query.value(8).toString()) * self.ntime))
            self.dataMA60.append(int(float(query.value(9).toString()) * self.ntime))
            self.dataMA240.append(int(float(query.value(10).toString()) * self.ntime))
            self.rec_h.append(self.c_p[nth - 1] - self.o_p[nth - 1])
            self.line_h.append(self.f_p[nth - 1] - self.h_p[nth - 1])
            if self.h_p[nth - 1] > self.maxh:
                self.maxh = self.h_p[nth - 1]
            if self.f_p[nth - 1] < self.minh:
                self.minh = self.f_p[nth - 1]
        self.maxw = (nth) * 15 - 5

    def DrawCandlestick(self):
        # 決定顏色
        # 決定x y w h
        # 決定座標
        for i in range(len(self.datearr)):
            # 因為左上角是 (0,0) 所以 y 軸要作變化
            xtime = self.xScale
            ytime = self.yScale
            lx  = xtime*(4 + i*15)
            ly  = ytime*(-self.h_p[i] + self.minh)
            lw  = 2
            lh  = ytime*(-self.line_h[i])
            sx  = xtime*(0 + i*15)
            sy  = ytime*(-self.o_p[i]+self.minh)
            sw  = xtime*(10)
            sh  = ytime*(-self.rec_h[i])
            # 畫直線
            self.item = QtGui.QGraphicsRectItem(lx,ly,lw,lh)
            self.item.setBrush(QtCore.Qt.white)
            self.scene.addItem(self.item)
            # 畫方圖
            self.item = QtGui.QGraphicsRectItem(sx,sy,sw,sh)
            self.item.setPen(QtCore.Qt.white)
            if self.c_p[i] > self.o_p[i]:
                self.item.setBrush(QtCore.Qt.red)
            else:
                self.item.setBrush(QtCore.Qt.green)
            self.scene.addItem(self.item)

    def DrawAllLine(self):
        for i in range(len(self.dataMA3)):
            if i > 0 :
                if self.MA3.checkState() == 2:
                    self.DrawALine(i, self.dataMA3, QtCore.Qt.cyan)
                if self.MA5.checkState() == 2:
                    self.DrawALine(i, self.dataMA5, QtCore.Qt.darkMagenta)
                if self.MA10.checkState() == 2:
                    self.DrawALine(i, self.dataMA10, QtCore.Qt.blue)
                if self.MA20.checkState() == 2:
                    self.DrawALine(i, self.dataMA20, QtCore.Qt.magenta)
                if self.MA60.checkState() == 2:
                    self.DrawALine(i, self.dataMA60, QtCore.Qt.yellow)
                if self.MA240.checkState() == 2:
                    self.DrawALine(i,self.dataMA240,QtCore.Qt.darkYellow)

    def DrawALine(self,n,linedataArr,color):
        xtime = self.xScale
        ytime = self.yScale
        lx1  = xtime*(5 + (n - 1) * 15)
        ly1  = ytime*(-linedataArr[n - 1] + self.minh)
        lx2  = xtime*(5 + n * 15)
        ly2  = ytime*(-linedataArr[n] + self.minh)
        self.item = QtGui.QGraphicsLineItem(lx1,ly1,lx2,ly2)
        self.item.setPen(QtGui.QPen(color, 2, QtCore.Qt.SolidLine,
                                    QtCore.Qt.RoundCap, QtCore.Qt.RoundJoin))
        self.scene.addItem(self.item)

    def DrawGrid(self,color):
        firstLineY = 50 - (self.maxh - self.minh)%50
        for nthyLine in range( (self.maxh - self.minh)/50 ):
            xtime = self.xScale
            ytime = self.yScale
            lx1 = xtime * (0)
            ly1 = ytime * (-firstLineY - 50*nthyLine)
            lx2 = xtime * (self.maxw)
            ly2 = ytime * (-firstLineY - 50*nthyLine)
            self.item = QtGui.QGraphicsLineItem(lx1, ly1, lx2, ly2)
            self.item.setPen(QtGui.QPen(color, 1, QtCore.Qt.SolidLine,
                                        QtCore.Qt.RoundCap, QtCore.Qt.RoundJoin))
            self.scene.addItem(self.item)

        for nthxLine in range(1,self.maxw / (15*5)+1,1):
            xtime = self.xScale
            ytime = self.yScale
            lx1 = xtime * (nthxLine*15*5)
            ly1 = ytime * (0)
            lx2 = xtime * (nthxLine*15*5)
            ly2 = ytime * (-(self.maxh-self.minh))
            self.item = QtGui.QGraphicsLineItem(lx1, ly1, lx2, ly2)
            self.item.setPen(QtGui.QPen(color, 1, QtCore.Qt.SolidLine,
                                        QtCore.Qt.RoundCap, QtCore.Qt.RoundJoin))
            self.scene.addItem(self.item)

    def __del__(self):
        self.db.close()


def main():
    app = QtGui.QApplication(sys.argv)
    dmw = Mainwindow()
    dmw.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
