import sqlite3
from PyQt5 import QtWidgets, uic


class CoffeeApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(CoffeeApp, self).__init__()
        uic.loadUi('main.ui', self)
        self.load_data()

    def load_data(self):
        connection = sqlite3.connect('coffee.sqlite')
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM coffee")
        rows = cursor.fetchall()
        self.tableWidget.setRowCount(len(rows))
        self.tableWidget.setColumnCount(len(rows[0]))
        for i, row in enumerate(rows):
            for j, val in enumerate(row):
                self.tableWidget.setItem(i, j, QtWidgets.QTableWidgetItem(str(val)))
        connection.close()


if __name__ == '__main__':
    import sys

    app = QtWidgets.QApplication(sys.argv)
    window = CoffeeApp()
    window.show()
    sys.exit(app.exec_())
