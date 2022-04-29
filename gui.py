# -*- coding: utf-8 -*-
"""
Python 3.9 программа консольного приложения телефонного справочника
Название файла  gui.py

Version: 0.1
Author: Andrej Marinchenko
Date: 2022-04-23
"""

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")  # создаем экземпляр объекта главного окна
        font = QtGui.QFont()  #
        font.setFamily("Tahoma")  # определяем шрифт
        MainWindow.setFont(font)  # применяем шрифт для главного окна
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)  # определяем порядок размещения кнопок слева на право
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.Russian, QtCore.QLocale.Russia))  # определяем язык и страну
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")  # тип размещения элементов сетка

        self.organization = QtWidgets.QLabel(self.centralwidget)
        self.organization.setObjectName("organization")
        self.gridLayout.addWidget(self.organization, 1, 1, 1, 1, QtCore.Qt.AlignRight)

        # self.division = QtWidgets.QLabel(self.centralwidget)
        # self.division.setObjectName("Подразделение")
        # self.gridLayout.addWidget(self.division, 1, 1, 1, 1)

        # self.subdivision = QtWidgets.QLabel(self.centralwidget)
        # self.subdivision.setObjectName("подразделение")
        # self.gridLayout.addWidget(self.subdivision, 0, 1, 1, 1, QtCore.Qt.AlignLeft)
        #
        # self.subdivision_level1 = QtWidgets.QLineEdit(self.centralwidget)
        # self.subdivision_level1.setObjectName("подразделение ур.1")
        # self.gridLayout.addWidget(self.subdivision_level1, 0, 2, 1, 1, QtCore.Qt.AlignRight)
        #
        # self.subdivision_level2 = QtWidgets.QLabel(self.centralwidget)
        # self.subdivision_level2.setObjectName("подразделение ур.2")
        # self.gridLayout.addWidget(self.subdivision_level2, 3, 1, 1, 1)

        self.table = QtWidgets.QTableWidget(self.centralwidget)
        self.table.setShowGrid(True)
        self.table.setObjectName("table")
        self.table.setColumnCount(13)
        self.table.setRowCount(2)

        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(6, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(7, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(8, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(9, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(10, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(11, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(12, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(13, item)

        # определяем положение таблицы в сетке
        self.gridLayout.addWidget(self.table, 0, 3, 10, 1)  # строка=0, колонка=3, отступ строка=10, отступ колонка=1

        self.organization = QtWidgets.QLabel(self.centralwidget)
        self.organization.setObjectName("organization")
        self.gridLayout.addWidget(self.organization, 2, 2, 1, 1, QtCore.Qt.AlignRight)

        self.division = QtWidgets.QLabel(self.centralwidget)
        self.division.setObjectName("division")
        self.gridLayout.addWidget(self.division, 1, 2, 1, 1, QtCore.Qt.AlignRight)


        MainWindow.setCentralWidget(self.centralwidget)
        self.retranslateUi(MainWindow)  # подключаем подписи элементов таблицы
        QtCore.QMetaObject.connectSlotsByName(MainWindow)



        # прописываем виджеты и действия
        exitAction = QtWidgets.QAction('Выход', self)
        exitAction.triggered.connect(self.quit_safe)

        saveAction = QtWidgets.QAction('Сохранить', self)
        saveAction.triggered.connect(self.save)

        about_programerAction = QtWidgets.QAction('О производителе', self)
        about_programerAction.triggered.connect(self.about_programer)

        about_licencAction = QtWidgets.QAction('Лицензия на публикацию программы', self)
        about_licencAction.triggered.connect(self.about_licenc)

        excelMenu_import = QtWidgets.QAction('Импорт данных из Excel', self)
        excelMenu_import.triggered.connect(self.import_excel)

        excelMenu_export = QtWidgets.QAction('Экспорт в формат Excel', self)
        excelMenu_export.triggered.connect(self.export_excel)

        # прописываем менюбар
        menubar = self.menuBar()

        fileMenu = menubar.addMenu('Файл')  # первая вкладка меню бара (ниже указано его содержание)
        fileMenu.addAction(saveAction)
        fileMenu.addAction(excelMenu_import)
        fileMenu.addAction(excelMenu_export)
        fileMenu.addAction(exitAction)

        aboutMenu = menubar.addMenu('О программе')  # вторая вкладка меню бара (ниже указано его содержание)
        aboutMenu.addAction(about_programerAction)
        aboutMenu.addAction(about_licencAction)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Телефонная книга"))

        item = self.table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Организация"))
        item = self.table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Управление"))
        item = self.table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Подразделение"))
        item = self.table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Подр-е ур.1"))
        item = self.table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Подра-е ур.2"))
        item = self.table.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Должность"))
        item = self.table.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Имя"))
        item = self.table.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Отчество"))
        item = self.table.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "Фамилия"))
        item = self.table.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "Внутр. телефон"))
        item = self.table.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "Мобильный телефон"))
        item = self.table.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "Городской телефон"))
        item = self.table.horizontalHeaderItem(12)
        item.setText(_translate("MainWindow", "Примечание"))


        self.organization.setText(_translate("MainWindow", "Организация"))
        self.division.setText(_translate("MainWindow", "Подразделение"))


