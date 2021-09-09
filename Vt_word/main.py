# Author name: Avijit Chowdhury(CUET)
from tkinter import *
import sys
import turtle
from PyQt5.QtGui import *
from PyQt5.QtPrintSupport import QPrinter

from PyQt5.QtWidgets import *


class vtword(QMainWindow):
    def __init__(self) -> object:
        super(vtword, self).__init__()
        self.editor = QTextEdit()
        self.setCentralWidget(self.editor)
        self.showMaximized()
        self.editor.setFontPointSize(20)
        self.fontsizebox = QSpinBox()
        self.createToolBar()
        self.create_menu_bar()

    def create_menu_bar(self):
        menu_bar = QMenuBar()

        file_menu = QMenu('File', self)
        menu_bar.addMenu(file_menu)

        save_as_pdf_action = QAction('save as pdf', self)
        save_as_pdf_action.triggered.connect(self.save_as_pdf)
        file_menu.addAction(save_as_pdf_action)

        edit_menu = QMenu('Edit', self)
        menu_bar.addMenu(edit_menu)

        view_menu = QMenu('View', self)
        menu_bar.addMenu(view_menu)

        self.setMenuBar(menu_bar)

    def createToolBar(self):
        toolbar = QToolBar()

        undo_action = QAction(QIcon('undo.png'), 'undo', self)
        undo_action.triggered.connect(self.editor.undo)
        toolbar.addAction(undo_action)

        redo_action = QAction(QIcon('redo.png'), 'redo', self)
        redo_action.triggered.connect(self.editor.redo)
        toolbar.addAction(redo_action)

        # for adding serpator between redo and cut
        toolbar.addSeparator()
        toolbar.addSeparator()

        cut_action = QAction(QIcon('cut.png'), 'cut', self)
        cut_action.triggered.connect(self.editor.cut)
        toolbar.addAction(cut_action)

        copy_action = QAction(QIcon('copy.png'), 'copy', self)
        copy_action.triggered.connect(self.editor.copy)
        toolbar.addAction(copy_action)

        paste_action = QAction(QIcon('paste.png'), 'paste', self)
        paste_action.triggered.connect(self.editor.paste)
        toolbar.addAction(paste_action)

        toolbar.addSeparator()
        toolbar.addSeparator()

        self.fontsizebox.setValue(20)
        self.fontsizebox.valueChanged.connect(self.set_font_size)
        #  self.fontsizebox.valueChanged().connect(self.set_font_size)
        toolbar.addWidget(self.fontsizebox)

        self.addToolBar(toolbar)

    #         self.font_size_box.setValue(20)
    #         self.font_size_box.valueChanged.connect(self.set_font_size)
    #         toolbar.addWidget(self.font_size_box)
    #
    #         self.addToolBar(toolbar)
    #
    #
    def set_font_size(self):
        value = self.fontsizebox.value()
        self.editor.setFontPointSize(value)

    def save_as_pdf(self):
        file_path, _ = QFileDialog.getSaveFileName(self, 'Export PDF', None, 'PDF Files (*.pdf)')
        printer = QPrinter(QPrinter.HighResolution)
        printer.setOutputFormat(QPrinter.PdfFormat)
        printer.setOutputFileName(file_path)
        self.editor.document().print_(printer)






app = QApplication(sys.argv)
window = vtword()
window.show()
window.backgroundRole()
sys.exit(app.exec_())

# gui = Tk(className='Python Examples - Window Color')
# set window size
