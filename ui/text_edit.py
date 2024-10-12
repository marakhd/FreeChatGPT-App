from PyQt5.QtWidgets import QTextEdit, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QKeyEvent


class EnterTextEdit(QTextEdit):
    def __init__(self, parent=None, button: QPushButton=None):
        super().__init__(parent)
        self.send_button = button
    
    def keyPressEvent(self, event):
        # Проверяем, что нажата клавиша Enter
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            # Если одновременно зажат Shift, делаем перенос строки
            if event.modifiers() == Qt.ShiftModifier:
                super().keyPressEvent(event)  # Обычное поведение Enter+Shift (перенос строки)
            else:
                # Обрабатываем нажатие Enter (например, можно вызвать какой-то метод)
                self.send_button.click()
        else:
            # Обрабатываем остальные клавиши стандартным образом
            super().keyPressEvent(event)

