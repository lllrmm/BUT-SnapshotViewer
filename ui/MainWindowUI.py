# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MainWindow.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QTreeWidget,
    QTreeWidgetItem, QVBoxLayout, QWidget)

class Ui_ButMainWindow(object):
    def setupUi(self, ButMainWindow):
        if not ButMainWindow.objectName():
            ButMainWindow.setObjectName(u"ButMainWindow")
        ButMainWindow.resize(806, 378)
        self.centralwidget = QWidget(ButMainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(2)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(5, 0, 5, 4)
        self.SnapshotInfoBar = QFrame(self.centralwidget)
        self.SnapshotInfoBar.setObjectName(u"SnapshotInfoBar")
        self.SnapshotInfoBar.setMaximumSize(QSize(16777215, 20))
        self.SnapshotInfoBar.setFrameShape(QFrame.Shape.StyledPanel)
        self.SnapshotInfoBar.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout_5 = QHBoxLayout(self.SnapshotInfoBar)
        self.horizontalLayout_5.setSpacing(2)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(1, 0, 0, 0)
        self.SnapshotInfoLabelsFrame = QFrame(self.SnapshotInfoBar)
        self.SnapshotInfoLabelsFrame.setObjectName(u"SnapshotInfoLabelsFrame")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.SnapshotInfoLabelsFrame.sizePolicy().hasHeightForWidth())
        self.SnapshotInfoLabelsFrame.setSizePolicy(sizePolicy)
        self.SnapshotInfoLabelsFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.SnapshotInfoLabelsFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.SnapshotInfoLabelsFrame)
        self.horizontalLayout_11.setSpacing(1)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.JsonPathLabel = QLabel(self.SnapshotInfoLabelsFrame)
        self.JsonPathLabel.setObjectName(u"JsonPathLabel")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.JsonPathLabel.sizePolicy().hasHeightForWidth())
        self.JsonPathLabel.setSizePolicy(sizePolicy1)

        self.horizontalLayout_11.addWidget(self.JsonPathLabel)

        self.JsonPathEdit = QLineEdit(self.SnapshotInfoLabelsFrame)
        self.JsonPathEdit.setObjectName(u"JsonPathEdit")
        sizePolicy.setHeightForWidth(self.JsonPathEdit.sizePolicy().hasHeightForWidth())
        self.JsonPathEdit.setSizePolicy(sizePolicy)
        self.JsonPathEdit.setFrame(False)
        self.JsonPathEdit.setDragEnabled(True)
        self.JsonPathEdit.setReadOnly(True)

        self.horizontalLayout_11.addWidget(self.JsonPathEdit)

        self.line = QFrame(self.SnapshotInfoLabelsFrame)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.Shape.VLine)
        self.line.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_11.addWidget(self.line)

        self.SnapshotIndexLabel = QLabel(self.SnapshotInfoLabelsFrame)
        self.SnapshotIndexLabel.setObjectName(u"SnapshotIndexLabel")
        sizePolicy1.setHeightForWidth(self.SnapshotIndexLabel.sizePolicy().hasHeightForWidth())
        self.SnapshotIndexLabel.setSizePolicy(sizePolicy1)
        self.SnapshotIndexLabel.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_11.addWidget(self.SnapshotIndexLabel)

        self.SnapshotIndexEdit = QLineEdit(self.SnapshotInfoLabelsFrame)
        self.SnapshotIndexEdit.setObjectName(u"SnapshotIndexEdit")
        sizePolicy1.setHeightForWidth(self.SnapshotIndexEdit.sizePolicy().hasHeightForWidth())
        self.SnapshotIndexEdit.setSizePolicy(sizePolicy1)
        self.SnapshotIndexEdit.setMaximumSize(QSize(40, 16777215))
        self.SnapshotIndexEdit.setFrame(False)
        self.SnapshotIndexEdit.setDragEnabled(True)
        self.SnapshotIndexEdit.setReadOnly(True)

        self.horizontalLayout_11.addWidget(self.SnapshotIndexEdit)

        self.SnapshotIndexLabel.raise_()
        self.JsonPathEdit.raise_()
        self.SnapshotIndexEdit.raise_()
        self.JsonPathLabel.raise_()
        self.line.raise_()

        self.horizontalLayout_5.addWidget(self.SnapshotInfoLabelsFrame)

        self.SnapshotInfoButton = QPushButton(self.SnapshotInfoBar)
        self.SnapshotInfoButton.setObjectName(u"SnapshotInfoButton")
        self.SnapshotInfoButton.setEnabled(True)
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Minimum)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(18)
        sizePolicy2.setHeightForWidth(self.SnapshotInfoButton.sizePolicy().hasHeightForWidth())
        self.SnapshotInfoButton.setSizePolicy(sizePolicy2)
        self.SnapshotInfoButton.setMaximumSize(QSize(20, 16777215))
        font = QFont()
        font.setUnderline(True)
        self.SnapshotInfoButton.setFont(font)
        self.SnapshotInfoButton.setText(u"i")
        self.SnapshotInfoButton.setFlat(False)

        self.horizontalLayout_5.addWidget(self.SnapshotInfoButton)


        self.verticalLayout.addWidget(self.SnapshotInfoBar)

        self.line_4 = QFrame(self.centralwidget)
        self.line_4.setObjectName(u"line_4")
        self.line_4.setFrameShape(QFrame.Shape.HLine)
        self.line_4.setFrameShadow(QFrame.Shadow.Sunken)

        self.verticalLayout.addWidget(self.line_4)

        self.FileExplorerFrame = QFrame(self.centralwidget)
        self.FileExplorerFrame.setObjectName(u"FileExplorerFrame")
        self.FileExplorerFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.FileExplorerFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.FileExplorerFrame)
        self.verticalLayout_3.setSpacing(2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.PathJumpFrame = QFrame(self.FileExplorerFrame)
        self.PathJumpFrame.setObjectName(u"PathJumpFrame")
        sizePolicy3 = QSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Maximum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.PathJumpFrame.sizePolicy().hasHeightForWidth())
        self.PathJumpFrame.setSizePolicy(sizePolicy3)
        self.PathJumpFrame.setMaximumSize(QSize(16777215, 22))
        self.PathJumpFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.horizontalLayout_2 = QHBoxLayout(self.PathJumpFrame)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.PathJumpInputBox = QLineEdit(self.PathJumpFrame)
        self.PathJumpInputBox.setObjectName(u"PathJumpInputBox")
        sizePolicy.setHeightForWidth(self.PathJumpInputBox.sizePolicy().hasHeightForWidth())
        self.PathJumpInputBox.setSizePolicy(sizePolicy)
        self.PathJumpInputBox.setFrame(False)
        self.PathJumpInputBox.setDragEnabled(True)
        self.PathJumpInputBox.setClearButtonEnabled(True)

        self.horizontalLayout_2.addWidget(self.PathJumpInputBox)

        self.PathJumpButton = QPushButton(self.PathJumpFrame)
        self.PathJumpButton.setObjectName(u"PathJumpButton")
        self.PathJumpButton.setEnabled(False)
        sizePolicy4 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.PathJumpButton.sizePolicy().hasHeightForWidth())
        self.PathJumpButton.setSizePolicy(sizePolicy4)
        self.PathJumpButton.setMinimumSize(QSize(10, 0))
        self.PathJumpButton.setMaximumSize(QSize(50, 16777215))
        self.PathJumpButton.setSizeIncrement(QSize(0, 0))

        self.horizontalLayout_2.addWidget(self.PathJumpButton)


        self.verticalLayout_3.addWidget(self.PathJumpFrame)

        self.ContentFrame = QFrame(self.FileExplorerFrame)
        self.ContentFrame.setObjectName(u"ContentFrame")
        sizePolicy5 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.ContentFrame.sizePolicy().hasHeightForWidth())
        self.ContentFrame.setSizePolicy(sizePolicy5)
        self.ContentFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.horizontalLayout = QHBoxLayout(self.ContentFrame)
        self.horizontalLayout.setSpacing(2)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.DirTreeFrame = QFrame(self.ContentFrame)
        self.DirTreeFrame.setObjectName(u"DirTreeFrame")
        self.DirTreeFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.DirTreeFrame.setFrameShadow(QFrame.Shadow.Plain)
        self.verticalLayout_2 = QVBoxLayout(self.DirTreeFrame)
        self.verticalLayout_2.setSpacing(1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.DirTree = QTreeWidget(self.DirTreeFrame)
        self.DirTree.setObjectName(u"DirTree")
        self.DirTree.setEnabled(True)
        sizePolicy6 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Minimum)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.DirTree.sizePolicy().hasHeightForWidth())
        self.DirTree.setSizePolicy(sizePolicy6)
        self.DirTree.setFrameShape(QFrame.Shape.StyledPanel)
        self.DirTree.setFrameShadow(QFrame.Shadow.Plain)
        self.DirTree.setSortingEnabled(True)
        self.DirTree.setAnimated(True)
        self.DirTree.setHeaderHidden(False)
        self.DirTree.setExpandsOnDoubleClick(False)
        self.DirTree.header().setVisible(True)
        self.DirTree.header().setProperty(u"showSortIndicator", True)

        self.verticalLayout_2.addWidget(self.DirTree)

        self.DirTreeButtonsFrame = QFrame(self.DirTreeFrame)
        self.DirTreeButtonsFrame.setObjectName(u"DirTreeButtonsFrame")
        sizePolicy3.setHeightForWidth(self.DirTreeButtonsFrame.sizePolicy().hasHeightForWidth())
        self.DirTreeButtonsFrame.setSizePolicy(sizePolicy3)
        self.DirTreeButtonsFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.DirTreeButtonsFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_2 = QGridLayout(self.DirTreeButtonsFrame)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout_2.setHorizontalSpacing(2)
        self.gridLayout_2.setContentsMargins(4, 3, 4, 3)
        self.SelectionControlButtonsFrame_2 = QFrame(self.DirTreeButtonsFrame)
        self.SelectionControlButtonsFrame_2.setObjectName(u"SelectionControlButtonsFrame_2")
        sizePolicy7 = QSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Maximum)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.SelectionControlButtonsFrame_2.sizePolicy().hasHeightForWidth())
        self.SelectionControlButtonsFrame_2.setSizePolicy(sizePolicy7)
        self.SelectionControlButtonsFrame_2.setFrameShape(QFrame.Shape.NoFrame)
        self.SelectionControlButtonsFrame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.SelectionControlButtonsFrame_2)
        self.horizontalLayout_7.setSpacing(2)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.ExpandButton = QPushButton(self.SelectionControlButtonsFrame_2)
        self.ExpandButton.setObjectName(u"ExpandButton")
        sizePolicy1.setHeightForWidth(self.ExpandButton.sizePolicy().hasHeightForWidth())
        self.ExpandButton.setSizePolicy(sizePolicy1)

        self.horizontalLayout_7.addWidget(self.ExpandButton)

        self.CollapseButton = QPushButton(self.SelectionControlButtonsFrame_2)
        self.CollapseButton.setObjectName(u"CollapseButton")
        sizePolicy1.setHeightForWidth(self.CollapseButton.sizePolicy().hasHeightForWidth())
        self.CollapseButton.setSizePolicy(sizePolicy1)

        self.horizontalLayout_7.addWidget(self.CollapseButton)


        self.gridLayout_2.addWidget(self.SelectionControlButtonsFrame_2, 0, 1, 1, 1)

        self.line_5 = QFrame(self.DirTreeButtonsFrame)
        self.line_5.setObjectName(u"line_5")
        self.line_5.setFrameShape(QFrame.Shape.VLine)
        self.line_5.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout_2.addWidget(self.line_5, 0, 2, 1, 1)

        self.HideDirTreeFrameButton = QPushButton(self.DirTreeButtonsFrame)
        self.HideDirTreeFrameButton.setObjectName(u"HideDirTreeFrameButton")
        sizePolicy.setHeightForWidth(self.HideDirTreeFrameButton.sizePolicy().hasHeightForWidth())
        self.HideDirTreeFrameButton.setSizePolicy(sizePolicy)
        self.HideDirTreeFrameButton.setMinimumSize(QSize(20, 0))
        self.HideDirTreeFrameButton.setMaximumSize(QSize(20, 16777215))
        self.HideDirTreeFrameButton.setText(u"<")

        self.gridLayout_2.addWidget(self.HideDirTreeFrameButton, 0, 3, 1, 1)


        self.verticalLayout_2.addWidget(self.DirTreeButtonsFrame)


        self.horizontalLayout.addWidget(self.DirTreeFrame)

        self.ShowDirTreeFrameButton = QPushButton(self.ContentFrame)
        self.ShowDirTreeFrameButton.setObjectName(u"ShowDirTreeFrameButton")
        self.ShowDirTreeFrameButton.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.ShowDirTreeFrameButton.sizePolicy().hasHeightForWidth())
        self.ShowDirTreeFrameButton.setSizePolicy(sizePolicy1)
        self.ShowDirTreeFrameButton.setMaximumSize(QSize(20, 16777215))
        self.ShowDirTreeFrameButton.setText(u">")
        self.ShowDirTreeFrameButton.setFlat(False)

        self.horizontalLayout.addWidget(self.ShowDirTreeFrameButton)

        self.FileViewFrame = QFrame(self.ContentFrame)
        self.FileViewFrame.setObjectName(u"FileViewFrame")
        sizePolicy8 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.FileViewFrame.sizePolicy().hasHeightForWidth())
        self.FileViewFrame.setSizePolicy(sizePolicy8)
        self.FileViewFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.FileViewFrame.setFrameShadow(QFrame.Shadow.Plain)
        self.FileViewFrame.setMidLineWidth(0)
        self.verticalLayout_4 = QVBoxLayout(self.FileViewFrame)
        self.verticalLayout_4.setSpacing(1)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 1, 0, 0)
        self.CurrentPathBarFrame = QFrame(self.FileViewFrame)
        self.CurrentPathBarFrame.setObjectName(u"CurrentPathBarFrame")
        sizePolicy3.setHeightForWidth(self.CurrentPathBarFrame.sizePolicy().hasHeightForWidth())
        self.CurrentPathBarFrame.setSizePolicy(sizePolicy3)
        self.CurrentPathBarFrame.setMinimumSize(QSize(0, 0))
        self.CurrentPathBarFrame.setMaximumSize(QSize(16777215, 18))
        self.CurrentPathBarFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.CurrentPathBarFrame.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout_10 = QHBoxLayout(self.CurrentPathBarFrame)
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(0, 0, 0, 0)
        self.CurrentPathBrowser = QLineEdit(self.CurrentPathBarFrame)
        self.CurrentPathBrowser.setObjectName(u"CurrentPathBrowser")
        sizePolicy.setHeightForWidth(self.CurrentPathBrowser.sizePolicy().hasHeightForWidth())
        self.CurrentPathBrowser.setSizePolicy(sizePolicy)
        self.CurrentPathBrowser.setMaximumSize(QSize(16777215, 16777215))
        self.CurrentPathBrowser.setFrame(False)
        self.CurrentPathBrowser.setEchoMode(QLineEdit.EchoMode.Normal)
        self.CurrentPathBrowser.setDragEnabled(True)
        self.CurrentPathBrowser.setReadOnly(True)
        self.CurrentPathBrowser.setClearButtonEnabled(False)

        self.horizontalLayout_10.addWidget(self.CurrentPathBrowser)

        self.GoBackDirButton = QPushButton(self.CurrentPathBarFrame)
        self.GoBackDirButton.setObjectName(u"GoBackDirButton")
        self.GoBackDirButton.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.GoBackDirButton.sizePolicy().hasHeightForWidth())
        self.GoBackDirButton.setSizePolicy(sizePolicy1)
        self.GoBackDirButton.setMaximumSize(QSize(34, 16777215))

        self.horizontalLayout_10.addWidget(self.GoBackDirButton)


        self.verticalLayout_4.addWidget(self.CurrentPathBarFrame)

        self.FileViewTree = QTreeWidget(self.FileViewFrame)
        self.FileViewTree.setObjectName(u"FileViewTree")
        sizePolicy.setHeightForWidth(self.FileViewTree.sizePolicy().hasHeightForWidth())
        self.FileViewTree.setSizePolicy(sizePolicy)
        self.FileViewTree.setLocale(QLocale(QLocale.Chinese, QLocale.China))
        self.FileViewTree.setFrameShape(QFrame.Shape.StyledPanel)
        self.FileViewTree.setFrameShadow(QFrame.Shadow.Plain)
        self.FileViewTree.setSelectionMode(QAbstractItemView.SelectionMode.ExtendedSelection)
        self.FileViewTree.setItemsExpandable(False)
        self.FileViewTree.setSortingEnabled(True)
        self.FileViewTree.setAnimated(False)
        self.FileViewTree.setExpandsOnDoubleClick(False)
        self.FileViewTree.setColumnCount(4)

        self.verticalLayout_4.addWidget(self.FileViewTree)

        self.FileViewButtonsFrame = QFrame(self.FileViewFrame)
        self.FileViewButtonsFrame.setObjectName(u"FileViewButtonsFrame")
        sizePolicy3.setHeightForWidth(self.FileViewButtonsFrame.sizePolicy().hasHeightForWidth())
        self.FileViewButtonsFrame.setSizePolicy(sizePolicy3)
        self.FileViewButtonsFrame.setFrameShape(QFrame.Shape.StyledPanel)
        self.FileViewButtonsFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.FileViewButtonsFrame)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(2)
        self.gridLayout.setContentsMargins(4, 3, 4, 3)
        self.line_2 = QFrame(self.FileViewButtonsFrame)
        self.line_2.setObjectName(u"line_2")
        self.line_2.setFrameShape(QFrame.Shape.VLine)
        self.line_2.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_2, 0, 2, 1, 1)

        self.ExportControlButtonsFrame = QFrame(self.FileViewButtonsFrame)
        self.ExportControlButtonsFrame.setObjectName(u"ExportControlButtonsFrame")
        sizePolicy7.setHeightForWidth(self.ExportControlButtonsFrame.sizePolicy().hasHeightForWidth())
        self.ExportControlButtonsFrame.setSizePolicy(sizePolicy7)
        self.ExportControlButtonsFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.ExportControlButtonsFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.ExportControlButtonsFrame)
        self.horizontalLayout_4.setSpacing(2)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.SetPoolDirsButton = QPushButton(self.ExportControlButtonsFrame)
        self.SetPoolDirsButton.setObjectName(u"SetPoolDirsButton")
        self.SetPoolDirsButton.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.SetPoolDirsButton.sizePolicy().hasHeightForWidth())
        self.SetPoolDirsButton.setSizePolicy(sizePolicy1)

        self.horizontalLayout_4.addWidget(self.SetPoolDirsButton)

        self.ExportButton = QPushButton(self.ExportControlButtonsFrame)
        self.ExportButton.setObjectName(u"ExportButton")
        self.ExportButton.setEnabled(False)
        sizePolicy1.setHeightForWidth(self.ExportButton.sizePolicy().hasHeightForWidth())
        self.ExportButton.setSizePolicy(sizePolicy1)

        self.horizontalLayout_4.addWidget(self.ExportButton)


        self.gridLayout.addWidget(self.ExportControlButtonsFrame, 0, 5, 1, 1)

        self.line_3 = QFrame(self.FileViewButtonsFrame)
        self.line_3.setObjectName(u"line_3")
        self.line_3.setFrameShape(QFrame.Shape.VLine)
        self.line_3.setFrameShadow(QFrame.Shadow.Sunken)

        self.gridLayout.addWidget(self.line_3, 0, 4, 1, 1)

        self.SelectionControlButtonsFrame = QFrame(self.FileViewButtonsFrame)
        self.SelectionControlButtonsFrame.setObjectName(u"SelectionControlButtonsFrame")
        sizePolicy7.setHeightForWidth(self.SelectionControlButtonsFrame.sizePolicy().hasHeightForWidth())
        self.SelectionControlButtonsFrame.setSizePolicy(sizePolicy7)
        self.SelectionControlButtonsFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.SelectionControlButtonsFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.SelectionControlButtonsFrame)
        self.horizontalLayout_3.setSpacing(2)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.SelectAllButton = QPushButton(self.SelectionControlButtonsFrame)
        self.SelectAllButton.setObjectName(u"SelectAllButton")
        sizePolicy1.setHeightForWidth(self.SelectAllButton.sizePolicy().hasHeightForWidth())
        self.SelectAllButton.setSizePolicy(sizePolicy1)

        self.horizontalLayout_3.addWidget(self.SelectAllButton)

        self.InvertSelectionButton = QPushButton(self.SelectionControlButtonsFrame)
        self.InvertSelectionButton.setObjectName(u"InvertSelectionButton")
        sizePolicy1.setHeightForWidth(self.InvertSelectionButton.sizePolicy().hasHeightForWidth())
        self.InvertSelectionButton.setSizePolicy(sizePolicy1)

        self.horizontalLayout_3.addWidget(self.InvertSelectionButton)

        self.ClearSelectionButton = QPushButton(self.SelectionControlButtonsFrame)
        self.ClearSelectionButton.setObjectName(u"ClearSelectionButton")
        sizePolicy1.setHeightForWidth(self.ClearSelectionButton.sizePolicy().hasHeightForWidth())
        self.ClearSelectionButton.setSizePolicy(sizePolicy1)

        self.horizontalLayout_3.addWidget(self.ClearSelectionButton)


        self.gridLayout.addWidget(self.SelectionControlButtonsFrame, 0, 1, 1, 1)

        self.CopyItemsInfoButton = QPushButton(self.FileViewButtonsFrame)
        self.CopyItemsInfoButton.setObjectName(u"CopyItemsInfoButton")
        sizePolicy1.setHeightForWidth(self.CopyItemsInfoButton.sizePolicy().hasHeightForWidth())
        self.CopyItemsInfoButton.setSizePolicy(sizePolicy1)

        self.gridLayout.addWidget(self.CopyItemsInfoButton, 0, 3, 1, 1)


        self.verticalLayout_4.addWidget(self.FileViewButtonsFrame)


        self.horizontalLayout.addWidget(self.FileViewFrame)


        self.verticalLayout_3.addWidget(self.ContentFrame)


        self.verticalLayout.addWidget(self.FileExplorerFrame)

        self.StatusBar = QFrame(self.centralwidget)
        self.StatusBar.setObjectName(u"StatusBar")
        sizePolicy3.setHeightForWidth(self.StatusBar.sizePolicy().hasHeightForWidth())
        self.StatusBar.setSizePolicy(sizePolicy3)
        self.StatusBar.setMaximumSize(QSize(16777215, 18))
        self.StatusBar.setFrameShape(QFrame.Shape.NoFrame)
        self.StatusBar.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.StatusBar)
        self.horizontalLayout_6.setSpacing(2)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(1, 0, 1, 0)
        self.TotalItemNumberLabel = QLabel(self.StatusBar)
        self.TotalItemNumberLabel.setObjectName(u"TotalItemNumberLabel")
        sizePolicy1.setHeightForWidth(self.TotalItemNumberLabel.sizePolicy().hasHeightForWidth())
        self.TotalItemNumberLabel.setSizePolicy(sizePolicy1)

        self.horizontalLayout_6.addWidget(self.TotalItemNumberLabel)

        self.line_6 = QFrame(self.StatusBar)
        self.line_6.setObjectName(u"line_6")
        self.line_6.setFrameShape(QFrame.Shape.VLine)
        self.line_6.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_6.addWidget(self.line_6)

        self.SelectedItemNumberLabel = QLabel(self.StatusBar)
        self.SelectedItemNumberLabel.setObjectName(u"SelectedItemNumberLabel")
        sizePolicy1.setHeightForWidth(self.SelectedItemNumberLabel.sizePolicy().hasHeightForWidth())
        self.SelectedItemNumberLabel.setSizePolicy(sizePolicy1)
        self.SelectedItemNumberLabel.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_6.addWidget(self.SelectedItemNumberLabel)

        self.line_7 = QFrame(self.StatusBar)
        self.line_7.setObjectName(u"line_7")
        self.line_7.setFrameShape(QFrame.Shape.VLine)
        self.line_7.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_6.addWidget(self.line_7)

        self.StatusBarSpacerFrame = QFrame(self.StatusBar)
        self.StatusBarSpacerFrame.setObjectName(u"StatusBarSpacerFrame")
        sizePolicy.setHeightForWidth(self.StatusBarSpacerFrame.sizePolicy().hasHeightForWidth())
        self.StatusBarSpacerFrame.setSizePolicy(sizePolicy)
        self.StatusBarSpacerFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.StatusBarSpacerFrame.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_8 = QHBoxLayout(self.StatusBarSpacerFrame)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")

        self.horizontalLayout_6.addWidget(self.StatusBarSpacerFrame)

        self.line_8 = QFrame(self.StatusBar)
        self.line_8.setObjectName(u"line_8")
        self.line_8.setFrameShape(QFrame.Shape.VLine)
        self.line_8.setFrameShadow(QFrame.Shadow.Sunken)

        self.horizontalLayout_6.addWidget(self.line_8)

        self.VersionFrame = QFrame(self.StatusBar)
        self.VersionFrame.setObjectName(u"VersionFrame")
        sizePolicy4.setHeightForWidth(self.VersionFrame.sizePolicy().hasHeightForWidth())
        self.VersionFrame.setSizePolicy(sizePolicy4)
        self.VersionFrame.setFrameShape(QFrame.Shape.NoFrame)
        self.VersionFrame.setFrameShadow(QFrame.Shadow.Plain)
        self.horizontalLayout_9 = QHBoxLayout(self.VersionFrame)
        self.horizontalLayout_9.setSpacing(1)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.SoftNameLabel = QLabel(self.VersionFrame)
        self.SoftNameLabel.setObjectName(u"SoftNameLabel")
        sizePolicy4.setHeightForWidth(self.SoftNameLabel.sizePolicy().hasHeightForWidth())
        self.SoftNameLabel.setSizePolicy(sizePolicy4)

        self.horizontalLayout_9.addWidget(self.SoftNameLabel)

        self.SoftVersionLabel = QLabel(self.VersionFrame)
        self.SoftVersionLabel.setObjectName(u"SoftVersionLabel")
        sizePolicy4.setHeightForWidth(self.SoftVersionLabel.sizePolicy().hasHeightForWidth())
        self.SoftVersionLabel.setSizePolicy(sizePolicy4)

        self.horizontalLayout_9.addWidget(self.SoftVersionLabel)


        self.horizontalLayout_6.addWidget(self.VersionFrame)


        self.verticalLayout.addWidget(self.StatusBar)

        ButMainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(ButMainWindow)
        self.ExpandButton.clicked.connect(self.DirTree.expandAll)
        self.CollapseButton.clicked.connect(self.DirTree.collapseAll)
        self.ClearSelectionButton.clicked.connect(self.FileViewTree.clearSelection)
        self.HideDirTreeFrameButton.clicked.connect(self.DirTreeFrame.hide)
        self.HideDirTreeFrameButton.clicked.connect(self.ShowDirTreeFrameButton.show)
        self.ShowDirTreeFrameButton.clicked.connect(self.ShowDirTreeFrameButton.hide)
        self.ShowDirTreeFrameButton.clicked.connect(self.DirTreeFrame.show)
        self.SelectAllButton.clicked.connect(self.FileViewTree.selectAll)

        QMetaObject.connectSlotsByName(ButMainWindow)
    # setupUi

    def retranslateUi(self, ButMainWindow):
        ButMainWindow.setWindowTitle(QCoreApplication.translate("ButMainWindow", u"BUT Snapshot Viewer", None))
        self.JsonPathLabel.setText(QCoreApplication.translate("ButMainWindow", u"Json file: ", None))
        self.SnapshotIndexLabel.setText(QCoreApplication.translate("ButMainWindow", u"Snapshot index: ", None))
        self.PathJumpButton.setText(QCoreApplication.translate("ButMainWindow", u"Jump", None))
        ___qtreewidgetitem = self.DirTree.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("ButMainWindow", u"Directory Tree", None));
        self.ExpandButton.setText(QCoreApplication.translate("ButMainWindow", u"Expand all", None))
        self.CollapseButton.setText(QCoreApplication.translate("ButMainWindow", u"Collapse all", None))
        self.CurrentPathBrowser.setText("")
        self.GoBackDirButton.setText(QCoreApplication.translate("ButMainWindow", u"Back", None))
        ___qtreewidgetitem1 = self.FileViewTree.headerItem()
        ___qtreewidgetitem1.setText(3, QCoreApplication.translate("ButMainWindow", u"info", None));
        ___qtreewidgetitem1.setText(2, QCoreApplication.translate("ButMainWindow", u"hash", None));
        ___qtreewidgetitem1.setText(1, QCoreApplication.translate("ButMainWindow", u"Type", None));
        ___qtreewidgetitem1.setText(0, QCoreApplication.translate("ButMainWindow", u"Name", None));
        self.SetPoolDirsButton.setText(QCoreApplication.translate("ButMainWindow", u"Set pool dirs", None))
        self.ExportButton.setText(QCoreApplication.translate("ButMainWindow", u"Restore selected", None))
        self.SelectAllButton.setText(QCoreApplication.translate("ButMainWindow", u"Select all", None))
        self.InvertSelectionButton.setText(QCoreApplication.translate("ButMainWindow", u"Invert selection", None))
        self.ClearSelectionButton.setText(QCoreApplication.translate("ButMainWindow", u"Clear selection", None))
        self.CopyItemsInfoButton.setText(QCoreApplication.translate("ButMainWindow", u"Copy selected files info (JsonText)", None))
        self.TotalItemNumberLabel.setText(QCoreApplication.translate("ButMainWindow", u"Total items: ", None))
        self.SelectedItemNumberLabel.setText(QCoreApplication.translate("ButMainWindow", u"Items selected: ", None))
        self.SoftNameLabel.setText(QCoreApplication.translate("ButMainWindow", u"BUT Snapshot Viewer ", None))
        self.SoftVersionLabel.setText(QCoreApplication.translate("ButMainWindow", u"0.0.0", None))
    # retranslateUi

