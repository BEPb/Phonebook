# -*- coding: utf-8 -*-

"""
Python 3.9 программа консольного приложения телефонного справочника
Название файла  main.py

Version: 0.1
Author: Andrej Marinchenko
Date: 2022-04-23
"""


import gui  # подключаем свой модуль класс
import sqlite3 as db
import xlsxwriter
import xlrd
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QApplication, QMessageBox, QFileDialog
from PyQt5.QtCore import pyqtSlot, QObject, QThread, pyqtSignal
from sys import argv


class load_worker(QObject):
    finished = pyqtSignal()
    def __init__(self, sql):
        super().__init__()
        self.sql = sql

    def run(self):
        global database_data
        database_data = None
        database_data = LoadData(self.sql)
        self.finished.emit()


class delete_worker(QObject):
    finished = pyqtSignal()
    def __init__(self, target):
        super().__init__()
        self.target = target

    def run(self):
        con = db.connect('.phones.sqlite3')
        for index in sorted(self.target.table.selectionModel().selectedRows()):
            row = index.row()
            sql = "DELETE FROM Phones WHERE name LIKE '%{0}%' AND middle_name LIKE '%{1}%' AND family_name LIKE '%{2}%'".format(
                self.target.table.model().data(self.target.table.model().index(row, 6)),
                self.target.table.model().data(self.target.table.model().index(row, 7)),
                self.target.table.model().data(self.target.table.model().index(row, 8))
            )

            print(self.target.table.model().data(self.target.table.model().index(row, 6)))
            print(self.target.table.model().data(self.target.table.model().index(row, 7)))
            print(self.target.table.model().data(self.target.table.model().index(row, 8)))
            cur = con.cursor()
            cur.execute(sql)
        con.commit()

        self.target.clear_table()  # очистка таблицы
        self.target.load_table('SELECT * FROM Phones')  # чтение таблицы

