import datetime
from HW_Function2_0 import phone_book_app


def decorator_time_log_place(name_file):
    def time_decorator(old_func):
        def new_func():
            start = datetime.datetime.now()
            old_func()
            finish = datetime.datetime.now()
            with open(name_file, "w") as file_handler:
                file_handler.write(f"Функция {old_func.__name__} начала работать в {start}, закончила в {finish}\n")
                file_handler.write(f'Время работы {finish - start}')
            return new_func

        return new_func

    return time_decorator


@decorator_time_log_place("log.txt")
def start_phone_book_app():
    phone_book_app()


start_phone_book_app()
