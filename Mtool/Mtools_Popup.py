import bpy
from PySide2 import QtWidgets

# ------------------
#   Open Window
# ------------------

class Open_Mtools_Popup(bpy.types.Operator):
    '''Open Mtools popup '''

    bl_idname = "mtools.open_mtools_popup"
    bl_label = "M Tools"
    bl_options = {'REGISTER'}

    def execute(self, context):
        self.app = QtWidgets.QApplication.instance()
        if not self.app:
            self.app = QtWidgets.QApplication(['blender'])
        #self.app.exec_()
        self.widget = Main_Window()

        return {'FINISHED'}

#-------------
# Main Window
#-------------
class Main_Window(QtWidgets):

    def __init__(self, ui_file, parent=None):
        super(Main_Window, self).__init__(parent)
        # ui = Ui_Form()

        '''
        ui_file = QtWidgets.QFile(ui_file)
        ui_file.open(QtWidgets.QFile.ReadOnly)

        loader = QtWidgets.QUiLoader()
        self.window = loader.load(ui_file)
        ui_file.close()
        script_file = os.path.realpath(__file__)
        directory = os.path.dirname(script_file)
        path = directory + r"\stylesheet\ConsoleStyle.qss"
        s_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), path)
        with open(s_path, 'r') as f:
            self.window.setStyleSheet(f.read())
        '''


        # ---------------------------------------
        # SET BUTTONS
        # ---------------------------------------

        # CleanMat_all ----
        button = self.window.findChild(QtWidgets.QPushButton, "IteMatBtn_all")
        #button.clicked.connect(IteMat)

        # CleanMat_all ----
        button = self.window.findChild(QtWidgets.QPushButton, "RemUnMat_all")
        #button.clicked.connect(RemUn)

        # CleanMat_all ----
        button = self.window.findChild(QtWidgets.QPushButton, "CleanMat_all")
        #button.clicked.connect(CleanMat)

        # CleanMat_all ----
        button = self.window.findChild(QtWidgets.QPushButton, "Suzanne")
        #button.clicked.connect(Suz)

        # self.Button3 = self.findChild(QtGui.QPushButton, 'pushButton_3')
        # widget = self.QtGui.findChild(QPushButton, "pushButton_3")
        # print(pushButton_4)
        # self.Button3.clicked.connect(self.Button3)

        self.window.show()
