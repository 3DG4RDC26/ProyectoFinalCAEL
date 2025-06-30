from PyQt5.QtWidgets import (
    QDialog, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QComboBox, QPushButton, QApplication, QWidget, QGroupBox, QSizePolicy, QMessageBox
)
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from controlers.Database import obtener_todos_usuarios, obtener_usuario
from controlers.Conexiones import crear_conexion
import matplotlib.pyplot as plt
import networkx as nx
from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg as FigureCanvas

class SetConexionGUI(QDialog):
    color1 = '#000000'  # Texto principal, bordes
    color2 = '#15284c'  # Fondo botones, encabezados tabla
    color3 = '#435ba0'  # Hover botones
    color4 = '#7f95ff'  # Fondo secciones
    color5 = '#c9d4ff'  # Fondo general

    def __init__(self):
        super().__init__()
        self.setWindowTitle('Establecer Conexion')
        self.setMinimumSize(1000, 600)
        self.setStyleSheet(f'background-color: {self.color5};')
        self.init_ui()

    def init_ui(self):
        main_layout = QHBoxLayout(self)
        left_layout = QVBoxLayout()
        left_layout.setSpacing(15)
        left_layout.setContentsMargins(30, 30, 30, 30)

        # Agrupa el formulario en un QGroupBox con borde negro
        form_group = QGroupBox()
        form_group.setStyleSheet('QGroupBox { border: 2px solid #000; border-radius: 4px; margin-top: 0.5em; background: none; }')
        form_layout = QVBoxLayout(form_group)
        form_layout.setSpacing(15)
        form_layout.setContentsMargins(15, 15, 15, 15)

        # Título
        titulo = QLabel('Establecer Conexion')
        titulo.setAlignment(Qt.AlignmentFlag.AlignCenter)
        titulo.setFont(QFont('Arial', 20, QFont.Bold))
        titulo.setStyleSheet(f'color: {self.color1}; background: none;')
        form_layout.addWidget(titulo)

        # Usuario 1
        form_layout.addWidget(QLabel('Usuario 1:'))
        label_id1 = QLabel('ID:')
        label_id1.setStyleSheet(f'color: {self.color1}; background: none;')
        form_layout.addWidget(label_id1)
        self.combo_id1 = QComboBox()
        self.combo_id1.setStyleSheet(f'background: {self.color4}; border: 1px solid {self.color2}; padding: 6px; color: {self.color1};')
        form_layout.addWidget(self.combo_id1)
        self.combo_id1.currentIndexChanged.connect(self.on_id1_selected)

        label_nombre1 = QLabel('Nombre:')
        label_nombre1.setStyleSheet(f'color: {self.color1}; background: none;')
        form_layout.addWidget(label_nombre1)
        self.input_nombre1 = QLineEdit()
        self.input_nombre1.setStyleSheet(f'background: {self.color4}; border: 1px solid {self.color2}; padding: 6px; color: {self.color1};')
        self.input_nombre1.setEnabled(False)
        form_layout.addWidget(self.input_nombre1)

        label_intereses1 = QLabel('Intereses')
        label_intereses1.setStyleSheet(f'color: {self.color1}; background: none;')
        form_layout.addWidget(label_intereses1)
        self.input_intereses1 = QLineEdit()
        self.input_intereses1.setStyleSheet(f'background: {self.color4}; border: 1px solid {self.color2}; padding: 6px; color: {self.color1};')
        self.input_intereses1.setEnabled(False)
        form_layout.addWidget(self.input_intereses1)

        # Espacio
        form_layout.addSpacing(20)

        # Usuario 2
        form_layout.addWidget(QLabel('Usuario 2:'))
        label_id2 = QLabel('ID:')
        label_id2.setStyleSheet(f'color: {self.color1}; background: none;')
        form_layout.addWidget(label_id2)
        self.combo_id2 = QComboBox()
        self.combo_id2.setStyleSheet(f'background: {self.color4}; border: 1px solid {self.color2}; padding: 6px; color: {self.color1};')
        form_layout.addWidget(self.combo_id2)
        self.combo_id2.currentIndexChanged.connect(self.on_id2_selected)

        label_nombre2 = QLabel('Nombre:')
        label_nombre2.setStyleSheet(f'color: {self.color1}; background: none;')
        form_layout.addWidget(label_nombre2)
        self.input_nombre2 = QLineEdit()
        self.input_nombre2.setStyleSheet(f'background: {self.color4}; border: 1px solid {self.color2}; padding: 6px; color: {self.color1};')
        self.input_nombre2.setEnabled(False)
        form_layout.addWidget(self.input_nombre2)

        label_intereses2 = QLabel('Intereses')
        label_intereses2.setStyleSheet(f'color: {self.color1}; background: none;')
        form_layout.addWidget(label_intereses2)
        self.input_intereses2 = QLineEdit()
        self.input_intereses2.setStyleSheet(f'background: {self.color4}; border: 1px solid {self.color2}; padding: 6px; color: {self.color1};')
        self.input_intereses2.setEnabled(False)
        form_layout.addWidget(self.input_intereses2)

        # Espacio flexible
        form_layout.addStretch(1)

        # QGroupBox solo para el formulario de los dos usuarios
        form_group.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        main_layout.addWidget(form_group, 1)

        # Peso y botón dentro del QGroupBox, al final del formulario
        label_peso = QLabel('Peso:')
        label_peso.setStyleSheet(f'color: {self.color1}; background: none;')
        form_layout.addWidget(label_peso)
        self.input_peso = QLineEdit()
        self.input_peso.setText('1')
        self.input_peso.setStyleSheet(f'background: {self.color4}; border: 1px solid {self.color2}; padding: 6px; color: {self.color1};')
        self.input_peso.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        form_layout.addWidget(self.input_peso)
        self.btn_establecer = QPushButton('Establecer conexion')
        self.btn_establecer.setStyleSheet('background: #c97c7c; color: #111; border-radius: 16px; padding: 8px 20px; font-weight: bold;')
        self.btn_establecer.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.btn_establecer.clicked.connect(self.establecer_conexion)
        form_layout.addWidget(self.btn_establecer, alignment=Qt.AlignmentFlag.AlignHCenter)

        # Visualización de grafo
        self.graph_widget = QWidget()
        self.graph_widget.setMinimumSize(500, 500)
        self.graph_widget.setStyleSheet('background: #d3d3d3;')
        self.graph_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.figure, self.ax = plt.subplots()
        self.canvas = FigureCanvas(self.figure)
        self.canvas.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        graph_layout = QVBoxLayout(self.graph_widget)
        graph_layout.addWidget(self.canvas)
        main_layout.addWidget(self.graph_widget, 2)

        self.cargar_ids()
        self.redibujar_grafo()

    def cargar_ids(self):
        self.combo_id1.blockSignals(True)
        self.combo_id2.blockSignals(True)
        self.combo_id1.clear()
        self.combo_id2.clear()
        usuarios = obtener_todos_usuarios()
        self.id_map = {}
        for usuario in usuarios:
            id_str = str(usuario.get('id', ''))
            self.combo_id1.addItem(id_str)
            self.combo_id2.addItem(id_str)
            self.id_map[id_str] = usuario
        self.combo_id1.setCurrentIndex(-1)
        self.combo_id2.setCurrentIndex(-1)
        self.combo_id1.blockSignals(False)
        self.combo_id2.blockSignals(False)

    def on_id1_selected(self, idx):
        id1 = self.combo_id1.currentText()
        usuario = self.id_map.get(id1)
        if usuario:
            self.input_nombre1.setText(usuario.get('nombre', ''))
            self.input_intereses1.setText(','.join(usuario.get('intereses', [])))
        else:
            self.input_nombre1.setText("")
            self.input_intereses1.setText("")
        # Deshabilitar el id seleccionado en el otro combo
        self.actualizar_combo2()
        self.redibujar_grafo()

    def on_id2_selected(self, idx):
        id2 = self.combo_id2.currentText()
        usuario = self.id_map.get(id2)
        if usuario:
            self.input_nombre2.setText(usuario.get('nombre', ''))
            self.input_intereses2.setText(','.join(usuario.get('intereses', [])))
        else:
            self.input_nombre2.setText("")
            self.input_intereses2.setText("")
        # Deshabilitar el id seleccionado en el otro combo
        self.actualizar_combo1()
        self.redibujar_grafo()

    def actualizar_combo2(self):
        id1 = self.combo_id1.currentText()
        current_id2 = self.combo_id2.currentText()
        self.combo_id2.blockSignals(True)
        self.combo_id2.clear()
        for id_str in self.id_map:
            if id_str != id1:
                self.combo_id2.addItem(id_str)
        # Restaura selección si es válida
        idx = self.combo_id2.findText(current_id2)
        self.combo_id2.setCurrentIndex(idx if idx >= 0 else -1)
        self.combo_id2.blockSignals(False)

    def actualizar_combo1(self):
        id2 = self.combo_id2.currentText()
        current_id1 = self.combo_id1.currentText()
        self.combo_id1.blockSignals(True)
        self.combo_id1.clear()
        for id_str in self.id_map:
            if id_str != id2:
                self.combo_id1.addItem(id_str)
        idx = self.combo_id1.findText(current_id1)
        self.combo_id1.setCurrentIndex(idx if idx >= 0 else -1)
        self.combo_id1.blockSignals(False)

    def redibujar_grafo(self):
        self.figure.clear()
        G = nx.Graph()
        id1 = self.combo_id1.currentText()
        id2 = self.combo_id2.currentText()
        if id1 and id2 and id1 != id2:
            G.add_node(id1)
            G.add_node(id2)
            G.add_edge(id1, id2)
        elif id1:
            G.add_node(id1)
        elif id2:
            G.add_node(id2)
        pos = nx.spring_layout(G)
        nx.draw(G, pos, ax=self.figure.add_subplot(111), with_labels=True, node_color='black', font_color='white', node_size=1200)
        self.canvas.draw()

    def establecer_conexion(self):
        id1 = self.combo_id1.currentText()
        id2 = self.combo_id2.currentText()
        peso = self.input_peso.text()
        res = crear_conexion(id1, id2, peso)
        if res['ok']:
            QMessageBox.information(self, 'Éxito', 'Conexión creada correctamente')
            self.accept()
        else:
            QMessageBox.warning(self, 'Error', res['error'])

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    window = SetConexionGUI()
    window.show()
    sys.exit(app.exec_())
