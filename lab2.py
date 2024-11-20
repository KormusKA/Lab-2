from csv import reader
import random
import xml.dom.minidom as minidom


def length_score():
        count = 0

        with open('books-en.csv', 'r') as csvfile:
            table = reader(csvfile, delimiter=';')

            for row in list(table):
                if len(row[1]) > 30:
                     count += 1

        print(f'\n Количество книг, в названии которых больше 30 символов: {count} штук')          

def book_search():
    flag = 0
    search = input('Введите автора на английском: ')
    
    with open('books-en.csv', 'r', encoding='windows-1251') as csvfile:
        table = reader(csvfile, delimiter=';')
        
        for row in table:
            lower_case = row[2].lower()
            index = lower_case.find(search.lower())

            if (index != -1) and (1997 <= int(row[3]) <= 2000):
                print(f'\n Книги {row[2]}:')
                print(f'{row[1]} была опубликована в {row[3]} году')
                flag += 1

        if flag == 0:
            print('\n Ничего не найдено.')
        else:
            print(f'\n Найдено {flag} книг, опубликованных с 1997 по 2000 года.')

def link_generator():
    output = open('library_link.txt', 'w')

    rand_numbers = []
    for i in range(20):
        rand_numbers.append(random.randint(1, 9409))
    
    with open('books-en.csv', 'r', encoding='windows-1251') as csvfile:
        table = reader(csvfile, delimiter=';')

        ind = 0
        flag =  1

        for row in table:

            if ind in rand_numbers:
                print(flag, row[1])
                output.write(f'{flag} {row[2]}. {row[1]} - {row[3]}\n')

                flag += 1
            ind += 1

    output.close()
    print('\n В файл записано 20 книг.')

def data_extraction():
    xml_file = open('currency.xml', 'r')
    xml_data = xml_file.read()

    dom = minidom.parseString(xml_data)
    dom.normalize()   

    elements = dom.getElementsByTagName('Valute')
    valute_disk = {}

    for node in elements:
        for child in node.childNodes:
            if child.nodeType == 1:
                if child.tagName == 'CharCode':
                    if child.firstChild.nodeType == 3:
                        CharCode = child.firstChild.data
                if child.tagName == 'Nominal':
                    if child.firstChild.nodeType == 3:
                        Nominal = int(child.firstChild.data)
        valute_disk[CharCode] = Nominal

    for key in valute_disk.keys():
        print(key, valute_disk[key])

    xml_file.close()

def publisher_list():
    with open('books-en.csv', 'r', encoding='windows-1251') as csvfile:
        table = reader(csvfile, delimiter=';')
        
        publishers = []

        for row in table:
            if row[4] not in publishers:
                publishers.append(row[4])
        
        print('Перечень издательств:\n')

        print(', '.join(map(str, sorted(publishers))))

        print(f'\n Всего {len(publishers)} издательств \n')

def most_popular_books():
    with open('books-en.csv', 'r', encoding='windows-1251') as csvfile:
        table = list(reader(csvfile, delimiter=';'))
        table.pop(0)

        popular = []

        for row in table:
            title = row[1]
            download = int(row[-2])

            popular.append((download, title))

        popular = sorted(popular, reverse=True)[:20]

        print('20 самых популярных книг: \n')
        for i in range(len(popular)):
            print(f'{i+1}. {popular[i][1]}')


if __name__ == "__main__":
    length_score()
    print('\n')

    book_search()
    print('\n')

    link_generator()
    print('\n')

    data_extraction()
    print('\n')

    publisher_list()

    most_popular_books()
