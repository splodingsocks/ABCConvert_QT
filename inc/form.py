# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'forms/form.ui'
#
# Created: Wed Mar 21 09:17:48 2012
#      by: pyside-uic 0.2.13 running on PySide 1.1.0
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(850, 500)
        self.horizontalLayout_2 = QtGui.QHBoxLayout(Form)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.tabBar = QtGui.QWidget(Form)
        self.tabBar.setObjectName("tabBar")
        self.verticalLayout_7 = QtGui.QVBoxLayout(self.tabBar)
        self.verticalLayout_7.setSpacing(-1)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.but_tab_convert = QtGui.QCheckBox(self.tabBar)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.but_tab_convert.sizePolicy().hasHeightForWidth())
        self.but_tab_convert.setSizePolicy(sizePolicy)
        self.but_tab_convert.setMinimumSize(QtCore.QSize(60, 60))
        self.but_tab_convert.setBaseSize(QtCore.QSize(35, 35))
        self.but_tab_convert.setText("")
        self.but_tab_convert.setCheckable(True)
        self.but_tab_convert.setChecked(True)
        self.but_tab_convert.setAutoExclusive(True)
        self.but_tab_convert.setObjectName("but_tab_convert")
        self.verticalLayout_7.addWidget(self.but_tab_convert)
        self.but_tab_history = QtGui.QCheckBox(self.tabBar)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.but_tab_history.sizePolicy().hasHeightForWidth())
        self.but_tab_history.setSizePolicy(sizePolicy)
        self.but_tab_history.setMinimumSize(QtCore.QSize(60, 60))
        self.but_tab_history.setBaseSize(QtCore.QSize(35, 35))
        self.but_tab_history.setText("")
        self.but_tab_history.setCheckable(True)
        self.but_tab_history.setChecked(False)
        self.but_tab_history.setAutoExclusive(True)
        self.but_tab_history.setObjectName("but_tab_history")
        self.verticalLayout_7.addWidget(self.but_tab_history)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_7.addItem(spacerItem)
        self.horizontalLayout_2.addWidget(self.tabBar)
        self.stackedWidget = QtGui.QStackedWidget(Form)
        self.stackedWidget.setLineWidth(0)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page_convert = QtGui.QWidget()
        self.page_convert.setObjectName("page_convert")
        self.verticalLayout_2 = QtGui.QVBoxLayout(self.page_convert)
        self.verticalLayout_2.setContentsMargins(12, 12, 12, 12)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        spacerItem1 = QtGui.QSpacerItem(20, 30, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem1)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_convert = QtGui.QFrame(self.page_convert)
        self.frame_convert.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_convert.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_convert.setObjectName("frame_convert")
        self.verticalLayout_3 = QtGui.QVBoxLayout(self.frame_convert)
        self.verticalLayout_3.setSpacing(-1)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtGui.QLabel(self.frame_convert)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label)
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.le_scenePath = QtGui.QLineEdit(self.frame_convert)
        self.le_scenePath.setObjectName("le_scenePath")
        self.horizontalLayout.addWidget(self.le_scenePath)
        self.but_pick = QtGui.QPushButton(self.frame_convert)
        self.but_pick.setObjectName("but_pick")
        self.horizontalLayout.addWidget(self.but_pick)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.but_go = QtGui.QPushButton(self.frame_convert)
        self.but_go.setObjectName("but_go")
        self.verticalLayout_3.addWidget(self.but_go)
        self.verticalLayout.addWidget(self.frame_convert)
        self.frame_progress = QtGui.QFrame(self.page_convert)
        self.frame_progress.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_progress.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_progress.setObjectName("frame_progress")
        self.verticalLayout_4 = QtGui.QVBoxLayout(self.frame_progress)
        self.verticalLayout_4.setSpacing(-1)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.te_activeLog = QtGui.QTextEdit(self.frame_progress)
        self.te_activeLog.setObjectName("te_activeLog")
        self.verticalLayout_4.addWidget(self.te_activeLog)
        self.progressBar = QtGui.QProgressBar(self.frame_progress)
        self.progressBar.setProperty("value", 24)
        self.progressBar.setObjectName("progressBar")
        self.verticalLayout_4.addWidget(self.progressBar)
        self.but_another = QtGui.QPushButton(self.frame_progress)
        self.but_another.setObjectName("but_another")
        self.verticalLayout_4.addWidget(self.but_another)
        self.verticalLayout.addWidget(self.frame_progress)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        spacerItem2 = QtGui.QSpacerItem(20, 42, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem2)
        self.stackedWidget.addWidget(self.page_convert)
        self.page_history = QtGui.QWidget()
        self.page_history.setObjectName("page_history")
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.page_history)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.label_8 = QtGui.QLabel(self.page_history)
        self.label_8.setObjectName("label_8")
        self.verticalLayout_5.addWidget(self.label_8)
        self.list_scenes = QtGui.QTableView(self.page_history)
        self.list_scenes.setObjectName("list_scenes")
        self.verticalLayout_5.addWidget(self.list_scenes)
        self.frame_3 = QtGui.QFrame(self.page_history)
        self.frame_3.setFrameShape(QtGui.QFrame.NoFrame)
        self.frame_3.setFrameShadow(QtGui.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.verticalLayout_6 = QtGui.QVBoxLayout(self.frame_3)
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName("gridLayout_2")
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem3, 1, 2, 1, 1)
        self.label_3 = QtGui.QLabel(self.frame_3)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 1, 3, 1, 1)
        self.label_sceneDate = QtGui.QLabel(self.frame_3)
        self.label_sceneDate.setObjectName("label_sceneDate")
        self.gridLayout_2.addWidget(self.label_sceneDate, 1, 4, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem4, 2, 2, 1, 1)
        self.label_4 = QtGui.QLabel(self.frame_3)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 2, 3, 1, 1)
        self.label_sceneStatus = QtGui.QLabel(self.frame_3)
        self.label_sceneStatus.setObjectName("label_sceneStatus")
        self.gridLayout_2.addWidget(self.label_sceneStatus, 2, 4, 1, 1)
        self.label_sceneName = QtGui.QLabel(self.frame_3)
        self.label_sceneName.setObjectName("label_sceneName")
        self.gridLayout_2.addWidget(self.label_sceneName, 0, 4, 1, 1)
        self.label_2 = QtGui.QLabel(self.frame_3)
        self.label_2.setObjectName("label_2")
        self.gridLayout_2.addWidget(self.label_2, 0, 3, 1, 1)
        self.label_9 = QtGui.QLabel(self.frame_3)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 2, 0, 1, 1)
        self.verticalLayout_6.addLayout(self.gridLayout_2)
        self.te_SceneLog = QtGui.QTextEdit(self.frame_3)
        self.te_SceneLog.setObjectName("te_SceneLog")
        self.verticalLayout_6.addWidget(self.te_SceneLog)
        self.verticalLayout_5.addWidget(self.frame_3)
        self.stackedWidget.addWidget(self.page_history)
        self.horizontalLayout_2.addWidget(self.stackedWidget)

        self.retranslateUi(Form)
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        Form.setWindowTitle(QtGui.QApplication.translate("Form", "Alembic Tool", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("Form", "Please enter the path to the scene:", None, QtGui.QApplication.UnicodeUTF8))
        self.but_pick.setText(QtGui.QApplication.translate("Form", "Pick it!", None, QtGui.QApplication.UnicodeUTF8))
        self.but_go.setText(QtGui.QApplication.translate("Form", "Go!", None, QtGui.QApplication.UnicodeUTF8))
        self.but_another.setText(QtGui.QApplication.translate("Form", "Do another one.", None, QtGui.QApplication.UnicodeUTF8))
        self.label_8.setText(QtGui.QApplication.translate("Form", "Scenes Converted", None, QtGui.QApplication.UnicodeUTF8))
        self.label_3.setText(QtGui.QApplication.translate("Form", "Date:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_sceneDate.setText(QtGui.QApplication.translate("Form", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_4.setText(QtGui.QApplication.translate("Form", "Status:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_sceneStatus.setText(QtGui.QApplication.translate("Form", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_sceneName.setText(QtGui.QApplication.translate("Form", "TextLabel", None, QtGui.QApplication.UnicodeUTF8))
        self.label_2.setText(QtGui.QApplication.translate("Form", "Scene:", None, QtGui.QApplication.UnicodeUTF8))
        self.label_9.setText(QtGui.QApplication.translate("Form", "Conversion Log", None, QtGui.QApplication.UnicodeUTF8))

