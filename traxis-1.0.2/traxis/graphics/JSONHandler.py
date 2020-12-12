# Copyright (C) 2020 Syed Haider Abidi, Nooruddin Ahmed and Christopher Dydula, Anas Ali, Ruchir Tullu
#
# This file is part of traxis.
#
# traxis is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# traxis is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with traxis.  If not, see <http://www.gnu.org/licenses/>.

from PyQt5.QtWidgets import *
from os import listdir
from os import getcwd
from os.path import isfile, join

class JSONSessions(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.cd = getcwd()
        self.initUI(self.cd)

    def initUI(self, path):
        vbox = QVBoxLayout()
        self.listWidget = QListWidget()
        vbox.addWidget(self.listWidget)
        self.setLayout(vbox)
        self.show()
        self.append_text(path)

    def append_text(self, path):
        self.cd = path
        self.listWidget.clear()
        AllFilesList = [f for f in listdir(self.cd ) if isfile(join(self.cd , f))]
        JSONFileList = []

        for j in range(0, len(AllFilesList)):
            if (AllFilesList[j][-1] == 'n') and (AllFilesList[j][-2] == 'o') and (AllFilesList[j][-3] == 's') and (AllFilesList[j][-4] == 'j') and (AllFilesList[j][-5] == '.'):
                JSONFileList.append(AllFilesList[j])

        for i in range(0, len(JSONFileList)):
            self.listWidget.addItem(JSONFileList[i])
