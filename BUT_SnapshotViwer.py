# BUT_SnapshotViwer.py

from pathlib import PurePosixPath as PPPath
from pathlib import Path
import sys

# 允许直接运行本脚本（无需手动设置 PYTHONPATH / 无需从项目根目录启动）
root = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(root / "src"))
sys.path.insert(0, str(root))

import PyFs.PyFsBasic as pyfs
import BUT
import copy
import json

from PySide6.QtCore import Qt, QSize
from PySide6.QtWidgets import (QApplication, QMainWindow, QTreeWidget, QTreeWidgetItem, 
                               QMessageBox, QFileDialog, QInputDialog)

from ui.MainWindowUI import Ui_ButMainWindow
from ui.SnapshotInfoUI import Ui_SnapshotInfoWindow



def DrawDirFileTree(dirObj: pyfs.Dir, FilterAllow, InfoHandler, ItemEditor, maxDepth: int) -> QTreeWidgetItem:
    def Dfs(subFiles: list[pyfs.File], parentNode: QTreeWidgetItem, parentPath: PPPath, depth: int):
        for fileObj in subFiles:
            relativeChildPath = parentPath.joinpath(fileObj.name)
            if not FilterAllow(fileObj, relativeChildPath):
                continue
            treeItem = QTreeWidgetItem(InfoHandler(fileObj, relativeChildPath))
            ItemEditor(treeItem, fileObj, relativeChildPath)
            parentNode.addChild(treeItem)
            if type(fileObj) == pyfs.Dir:
                if depth == maxDepth:
                    continue
                Dfs(fileObj.subFiles, treeItem, relativeChildPath, (depth+1))

    rootPath = PPPath('') ## 不可以有斜杠！！！！！！！！
    rootNode = QTreeWidgetItem(InfoHandler(dirObj, rootPath))
    ItemEditor(rootNode, dirObj, rootPath)
    Dfs(dirObj.subFiles, rootNode, rootPath, 1)
    return rootNode



def GetItemRowIndex(TreeWidget: QTreeWidget, item: QTreeWidgetItem):
    for i in range(0, TreeWidget.topLevelItemCount()):
        if TreeWidget.topLevelItem(i) == item:
            return i



class ButMainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_ButMainWindow()
        self.ui.setupUi(self)



class SnapshotInfoWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_SnapshotInfoWindow()
        self.ui.setupUi(self)



