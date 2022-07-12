import time


def repeater(call_count, start_sleep_time, factor, border_sleep_time):
    def outer(fnc):
        def inner():
            if call_count == 0:
                return print(f'Запусков не будет')
            else:
                print(f'Кол-во запусков = {call_count}')
                print('Начало работы')
                for n in range(call_count):
                    t = start_sleep_time * factor ** n
                    if t >= border_sleep_time:
                        t = border_sleep_time
                    print(f'Запуск номер {n + 1}. Ожидание: {t} секунд.', end=' ')
                    time.sleep(t)
                    func_result = fnc()
                    print(f'Результат декорируемой функций = {func_result}.')
                print('Конец работы')

        return inner

    return outer


@repeater(call_count=4, start_sleep_time=1, factor=2, border_sleep_time=55)
def func():
    return 'Hello, admin'


if __name__ == '__main__':
    func()
