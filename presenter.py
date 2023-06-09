import json
import os

FILE = "articles.txt"

if not os.path.exists(FILE):
    with open(FILE, "a") as f:
        f.write(json.dumps([]))


def read_file():
    with open(FILE, "r") as f:
        return json.loads(f.read())


def write_file(data):
    with open(FILE, "w") as f:
        f.write(json.dumps(data))


def add_to_articles(data):
    articles = read_file()
    articles.append(data)
    write_file(articles)


def file_data_isset(action):
    def wrapper(*args, **kwargs):
        articles = read_file()
        if articles:
            return action(*args, **kwargs)
        else:
            print("Статей немає.")
    return wrapper


@file_data_isset
def read_articles():
    articles = read_file()
    for number, element in enumerate(articles, 1):
        print(f"{number} - {element['title']}")


@file_data_isset
def get_article_number():
    read_articles()
    while True:
        number = input("Оберіть номер статті: ")
        if number.isdigit() and 0 < int(number) <= len(read_file()):
            return int(number) - 1
        else:
            print("Будь ласка, оберіть статтю зі списку.")
            break


@file_data_isset
def check_number(articles):
    number = get_article_number()
    if number is not None:
        return number


def create_article():
    article = {"title": input("Введіть заголовок статті: "),
               "text": input("Введіть текст статті: ")}
    add_to_articles(article)
    print("Стаття створена.")


@file_data_isset
def del_article(articles):
    number = check_number(articles)
    if number is None:
        return
    del articles[number]
    write_file(articles)
    print("Статтю видалено.")


@file_data_isset
def edit_article(articles):
    number = check_number(articles)
    if number is None:
        return
    article = articles[number]
    article.update({'title': input("Введіть новий заголовок статті: "),
                    'text': input("Введіть новий текст статті: ")})
    write_file(articles)
    print("Статтю відредаговано.")


@file_data_isset
def print_article(articles):
    number = check_number(articles)
    if number is None:
        return
    article = articles[number]
    print(article)
