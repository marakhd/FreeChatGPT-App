from PyQt5.QtWidgets import QApplication, QMainWindow, QListWidgetItem, QTextBrowser, QLabel, QVBoxLayout, QSizePolicy, QWidget, QHBoxLayout,QSpacerItem
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtCore import QTimer, Qt

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
        self.ui_dir = Path(__file__).resolve().parent / 'ui'
        self.setWindowIcon(QIcon(str(self.ui_dir / 'icon.png')))


        self.result_queue = Queue()

        self.inputField.setFocus()

        self.sendButton.clicked.connect(self._response)

        self.offBtnSend.triggered.connect(self.__state_btn)

        self.clearCtx.triggered.connect(self.__clear_ctx)

        self.ctx = []

    def __create_msg(self, text: str, is_gpt: bool) -> None:
        sender_widget = QWidget()
        sender_icon_lbl = QLabel()
        sender_txt_lbl = QLabel()
        sender_layout = QHBoxLayout()
        msg = QTextBrowser()

        msg.setOpenExternalLinks(True)  # Открывать ссылки в QTextBrowser
        msg.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)  # Динамическая ширина


        layout = QVBoxLayout(sender_widget)
        layout.addLayout(sender_layout)
        layout.addWidget(msg)
        
        sender_layout.addWidget(sender_icon_lbl)
        sender_layout.addWidget(sender_txt_lbl)
        sender_layout.addItem(QSpacerItem(20, 20, QSizePolicy.Expanding, QSizePolicy.Expanding))
        
        load_icon = lambda path, size=(16, 16): (QPixmap(str(self.ui_dir / path))
        .scaled(size[0], size[1], aspectRatioMode=Qt.KeepAspectRatio, transformMode=Qt.SmoothTransformation))

        gpt_pm = load_icon('icon.png')
        user_pm = load_icon('user_icon.png')
        sender_txt_lbl.setText("ChatGPT:" if is_gpt else "Вы:")
        sender_txt_lbl.setStyleSheet("font-weight: 100; font-size: 20px;")
        sender_icon_lbl.setPixmap(gpt_pm if is_gpt else user_pm)
        msg.setMarkdown(text)

        item = QListWidgetItem(self.chatListWidget)
        item.setSizeHint(sender_widget.sizeHint())
        self.chatListWidget.addItem(item)
        self.chatListWidget.setItemWidget(item, sender_widget)
        self.chatListWidget.scrollToBottom()

    def _response(self) -> None:
        text = self.inputField.toPlainText().strip()
        self.inputField.clear()
        if text:
            self.ctx.append(f"Вы: \n{text}")
            self.__create_msg(text=text, is_gpt=False)
            Thread(target=self.__response, args=(text,)).start()
            self.__check_thread()

    def __response(self, text: str) -> None:
        text = "\n".join(self.ctx) + "\n" + text
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[{
                "role": "user",
                "content": text
            }]
        )
        res = response.choices[0].message.content
        self.ctx.append(f"ChatGPT: \n{res}")
        self.result_queue.put(res)
    
    def __check_thread(self) -> None:
        try:
            answer = self.result_queue.get_nowait()
            self.__create_msg(text=answer, is_gpt=True)
        except Empty:
            # self.textBrowser.setMarkdown("Ожидание ответа...")
            QTimer.singleShot(100, self.__check_thread)
    
    def __state_btn(self) -> None:
        self.btnWidget.setVisible(not self.offBtnSend.isChecked())

    def __clear_ctx(self) -> None:
        self.chatListWidget.clear()
        self.ctx.clear()


if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    form = App()
    form.show()
    sys.exit(app.exec_())

