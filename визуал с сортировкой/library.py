"""class Book:
    title = 'Python OOP'
    author = 'Суворов'
    pages = 125
    year = 2021

    def set_title(self, title):
        self.title = title


titles = ['Репка', 'Морозко', 'Колобок']
books = [Book() for i in range(3)]
for i in range(len(titles)):
    books[i].set_title(titles[i])
# book.set_title('31ИС-21')
for b in books:
    print(b.title)

#Задание 1.
В текстовом файле 'books.txt' с новой строки хранятся названия книг.
Создать список книг из этих названий.
Отсортировать его по алфавиту с использованием sorted и key
Выгрузить отсортированный список в файл 'sorted_books.txt'
Отправить в ЭлЖур не поздней 9.55
"""
import sys

from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout,QMainWindow
class Book:
    def __init__(self, t):
        self.title = t
"""
    Добавил визуал - при нажатии на кнопки в файл sorted_books.txt будут добавлены названия книг,
    отсортированые в зависимости от нажатой кнопки
"""


class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()

        self.setWindowTitle("Сортировщик")
        self.setMaximumSize(100, 100)

        self.btn_sort = QPushButton("По алфавиту")
        self.btn_sort_revercec = QPushButton("Обратный алф порядок")
        self.btn_save = QPushButton("Сохранить")
        self.btn_save.clicked.connect(alfabet)
        self.btn_sort.clicked.connect(sort)
        self.btn_sort_revercec.clicked.connect(sort_rev)

        self.layout_all = QVBoxLayout()
        self.layout_all.addWidget(self.btn_sort)
        self.layout_all.addWidget(self.btn_sort_revercec)
        self.layout_all.addWidget(self.btn_save)

        self.widget = QWidget()
        self.widget.setLayout(self.layout_all)
        self.setCentralWidget(self.widget)



def sort():
    lst.sort()

def sort_rev():
    lst.sort(reverse=True)

f = open("books.txt", 'r', encoding='utf8')
lst = []
for line in f:
    lst.append(line)


f.close()

books = [Book for i in range(len(lst))]
for i in range(len(lst)):
    books[i] = Book(lst[i])

lst.sort(key=sort())

for b in books:
    print(b.title)

f_out = open("sorted_books.txt", 'w', encoding='utf8')
for i in lst:
    f_out.write(i)

f_out.close()

def alfabet():
    f_out = open("sorted_books.txt", 'w', encoding='utf8')
    for i in lst:
        f_out.write(i)
    window.close()

app = QApplication(sys.argv)

window =MainWindow()
window.show()

app.exec()