class ButSnapshotViewer:
    def __init__(self, parent=None):
        self.snapshot :BUT.Snapshot = None
        self.jsonPath :Path = None
        self.snapshotIndex :int = None
        self.loaded = False
        self.currentFileViewPath :PPPath = None

        self.MainWin = ButMainWindow(parent)
        self.SnapshotInfoWin = SnapshotInfoWindow(self.MainWin)
        self.SnapshotInfoWin.setWindowFlag(Qt.WindowType.WindowMinimizeButtonHint, False)

        self.MainWin.ui.FileExplorerFrame.setEnabled(False)
        self.MainWin.ui.SnapshotInfoBar.setEnabled(False)

        self.MainWin.ui.DirTree.itemClicked.connect(self.OnDirTreeItemClicked)
        self.MainWin.ui.PathJumpInputBox.textChanged.connect(self.OnPathJumpInputBoxTextChanged)
        self.MainWin.ui.PathJumpButton.clicked.connect(self.OnPathJumpButtonClicked)
        self.MainWin.ui.GoBackDirButton.clicked.connect(self.OnGoBackDirButtonClicked)
        self.MainWin.ui.FileViewTree.itemDoubleClicked.connect(self.OnFileViewItemDoubleClicked)
        self.MainWin.ui.FileViewTree.itemSelectionChanged.connect(self.OnFileViewSelectionChanged)
        self.MainWin.ui.InvertSelectionButton.clicked.connect(self.InvertFileViewSelection)
        self.MainWin.ui.CopyItemsInfoButton.clicked.connect(self.OnCopyItemsInfoButtonClicked)
        self.MainWin.ui.SnapshotInfoButton.clicked.connect(self.OnSnapshotInfoButtonClicked)
        self.SnapshotInfoWin.ui.CopySnapshotInfoButton.clicked.connect(self.OnCopySnapshotInfoButtonClicked)

        self.MainWin.ui.ShowDirTreeFrameButton.hide()
        self.MainWin.ui.JsonPathEdit.setText(str(self.jsonPath))
        self.MainWin.ui.SnapshotIndexEdit.setText(str(self.snapshotIndex))
        self.MainWin.resize(QSize(self.MainWin.width(), 600))

        # 未完成
        self.MainWin.ui.ExportControlButtonsFrame.hide()
        self.MainWin.ui.line_3.hide()


    def LoadSnapshot(self, snapshot: BUT.Snapshot, jsonPath: Path=None, snapshotIndex: int=None):
        if not self.loaded:
            self.snapshot = snapshot
            self.jsonPath = jsonPath
            self.snapshotIndex = snapshotIndex
            self.UpdateSnapshotInfoBar()
            self.UpdateDirTree()
            self.UpdateFileView(PPPath(''))
            self.loaded = True
            self.MainWin.ui.SnapshotInfoBar.setEnabled(True)
            self.MainWin.ui.FileExplorerFrame.setEnabled(True)
        else:
            pass


    def ShowMainWindow(self):
        self.MainWin.show()


    def UpdateSnapshotInfoBar(self):
            self.MainWin.ui.JsonPathEdit.setText(str(self.jsonPath))
            self.MainWin.ui.SnapshotIndexEdit.setText(str(self.snapshotIndex))


    def UpdateDirTree(self):
        Dt = self.MainWin.ui.DirTree

        def InfoHandler(fileObj: pyfs.File, relativePath: PPPath):
            return (fileObj.name,)

        def FilterAllow(fileObj: pyfs.File, relativePath: PPPath):
            if type(fileObj) == pyfs.File:
                return False
            return True

        def ItemEditor(treeItem: QTreeWidgetItem, fileObj: pyfs.File, relativeChildPath):
            path = relativeChildPath
            treeItem.setData(0, Qt.ItemDataRole.UserRole, path)

        ti = DrawDirFileTree(self.snapshot.fsManager.rootDir, FilterAllow, InfoHandler, ItemEditor, -1)

        Dt.clear()
        Dt.addTopLevelItem(ti)
        Dt.sortItems(0, Qt.SortOrder.AscendingOrder) #排序


    def GetDirTreeItemByPath(self, path: PPPath, PathItemHandler=None) -> QTreeWidgetItem:
        Dt = self.MainWin.ui.DirTree
        if pyfs.IsRootPath(path):
            item = Dt.topLevelItem(0)
            if PathItemHandler is not None:
                PathItemHandler(item)
            return item

        targetPathList = pyfs.SplitPath(path)
        targetPathDepth = len(targetPathList)

        def Dfs(rootNode: QTreeWidgetItem, depth: int):
            '''
            depth from 0
            '''
            for i in range(0, rootNode.childCount()):
                item = rootNode.child(i)
                path :PPPath = item.data(0, Qt.ItemDataRole.UserRole)
                pathList = pyfs.SplitPath(path)
                currentTargetName = targetPathList[depth]
                if pathList[depth] == currentTargetName:
                    break
            if PathItemHandler is not None:
                PathItemHandler(item)
            if depth == (targetPathDepth-1):
                return item
            return Dfs(item, (depth+1))

        return Dfs(Dt.topLevelItem(0), 0)


    def UpdateFileView(self, rootPath: PPPath, highlightFilesNames: list[str]=None):
        Fv = self.MainWin.ui.FileViewTree
        itemsToHighlight :list[QTreeWidgetItem] = []
        innerHighlightFilesNames = copy.copy(highlightFilesNames)

        def InfoHandler(fileObj: pyfs.File, relativePath: PPPath):
            if pyfs.IsRootPath(relativePath):
                return(fileObj.name, )

            if type(fileObj) == pyfs.File:
                return (
                    fileObj.name,
                    PPPath(fileObj.name).suffix,
                    str(fileObj.info['hash']),
                    str(fileObj.info['info'])
                )
            elif type(fileObj) == pyfs.Dir:
                return (
                    fileObj.name,
                    'Dir',
                    '',
                    str(fileObj.info['info'])
                )

        def FilterAllow(fileObj: pyfs.File, relativePath: PPPath):
            return True

        def ItemEditor(treeItem: QTreeWidgetItem, fileObj: pyfs.File, relativeChildPath: PPPath):
            path = rootPath.joinpath(relativeChildPath)
            fileType = type(fileObj)
            treeItem.setData(0, Qt.ItemDataRole.UserRole, path)
            treeItem.setData(2, Qt.ItemDataRole.UserRole, fileType)
            if innerHighlightFilesNames is not None:
                if fileObj.name in innerHighlightFilesNames:
                    itemsToHighlight.append(treeItem)
                    innerHighlightFilesNames.remove(fileObj.name)

        dirObj = self.snapshot.fsManager.GetFileObj(rootPath, pyfs.Dir)
        ti = DrawDirFileTree(dirObj, FilterAllow, InfoHandler, ItemEditor, 1)
        if (innerHighlightFilesNames is not None) and \
            (len(innerHighlightFilesNames) != 0):
            raise Exception('部分无法highlight（找不到）')
        Fv.clear()
        Fv.addTopLevelItems(ti.takeChildren())
        Fv.sortItems(0, Qt.SortOrder.AscendingOrder) #排序
        Fv.sortItems(1, Qt.SortOrder.AscendingOrder)

        if len(itemsToHighlight) == 1: # 提高效率
            item = itemsToHighlight[0]
            item.setSelected(True) # 选中
            Fv.scrollToItem(item)
        else:
            topHighlightItem :QTreeWidgetItem = None
            topHighlightItemRowIndex :int = (Fv.topLevelItemCount()-1) # 最后一项
            for item in itemsToHighlight:
                item.setSelected(True) # 选中
                rowIndex = GetItemRowIndex(Fv, item)
                if rowIndex < topHighlightItemRowIndex:
                    topHighlightItemRowIndex = rowIndex
                    topHighlightItem = item

            Fv.scrollToItem(topHighlightItem)

        self.currentFileViewPath = rootPath
        self.MainWin.ui.CurrentPathBrowser.setText(str(self.currentFileViewPath))
        if pyfs.IsRootPath(self.currentFileViewPath):
            self.MainWin.ui.GoBackDirButton.setEnabled(False)
        else:
            self.MainWin.ui.GoBackDirButton.setEnabled(True)

        self.MainWin.ui.TotalItemNumberLabel.setText(f'Total items: {Fv.topLevelItemCount()}')
        self.MainWin.ui.SelectedItemNumberLabel.setText(f'Items selected: {len(Fv.selectedItems())}')


        Dt = self.MainWin.ui.DirTree

        targetItem = self.GetDirTreeItemByPath(rootPath)
        Dt.expandRecursively(Dt.indexFromItem(targetItem), 0)
        Dt.setCurrentItem(targetItem)


    def OnDirTreeItemClicked(self, item: QTreeWidgetItem, column: int):
        path = item.data(0, Qt.ItemDataRole.UserRole)
        self.UpdateFileView(path)


    def OnPathJumpInputBoxTextChanged(self):
        jumpPath = self.MainWin.ui.PathJumpInputBox.text()
        if len(jumpPath) != 0: # 不为空
            self.MainWin.ui.PathJumpButton.setEnabled(True)
        else:
            self.MainWin.ui.PathJumpButton.setEnabled(False)


    def OnPathJumpButtonClicked(self):
        jumpPath = self.MainWin.ui.PathJumpInputBox.text()
        jumpPath = PPPath(jumpPath)
        try:
            self.snapshot.fsManager.GetFileObj(jumpPath, pyfs.Dir)
        except pyfs.FsError as e:
            # print(e.args)
            if e.args[0] == pyfs.ERROR_NOT_EXIST:
                pass
            QMessageBox.warning(self.MainWin, 'Not exist', 'Dir does not exist.', QMessageBox.StandardButton.Close)
        else:
            self.UpdateFileView(jumpPath)


    def OnGoBackDirButtonClicked(self):
        # if not pyfs.IsRootPath(self.currentFileViewPath):
        self.UpdateFileView(self.currentFileViewPath.parent, set((self.currentFileViewPath.name,)))


    def OnFileViewItemDoubleClicked(self, item: QTreeWidgetItem, column: int):
        path = item.data(0, Qt.ItemDataRole.UserRole)
        try:
            self.snapshot.fsManager.GetFileObj(path, pyfs.Dir)
        except pyfs.FsError as e: # Not a Dir!
            if e.args[0] == pyfs.ERROR_NOT_EXIST:
                pass
            else:
                raise e
        else:
            self.UpdateFileView(path)
            return


    def OnFileViewSelectionChanged(self):
        Fv = self.MainWin.ui.FileViewTree
        self.MainWin.ui.SelectedItemNumberLabel.setText(f'Items selected: {len(Fv.selectedItems())}')


    def InvertFileViewSelection(self):
        Fv = self.MainWin.ui.FileViewTree
        for i in range(0, Fv.topLevelItemCount()):
            item = Fv.topLevelItem(i)
            item.setSelected((not item.isSelected()))


    def GetSelectedItemsInfoPack(self) -> dict:
        Fv = self.MainWin.ui.FileViewTree
        infoPack = {}
        selectedItems = Fv.selectedItems()
        for item in selectedItems:
            path: PPPath = item.data(0, Qt.ItemDataRole.UserRole)
            fileType: pyfs.File = item.data(2, Qt.ItemDataRole.UserRole)
            fileObj = self.snapshot.fsManager.GetFileObj(path, fileType)
            infoPack[str(path)] = fileObj.Pack()
        return infoPack


    def OnCopyItemsInfoButtonClicked(self):
        infoPack = self.GetSelectedItemsInfoPack()
        if len(infoPack.keys()) == 0:
            QMessageBox.warning(self.MainWin, 'Nothing selected', 'No item has been selected.',  QMessageBox.StandardButton.Close)
            return
        infoJsonText = json.dumps(infoPack)
        clipboard = QApplication.clipboard()
        clipboard.setText(infoJsonText)
        QMessageBox.information(self.MainWin, 'Info copied', 'Json text has been copied to the clipboard.',  QMessageBox.StandardButton.Ok)


    def FillSnapshotInfoWindow(self):
        SiWin = self.SnapshotInfoWin
        SiWin.ui.SnapshotRootPathEdit.setText(str(self.snapshot.rootPath))
        infoJsonText = json.dumps(self.snapshot.info)
        SiWin.ui.SnapshotInfoEdit.setPlainText(infoJsonText)


    def OnSnapshotInfoButtonClicked(self):
        self.FillSnapshotInfoWindow()
        self.SnapshotInfoWin.show()


    def OnCopySnapshotInfoButtonClicked(self):
        clipboard = QApplication.clipboard()
        clipboard.setText(json.dumps(self.snapshot.info))
        QMessageBox.information(self.SnapshotInfoWin, 'Info copied', 'Json text has been copied to the clipboard.',  QMessageBox.StandardButton.Ok)



