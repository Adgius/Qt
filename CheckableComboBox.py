from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
 
class CheckableComboBox(QtWidgets.QComboBox):
    def __init__(self, parent=None):
        super(CheckableComboBox, self).__init__(parent)
        self.view().pressed.connect(self.itemChecked)
        self._changed = False
        self.activated.connect(self.changeText)
        self.setEditable(True)
        self.lineEdit().setReadOnly(True)

    def itemChecked(self, index):
        item = self.model().itemFromIndex(index)
        if item.checkState() == Qt.Checked:
            item.setCheckState(Qt.Unchecked)
        else:
            item.setCheckState(Qt.Checked)
        self._changed = True
        
    def addItem(self, text, index):
        super(CheckableComboBox, self).addItem(text)
        item = self.model().item(index, self.modelColumn())
        item.setCheckState(Qt.Unchecked)

    def hidePopup(self): #Родительский метод, скрывает всплывающий список
        if not self._changed:
            super(CheckableComboBox, self).hidePopup()
        self._changed = False

    def collect_checked(self):
        checkedItems = []
        for i in range(self.count()):
            item = self.model().item(i, 0)
            if item.checkState() == Qt.Checked:
                checkedItems.append(item.text())   
        return checkedItems     

    def changeText(self):
        checkedItems = self.collect_checked()
        checkedItems = '; '.join(checkedItems)
        self.setCurrentText(checkedItems)
        self.lineEdit().setReadOnly(True)