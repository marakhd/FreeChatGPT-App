from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QKeyEvent


class EnterTextEdit(QTextEdit):
    def keyPressEvent(self, event):
        # Проверяем, что нажата клавиша Enter
        if event.key() == Qt.Key_Return or event.key() == Qt.Key_Enter:
            # Если одновременно зажат Shift, делаем перенос строки
            if event.modifiers() == Qt.ShiftModifier:
                super().keyPressEvent(event)  # Обычное поведение Enter+Shift (перенос строки)
            else:
                # Обрабатываем нажатие Enter (например, можно вызвать какой-то метод)
                self.on_enter_pressed() if self.on_enter_pressed else ...
        else:
            # Обрабатываем остальные клавиши стандартным образом
            super().keyPressEvent(event)
            
    def register_hendler(self, handler):
        self.on_enter_pressed = handler

