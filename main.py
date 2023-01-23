from clss_for_scrapping import Monitoring, Fill_Table
from config import CHAT_ID, TOKEN


def get_choice() -> str:
    # Get the user's choice of program mode
    # Получить выбор пользователя о режиме программы
    while True:
        choice = input(
            'В каком режиме запустить программу?\n'
            '1 - Заполнение таблицы матчами\n'
            '2 - Мониторинг заполненных матчей\n'
            '3 - Выйти\n'
        )
        if choice in ['1', '2', '3']:
            break
        else:
            print('Такого варианта нет, попробуйте еще раз!')
    return choice


def main():
    choice = get_choice()

    if choice == '1':
        try:
            print('Процесс пошел')
            bskb = Fill_Table()
            bskb.fill_table()
        except Exception as ex:
            print(ex)
        else:
            Fill_Table.send_message('Работа программы завершена', CHAT_ID, TOKEN)

    elif choice == '2':
        try:
            print('Процесс пошел')
            bskb = Monitoring()
            bskb.monitoring()
        except Exception as ex:
            print(ex)
        else:
            Monitoring.send_message('Работа программы завершена', CHAT_ID, TOKEN)



if __name__ == '__main__':
    try:
        print('Доброго времени суток')
        main()
        print('Работа программы завершена')
        input('Нажмите Enter, чтобы выйти')
    except Exception as ex:
        print(ex)

