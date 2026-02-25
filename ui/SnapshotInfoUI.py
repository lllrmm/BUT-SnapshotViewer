# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'SnapshotInfo.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QFrame, QHBoxLayout, QLabel,
    QLineEdit, QMainWindow, QPlainTextEdit, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_SnapshotInfoWindow(object):
    def setupUi(self, SnapshotInfoWindow):
        if not SnapshotInfoWindow.objectName():
            SnapshotInfoWindow.setObjectName(u"SnapshotInfoWindow")
        SnapshotInfoWindow.resize(420, 270)
        self.centralwidget = QWidget(SnapshotInfoWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(1)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(4, 4, 4, 4)
        self.SnapshotInfoBar_2 = QFrame(self.centralwidget)
        self.SnapshotInfoBar_2.setObjectName(u"SnapshotInfoBar_2")
        self.SnapshotInfoBar_2.setMaximumSize(QSize(16777215, 20))
        self.SnapshotInfoBar_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.SnapshotInfoBar_2.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout_2 = QHBoxLayout(self.SnapshotInfoBar_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(1, 0, 1, 0)
        self.SnapshotRootPathLabel = QLabel(self.SnapshotInfoBar_2)
        self.SnapshotRootPathLabel.setObjectName(u"SnapshotRootPathLabel")

        self.horizontalLayout_2.addWidget(self.SnapshotRootPathLabel)

        self.SnapshotRootPathEdit = QLineEdit(self.SnapshotInfoBar_2)
        self.SnapshotRootPathEdit.setObjectName(u"SnapshotRootPathEdit")
        self.SnapshotRootPathEdit.setFrame(False)
        self.SnapshotRootPathEdit.setDragEnabled(True)
        self.SnapshotRootPathEdit.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.SnapshotRootPathEdit)


        self.verticalLayout.addWidget(self.SnapshotInfoBar_2)

        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Plain)
        self.verticalLayout_2 = QVBoxLayout(self.frame)
        self.verticalLayout_2.setSpacing(1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 1, 0, 0)
        self.SnapshotInfoBar_3 = QFrame(self.frame)
        self.SnapshotInfoBar_3.setObjectName(u"SnapshotInfoBar_3")
        self.SnapshotInfoBar_3.setMaximumSize(QSize(16777215, 20))
        self.SnapshotInfoBar_3.setFrameShape(QFrame.Shape.NoFrame)
        self.SnapshotInfoBar_3.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.SnapshotInfoBar_3)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(1, 0, 1, 0)
        self.SnapshotInfoLabel = QLabel(self.SnapshotInfoBar_3)
        self.SnapshotInfoLabel.setObjectName(u"SnapshotInfoLabel")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SnapshotInfoLabel.sizePolicy().hasHeightForWidth())
        self.SnapshotInfoLabel.setSizePolicy(sizePolicy)

        self.horizontalLayout_3.addWidget(self.SnapshotInfoLabel)

        self.CopySnapshotInfoButton = QPushButton(self.SnapshotInfoBar_3)
        self.CopySnapshotInfoButton.setObjectName(u"CopySnapshotInfoButton")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.CopySnapshotInfoButton.sizePolicy().hasHeightForWidth())
        self.CopySnapshotInfoButton.setSizePolicy(sizePolicy1)

        self.horizontalLayout_3.addWidget(self.CopySnapshotInfoButton)


        self.verticalLayout_2.addWidget(self.SnapshotInfoBar_3)

        self.SnapshotInfoEdit = QPlainTextEdit(self.frame)
        self.SnapshotInfoEdit.setObjectName(u"SnapshotInfoEdit")
        self.SnapshotInfoEdit.setUndoRedoEnabled(False)
        self.SnapshotInfoEdit.setLineWrapMode(QPlainTextEdit.LineWrapMode.WidgetWidth)
        self.SnapshotInfoEdit.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.SnapshotInfoEdit)


        self.verticalLayout.addWidget(self.frame)

        SnapshotInfoWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(SnapshotInfoWindow)

        QMetaObject.connectSlotsByName(SnapshotInfoWindow)
    # setupUi

    def retranslateUi(self, SnapshotInfoWindow):
        SnapshotInfoWindow.setWindowTitle(QCoreApplication.translate("SnapshotInfoWindow", u"Snapshot Details", None))
        self.SnapshotRootPathLabel.setText(QCoreApplication.translate("SnapshotInfoWindow", u"Snapshot rootPath: ", None))
        self.SnapshotInfoLabel.setText(QCoreApplication.translate("SnapshotInfoWindow", u"SnapShot info: ", None))
        self.CopySnapshotInfoButton.setText(QCoreApplication.translate("SnapshotInfoWindow", u"Copy snapshot info to clipboard", None))
    # retranslateUi

