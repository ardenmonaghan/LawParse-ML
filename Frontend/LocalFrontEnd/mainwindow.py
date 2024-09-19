# This Python file uses the following encoding: utf-8
import sys
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QGridLayout, QLabel
from PySide6.QtWidgets import QApplication, QMainWindow, QListWidgetItem
from PySide6.QtGui import QIcon, QPixmap, QFont
from PySide6.QtCore import Qt, QSize

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from form_ui import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Apply the stylesheet
        self.setStyleSheet(self.get_stylesheet())

        # initialize ui elements

        self.title_label = self.ui.title_label
        self.title_label.setText("LocalParse")

        self.title_icon = self.ui.title_icon
        self.title_icon.setText("")
        icon = QPixmap("../images/invert_logo.png")
        scaled_icon = icon.scaled(
            50, 50, Qt.AspectRatioMode.KeepAspectRatio, Qt.TransformationMode.SmoothTransformation)
        self.title_icon.setPixmap(scaled_icon)
        self.title_icon.setScaledContents(True)
        self.title_icon.update()  # Add this line

        self.side_menu = self.ui.listWidget

        # It means users can't select or interact with the menu using the keyboard, only with the mouse. This is often used for visual elements that don't need keyboard interaction.
        self.side_menu.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.side_menu_icon_only = self.ui.listWidget_icon_only
        self.side_menu_icon_only.setFocusPolicy(Qt.FocusPolicy.NoFocus)

        self.menu_btn = self.ui.pushButton

        self.menu_btn.setObjectName("menu_btn")
        self.menu_btn.setText("")
        self.menu_btn.setIcon(QIcon("../images/open.png"))
        self.menu_btn.setIconSize(QSize(20, 20))
        self.menu_btn.setCheckable(True)
        self.menu_btn.setChecked(False)

        self.main_content = self.ui.stackedWidget

        self.menu_list = [
            {"name": "Home", "icon": "../images/home.svg", "page": "Dashboard"},
            {"name": "Prompt Llama", "icon": "../images/gear.svg",
                "page": "Prompt_Page"},
            {"name": "Compare Versions", "icon": "../images/version_control.svg",
                "page": "Version_Control"},
        ]

        # Initializing the UI elements and slots
        self.init_list_widget()
        self.init_signal_slot()
        self.init_stackwidget()

    def get_stylesheet(self):
        return """
        QMainWindow {
            background-color: #2d2d2d;
            color: #ffffff;
        }
        
        QLabel {
            color: #ffffff;
        }

        #title_frame {
            border: none;
            background-color: #2d2d2d;
        }
        
        #title_label {
            font-size: 20px;
            font-weight: bold;
            font-family: Amazone BT, sans-serif;
        }
        
        QListWidget {
            background-color: #2d2d2d;
            border: none;
            color: #ffffff;
        }
        
        QListWidget::item {
            height: 40px;
            padding-left: 10px;
            font-family: Amazone BT, sans-serif;
        }
        
        QListWidget::item:hover {
            background-color: #454545;
            border-radius: 10px;
        }
        
        #menu_btn {
            border: none;
        }
        
        QPushButton#menu_btn:hover {
            background-color: #3a3a3a;
        }
        
        QStackedWidget {
            background-color: #1e1e1e;
        }
        
        QLabel {
            color: #ffffff;
        }
        """

    def init_signal_slot(self):
        # Connects signals and slots for menu buton and side menu
        self.menu_btn.toggled["bool"].connect(self.side_menu.setHidden)
        self.menu_btn.toggled["bool"].connect(self.title_label.setHidden)
        self.menu_btn.toggled["bool"].connect(self.title_icon.setHidden)
        self.menu_btn.toggled["bool"].connect(
            self.side_menu_icon_only.setVisible)

        # Connect signals and slots for switching between menu items
        self.side_menu.currentRowChanged["int"].connect(
            self.main_content.setCurrentIndex)
        self.side_menu_icon_only.currentRowChanged["int"].connect(
            self.main_content.setCurrentIndex)
        self.side_menu.currentRowChanged["int"].connect(
            self.side_menu_icon_only.setCurrentRow)
        self.side_menu_icon_only.currentRowChanged["int"].connect(
            self.side_menu.setCurrentRow)

        self.menu_btn.toggled.connect(self.button_icon_change)

    def button_icon_change(self, status):
        if status:
            self.menu_btn.setIcon(QIcon("../images/close.svg"))
        else:
            self.menu_btn.setIcon(QIcon("../images/open.svg"))

    def init_list_widget(self):
        # Initialize the side menu and side menu with icons only
        self.side_menu.clear()
        self.side_menu_icon_only.clear()

        for menu in self.menu_list:
            # For icon-only menu
            item = QListWidgetItem()
            icon = QIcon(menu.get("icon"))
            item.setIcon(icon)
            # Increase icon size here (e.g., to 32x32 pixels)
            item.setSizeHint(QSize(40, 40))
            self.side_menu_icon_only.addItem(item)
            # Set icon size for the whole list
            self.side_menu_icon_only.setIconSize(QSize(28, 28))

            # For menu with icons and text
            item_new = QListWidgetItem()
            item_new.setIcon(icon)
            item_new.setText(menu.get("name"))
            self.side_menu.addItem(item_new)
            # Set icon size for the whole list
            self.side_menu.setIconSize(QSize(28, 28))

        self.side_menu_icon_only.setCurrentRow(0)
        self.side_menu.setCurrentRow(0)

    def init_stackwidget(self):
        # Initialize the stack widget with content page
        widget_list = self.main_content.findChildren(QWidget)
        for widget in widget_list:
            self.main_content.removeWidget(widget)

        for menu in self.menu_list:
            text = menu.get("name")
            layout = QGridLayout()
            label = QLabel(text=text)
            label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            font = QFont()
            font.setPixelSize(40)
            label.setFont(font)
            layout.addWidget(label)

            new_page = QWidget()
            new_page.setLayout(layout)
            self.main_content.addWidget(new_page)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
