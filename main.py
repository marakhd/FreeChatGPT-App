from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QTimer

from g4f.client import Client
from pathlib import Path
from threading import Thread
from queue import Queue, Empty

from ui.ui import Ui_MainWindow

client = Client()

class App(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(App, self).__init__()
        self.setupUi(self)
        self.setFixedSize(self.size())
        self.setWindowTitle("ChatGPT")
        self.setWindowIcon(QIcon(str(Path(__file__).resolve().parent / 'ui' / 'icon.png')))

        self.result_queue = Queue()

        self.inputField.setFocus()
        self.inputField.register_hendler(self._response)

        self.sendButton.clicked.connect(self._response)

        self.action_2.triggered.connect(self.__state_btn)
    
    def _response(self) -> None:
        text = self.inputField.toPlainText()
        self.inputField.clear()
        
        Thread(target=self.__response, args=(text,)).start()
        self.__check_thread()

    def __response(self, text: str) -> str:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{
                "role": "user",
                "content": text
            }]
        )
        res = response.choices[0].message.content
        self.result_queue.put(res)
    
    def __check_thread(self) -> None:
        try:
            answer = self.result_queue.get_nowait()
            self.textBrowser.setMarkdown(answer)
        except Empty:
            self.textBrowser.setMarkdown("Ожидание ответа...")
            QTimer.singleShot(100, self.__check_thread)
    
    def __state_btn(self) -> None:
        self.sendButton.setVisible(not self.action_2.isChecked())


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    form = App()
    form.show()
    sys.exit(app.exec_())

