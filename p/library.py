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

class Book:
    def __init__(self, t):
        self.title = t
def sort():
    lst.sort()

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