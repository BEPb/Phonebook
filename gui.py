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


        self.table = QtWidgets.QTableWidget(self.centralwidget)
        self.table.setShowGrid(True)
        self.table.setObjectName("table")
        self.table.setColumnCount(13)
        # self.table.setRowCount(1)



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
        self.gridLayout.addWidget(self.table, 0, 3, 15, 1)  # строка=0, колонка=3, отступ строка=10, отступ колонка=1

        # подпись ячейки
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setObjectName("label_1")
        self.gridLayout.addWidget(self.label_1, 0, 1, 1, 1)
        # ячейка ввода
        self.organization = QtWidgets.QLineEdit(self.centralwidget)
        self.organization.setObjectName("organization")
        self.gridLayout.addWidget(self.organization, 0, 2, 1, 1, QtCore.Qt.AlignLeft)

        # подпись ячейки
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 1, 1, 1)
        # ячейка ввода
        self.division = QtWidgets.QLineEdit(self.centralwidget)
        self.division.setObjectName("division")
        self.gridLayout.addWidget(self.division, 1, 2, 1, 1, QtCore.Qt.AlignLeft)

        # подпись ячейки
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 1, 1, 1)
        # ячейка ввода
        self.subdivision = QtWidgets.QLineEdit(self.centralwidget)
        self.subdivision.setObjectName("subdivision")
        self.gridLayout.addWidget(self.subdivision, 2, 2, 1, 1, QtCore.Qt.AlignLeft)

        # подпись ячейки
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 3, 1, 1, 1)
        # ячейка ввода
        self.subdivision_level1 = QtWidgets.QLineEdit(self.centralwidget)
        self.subdivision_level1.setObjectName("subdivision_level1")
        self.gridLayout.addWidget(self.subdivision_level1, 3, 2, 1, 1, QtCore.Qt.AlignLeft)

        # подпись ячейки
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 4, 1, 1, 1)
        # ячейка ввода
        self.subdivision_level2 = QtWidgets.QLineEdit(self.centralwidget)
        self.subdivision_level2.setObjectName("subdivision_level2")
        self.gridLayout.addWidget(self.subdivision_level2, 4, 2, 1, 1, QtCore.Qt.AlignLeft)

        # подпись ячейки
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 5, 1, 1, 1)
        # ячейка ввода
        self.position = QtWidgets.QLineEdit(self.centralwidget)
        self.position.setObjectName("position")
        self.gridLayout.addWidget(self.position, 5, 2, 1, 1, QtCore.Qt.AlignLeft)

        # подпись ячейки
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 6, 1, 1, 1)
        # ячейка ввода
        self.name = QtWidgets.QLineEdit(self.centralwidget)
        self.name.setObjectName("name")
        self.gridLayout.addWidget(self.name, 6, 2, 1, 1, QtCore.Qt.AlignLeft)

        # подпись ячейки
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 7, 1, 1, 1)
        # ячейка ввода
        self.family_name = QtWidgets.QLineEdit(self.centralwidget)
        self.family_name.setObjectName("family_name")
        self.gridLayout.addWidget(self.family_name, 7, 2, 1, 1, QtCore.Qt.AlignLeft)

        # подпись ячейки
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 8, 1, 1, 1)
        # ячейка ввода
        self.middle_name = QtWidgets.QLineEdit(self.centralwidget)
        self.middle_name.setObjectName("middle_name")
        self.gridLayout.addWidget(self.middle_name, 8, 2, 1, 1, QtCore.Qt.AlignLeft)

        # подпись ячейки
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setObjectName("label_10")
        self.gridLayout.addWidget(self.label_10, 9, 1, 1, 1)
        # ячейка ввода
        self.work_number = QtWidgets.QLineEdit(self.centralwidget)
        self.work_number.setObjectName("work_number")
        self.gridLayout.addWidget(self.work_number, 9, 2, 1, 1, QtCore.Qt.AlignLeft)

        # подпись ячейки
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 10, 1, 1, 1)
        # ячейка ввода
        self.mobile_phone = QtWidgets.QLineEdit(self.centralwidget)
        self.mobile_phone.setObjectName("mobile_phone")
        self.gridLayout.addWidget(self.mobile_phone, 10, 2, 1, 1, QtCore.Qt.AlignLeft)

        # подпись ячейки
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setObjectName("label_12")
        self.gridLayout.addWidget(self.label_12, 11, 1, 1, 1)
        # ячейка ввода
        self.city_phone = QtWidgets.QLineEdit(self.centralwidget)
        self.city_phone.setObjectName("city_phone")
        self.gridLayout.addWidget(self.city_phone, 11, 2, 1, 1, QtCore.Qt.AlignLeft)

        # подпись ячейки
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setObjectName("label_13")
        self.gridLayout.addWidget(self.label_13, 12, 1, 1, 1)
        # ячейка ввода
        self.mark = QtWidgets.QLineEdit(self.centralwidget)
        self.mark.setObjectName("mark")
        self.gridLayout.addWidget(self.mark, 12, 2, 1, 1, QtCore.Qt.AlignLeft)

        # кнопка добавить
        self.add = QtWidgets.QPushButton(self.centralwidget)
        self.add.setObjectName("add")
        self.gridLayout.addWidget(self.add, 14, 0, 1, 3)

        # кнопка удалить
        self.remove = QtWidgets.QPushButton(self.centralwidget)
        self.remove.setObjectName("remove")
        self.gridLayout.addWidget(self.remove, 15, 0, 1, 3)

        # кнопка поиск
        self.search = QtWidgets.QPushButton(self.centralwidget)
        self.search.setObjectName("search")
        self.gridLayout.addWidget(self.search, 16, 0, 1, 3)

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

        # Кнопки
        self.add.clicked.connect(self.add_button)
        self.search.clicked.connect(self.search_button)
        self.remove.clicked.connect(self.delete_button)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Телефонная книга"))

        # подпись колонок таблицы
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
        self.table.resizeColumnsToContents()  # выравнивание ширины колонок по контенту

        # подписываем ячейки ввода данных
        self.label_1.setText(_translate("MainWindow", "Организация"))
        self.label_2.setText(_translate("MainWindow", "Управление"))
        self.label_3.setText(_translate("MainWindow", "Подразделение"))
        self.label_4.setText(_translate("MainWindow", "Подр. ур1"))
        self.label_5.setText(_translate("MainWindow", "Подр. ур2"))
        self.label_6.setText(_translate("MainWindow", "Должность"))
        self.label_7.setText(_translate("MainWindow", "Имя"))
        self.label_8.setText(_translate("MainWindow", "Отчество"))
        self.label_9.setText(_translate("MainWindow", "Фамилия"))
        self.label_10.setText(_translate("MainWindow", "Внутр. телефон"))
        self.label_11.setText(_translate("MainWindow", "Моб. телефон"))
        self.label_12.setText(_translate("MainWindow", "Гор. телефон"))
        self.label_13.setText(_translate("MainWindow", "Примечание"))

        # подпись кнопки
        self.add.setText(_translate("MainWindow", "Добавить"))
        self.search.setText(_translate("MainWindow", "Поиск"))
        self.remove.setText(_translate("MainWindow", "Удалить"))




