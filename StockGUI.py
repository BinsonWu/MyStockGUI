# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created: Sat Mar 11 14:45:23 2017
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1200, 900)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("AR PL UKai TW"))
        font.setPointSize(13)
        font.setItalic(False)
        MainWindow.setFont(font)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setDocumentMode(True)
        self.centralWidget = QtGui.QWidget(MainWindow)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("AR PL UKai CN"))
        font.setItalic(False)
        self.centralWidget.setFont(font)
        self.centralWidget.setCursor(QtGui.QCursor(QtCore.Qt.UpArrowCursor))
        self.centralWidget.setObjectName(_fromUtf8("centralWidget"))
        self.gridLayout = QtGui.QGridLayout(self.centralWidget)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.all = QtGui.QHBoxLayout()
        self.all.setObjectName(_fromUtf8("all"))
        self.left_ver = QtGui.QVBoxLayout()
        self.left_ver.setObjectName(_fromUtf8("left_ver"))
        self.graph_set = QtGui.QHBoxLayout()
        self.graph_set.setObjectName(_fromUtf8("graph_set"))
        self.MA3 = QtGui.QCheckBox(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MA3.sizePolicy().hasHeightForWidth())
        self.MA3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.MA3.setFont(font)
        self.MA3.setObjectName(_fromUtf8("MA3"))
        self.graph_set.addWidget(self.MA3)
        self.MA5 = QtGui.QCheckBox(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MA5.sizePolicy().hasHeightForWidth())
        self.MA5.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.MA5.setFont(font)
        self.MA5.setObjectName(_fromUtf8("MA5"))
        self.graph_set.addWidget(self.MA5)
        self.MA10 = QtGui.QCheckBox(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MA10.sizePolicy().hasHeightForWidth())
        self.MA10.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.MA10.setFont(font)
        self.MA10.setObjectName(_fromUtf8("MA10"))
        self.graph_set.addWidget(self.MA10)
        self.MA20 = QtGui.QCheckBox(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MA20.sizePolicy().hasHeightForWidth())
        self.MA20.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.MA20.setFont(font)
        self.MA20.setObjectName(_fromUtf8("MA20"))
        self.graph_set.addWidget(self.MA20)
        self.MA60 = QtGui.QCheckBox(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MA60.sizePolicy().hasHeightForWidth())
        self.MA60.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.MA60.setFont(font)
        self.MA60.setObjectName(_fromUtf8("MA60"))
        self.graph_set.addWidget(self.MA60)
        self.MA240 = QtGui.QCheckBox(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MA240.sizePolicy().hasHeightForWidth())
        self.MA240.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.MA240.setFont(font)
        self.MA240.setObjectName(_fromUtf8("MA240"))
        self.graph_set.addWidget(self.MA240)
        self.graph_set.setStretch(0, 1)
        self.graph_set.setStretch(1, 1)
        self.graph_set.setStretch(2, 1)
        self.graph_set.setStretch(3, 1)
        self.graph_set.setStretch(4, 1)
        self.graph_set.setStretch(5, 1)
        self.left_ver.addLayout(self.graph_set)
        self.graphicsView = QtGui.QGraphicsView(self.centralWidget)
        self.graphicsView.setObjectName(_fromUtf8("graphicsView"))
        self.left_ver.addWidget(self.graphicsView)
        self.graphicsView2 = QtGui.QGraphicsView(self.centralWidget)
        self.graphicsView2.setObjectName(_fromUtf8("graphicsView2"))
        self.left_ver.addWidget(self.graphicsView2)
        self.left_ver.setStretch(0, 1)
        self.left_ver.setStretch(1, 10)
        self.left_ver.setStretch(2, 5)
        self.all.addLayout(self.left_ver)
        self.right_ver = QtGui.QVBoxLayout()
        self.right_ver.setSpacing(8)
        self.right_ver.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.right_ver.setObjectName(_fromUtf8("right_ver"))
        self.stock_ver = QtGui.QHBoxLayout()
        self.stock_ver.setObjectName(_fromUtf8("stock_ver"))
        self.StockCB = QtGui.QComboBox(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.StockCB.sizePolicy().hasHeightForWidth())
        self.StockCB.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("AR PL UKai CN"))
        font.setPointSize(16)
        font.setKerning(False)
        self.StockCB.setFont(font)
        self.StockCB.setMouseTracking(False)
        self.StockCB.setEditable(True)
        self.StockCB.setProperty("currentText", _fromUtf8(""))
        self.StockCB.setSizeAdjustPolicy(QtGui.QComboBox.AdjustToContentsOnFirstShow)
        self.StockCB.setIconSize(QtCore.QSize(16, 16))
        self.StockCB.setDuplicatesEnabled(False)
        self.StockCB.setFrame(False)
        self.StockCB.setObjectName(_fromUtf8("StockCB"))
        self.stock_ver.addWidget(self.StockCB)
        self.showbutton = QtGui.QPushButton(self.centralWidget)
        self.showbutton.setEnabled(True)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.showbutton.sizePolicy().hasHeightForWidth())
        self.showbutton.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.showbutton.setFont(font)
        self.showbutton.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        self.showbutton.setObjectName(_fromUtf8("showbutton"))
        self.stock_ver.addWidget(self.showbutton)
        self.stock_ver.setStretch(0, 3)
        self.stock_ver.setStretch(1, 1)
        self.right_ver.addLayout(self.stock_ver)
        self.year_layout = QtGui.QHBoxLayout()
        self.year_layout.setObjectName(_fromUtf8("year_layout"))
        self.yearText1 = QtGui.QLineEdit(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.yearText1.sizePolicy().hasHeightForWidth())
        self.yearText1.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.yearText1.setFont(font)
        self.yearText1.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.yearText1.setProperty("clearButtonEnabled", False)
        self.yearText1.setObjectName(_fromUtf8("yearText1"))
        self.year_layout.addWidget(self.yearText1)
        self.connectIcon = QtGui.QLabel(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Maximum, QtGui.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.connectIcon.sizePolicy().hasHeightForWidth())
        self.connectIcon.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("AR PL UKai CN"))
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.connectIcon.setFont(font)
        self.connectIcon.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.connectIcon.setLineWidth(0)
        self.connectIcon.setScaledContents(True)
        self.connectIcon.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignHCenter)
        self.connectIcon.setWordWrap(True)
        self.connectIcon.setOpenExternalLinks(True)
        self.connectIcon.setObjectName(_fromUtf8("connectIcon"))
        self.year_layout.addWidget(self.connectIcon)
        self.yearText2 = QtGui.QLineEdit(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Ignored, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.yearText2.sizePolicy().hasHeightForWidth())
        self.yearText2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.yearText2.setFont(font)
        self.yearText2.setFrame(True)
        self.yearText2.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.yearText2.setObjectName(_fromUtf8("yearText2"))
        self.year_layout.addWidget(self.yearText2)
        self.year_layout.setStretch(0, 3)
        self.year_layout.setStretch(1, 1)
        self.year_layout.setStretch(2, 3)
        self.right_ver.addLayout(self.year_layout)
        self.h_p_layout = QtGui.QHBoxLayout()
        self.h_p_layout.setObjectName(_fromUtf8("h_p_layout"))
        self.h_p_Label = QtGui.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.h_p_Label.setFont(font)
        self.h_p_Label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.h_p_Label.setObjectName(_fromUtf8("h_p_Label"))
        self.h_p_layout.addWidget(self.h_p_Label)
        self.h_p_Text = QtGui.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.h_p_Text.setFont(font)
        self.h_p_Text.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.h_p_Text.setObjectName(_fromUtf8("h_p_Text"))
        self.h_p_layout.addWidget(self.h_p_Text)
        self.h_p_layout.setStretch(0, 1)
        self.h_p_layout.setStretch(1, 1)
        self.right_ver.addLayout(self.h_p_layout)
        self.l_p_layout = QtGui.QHBoxLayout()
        self.l_p_layout.setObjectName(_fromUtf8("l_p_layout"))
        self.l_p_Label = QtGui.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.l_p_Label.setFont(font)
        self.l_p_Label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.l_p_Label.setObjectName(_fromUtf8("l_p_Label"))
        self.l_p_layout.addWidget(self.l_p_Label)
        self.l_p_Text = QtGui.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.l_p_Text.setFont(font)
        self.l_p_Text.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.l_p_Text.setObjectName(_fromUtf8("l_p_Text"))
        self.l_p_layout.addWidget(self.l_p_Text)
        self.l_p_layout.setStretch(0, 1)
        self.l_p_layout.setStretch(1, 1)
        self.right_ver.addLayout(self.l_p_layout)
        self.CurseLayout = QtGui.QHBoxLayout()
        self.CurseLayout.setObjectName(_fromUtf8("CurseLayout"))
        self.CurseLabel = QtGui.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("AR PL UKai CN"))
        font.setPointSize(20)
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        self.CurseLabel.setFont(font)
        self.CurseLabel.setObjectName(_fromUtf8("CurseLabel"))
        self.CurseLayout.addWidget(self.CurseLabel)
        self.dateText = QtGui.QLabel(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateText.sizePolicy().hasHeightForWidth())
        self.dateText.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("AR PL UKai CN"))
        font.setPointSize(20)
        font.setItalic(False)
        self.dateText.setFont(font)
        self.dateText.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.dateText.setAutoFillBackground(True)
        self.dateText.setFrameShape(QtGui.QFrame.StyledPanel)
        self.dateText.setScaledContents(False)
        self.dateText.setAlignment(QtCore.Qt.AlignCenter)
        self.dateText.setObjectName(_fromUtf8("dateText"))
        self.CurseLayout.addWidget(self.dateText)
        self.pointText = QtGui.QLabel(self.centralWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pointText.sizePolicy().hasHeightForWidth())
        self.pointText.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("AR PL UKai CN"))
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        self.pointText.setFont(font)
        self.pointText.setFocusPolicy(QtCore.Qt.ClickFocus)
        self.pointText.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.pointText.setAutoFillBackground(True)
        self.pointText.setFrameShape(QtGui.QFrame.StyledPanel)
        self.pointText.setLineWidth(0)
        self.pointText.setAlignment(QtCore.Qt.AlignCenter)
        self.pointText.setWordWrap(False)
        self.pointText.setMargin(0)
        self.pointText.setObjectName(_fromUtf8("pointText"))
        self.CurseLayout.addWidget(self.pointText)
        self.CurseLayout.setStretch(1, 1)
        self.CurseLayout.setStretch(2, 1)
        self.right_ver.addLayout(self.CurseLayout)
        self.opLayout = QtGui.QHBoxLayout()
        self.opLayout.setObjectName(_fromUtf8("opLayout"))
        self.opLabel = QtGui.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.opLabel.setFont(font)
        self.opLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.opLabel.setObjectName(_fromUtf8("opLabel"))
        self.opLayout.addWidget(self.opLabel)
        self.opText = QtGui.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.opText.setFont(font)
        self.opText.setObjectName(_fromUtf8("opText"))
        self.opLayout.addWidget(self.opText)
        self.right_ver.addLayout(self.opLayout)
        self.clLatout = QtGui.QHBoxLayout()
        self.clLatout.setObjectName(_fromUtf8("clLatout"))
        self.clLabel = QtGui.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.clLabel.setFont(font)
        self.clLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.clLabel.setObjectName(_fromUtf8("clLabel"))
        self.clLatout.addWidget(self.clLabel)
        self.clText = QtGui.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.clText.setFont(font)
        self.clText.setObjectName(_fromUtf8("clText"))
        self.clLatout.addWidget(self.clText)
        self.right_ver.addLayout(self.clLatout)
        self.hpLayout = QtGui.QHBoxLayout()
        self.hpLayout.setObjectName(_fromUtf8("hpLayout"))
        self.hpLabel = QtGui.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.hpLabel.setFont(font)
        self.hpLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.hpLabel.setObjectName(_fromUtf8("hpLabel"))
        self.hpLayout.addWidget(self.hpLabel)
        self.hpText = QtGui.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.hpText.setFont(font)
        self.hpText.setObjectName(_fromUtf8("hpText"))
        self.hpLayout.addWidget(self.hpText)
        self.right_ver.addLayout(self.hpLayout)
        self.fpLayout = QtGui.QHBoxLayout()
        self.fpLayout.setObjectName(_fromUtf8("fpLayout"))
        self.fpLabel = QtGui.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.fpLabel.setFont(font)
        self.fpLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.fpLabel.setObjectName(_fromUtf8("fpLabel"))
        self.fpLayout.addWidget(self.fpLabel)
        self.fpText = QtGui.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.fpText.setFont(font)
        self.fpText.setObjectName(_fromUtf8("fpText"))
        self.fpLayout.addWidget(self.fpText)
        self.right_ver.addLayout(self.fpLayout)
        self.MA3Layout = QtGui.QHBoxLayout()
        self.MA3Layout.setObjectName(_fromUtf8("MA3Layout"))
        self.MA3Label = QtGui.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.MA3Label.setFont(font)
        self.MA3Label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.MA3Label.setObjectName(_fromUtf8("MA3Label"))
        self.MA3Layout.addWidget(self.MA3Label)
        self.MA3Text = QtGui.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.MA3Text.setFont(font)
        self.MA3Text.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.MA3Text.setObjectName(_fromUtf8("MA3Text"))
        self.MA3Layout.addWidget(self.MA3Text)
        self.right_ver.addLayout(self.MA3Layout)
        self.MA5Layout = QtGui.QHBoxLayout()
        self.MA5Layout.setObjectName(_fromUtf8("MA5Layout"))
        self.MA5Label = QtGui.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.MA5Label.setFont(font)
        self.MA5Label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.MA5Label.setObjectName(_fromUtf8("MA5Label"))
        self.MA5Layout.addWidget(self.MA5Label)
        self.MA5Text = QtGui.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.MA5Text.setFont(font)
        self.MA5Text.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.MA5Text.setObjectName(_fromUtf8("MA5Text"))
        self.MA5Layout.addWidget(self.MA5Text)
        self.right_ver.addLayout(self.MA5Layout)
        self.MA10Layout = QtGui.QHBoxLayout()
        self.MA10Layout.setObjectName(_fromUtf8("MA10Layout"))
        self.MA10Label = QtGui.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.MA10Label.setFont(font)
        self.MA10Label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.MA10Label.setObjectName(_fromUtf8("MA10Label"))
        self.MA10Layout.addWidget(self.MA10Label)
        self.MA10Text = QtGui.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.MA10Text.setFont(font)
        self.MA10Text.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.MA10Text.setObjectName(_fromUtf8("MA10Text"))
        self.MA10Layout.addWidget(self.MA10Text)
        self.right_ver.addLayout(self.MA10Layout)
        self.MA20Layout = QtGui.QHBoxLayout()
        self.MA20Layout.setObjectName(_fromUtf8("MA20Layout"))
        self.MA20Label = QtGui.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.MA20Label.setFont(font)
        self.MA20Label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.MA20Label.setObjectName(_fromUtf8("MA20Label"))
        self.MA20Layout.addWidget(self.MA20Label)
        self.MA20Text = QtGui.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.MA20Text.setFont(font)
        self.MA20Text.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.MA20Text.setObjectName(_fromUtf8("MA20Text"))
        self.MA20Layout.addWidget(self.MA20Text)
        self.right_ver.addLayout(self.MA20Layout)
        self.MA60Layout = QtGui.QHBoxLayout()
        self.MA60Layout.setObjectName(_fromUtf8("MA60Layout"))
        self.MA60Label = QtGui.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.MA60Label.setFont(font)
        self.MA60Label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.MA60Label.setObjectName(_fromUtf8("MA60Label"))
        self.MA60Layout.addWidget(self.MA60Label)
        self.MA60Text = QtGui.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.MA60Text.setFont(font)
        self.MA60Text.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.MA60Text.setObjectName(_fromUtf8("MA60Text"))
        self.MA60Layout.addWidget(self.MA60Text)
        self.right_ver.addLayout(self.MA60Layout)
        self.MA240Layout = QtGui.QHBoxLayout()
        self.MA240Layout.setObjectName(_fromUtf8("MA240Layout"))
        self.MA240Label = QtGui.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.MA240Label.setFont(font)
        self.MA240Label.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.MA240Label.setObjectName(_fromUtf8("MA240Label"))
        self.MA240Layout.addWidget(self.MA240Label)
        self.MA240Text = QtGui.QLabel(self.centralWidget)
        font = QtGui.QFont()
        font.setPointSize(18)
        self.MA240Text.setFont(font)
        self.MA240Text.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.MA240Text.setObjectName(_fromUtf8("MA240Text"))
        self.MA240Layout.addWidget(self.MA240Text)
        self.right_ver.addLayout(self.MA240Layout)
        self.right_ver.setStretch(0, 1)
        self.right_ver.setStretch(1, 1)
        self.right_ver.setStretch(2, 1)
        self.right_ver.setStretch(3, 1)
        self.right_ver.setStretch(4, 1)
        self.right_ver.setStretch(5, 1)
        self.right_ver.setStretch(6, 1)
        self.right_ver.setStretch(7, 1)
        self.right_ver.setStretch(8, 1)
        self.right_ver.setStretch(9, 1)
        self.right_ver.setStretch(10, 1)
        self.right_ver.setStretch(11, 1)
        self.right_ver.setStretch(12, 1)
        self.right_ver.setStretch(13, 1)
        self.right_ver.setStretch(14, 1)
        self.all.addLayout(self.right_ver)
        self.all.setStretch(0, 2)
        self.all.setStretch(1, 1)
        self.gridLayout.addLayout(self.all, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.StockCB, self.showbutton)
        MainWindow.setTabOrder(self.showbutton, self.yearText1)
        MainWindow.setTabOrder(self.yearText1, self.yearText2)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Candlestick", None))
        self.MA3.setText(_translate("MainWindow", "MA3", None))
        self.MA5.setText(_translate("MainWindow", "MA5", None))
        self.MA10.setText(_translate("MainWindow", "MA10", None))
        self.MA20.setText(_translate("MainWindow", "MA20", None))
        self.MA60.setText(_translate("MainWindow", "MA60", None))
        self.MA240.setText(_translate("MainWindow", "MA240", None))
        self.showbutton.setText(_translate("MainWindow", "Show", None))
        self.yearText1.setText(_translate("MainWindow", "81", None))
        self.connectIcon.setText(_translate("MainWindow", "~", None))
        self.yearText2.setText(_translate("MainWindow", "106", None))
        self.h_p_Label.setText(_translate("MainWindow", "範圍內最高價:", None))
        self.h_p_Text.setText(_translate("MainWindow", "High", None))
        self.l_p_Label.setText(_translate("MainWindow", "範圍內最低價:", None))
        self.l_p_Text.setText(_translate("MainWindow", "Low", None))
        self.CurseLabel.setText(_translate("MainWindow", "游標:", None))
        self.dateText.setText(_translate("MainWindow", "日期", None))
        self.pointText.setText(_translate("MainWindow", "點數", None))
        self.opLabel.setText(_translate("MainWindow", "開盤價：", None))
        self.opText.setText(_translate("MainWindow", "None", None))
        self.clLabel.setText(_translate("MainWindow", "收盤價：", None))
        self.clText.setText(_translate("MainWindow", "None", None))
        self.hpLabel.setText(_translate("MainWindow", "最高價：", None))
        self.hpText.setText(_translate("MainWindow", "None", None))
        self.fpLabel.setText(_translate("MainWindow", "最低價：", None))
        self.fpText.setText(_translate("MainWindow", "None", None))
        self.MA3Label.setText(_translate("MainWindow", "MA3:", None))
        self.MA3Text.setText(_translate("MainWindow", "None", None))
        self.MA5Label.setText(_translate("MainWindow", "MA5:", None))
        self.MA5Text.setText(_translate("MainWindow", "None", None))
        self.MA10Label.setText(_translate("MainWindow", "MA10:", None))
        self.MA10Text.setText(_translate("MainWindow", "None", None))
        self.MA20Label.setText(_translate("MainWindow", "MA20:", None))
        self.MA20Text.setText(_translate("MainWindow", "None", None))
        self.MA60Label.setText(_translate("MainWindow", "MA60:", None))
        self.MA60Text.setText(_translate("MainWindow", "None", None))
        self.MA240Label.setText(_translate("MainWindow", "MA240:", None))
        self.MA240Text.setText(_translate("MainWindow", "None", None))

