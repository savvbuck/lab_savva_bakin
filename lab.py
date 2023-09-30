import csv
import random


with open('books.csv', 'r') as csvfile:
    books = []
    search_res = []
    cnt = 0
    reader = csv.reader(csvfile, delimiter=';')
    for row in reader:
        books.append(row)
    print(f'Колличество записей: {len(books) - 1}')
    for book in books:
        if len(book[1]) > 30:
            cnt += 1
    print(f'Колличесвто книг, с названием большим, чем 30 символов: {cnt}')
    request = input('Какого автора вы хотите найти: ')
    for book in books:
        if request in (book[3] or book[4]) and ('2016' or '2017' or '2018') in book[6]:
            search_res.append(book[1])
    print(f'Книги {request} в период с 2016 по 2018: {search_res}')
with open('generator.txt', 'w') as f:
    for i in range(20):
        book_r = random.randint(1, len(books) - 1)
        f.write(f'{book_r}){books[book_r][3]}. {books[book_r][1]} - {books[book_r][6]}\n')