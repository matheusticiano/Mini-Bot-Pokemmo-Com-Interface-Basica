from PySide6.QtCore import QObject, Signal, Slot
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QMainWindow
from threading import Thread
from actions import pesca, checa_pokemon_e_contador, checa_seta


class Worker(QObject):
    finished = Signal()

    def __init__(self):
        super().__init__()

        self.is_running = True

    @Slot()
    def run(self):
        while self.is_running:
            pesca()
            checa_seta()
            checa_pokemon_e_contador()

        self.finished.emit()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.thread = None
        self.worker = None

        self.setup_ui()

    def setup_ui(self):
        self.setWindowTitle('Mini-Bot-PokeMMO')

        self.label = QLabel("Clique em Iniciar para Farmar")
        self.btn_start = QPushButton("Iniciar")
        self.btn_pause = QPushButton("Pausar")
        self.btn_stop = QPushButton("Encerrar")

        vbox = QVBoxLayout()
        hbox = QHBoxLayout()
        hbox.addWidget(self.btn_start)
        hbox.addWidget(self.btn_pause)
        hbox.addWidget(self.btn_stop)
        vbox.addWidget(self.label)
        vbox.addLayout(hbox)

        widget = QWidget()
        widget.setLayout(vbox)
        self.setCentralWidget(widget)

        self.btn_start.clicked.connect(self.start)
        self.btn_pause.clicked.connect(self.pause)
        self.btn_stop.clicked.connect(self.stop)

        self.adjustSize()
        self.setFixedSize(280, 100)

    def start(self):
        self.btn_start.setEnabled(False)
        self.btn_pause.setEnabled(True)
        self.btn_stop.setEnabled(True)

        self.label.setText("Farm em execução...")

        self.worker = Worker()
        self.thread = Thread(target=self.worker.run)
        self.thread.start()

    def pause(self):
        if self.worker.is_running:
            self.worker.is_running = False
            self.btn_pause.setText("Continuar")
            self.label.setText("Farm pausado")
        else:
            self.worker.is_running = True
            self.btn_pause.setText("Pausar")
            self.label.setText("Farm em execução...")

    def stop(self):
        self.worker.is_running = False
        self.thread.join()
        self.btn_start.setEnabled(True)
        self.btn_pause.setEnabled(False)
        self.btn_pause.setText("Pausar")
        self.btn_stop.setEnabled(False)
        self.label.setText("Clique em Iniciar para Farmar")
