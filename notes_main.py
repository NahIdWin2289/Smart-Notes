from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QVBoxLayout, QHBoxLayout, QListWidget, QTextEdit, QLineEdit, QInputDialog
import json

def show_note():
    name = list_notes.selectedItems()[0].text()
    big_text_pole.setText(notes[name]['текст'])
    list_tegs.clear()
    list_tegs.addItems(notes[name]['теги'])

def add_note():
    note_name, ok = QInputDialog.getText(main_win, 'Добавить заметку', 'Название заметки:')
    if ok and note_name != '':
        notes[note_name] = {'текст' : '', 'теги' : []}
        list_notes.addItem(note_name)

def del_note():
    if list_notes.selectedItems():
        name = list_notes.selectedItems()[0].text()
        del notes[name]
        list_notes.clear()
        list_notes.addItems(notes)
        big_text_pole.clear()
        list_tegs.clear()

def save_note():
    if list_notes.selectedItems():
        name = list_notes.selectedItems()[0].text()
        text_name = big_text_pole.toPlainText()
        notes[name]['текст'] = text_name

def add_teg():
    if list_notes.selectedItems():
        name = list_notes.selectedItems()[0].text()
        text_name = small_list.text()
        if text_name != '' and text_name not in notes[name]['теги']:
            notes[name]['теги'].append(text_name)
            list_tegs.addItem(text_name)
            small_list.clear()

def del_teg():
    if list_tegs.selectedItems():
        name = list_notes.selectedItems()[0].text()
        teg_name = list_tegs.selectedItems()[0].text()
        notes[name]['теги'].remove(teg_name)
        list_tegs.clear()
        list_tegs.addItems(notes[name]['теги'])

def search_teg():
    teg = small_list.text()
    if button_seek.text() == 'Искать заметки по тегу' and teg:
        notes_filtered = {} 
        for i in notes:
            if teg in notes[i]['теги']:
                notes_filtered[i] = notes[i]
        button_seek.setText('Сбросить поиск')
        list_tegs.clear()
        list_notes.clear()
        list_notes.addItems(notes_filtered)
    elif button_seek.text() == 'Сбросить поиск':
        small_list.clear()
        list_tegs.clear()
        list_notes.clear()
        list_notes.addItems(notes)
        button_seek.setText('Искать заметки по тегу')
with open('nots.json', 'r', encoding = 'UTF-8') as file:
    notes = json.load(file)

app = QApplication([])
main_win = QWidget()
main_win.setWindowTitle('Умные заметки')
main_win.resize(900, 600)


big_text_pole = QTextEdit()
label_spisok = QLabel('Список заметок') 
list_notes = QListWidget()
button_create = QPushButton('Создать заметку')
button_delete = QPushButton('Удалить заметку')
button_save = QPushButton('Сохранить заметку')
label_tegs = QLabel('Список тегов')
list_tegs = QListWidget()
small_list = QLineEdit()
small_list.setPlaceholderText('Введите тег')
button_set_teg = QPushButton('Добавить к заметке')
button_delteg = QPushButton('Открепить от заметки')
button_seek = QPushButton('Искать заметки по тегу')


small_hbox1 = QHBoxLayout()
small_hbox2 = QHBoxLayout()
right_vbox = QVBoxLayout()
big_hbox = QHBoxLayout()


small_hbox1.addWidget(button_create)
small_hbox1.addWidget(button_delete)
small_hbox2.addWidget(button_set_teg)
small_hbox2.addWidget(button_delteg)
right_vbox.addWidget(label_spisok)
right_vbox.addWidget(list_notes)
right_vbox.addLayout(small_hbox1)
right_vbox.addWidget(button_save)
right_vbox.addWidget(label_tegs)
right_vbox.addWidget(list_tegs)
right_vbox.addWidget(small_list)
right_vbox.addLayout(small_hbox2)
right_vbox.addWidget(button_seek)
big_hbox.addWidget(big_text_pole)
big_hbox.addLayout(right_vbox)

list_notes.addItems(notes)

list_notes.itemClicked.connect(show_note)
button_create.clicked.connect(add_note)
button_delete.clicked.connect(del_note)
button_save.clicked.connect(save_note)
button_set_teg.clicked.connect(add_teg)
button_delteg.clicked.connect(del_teg)
button_seek.clicked.connect(search_teg)
main_win.setLayout(big_hbox)
main_win.show()
app.exec()

with open('nots.json', 'w', encoding = 'UTF-8') as file:
     json.dump(notes, file)