from presenter import (add_to_articles,
                       read_articles,
                       get_article_number,
                       read_file,
                       write_file,
                       edit_article,
                       create_article,
                       check_number,
                       del_article,
                       print_article)
articles = read_file()
while True:
    choice = input(
        """МЕНЮ
1 - Створити статтю
2 - Вивести всі статті
3 - Читати статтю
4 - Видалити статтю
5 - Оновити статтю
6 - Вихід: """)
    if choice == "1":
        create_article()

    elif choice == "2":
        read_articles()

    elif choice == "3":
        print_article(articles)

    elif choice == "4":
        del_article(articles)

    elif choice == "5":
        edit_article(articles)
    elif choice == "6":
        break

    else:
        print("Оберіть дію з меню")
