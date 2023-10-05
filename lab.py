import csv
import random


books = []
search_res = []
cnt = 0
max_len = 30
with open('books.csv', 'r', encoding='windows-1251') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    for row in reader:
        books.append(row)
    print(f'Колличество записей: {len(books) - 1}')
    for book in books:
        name = book[1]
        if len(name) > max_len:
            cnt += 1
    print(f'Колличесвто книг, с названием большим, чем 30 символов: {cnt}')
    request = input('Какого автора вы хотите найти: ')
    for book in books:
        name = book[1]
        author_name = book[3]
        author_fulname = book[4]
        date = book[6]
        print(author_name)
        if ((request in author_name) or (request in author_fulname)) and (('2016' in date) or ('2017' in date) or ('2018' in date)):
            search_res.append(name)  
    print(f'Книги {request} в период с 2016 по 2018: {search_res}')
with open('generator.txt', 'w', encoding='windows-1251') as f:
    for i in range(20):
        book_random_number = random.randint(1, len(books) - 1)
        author_name = books[book_random_number][3]
        name = books[book_random_number][1]
        date = books[book_random_number][6]
        f.write(f'{book_random_number}){author_name}. {name} - {date}\n')