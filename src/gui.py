# from PyQt6.QtGui import QColor
from PyQt6.QtCore import Qt, QTimer, QThread
from PyQt6.QtWidgets import QMainWindow, QPushButton, QVBoxLayout, QLineEdit, QWidget, QComboBox, QLabel, QFileDialog
from PyQt6.QtGui import QTextOption
import PyQt6.Qt6


class Gui(QMainWindow):

    # constructor
    def __init__(self):
        super().__init__()
        # main window settings
        self.setWindowTitle("Screen & voice recorder")
        self.setFixedSize(500, 500)

        # main content
        self.mainContentLayout = QVBoxLayout()
        self.mainContentWidget = QWidget()
        self.mainContentWidget.setLayout(self.mainContentLayout)

        # directory choice widgets
        self.directoryChoiceLayout = QVBoxLayout()

        self.directoryChoiceLabel = QLabel()
        self.directoryChoiceLabel.setText("Choose directory where your recordings will be saved:")
        self.directoryChoiceLayout.addWidget(self.directoryChoiceLabel, alignment=Qt.AlignmentFlag.AlignBottom)

        self.saveToDirectory = QLineEdit()
        self.saveToDirectory.setFixedSize(475, 25)
        self.saveToDirectory.setDisabled(True)
        self.directoryChoiceLayout.addWidget(self.saveToDirectory)

        self.chooseDirectoryButton = QPushButton()
        self.chooseDirectoryButton.setFixedSize(120, 25)
        self.chooseDirectoryButton.setText("Choose directory...")
        self.chooseDirectoryButton.clicked.connect(self.choose_directory)
        self.directoryChoiceLayout.addWidget(self.chooseDirectoryButton, alignment=Qt.AlignmentFlag.AlignTop)

        self.mainContentLayout.addLayout(self.directoryChoiceLayout)

        # screen choice widgets
        self.screenChoiceLayout = QVBoxLayout()

        self.screenChoiceLabel = QLabel()
        self.screenChoiceLabel.setText("Set screen source:")
        self.screenChoiceLayout.addWidget(self.screenChoiceLabel, alignment=Qt.AlignmentFlag.AlignBottom)

        self.chosenScreenSource = QLineEdit()
        self.chosenScreenSource.setFixedSize(475, 25)
        self.chosenScreenSource.setDisabled(True)
        self.screenChoiceLayout.addWidget(self.chosenScreenSource)

        self.screenChoiceList = QComboBox()
        self.screenChoiceList.setFixedSize(475, 25)
        self.screenChoiceLayout.addWidget(self.screenChoiceList, alignment=Qt.AlignmentFlag.AlignTop)

        self.mainContentLayout.addLayout(self.screenChoiceLayout)

        # audio choice widgets
        self.audioChoiceLayout = QVBoxLayout()

        self.audioChoiceLabel = QLabel()
        self.audioChoiceLabel.setText("Choose audio source:")
        self.audioChoiceLayout.addWidget(self.audioChoiceLabel, alignment=Qt.AlignmentFlag.AlignBottom)

        self.chosenAudioSource = QLineEdit()
        self.chosenAudioSource.setFixedSize(475, 25)
        self.chosenAudioSource.setDisabled(True)
        self.audioChoiceLayout.addWidget(self.chosenAudioSource)

        self.chooseAudioList = QComboBox()
        self.chooseAudioList.setFixedSize(475, 25)
        self.audioChoiceLayout.addWidget(self.chooseAudioList, alignment=Qt.AlignmentFlag.AlignTop)

        self.mainContentLayout.addLayout(self.audioChoiceLayout)

        # recording control buttons

        self.setCentralWidget(self.mainContentWidget)

    # directory choice dialog
    def choose_directory(self):
        chosen_directory = QFileDialog.getExistingDirectory(self, "Select directory")
        if chosen_directory:
            self.saveToDirectory.setText(chosen_directory)
