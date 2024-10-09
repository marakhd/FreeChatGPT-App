from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt

from g4f.client import Client
from pathlib import Path

from ui.ui import Ui_MainWindow

client = Client()

class App(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(App, self).__init__()
        self.setupUi(self)
        self.setFixedSize(self.size())
        self.setWindowTitle("ChatGPT")
        self.setWindowIcon(QIcon(str(Path(__file__).resolve().parent / 'ui' / 'icon.png')))

        self.inputField.setFocus()
        self.inputField.register_hendler(self._response)

        self.sendButton.clicked.connect(self._response)

        self.action_2.triggered.connect(self.__state_btn)
    
    def _response(self) -> None:
        text = self.inputField.toPlainText()
        self.inputField.clear()
        self.textBrowser.append(self.__response(text))

    @staticmethod
    def __response(text: str) -> str:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{
                "role": "user",
                "content": text
            }]
        )
        return response.choices[0].message.content
            
    def __state_btn(self) -> None:
        self.sendButton.setVisible(not self.action_2.isChecked())


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    form = App()
    form.show()
    sys.exit(app.exec_())

