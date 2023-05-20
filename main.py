call_count = 0


def f(x):
    global call_count
    call_count += 1
    return 3 * pow(x, 4) - 8 * pow(x, 3) + 6 * pow(x, 2)


def bitwise_search_method():
    iter_count = 0
    h = (b - a) / 4
    x_0 = a
    x_1 = x_0 + h
    f_0 = f(x_0)
    f_1 = f(x_1)
    while abs(h) > eps:
        iter_count += 1
        if f_0 > f_1:
            x_0 = x_1
            f_0 = f_1
            x_1 += h
            f_1 = f(x_1)
        else:
            x_1 = x_0
            f_1 = f_0
            x_0 -= h
            f_0 = f(x_0)
            h = -h / 4
    return x_0, iter_count


a = -1
b = 0.5
eps = 0.0001
min, iters = bitwise_search_method()
print("Число итераций: ", iters)
print("Количество вычислений функции: ", call_count)
print("Найденное решение (min): ", min)
print("Значение функции: ", f(min))


