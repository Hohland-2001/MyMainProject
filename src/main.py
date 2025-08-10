from src.processing import filter_by_code, filter_by_state, process_bank_search, sort_by_date
from src.read_operations import read_operations_from_csv, read_operations_from_excel
from src.utils import read_operations_from_json
from src.widget import get_date, mask_account_card


def main() -> None:
    """Главная функция, выполняющая логику программы"""
    print(
        "Программа: Привет! Добро пожаловать в программу работы с банковскими транзакциями.\n"
        "Выберите необходимый пункт меню:\n"
        "1. Получить информацию о транзакциях из JSON-файла\n"
        "2. Получить информацию о транзакциях из CSV-файла\n"
        "3. Получить информацию о транзакциях из XLSX-файла\n"
    )

    user_response_menu = input("Пользователь: ")

    if user_response_menu == "1":
        print("\nПрограмма: Для обработки выбран JSON-файл.\n")
        data = read_operations_from_json()
    elif user_response_menu == "2":
        print("\nПрограмма: Для обработки выбран CSV-файла.\n")
        data = read_operations_from_csv()
    elif user_response_menu == "3":
        print("\nПрограмма: Для обработки выбран XLSX-файла.\n")
        data = read_operations_from_excel()
    else:
        print(
            "Выберите необходимый пункт меню:\n"
            "1. Получить информацию о транзакциях из JSON-файла\n"
            "2. Получить информацию о транзакциях из CSV-файла\n"
            "3. Получить информацию о транзакциях из XLSX-файла\n"
        )

    print(
        "Программа: Введите статус, по которому необходимо выполнить фильтрацию.\n"
        "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n"
    )

    user_response_state = input("Пользователь: ")
    user_response_state = user_response_state.upper()

    if user_response_state == "EXECUTED":
        print(f'\nПрограмма: Операции отфильтрованы по статусу "{user_response_state}"\n')
        list_state = filter_by_state(data, user_response_state)
    elif user_response_state == "CANCELED":
        print(f'\nПрограмма: Операции отфильтрованы по статусу "{user_response_state}"\n')
        list_state = filter_by_state(data, user_response_state)
    elif user_response_state == "PENDING":
        print(f'\nПрограмма: Операции отфильтрованы по статусу "{user_response_state}"\n')
        list_state = filter_by_state(data, user_response_state)
    else:
        print(
            f'\nПрограмма: Статус операции "{user_response_state}" недоступен.\n'
            "\nПрограмма: Введите статус, по которому необходимо выполнить фильтрацию.\n"
            "Доступные для фильтровки статусы: EXECUTED, CANCELED, PENDING\n"
        )

    print("Программа: Отсортировать операции по дате? Да/Нет\n")
    user_response_date = input("Пользователь: ")
    user_response_date = user_response_date.lower()

    if user_response_date == "да":
        print("\nПрограмма: Отсортировать по возрастанию или по убыванию? по возрастанию/по убыванию\n")
        user_response_date_reverse = input("Пользователь: ")
        if user_response_date_reverse.lower() == "по возрастанию":
            list_state_date = sort_by_date(list_state, False)
        elif user_response_date_reverse.lower() == "по убыванию":
            list_state_date = sort_by_date(list_state)
        else:
            print("Введено неверное значение")
    else:
        list_state_date = list_state

    print("\nПрограмма: Выводить только рублевые транзакции? Да/Нет\n")
    user_response_code = input("Пользователь: ")
    user_response_code = user_response_code.lower()
    if user_response_code == "да":
        list_state_date_code = filter_by_code(list_state_date)
    else:
        list_state_date_code = list_state_date

    print("\nПрограмма: Отфильтровать список транзакций по определенному слову в описании? Да/Нет\n")
    user_response_description = input("Пользователь: ")
    user_response_description = user_response_description.lower()

    if user_response_description == "да":
        user_response_search = input("\nПрограмма: Введите слова для поиска: ")
        list_state_date_code_description = process_bank_search(list_state_date_code, user_response_search)
    else:
        list_state_date_code_description = list_state_date_code

    print("\nПрограмма: Распечатываю итоговый список транзакций..")
    print(f"\nПрограмма: Всего банковских операций в выборке: {len(list_state_date_code_description)}\n")

    for element_of_list in list_state_date_code_description:
        if "from" in element_of_list.keys():
            print(
                f"{get_date(element_of_list['date'])} {element_of_list['description']}\n"
                f"{mask_account_card(element_of_list['from'])} -> {mask_account_card(element_of_list['to'])}\n"
                f"Сумма: {element_of_list['operationAmount']['amount']}"
                f"{element_of_list['operationAmount']['currency']['name']}\n"
            )
        else:
            print(
                f"{get_date(element_of_list['date'])} {element_of_list['description']}\n"
                f"{mask_account_card(element_of_list['to'])}\n"
                f"Сумма: {element_of_list['operationAmount']['amount']}"
                f"{element_of_list['operationAmount']['currency']['name']}\n"
            )
    return None
