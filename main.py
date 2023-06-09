import os
import sys
import shutil
from config import path_current_mods, path_available_mods
import webbrowser
from PyQt6 import uic
from PyQt6.QtWidgets import QMainWindow, QApplication, QRadioButton


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        uic.loadUi('design.ui', self)

        self.delete_actual_mods_button.clicked.connect(self.delete_actual_mods)
        self.swap_button.clicked.connect(self.swap)
        self.guide_button.clicked.connect(lambda: webbrowser.open(
            'https://github.com/101Perl/ModSwap/tree/main#how-to-use-it'))

        with os.scandir(path_available_mods) as files:
            subdir = [file.name for file in files if file.is_dir()]
        for folder in subdir:
            folder_radio_button = QRadioButton(f'{folder}')
            self.folders_list.addWidget(folder_radio_button)
            folder_radio_button.clicked.connect(lambda: self.radio_clicked())

    def delete_actual_mods(self):
        try:
            shutil.rmtree(path_current_mods)
            self.status_text.setText('Successfully deleted')
        except Exception as Error:
            self.status_text.setText('Error')

    def radio_clicked(self):
        radio_sender = self.sender()
        global radio_sender_text
        radio_sender_text = radio_sender.text()

    def swap(self):
        try:
            self.folder_name = radio_sender_text
            self.directory = f'{path_available_mods}/{self.folder_name}/'
            self.delete_actual_mods()
            self.status_text.setText('')
            shutil.copytree(self.directory, path_current_mods)
            self.status_text.setText('Successfully copied')
        except NameError:
            self.status_text.setText('Folder is not selected')


app = QApplication(sys.argv)
window = MainWindow()
window.show()

app.exec()
