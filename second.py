from PyQt5 import QtWidgets, uic
import sys

lst_1 =['Физика', 'Химия', 'Математика']
lst_2 =['5', '4', '3', '2', '1', '0']

class Simple_table(QtWidgets.QMainWindow):
    def __init__(self, **kwargs):
        super(Simple_table, self).__init__()
        self.ui = uic.loadUi('Simple_table.ui', self)
        
        self.ui.pushButton.clicked.connect(self.add_row)
        self.ui.pushButton_2.clicked.connect(self.remove_row)

        self.ui.tableWidget.setColumnCount(3)
        self.ui.tableWidget.setHorizontalHeaderLabels(['ФИО', 'Предмет', 'Оценка'])
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(0, 
            QtWidgets.QHeaderView.Stretch) 
        
        self.students = kwargs.get('FIO')
        self.fill_table()

    def fill_table(self):
        for fio in self.students:
            self.add_row()
            label = QtWidgets.QLineEdit()
            label.setText(fio)
            self.ui.tableWidget.setCellWidget(0, 0, label)


    def add_row(self):
        label = QtWidgets.QLineEdit()

        combo_1 = QtWidgets.QComboBox()
        combo_1.setEditable(True)
        for i in lst_1:
            combo_1.addItem(i)
        combo_1.setCurrentText('')

        combo_2 = QtWidgets.QComboBox()
        combo_2.setEditable(True)
        for i in lst_2:
            combo_2.addItem(i)
        combo_2.setCurrentText('')

        if self.ui.tableWidget.currentRow() != -1:
            rowPosition = self.ui.tableWidget.currentRow()
            self.ui.tableWidget.insertRow(rowPosition+1)
            self.ui.tableWidget.setCellWidget(rowPosition+1, 0, label)
            self.ui.tableWidget.setCellWidget(rowPosition+1, 1, combo_1)
            self.ui.tableWidget.setCellWidget(rowPosition+1, 2, combo_2)
        else:
            self.ui.tableWidget.insertRow(0)
            self.ui.tableWidget.setCellWidget(0, 0, label)
            self.ui.tableWidget.setCellWidget(0, 1, combo_1)
            self.ui.tableWidget.setCellWidget(0, 2, combo_2)

    def remove_row(self):
        ind = self.ui.tableWidget.selectionModel().selectedRows()
        if len(ind) > 0:
            for i in ind:
                self.ui.tableWidget.removeRow(i.row())

if __name__ == "__main__":
    app = QtWidgets.QApplication([])
    application = Simple_table()
    application.show()
    sys.exit(app.exec())