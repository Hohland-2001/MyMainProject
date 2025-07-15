def log(filename=None):
    """Декоратор для логирования функций и вывода результатов в консоль или файл"""

    def wrapper(function):
        def inner(*args, **kwargs):
            try:
                result = function(*args, **kwargs)
                if filename is None or filename == "":
                    print(f"{function.__name__} ok")
                else:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f"{function.__name__} ok\n")
            except Exception as e:
                result = None
                if filename is None or filename == "":
                    print(f"{function.__name__} error: {e}. Inputs: {[*args]} {[*kwargs]}")
                else:
                    with open(filename, "a", encoding="utf-8") as file:
                        file.write(f"{function.__name__} error: {e}. Inputs: {[*args]} {[*kwargs]}\n")
            return result

        return inner

    return wrapper


@log()
def my_function(x, y):
    """ "Тестовая функция"""
    return x + y


print(my_function("1", 2))
