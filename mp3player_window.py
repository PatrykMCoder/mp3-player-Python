from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QFileDialog, QMessageBox
import threading
from os import walk
import time

class Ui_MainWindow(QMainWindow):

    def __init__(self):
        super(Ui_MainWindow, self).__init__()
        self.selected_file = None
        self.play = False
        self.button_text = 'Play'
        self.title = 'Title'
        self.mixer = None
        self.path_to_folder = None
        self.from_folder = None

    def setup_ui(self, main_window):
        main_window.setObjectName("MainWindow")
        main_window.resize(660, 411)
        main_window.setFixedSize(660, 411)

        self.central_widget = QtWidgets.QWidget(main_window)
        self.central_widget.setObjectName("centralwidget")
        self.label_title = QtWidgets.QLabel(self.central_widget)
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

        self.push_button_previous = QtWidgets.QPushButton(self.central_widget)
        self.push_button_previous.setGeometry(QtCore.QRect(70, 330, 113, 32))
        self.push_button_previous.setObjectName("pushButton_previous")

        self.push_button_play = QtWidgets.QPushButton(self.central_widget)
        self.push_button_play.setGeometry(QtCore.QRect(250, 330, 113, 32))
        self.push_button_play.setObjectName("pushButton_play")
        self.push_button_play.setText(self.button_text)
        self.push_button_play.clicked.connect(lambda: self.change_state_player(self.play))

        self.push_button_next = QtWidgets.QPushButton(self.central_widget)
        self.push_button_next.setGeometry(QtCore.QRect(460, 330, 113, 32))
        self.push_button_next.setObjectName("pushButton_next")

        self.progress_bar_time = QtWidgets.QProgressBar(self.central_widget)
        self.progress_bar_time.setGeometry(QtCore.QRect(77, 290, 491, 23))
        self.progress_bar_time.setProperty("value", 24)
        self.progress_bar_time.setObjectName("progressBar_time")

        self.label_current_time = QtWidgets.QLabel(self.central_widget)
        self.label_current_time.setGeometry(QtCore.QRect(0, 290, 59, 16))
        self.label_current_time.setAlignment(QtCore.Qt.AlignCenter)
        self.label_current_time.setObjectName("label_current_time")

        self.label_full_time = QtWidgets.QLabel(self.central_widget)
        self.label_full_time.setGeometry(QtCore.QRect(590, 290, 59, 16))
        self.label_full_time.setAlignment(QtCore.Qt.AlignCenter)
        self.label_full_time.setObjectName("label_full_time")

        self.label_album = QtWidgets.QLabel(self.central_widget)
        self.label_album.setGeometry(QtCore.QRect(210, 40, 211, 121))
        self.label_album.setObjectName("label_album")
        self.label_album.setPixmap(QtGui.QPixmap('src/album_icon.png'))
        self.label_album.setScaledContents(True)

        main_window.setCentralWidget(self.central_widget)

        self.menu_bar = QtWidgets.QMenuBar(main_window)
        self.menu_bar.setGeometry(QtCore.QRect(0, 0, 660, 22))
        self.menu_bar.setObjectName("menubar")

        self.menu_file = QtWidgets.QMenu(self.menu_bar)
        self.menu_file.setObjectName("menuFile")
        self.menu_play = QtWidgets.QMenu(self.menu_bar)
        self.menu_play.setObjectName("menuPlay")

        main_window.setMenuBar(self.menu_bar)
        self.status_bar = QtWidgets.QStatusBar(main_window)
        self.status_bar.setObjectName("statusbar")

        main_window.setStatusBar(self.status_bar)

        self.action_open_file = QtWidgets.QAction(main_window)
        self.action_open_file.setObjectName("action_open_file")
        self.action_open_file.triggered.connect(self.open_file)

        self.action_open_folder = QtWidgets.QAction(main_window)
        self.action_open_folder.setObjectName("action_open_folder")
        self.action_open_folder.triggered.connect(self.open_folder)

        self.action_start = QtWidgets.QAction(main_window)
        self.action_start.setObjectName("action_start")

        self.action_stop = QtWidgets.QAction(main_window)
        self.action_stop.setObjectName("action_stop")

        self.action_next = QtWidgets.QAction(main_window)
        self.action_next.setObjectName("action_next")

        self.action_previous = QtWidgets.QAction(main_window)
        self.action_previous.setObjectName("action_previous")

        self.action_shuffle = QtWidgets.QAction(main_window)
        self.action_shuffle.setObjectName("action_shuffle_2")

        self.action_repeat = QtWidgets.QAction(main_window)
        self.action_repeat.setObjectName("action_repeat_2")

        self.menu_file.addAction(self.action_open_file)
        self.menu_file.addAction(self.action_open_folder)
        self.menu_play.addAction(self.action_start)
        self.menu_play.addAction(self.action_stop)
        self.menu_play.addAction(self.action_next)
        self.menu_play.addAction(self.action_previous)
        self.menu_play.addAction(self.action_shuffle)
        self.menu_play.addAction(self.action_repeat)
        self.menu_bar.addAction(self.menu_file.menuAction())
        self.menu_bar.addAction(self.menu_play.menuAction())

        self.retranslate_ui(main_window)
        self.update_ui(self.button_text, self.title)

        QtCore.QMetaObject.connectSlotsByName(main_window)

    def retranslate_ui(self, main_window):
        _translate = QtCore.QCoreApplication.translate

        main_window.setWindowTitle(_translate("MainWindow", "MEDIA PLAYER"))

        self.label_title.setText(_translate("MainWindow", "Title"))

        self.push_button_previous.setText(_translate("MainWindow", "Previous"))
        self.push_button_play.setText(_translate("MainWindow", "Play"))
        self.push_button_next.setText(_translate("MainWindow", "Next"))

        self.label_current_time.setText(_translate("MainWindow", "0:20"))

        self.label_full_time.setText(_translate("MainWindow", "3:20"))

        self.menu_file.setTitle(_translate("MainWindow", "File"))

        self.menu_play.setTitle(_translate("MainWindow", "Play"))

        self.action_open_file.setText(_translate("MainWindow", "Open file"))
        self.action_open_file.setShortcut(_translate("MainWindow", "Meta+O"))

        self.action_open_folder.setText(_translate("MainWindow", "Open folder"))

        self.action_start.setText(_translate("MainWindow", "Start"))
        self.action_start.setShortcut(_translate("MainWindow", "Meta+S"))

        self.action_stop.setText(_translate("MainWindow", "Pause"))
        self.action_stop.setShortcut(_translate("MainWindow", "Meta+P"))

        self.action_next.setText(_translate("MainWindow", "Next"))
        self.action_next.setShortcut(_translate("MainWindow", "Alt+Right"))

        self.action_previous.setText(_translate("MainWindow", "Previous"))
        self.action_previous.setShortcut(_translate("MainWindow", "Alt+Left"))

        self.action_repeat.setText(_translate("MainWindow", "Repeat"))
        self.action_shuffle.setText(_translate("MainWindow", "Shuffle"))

        self.action_open_folder.setText(_translate("MainWindow", "Open folder"))

    def update_ui(self, text, title):
        self.push_button_play.setText(text)
        self.label_title.setText(title)

    def open_file(self):
        file_extensions = ['wma', 'aac', 'flac', 'wav']

        dialog_file = QFileDialog()
        dialog_file.setFileMode(QFileDialog.AnyFile)
        dialog_file.show()

        if dialog_file.exec_():
            if self.selected_file is None:
                self.selected_file = dialog_file.selectedFiles()
            else:
                self.selected_file = None
                self.selected_file = dialog_file.selectedFiles()

        current_file_extension = str(self.selected_file).replace("'", "").replace("]", "").replace("-", "").split(".")[
            -1]
        if current_file_extension not in file_extensions:
            self.selected_file = None
            self.play = False

            error_dialog = QMessageBox()
            error_dialog.setText('You selected not supported')
            error_dialog.setWindowTitle('Warring!')
            error_dialog.setInformativeText('You should select file type: .mp3, .wma, .acc, .flac')
            error_dialog.setIcon(QMessageBox.Warning)
            error_dialog.exec_()
        else:
            self.play = True

        self.from_folder = False
        self.play_sound()

    def open_folder(self):
        file_extensions = ['wma', 'aac', 'flac', 'wav']
        dialog_folder = QFileDialog().getExistingDirectory(self, 'Select folder')
        files = []
        for (dirpath, dirnames, filenames) in walk(dialog_folder):
            self.path_to_folder = dirpath
            files.extend(filenames)

        for f in files:
            file_extension = str(f).replace("'", "").replace("]", "").replace("-", "").split(".")[-1]
            if file_extension not in file_extensions:
                files.remove(f)
        self.selected_file = files
        self.play = True
        self.from_folder = True
        self.play_sound()

    # HERE IS UI FREEZE WHILE IS PLAYING MUSIC. MAKE IT BETTER
    def play_sound(self):
        if self.play:
            import pygame
            pygame.init()
            # only for test use pygame. In future find or create own library for this
            for f in self.selected_file:
                if self.from_folder:
                    self.mixer = pygame.mixer.Sound(str(self.path_to_folder + "/" + f))
                else:
                    self.mixer = pygame.mixer.Sound(str(f))
                # self.title = f
                # self.button_text = "Pause"
                channel = self.mixer.play()
                # while channel.get_busy():
                #     pygame.time.wait(int(self.mixer.get_length()))
        else:
            if self.mixer is not None:
                self.mixer.stop()

        # thread_update_ui = threading.Thread(target=self.update_ui(self.button_text, self.title))
        # thread_update_ui.start()

    def change_state_player(self, current_state):
        if self.selected_file is not None:
        if self.selected_file is not None:
            if current_state is True:
                self.play = False
                self.button_text = 'Play'
            elif current_state is False:
                self.play = True
                self.button_text = 'Pause'

            self.play_sound()
        else:
            self.button_text = "Play"

        thread_update_ui = threading.Thread(target=self.update_ui(self.button_text, self.title))
        thread_update_ui.start()


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    main_window = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setup_ui(main_window)
    main_window.show()
    sys.exit(app.exec_())
