from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QMessageBox

class Ui_MainWindow(QMainWindow):
    
    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.selected_file = None
        self.play = False

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(660, 411)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_title = QtWidgets.QLabel(self.centralwidget)
        self.label_title.setGeometry(QtCore.QRect(130, 200, 371, 91))
        
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        font.setStrikeOut(False)
        font.setKerning(False)

        self.label_title.setFont(font)
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setObjectName("label_title")

        self.pushButton_previous = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_previous.setGeometry(QtCore.QRect(70, 330, 113, 32))
        self.pushButton_previous.setObjectName("pushButton_previous")

        self.pushButton_play = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_play.setGeometry(QtCore.QRect(250, 330, 113, 32))
        self.pushButton_play.setObjectName("pushButton_play")

        self.pushButton_next = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_next.setGeometry(QtCore.QRect(460, 330, 113, 32))
        self.pushButton_next.setObjectName("pushButton_next")

        self.progressBar_time = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_time.setGeometry(QtCore.QRect(77, 290, 491, 23))
        self.progressBar_time.setProperty("value", 24)
        self.progressBar_time.setObjectName("progressBar_time")

        self.label_current_time = QtWidgets.QLabel(self.centralwidget)
        self.label_current_time.setGeometry(QtCore.QRect(0, 290, 59, 16))
        self.label_current_time.setAlignment(QtCore.Qt.AlignCenter)
        self.label_current_time.setObjectName("label_current_time")

        self.label_full_time = QtWidgets.QLabel(self.centralwidget)
        self.label_full_time.setGeometry(QtCore.QRect(590, 290, 59, 16))
        self.label_full_time.setAlignment(QtCore.Qt.AlignCenter)
        self.label_full_time.setObjectName("label_full_time")

        self.label_album = QtWidgets.QLabel(self.centralwidget)
        self.label_album.setGeometry(QtCore.QRect(210, 40, 211, 121))
        self.label_album.setObjectName("label_album")
        self.label_album.setPixmap(QtGui.QPixmap('src/album_icon.png'))
        self.label_album.setScaledContents(True)

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 660, 22))
        self.menubar.setObjectName("menubar")

        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuPlay = QtWidgets.QMenu(self.menubar)
        self.menuPlay.setObjectName("menuPlay")

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        MainWindow.setStatusBar(self.statusbar)

        self.action_open_file = QtWidgets.QAction(MainWindow)
        self.action_open_file.setObjectName("action_open_file")
        self.action_open_file.triggered.connect(self.open_file)

        self.action_start = QtWidgets.QAction(MainWindow)
        self.action_start.setObjectName("action_start")

        self.action_stop = QtWidgets.QAction(MainWindow)
        self.action_stop.setObjectName("action_stop")

        self.action_next = QtWidgets.QAction(MainWindow)
        self.action_next.setObjectName("action_next")

        self.action_previous = QtWidgets.QAction(MainWindow)
        self.action_previous.setObjectName("action_previous")

        self.menuFile.addAction(self.action_open_file)
        self.menuPlay.addAction(self.action_start)
        self.menuPlay.addAction(self.action_stop)
        self.menuPlay.addAction(self.action_next)
        self.menuPlay.addAction(self.action_previous)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuPlay.menuAction())

        self.retranslateUi(MainWindow)
        
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate

        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))

        self.label_title.setText(_translate("MainWindow", "Title"))

        self.pushButton_previous.setText(_translate("MainWindow", "Previous"))
        self.pushButton_play.setText(_translate("MainWindow", "Play"))
        self.pushButton_next.setText(_translate("MainWindow", "Next"))

        self.label_current_time.setText(_translate("MainWindow", "0:20"))

        self.label_full_time.setText(_translate("MainWindow", "3:20"))

        self.menuFile.setTitle(_translate("MainWindow", "File"))

        self.menuPlay.setTitle(_translate("MainWindow", "Play"))

        self.action_open_file.setText(_translate("MainWindow", "Open file"))
        self.action_open_file.setShortcut(_translate("MainWindow", "Meta+O"))

        self.action_start.setText(_translate("MainWindow", "Start"))
        self.action_start.setShortcut(_translate("MainWindow", "Meta+S"))

        self.action_stop.setText(_translate("MainWindow", "Pause"))
        self.action_stop.setShortcut(_translate("MainWindow", "Meta+P"))

        self.action_next.setText(_translate("MainWindow", "Next"))
        self.action_next.setShortcut(_translate("MainWindow", "Alt+Right"))

        self.action_previous.setText(_translate("MainWindow", "Previous"))
        self.action_previous.setShortcut(_translate("MainWindow", "Alt+Left"))

    def open_file(self):
        
        file_extensions = ['mp3', 'wma', 'aac', 'flac', 'wav']
        current_file_extension = None

        dialog_file = QFileDialog(self)
        dialog_file.setFileMode(QFileDialog.AnyFile)
        dialog_file.show()


        if dialog_file.exec_():
            if self.selected_file == None:
                self.selected_file = dialog_file.selectedFiles()
            else:
                self.selected_file = None
                self.selected_file = dialog_file.selectedFiles()
            
        current_file_extension = str(self.selected_file).replace("'", "").replace("]", "").replace("-", "").split(".")[-1]
        if not current_file_extension in file_extensions:
            self.selected_file = None
            self.play = False

            error_dialog = QMessageBox()
            error_dialog.setText('You do not selected music file')
            error_dialog.setWindowTitle('Warring!')
            error_dialog.setInformativeText('You should select file type: .mp3, .wma, .acc, .flac')
            error_dialog.setIcon(QMessageBox.Warning)
            error_dialog.exec_()
        else:
            self.play = True
        
        self.play_sound()

    def play_sound(self):
        if self.play:
            # only for test use pygame. In future find or create own library for this
            import pygame
            pygame.init()
            pygame.mixer.Sound(str(self.selected_file[0])).play()
        else:
            pass
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
