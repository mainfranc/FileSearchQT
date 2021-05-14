from PySide2.QtCore import (QFile, QFileInfo, QIODevice, QTextStream, Qt, Signal, QThread)
from PySide2.QtWidgets import (QMainWindow, QApplication, QTableWidgetItem, QFileDialog)

import time
import re
import os, sys

import Find_File

class Monitor(QMainWindow):
    def __init__(self, parent=None):
        super().__init__()
        self.ui = Find_File.Ui_MainWindow()
        self.ui.setupUi(self)
        self.regex_filename = False
        self.regex_text = False
        self.match_count = 0

        #Buttons click
        self.ui.btnBrowse.clicked.connect(self.btnBrowsePressed)
        self.thread = File_Thread()
        self.thread.mysignal.connect(self.btnFindFileclicked, Qt.QueuedConnection)
        self.ui.btnFindFile.clicked.connect(self.thread.start)

    def btnBrowsePressed(self):
        folder_name = QFileDialog.getExistingDirectory()
        if not os.path.isfile(folder_name):
            self.ui.txtDirectory.setText(folder_name)
            return None
        print('Please choose the correct folder')

    def btnFindFileclicked(self):
        self.match_count = 0
        self.result = []
        self.list_folder_structure(self.ui.txtDirectory.text())
        self.update_table()

    def list_folder_structure(self, start_dir):
        os.chdir(start_dir)
        curr_folder = start_dir
        for i in os.listdir(path='.'):
            is_it_file = os.path.isfile(curr_folder + '/' + i)
            if is_it_file:
                if self.check_is_right(i, curr_folder):
                    self.result.append((i, curr_folder))
            else:
                self.list_folder_structure(curr_folder + '/' + i)

    def update_table(self):
        self.ui.tblFiles.clearContents()
        for row in range(self.ui.tblFiles.rowCount(), -1, -1):
            self.ui.tblFiles.removeRow(row)
        rowPosition = 0
        for i in self.result:
            self.ui.tblFiles.insertRow(rowPosition)
            self.ui.tblFiles.setItem(rowPosition, 0, QTableWidgetItem(i[0]))
            self.ui.tblFiles.setItem(rowPosition, 1, QTableWidgetItem(i[1] + "/"))
            file_size = QFileInfo(i[1] + "/" + i[0]).size()
            self.ui.tblFiles.setItem(rowPosition, 2, QTableWidgetItem(str(round(file_size / 1024, 1)) + ' kb'))
            rowPosition += 1
        self.ui.lblStatus.setText(f"{self.match_count} file{'s' if self.match_count else ''} found")

    def check_is_right(self, filename, filepath):
        self.regex_filename = self.ui.chkFileNameReg.isChecked()
        self.regex_text = self.ui.chkTextToFindReg.isChecked()
        if filename[-4:] == '.exe':
            return False
        return all((self.file_name_appl(filename), self.text_in_file(filename, filepath)))

    def file_name_appl(self, filename):
        fn_to_search = self.ui.txtFileName.text()
        if self.regex_filename:
            does_match = re.compile(r"\\" + fn_to_search).match
            if does_match(filename):
                return True
            return False
        if fn_to_search in filename:
            return True
        return False

    def text_in_file(self, filename, filepath):
        filepath = filepath if filepath[-1] == '/' else filepath + '/'
        inFile = QFile(filepath + filename)
        text_in = QTextStream(inFile)
        txt_to_find = self.ui.txtTextToFind.text()
        if self.regex_text:

            does_match = re.compile(r"\\" + txt_to_find).match
        if inFile.open(QIODevice.ReadOnly):
            while not text_in.atEnd():
                line = text_in.readLine()
                if self.regex_text:
                    if does_match(line):
                        self.match_count += 1
                        return True
                else:
                    if txt_to_find in line:
                        self.match_count += 1
                        return True
                return False


class File_Thread(QThread):
    mysignal = Signal()
    def run(self) -> None:
        self.mysignal.emit()
        time.sleep(5)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    myWindow = Monitor()
    myWindow.show()

    sys.exit(app.exec_())