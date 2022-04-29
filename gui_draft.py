# -*- coding: utf-8 -*-


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        font = QtGui.QFont()
        font.setFamily("Tahoma")
        MainWindow.setFont(font)
        MainWindow.setLayoutDirection(QtCore.Qt.RightToLeft)
        MainWindow.setLocale(QtCore.QLocale(QtCore.QLocale.Persian, QtCore.QLocale.Iran))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")


        self.division = QtWidgets.QLabel(self.centralwidget)
        self.division.setObjectName("Организация")
        self.gridLayout.addWidget(self.division, 1, 1, 1, 1)

        self.subdivision = QtWidgets.QLabel(self.centralwidget)
        self.subdivision.setObjectName("подразделение")
        self.gridLayout.addWidget(self.subdivision, 0, 1, 1, 1)

        self.subdivision_level1 = QtWidgets.QLineEdit(self.centralwidget)
        self.subdivision_level1.setObjectName("подразделение ур.1")
        self.gridLayout.addWidget(self.subdivision_level1, 0, 0, 1, 1, QtCore.Qt.AlignLeft)

        self.subdivision_level2 = QtWidgets.QLabel(self.centralwidget)
        self.subdivision_level2.setObjectName("подразделение ур.2")
        self.gridLayout.addWidget(self.subdivision_level2, 3, 1, 1, 1)

        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setObjectName("label_9")
        self.gridLayout.addWidget(self.label_9, 4, 1, 1, 1)

        self.phone3 = QtWidgets.QLineEdit(self.centralwidget)
        self.phone3.setObjectName("phone3")
        self.gridLayout.addWidget(self.phone3, 4, 0, 1, 1, QtCore.Qt.AlignLeft)

        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setEnabled(True)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 5, 1, 1, 1, QtCore.Qt.AlignLeft)

        self.home1 = QtWidgets.QLineEdit(self.centralwidget)
        self.home1.setObjectName("home1")
        self.gridLayout.addWidget(self.home1, 5, 0, 1, 1, QtCore.Qt.AlignLeft)

        self.home2 = QtWidgets.QLineEdit(self.centralwidget)
        self.home2.setObjectName("home2")
        self.gridLayout.addWidget(self.home2, 6, 0, 1, 1, QtCore.Qt.AlignLeft)

        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setObjectName("label_11")
        self.gridLayout.addWidget(self.label_11, 2, 1, 1, 1)

        self.work_number = QtWidgets.QLineEdit(self.centralwidget)
        self.work_number.setObjectName("work_number")
        self.gridLayout.addWidget(self.work_number, 7, 0, 1, 1, QtCore.Qt.AlignLeft)

        self.table = QtWidgets.QTableWidget(self.centralwidget)
        self.table.setShowGrid(True)
        self.table.setObjectName("table")
        self.table.setColumnCount(16)
        self.table.setRowCount(0)


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



        self.gridLayout.addWidget(self.table, 0, 3, 18, 1)
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setObjectName("label_7")
        self.gridLayout.addWidget(self.label_7, 6, 1, 1, 1)
        self.family = QtWidgets.QLineEdit(self.centralwidget)
        self.family.setObjectName("family")
        self.gridLayout.addWidget(self.family, 1, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.phone1 = QtWidgets.QLineEdit(self.centralwidget)
        self.phone1.setObjectName("phone1")
        self.gridLayout.addWidget(self.phone1, 2, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 7, 1, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 8, 1, 1, 1)
        self.phone2 = QtWidgets.QLineEdit(self.centralwidget)
        self.phone2.setObjectName("phone2")
        self.gridLayout.addWidget(self.phone2, 3, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.website = QtWidgets.QLineEdit(self.centralwidget)
        self.website.setObjectName("website")
        self.gridLayout.addWidget(self.website, 10, 0, 1, 2)
        self.email = QtWidgets.QLineEdit(self.centralwidget)
        self.email.setObjectName("email")
        self.gridLayout.addWidget(self.email, 11, 0, 1, 2)
        self.messager = QtWidgets.QComboBox(self.centralwidget)
        self.messager.setMinimumSize(QtCore.QSize(70, 0))
        self.messager.setObjectName("messager")
        self.messager.addItem("")
        self.messager.addItem("")
        self.messager.addItem("")
        self.messager.addItem("")
        self.messager.addItem("")


        self.gridLayout.addWidget(self.messager, 13, 0, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 11, 2, 1, 1)
        self.remove = QtWidgets.QPushButton(self.centralwidget)
        self.remove.setObjectName("remove")
        self.gridLayout.addWidget(self.remove, 15, 0, 1, 3)
        self.search = QtWidgets.QPushButton(self.centralwidget)
        self.search.setObjectName("search")
        self.gridLayout.addWidget(self.search, 16, 0, 1, 3)
        self.fax = QtWidgets.QLineEdit(self.centralwidget)
        self.fax.setObjectName("fax")
        self.gridLayout.addWidget(self.fax, 8, 0, 1, 1, QtCore.Qt.AlignLeft)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 9, 2, 1, 1)
        self.workpath_text = QtWidgets.QLabel(self.centralwidget)
        self.workpath_text.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.workpath_text.setObjectName("workpath_text")
        self.gridLayout.addWidget(self.workpath_text, 12, 2, 1, 1)
        self.workpath = QtWidgets.QLineEdit(self.centralwidget)
        self.workpath.setObjectName("workpath")
        self.gridLayout.addWidget(self.workpath, 12, 0, 1, 2)
        self.home_path = QtWidgets.QLineEdit(self.centralwidget)
        self.home_path.setObjectName("home_path")
        self.gridLayout.addWidget(self.home_path, 9, 0, 1, 2)
        self.phone_msg = QtWidgets.QLineEdit(self.centralwidget)
        self.phone_msg.setObjectName("phone_msg")
        self.gridLayout.addWidget(self.phone_msg, 13, 1, 1, 1, QtCore.Qt.AlignLeft)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 13, 2, 1, 1, QtCore.Qt.AlignLeft)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 10, 2, 1, 1)
        self.export_2 = QtWidgets.QPushButton(self.centralwidget)
        self.export_2.setObjectName("export_2")
        self.gridLayout.addWidget(self.export_2, 17, 0, 1, 3)
        self.add = QtWidgets.QPushButton(self.centralwidget)
        self.add.setObjectName("add")
        self.gridLayout.addWidget(self.add, 14, 0, 1, 3)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)        
        #Buttons
        self.add.clicked.connect(self.add_button)
        self.search.clicked.connect(self.search_button)
        self.remove.clicked.connect(self.delete_button)
        self.export_2.clicked.connect(self.export)
        
        #Regex for persion
        persian_alpha_codepoints = '\u0621-\u0628\u062A-\u063A\u0641-\u0642\u0644-\u0648\u064E-\u0651\u0655\u067E\u0686\u0698\u06A9\u06AF\u06BE\u06CC'
        arabic_numbers_codepoints = '\u0660-\u0669'
        additional_arabic_characters_codepoints = '\u0629\u0643\u0649-\u064B\u064D\u06D5'
        punctuation_marks_codepoints = '\u060C\u061B\u061F\u0640\u066A\u066B\u066C'
        space_codepoints ='\u0020\u2000-\u200F\u2028-\u202F'
        persian_num_codepoints = '\u06F0-\u06F9'
        
        #OnlyInt part
        self.only_int = QtCore.QRegExp("[0-9" + persian_num_codepoints + arabic_numbers_codepoints + "]+")
        self.only_int_reg = QtGui.QRegExpValidator(self.only_int)
        self.home1.setValidator(self.only_int_reg)
        self.home2.setValidator(self.only_int_reg)
        self.work_number.setValidator(self.only_int_reg)
        self.phone1.setValidator(self.only_int_reg)
        self.phone2.setValidator(self.only_int_reg)
        self.phone3.setValidator(self.only_int_reg)
        self.fax.setValidator(self.only_int_reg)
        self.phone_msg.setValidator(self.only_int_reg)
        
        #Only al part
        self.only_english = QtCore.QRegExp('[A-Za-z0-9 0-9\\#\+\-\−\_@\.]+')
        self.only_persian = QtCore.QRegExp(r"[\s,"+persian_alpha_codepoints+additional_arabic_characters_codepoints
                     +punctuation_marks_codepoints+space_codepoints+arabic_numbers_codepoints+persian_num_codepoints+r" 0-9\\#\+\-\−\_@\.]+")

        self.only_english_reg = QtGui.QRegExpValidator(self.only_english)
        self.only_persian_reg = QtGui.QRegExpValidator(self.only_persian)
        
        self.website.setValidator(self.only_english_reg)
        self.email.setValidator(self.only_english_reg)

        self.subdivision_level1.setValidator(self.only_persian_reg)
        self.family.setValidator(self.only_persian_reg)
        
        self.home_path.setValidator(self.only_persian_reg)
        self.workpath.setValidator(self.only_persian_reg)


        exitAction = QtWidgets.QAction('Выход', self)
        exitAction.triggered.connect(self.quit_safe)
        
        saveAction = QtWidgets.QAction('Сохранить', self)
        saveAction.triggered.connect(self.save)

        about_programerAction = QtWidgets.QAction('О производителе', self)
        about_programerAction.triggered.connect(self.about_programer)

        about_licencAction = QtWidgets.QAction('Лицензия на публикацию программы', self)
        about_licencAction.triggered.connect(self.about_licenc)

        about_licencAction = QtWidgets.QAction('Лицензия на публикацию программы', self)
        about_licencAction.triggered.connect(self.about_licenc)

        excelMenu_import = QtWidgets.QAction('Импорт данных из Excel', self)
        excelMenu_import.triggered.connect(self.import_excel)

        excelMenu_export = QtWidgets.QAction('Вывод в формате Excel', self)
        excelMenu_export.triggered.connect(self.export_excel)

        menubar = self.menuBar()

        fileMenu = menubar.addMenu('сохранить файл')
        fileMenu.addAction(saveAction)
        fileMenu.addAction(exitAction)

        excelMenu = menubar.addMenu('импорт эксель')
        excelMenu.addAction(excelMenu_import)
        excelMenu.addAction(excelMenu_export)

        aboutMenu = menubar.addMenu('о программе')
        aboutMenu.addAction(about_programerAction)
        aboutMenu.addAction(about_licencAction)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Телефонная книга"))
        self.division.setText(_translate("MainWindow", "Организация"))
        self.subdivision.setText(_translate("MainWindow", "Подразделение"))
        # self.subdivision_level1.setText(_translate("MainWindow", "Подразделение ур1"))
        self.subdivision_level2.setText(_translate("MainWindow", "Подразделение ур2"))
        self.label_9.setText(_translate("MainWindow", "Номер телефона 3"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p>Номер домашнего телефона</p></body></html>"))
        self.label_11.setText(_translate("MainWindow", "телефонный номер 1"))
        item = self.table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "название"))
        item = self.table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "фамилия"))
        item = self.table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "телефонный номер 1"))
        item = self.table.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "телефонный номер 2"))
        item = self.table.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "телефонный номер 3"))
        item = self.table.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Номер домашнего телефона 1"))
        item = self.table.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Номер домашнего телефона 2"))
        item = self.table.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Номер рабочего места"))
        item = self.table.horizontalHeaderItem(8)
        item.setText(_translate("MainWindow", "текст 8"))
        item = self.table.horizontalHeaderItem(9)
        item.setText(_translate("MainWindow", "текст 9"))
        item = self.table.horizontalHeaderItem(10)
        item.setText(_translate("MainWindow", "текст 10"))
        item = self.table.horizontalHeaderItem(11)
        item.setText(_translate("MainWindow", "текст 11"))
        item = self.table.horizontalHeaderItem(12)
        item.setText(_translate("MainWindow", "текст 12"))
        item = self.table.horizontalHeaderItem(13)
        item.setText(_translate("MainWindow", "текст 13"))

        self.label_7.setText(_translate("MainWindow", "Номер домашнего телефона 2"))
        self.label_6.setText(_translate("MainWindow", "Номер рабочего места"))
        self.label_5.setText(_translate("MainWindow", "факс"))
        self.messager.setItemText(0, _translate("MainWindow", "«Эта»"))
        self.messager.setItemText(1, _translate("MainWindow", "«Соруш»"))
        self.messager.setItemText(2, _translate("MainWindow", "«WhatsApp»"))
        self.messager.setItemText(3, _translate("MainWindow", "«Telegram»"))
        self.messager.setItemText(4, _translate("MainWindow", "«Другие мессенджеры»"))
        self.label_2.setText(_translate("MainWindow", "Эл. адрес"))
        self.remove.setText(_translate("MainWindow", "Цель"))
        self.search.setText(_translate("MainWindow", "Поиск"))
        self.label_4.setText(_translate("MainWindow", "Домашний адрес"))
        self.workpath_text.setText(_translate("MainWindow", "рабочий адрес"))
        self.label.setText(_translate("MainWindow", "виртуальный номер телефона"))
        self.label_3.setText(_translate("MainWindow", "интернет сайт"))
        self.export_2.setText(_translate("MainWindow", "Вывод в Excel"))
        self.add.setText(_translate("MainWindow", "Добавлять"))
        self.all_messager_types = ['«Эта»', '«Соруш»', '«WhatsApp»', '«Telegram»', '«Другие мессенджеры»']
