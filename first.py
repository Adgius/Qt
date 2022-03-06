from PyQt5 import QtWidgets, uic
from PyQt5.QtCore import Qt
from second import Simple_table
import sys
    
lst = ['Кузнецов А.Г.', 'Иванов В.В.', 'Сидоров О.Д.', 'Жмышенко В.А.']

class Simple_combo(QtWidgets.QMainWindow):
    def __init__(self):
        super(Simple_combo, self).__init__()
        self.ui = uic.loadUi('Simple_combo.ui', self)
        self.ui.open_window_btn.clicked.connect(self.open_window)

        for i, fio in enumerate(lst):
            self.ui.comboBox.addItem(fio, i)
        self.ui.comboBox.setCurrentText('Нажмите для выбора')

    def open_window(self):
        Form = Simple_table(FIO=self.ui.comboBox.collect_checked())
        Form.setWindowModality(Qt.ApplicationModal)
        Form.show()

 
app = QtWidgets.QApplication([])
application = Simple_combo()
application.show()
 
sys.exit(app.exec())