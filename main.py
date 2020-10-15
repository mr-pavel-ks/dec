from datetime import datetime

def decorator(dir):
    def decorator_2(func):
        def my_def(*args, **kwargs):
            start = datetime.now(tz=None)
            result = func(*args, **kwargs)
            with open(dir, 'a') as f:
                f.write(f'Start function: {start}\nName function: {func.__name__}\nArg function: {args,kwargs} \nReturn: {result}\n')
            return result
        return my_def
    return decorator_2




documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': []
}

@decorator('Dir_log/log.txt')
def people():
    number_doc = input('Введите номер документа:')
    for doc in documents:
        if doc['number'] == number_doc:
            print(doc['name'])
            return
    if doc['number'] != number_doc:
        print('Неверно указан номер документа')

@decorator('Dir_log/log.txt')
def shelf():
    number_doc = input('Введите номер документа: ')
    for num_shelfs, num_doc_shelfs in directories.items():
        for num in num_doc_shelfs:
            if num == number_doc:
                print(f'Документ находится на {num_shelfs} полке')
                return
    if num != number_doc:
        print('Не найден документ с указанным номером')

@decorator('Dir_log/log.txt')
def my_list():
    for doc in documents:
        print(f'{doc["type"]} "{doc["number"]}" "{doc["name"]}"')

@decorator('Dir_log/log.txt')
def add():
    new_type = input('Введите тип документа: ')
    new_number = int(input('Введите номер документа: '))
    new_name = input('Введите имя владельца документа: ')
    flag = True
    x = {}
    x["type"] = new_type
    x["number"] = new_number
    x["name"] = new_name
    documents.append(x)
    print(documents)

    while flag:
        new_shelf = input('Введите номер полки: ')
        for key, valye in directories.items():
            if new_shelf == key:
                valye.append(new_number)
                flag = False
        print(directories)


command = input('Введите необходимую команду: ')
if command == 'p':
    people()
if command == 's':
    shelf()
if command == 'l':
    my_list()
if command == 'a':
    add()