# класс создания графического приложения
class App(QtWidgets.QMainWindow, gui.Ui_MainWindow):  # на входе библиотека виджета и подключенный собств. модуль
    def __init__(self, parent=None):  # инициализация класса
        super(App, self).__init__(parent)
        self.setupUi(self)
        self.load_table('SELECT * FROM phones')
        self.showMaximized()

    # функция сохранения данных
    def save(self):
        cur = con.cursor()
        for i in range(self.table.rowCount()):  # перебираем все строки
            column = []
            for j in range(self.table.columnCount()):  # перебираем все колонки
                if j != 12:
                    column.append(self.table.model().data(self.table.model().index(i, j)))
                else:
                    column.append(self.table.cellWidget(i,j).currentText())
            
            sql = """UPDATE Phones 
            SET organization = '%s',
            division = '%s',
            subdivision = '%s',
            subdivision_level1 = '%s',
            subdivision_level2 = '%s',
            position = '%s',
            name = '%s',
            middle_name = '%s',
            family_name = '%s',
            work_number = '%s',
            mobile_phone = '%s',
            city_phone = '%s',
            mark = '%s',
            WHERE id = %s;""" % tuple(column)
            cur.execute(sql)
            con.commit()
 
    def clear_table(self):
        self.table.setRowCount(0)

    # функция чтения данных
    def load_table(self, sql):
        global database_data
        database_data = None
        self.thread = QThread(self)
        self.worker = load_worker(sql)
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.thread.start()
        self.thread.finished.connect(self.load_table_thread_callback)

    def load_table_thread_callback(self):
        global database_data
        if database_data == []:
            return False
        
        for row in database_data:
            row_pos = self.table.rowCount()
            self.table.insertRow(row_pos)
            for i, column in enumerate(row, 0):
                normal_widget_item = True
                item = QtWidgets.QTableWidgetItem(str(column))
                # if i == 12:
                #     item = QtWidgets.QComboBox()
                #     item.addItems(self.all_messager_types)
                #     item.setCurrentIndex(self.all_messager_types.index(column))
                #     normal_widget_item = False
                #
                if i == 12:
                    flags = QtCore.Qt.ItemFlags()
                    flags != QtCore.Qt.ItemIsEnabled
                    item.setFlags(flags)
                
                if normal_widget_item:
                    self.table.setItem(row_pos, i, item)
                else:
                    self.table.setCellWidget(row_pos,i,item)
        
        self.table.resizeColumnsToContents()
        
    def error(self, text, title = "Проблема"):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText(text)
        msg.setWindowTitle("Проблема")
        msg.exec_()
        del msg

    def info(self, text, title = "Информация"):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(text)
        msg.setWindowTitle("Информация")
        msg.exec_()
        del msg

    def question(self,title,text):
        buttonReply = QMessageBox.question(self, title, text, QMessageBox.Yes | QMessageBox.No, QMessageBox.No)
        if buttonReply == QMessageBox.Yes:
            del buttonReply
            return True
        else:
            del buttonReply
            return False
    

    def export_excel(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getSaveFileName(self,"Export", "","Xls Files (*.xlsx)", options=options)
        if fileName:
            workbook = xlsxwriter.Workbook(fileName)
            worksheet = workbook.add_worksheet()
            
            for i in range(self.table.columnCount()):
                    text = self.table.horizontalHeaderItem(i).text()
                    worksheet.write(0, i,text)

            for i in range(self.table.columnCount()):
                for j in range(self.table.rowCount()):
                    if i != 12:
                        text = self.table.item(j, i).text()
                    else:
                        text = self.table.cellWidget(j,i).currentText()
                    # text = self.table.cellWidget(j, i).currentText()
                    worksheet.write(j + 1, i,text)
            workbook.close()
            self.info('Вывод успешно создан!')
    
    def import_excel(self):
        options = QFileDialog.Options()
        options = QFileDialog.DontUseNativeDialog
        user_file, _ = QFileDialog.getOpenFileName(self,"Please select a file", "","Excel File (*.xlsx)", options=options)
        if user_file:
            wb = xlrd.open_workbook(user_file)
            sheet = wb.sheet_by_index(0)
            
            for i,row in enumerate(range(sheet.nrows)):
                if i == 0:
                    continue
                row_data = []
                for j,col in enumerate(range(sheet.ncols)):
                    if j == 12:
                        continue
                    row_data.append(sheet.cell_value(row, col))
                try:
                    AddData(row_data)
                    self.load_table('SELECT * FROM Phones')                    
                    self.info('Информация введена успешно!')
                
                except db.IntegrityError:
                    self.error('Пользователь {0} доступен!'.format(i))
                
                except db.ProgrammingError:
                    self.error('Файл Excel был изменен. Пользователь {0} не добавлен в базу данных.'.format(i))

    def quit_safe(self):
        self.save()
        exit(0)
    
    def closeEvent(self, event):
        self.quit_safe()
        event.accept()

    def about_programer(self):
        self.info("Эта программа была создана Андреем Маринченко. \n Вы можете использовать адрес электронной почты "
                  "andrej.marinchenko@gmail.com чтобы связаться")

    def about_licenc(self):
        self.info('Эта программа выпущена под лицензией GPL версии 3.')
    
    def reset_textboxs(self):
        self.clear_table()
        self.load_table('SELECT * FROM phones')
        self.organization.setText("")
        self.division.setText("")
        self.subdivision.setText("")
        self.subdivision_level1.setText("")
        self.subdivision_level2.setText("")
        self.position.setText("")
        self.name.setText("")
        self.family_name.setText("")
        self.middle_name.setText("")
        self.work_number.setText("")
        self.mobile_phone.setText("")
        self.city_phone.setText("")
        self.mark.setText("")

    # функция добавления данных в таблицу
    @pyqtSlot()
    def add_button(self):
        datas = {
            'organization' : self.organization.text(),
            'division' : self.division.text(),
            'subdivision' : self.subdivision.text(),
            'subdivision_level1' : self.subdivision_level1.text(),
            'subdivision_level2' : self.subdivision_level2.text(),
            'position' : self.position.text(),
            'name' : self.name.text(),
            'family_name' : self.family_name.text(),
            'middle_name' : self.middle_name.text(),
            'work_number' : self.work_number.text(),
            'mobile_phone' : self.mobile_phone.text(),
            'city_phone' : self.city_phone.text(),
            'mark' : self.mark.text()
        }
        if datas['name'] and datas['family_name']:
            try:
                AddData(list(datas.values()))
                self.reset_textboxs()
                row_pos = self.table.rowCount()
                self.table.insertRow(row_pos)
                for i, column in enumerate(datas.values(), 0):
                    normal_widget_item = True
                    item = QtWidgets.QTableWidgetItem(str(column))
                    # if i == 12:
                    #     item = QtWidgets.QComboBox()
                    #     item.addItems(self.all_messager_types)
                    #     item.setCurrentIndex(self.all_messager_types.index(column))
                    #     normal_widget_item = False

                    if i == 12:
                        flags = QtCore.Qt.ItemFlags()
                        flags != QtCore.Qt.ItemIsEnabled
                        item.setFlags(flags)

                    if normal_widget_item:
                        self.table.setItem(row_pos, i, item)
                    else:
                        self.table.setCellWidget(row_pos, i, item)
            
                self.table.resizeColumnsToContents()
            except db.IntegrityError:
                self.error('Необходимая информация доступна в базе данных')
        else:
            self.error('Пожалуйста, заполните имя и фамилию')

    # функция поиска в каждой ячейке
    @pyqtSlot()
    def search_button(self):
        datas = {
            'organization' : self.organization.text(),
            'division' : self.division.text(),
            'subdivision' : self.subdivision.text(),
            'subdivision_level1' : self.subdivision_level1.text(),
            'subdivision_level2' : self.subdivision_level2.text(),
            'position' : self.position.text(),
            'name' : self.name.text(),
            'family_name' : self.family_name.text(),
            'middle_name' : self.middle_name.text(),
            'work_number' : self.work_number.text(),
            'mobile_phone' : self.mobile_phone.text(),
            'city_phone' : self.city_phone.text(),
            'mark' : self.mark.text()
            }
        sql = """
        SELECT * FROM Phones WHERE 
        organization LIKE '%{0}%' AND 
        division LIKE '%{1}%' AND 
        subdivision LIKE '%{2}%' AND 
        subdivision_level1 LIKE '%{3}%' AND
        subdivision_level2 LIKE '%{4}%' AND
        position LIKE '%{5}%' AND
        name LIKE '%{6}%' AND
        family_name LIKE '%{7}%' AND
        middle_name LIKE '%{8}%' AND
        work_number LIKE '%{9}%' AND
        mobile_phone LIKE '%{10}%' AND
        city_phone LIKE '%{11}%' AND
        mark LIKE '%{12}%'        
        """.format(
            datas['organization'],
            datas['division'],
            datas['subdivision'],
            datas['subdivision_level1'],
            datas['subdivision_level2'],
            datas['position'],
            datas['name'],
            datas['family_name'],
            datas['middle_name'],
            datas['work_number'],
            datas['mobile_phone'],
            datas['city_phone'],
            datas['mark']
        )
        self.clear_table()
        if self.load_table(sql) == False:
            self.error("Ошибка чтения")

    # функция удаления строки данных
    @pyqtSlot()
    def delete_button(self):
        if self.table.selectionModel().selectedRows() == []:  # если строка данных не выбрана
            self.error("Пожалуйста, выберите пользователя для удаления")
            return False
        
        if self.question("Удалить пользователя", "Уверены ли вы?"):  # окно подтверждения удаления строки пользователя

            self.del_thread = QThread(self)
            self.worker = delete_worker(self)
            self.worker.moveToThread(self.del_thread)
            self.del_thread.started.connect(self.worker.run)
            self.worker.finished.connect(self.thread.quit)
            self.worker.finished.connect(self.worker.deleteLater)
            self.del_thread.finished.connect(self.del_thread.deleteLater)
            self.del_thread.start()
    
    @pyqtSlot()
    def export(self):
        self.export_excel()

# функция создания таблицы данных телефонного справочника
def CreateTable():
    global con  # глобальная переменная
    cur = con.cursor()  # курсор подключения к базе данных
    cur.execute('''
        CREATE TABLE IF NOT EXISTS `phones`(
            organization TEXT,
            division TEXT,
            subdivision TEXT,
            subdivision_level1 TEXT,
            subdivision_level2 TEXT,
            position TEXT,
            name TEXT,
            family_name TEXT,
            middle_name TEXT,
            work_number TEXT,
            mobile_phone TEXT,
            city_phone TEXT,
            mark TEXT,
            id INTEGER PRIMARY KEY AUTOINCREMENT
        )
        ''')
    return True  # создание базы данных успешно

# функция чтения базы данных
def LoadData(sql):
    con = db.connect('.phones.sqlite3')  # глобальная переменная
    cur = con.cursor()
    cur.execute(sql)
    return cur.fetchall()

# функция добавления данных в базу
def AddData(values):
    cur = con.cursor()
    cur.execute('''
    INSERT INTO `phones`(organization, division, subdivision, subdivision_level1, subdivision_level2, position, name, family_name, middle_name, work_number, mobile_phone, city_phone, mark)
    VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)
    ''',values)
    con.commit()
    return True

# главная функция
def main():
    global con, mainWindow  # определяем глобальные переменные
    con = db.connect('.phones.sqlite3')  # подключение к базе данных
    CreateTable()  # создание таблицы (определены все колонки, на выходе истина)
    mainApp = QApplication(argv)  # главное окно
    mainWindow = App()  #
    mainApp.exec_()  #
    con.close()  #

# проверка на запуск главной программы
if __name__ == "__main__" : main()