def GetSnapshotsOverview(Am: BUT.ArchiveManager):
    shotsOverview = []
    for snapshot in Am.snapshots:
        overview = {
            'info': snapshot.info,
            'rootPath': str(snapshot.rootPath)
        }
        shotsOverview.append(overview)
    return shotsOverview



if __name__ == '__main__':
    App = QApplication(sys.argv)
    Bsv = ButSnapshotViewer()
    Bsv.ShowMainWindow()

    args = sys.argv
    useArgDataJsonPath = False
    useArgShotIndex = False

    if (len(args) >= (1+1)):
        dataJsonPath = Path(args[1])
        useArgDataJsonPath = True
        if (len(args) >= (2+1)):
            shotIndex = int(args[2])
            useArgShotIndex = True

    while True:
        if not useArgDataJsonPath:
            options = QFileDialog.Option.ReadOnly
            selectedFilePath, selectedFileType = QFileDialog.getOpenFileName(Bsv.MainWin, "选择 BUT json 文件", "", "Json文本 (*.json);;所有文件 (*)", options=options)
            if selectedFileType == '':
                sys.exit()
            dataJsonPath = Path(selectedFilePath)

        try:
            Am = BUT.ArchiveManager(jsonPath=dataJsonPath)
        except Exception as e:
            useArgDataJsonPath = False
            useArgShotIndex = False
            continue
        else:
            break

    Bsv.jsonPath = dataJsonPath
    Bsv.UpdateSnapshotInfoBar()

    while True:
        if not useArgShotIndex:
            # overview = GetSnapshotsOverview(Am)
            # json_str = json.dumps(overview, indent=4, ensure_ascii=False, sort_keys=True)
            selectedShotIndex, ok = text, ok = QInputDialog.getText(Bsv.MainWin, "Input snapshot index", f'From 0 to {(len(Am.snapshots)-1)}')
            if not ok:
                sys.exit()

        try:
            if not useArgShotIndex:
                shotIndex = int(selectedShotIndex)
            snapshot = Am.snapshots[shotIndex]
        except Exception as e:
            useArgShotIndex = False
            continue
        else:
            break

    Bsv.LoadSnapshot(Am.snapshots[shotIndex], dataJsonPath, shotIndex)
    sys.exit(App.exec())