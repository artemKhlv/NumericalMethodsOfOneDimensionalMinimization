call_count = 0


def f(x):
    global call_count
    call_count += 1
    return 3 * pow(x, 4) - 8 * pow(x, 3) + 6 * pow(x, 2)


def quadratic_interpolation():
    iter_count = 0
    a = A
    b = B
    eps = EPS
    delta_x = DELTA
    x_1 = (a + b) / 2
    x_2 = x_1 + delta_x

    while True:
        iter_count += 1
        if f(x_1) > f(x_2):
            x_3 = x_1 + 2 * delta_x
        else:
            x_3 = x_1 - delta_x

        X = {x_1, x_2, x_3}
        F_m = min([f(x) for x in X])
        x_m = min(X, key=f)

        x_average = (x_1 + x_2 + x_3 - x_m) / 2

        while not a <= x_average <= b:
            x_average = (x_m + x_average) / 2

        if abs(F_m - f(x_average)) <= eps and abs(x_m - x_average) <= eps:
            return x_average, iter_count

        if x_average < x_m:
            a = x_average
        else:
            b = x_average

        x_1, x_2 = sorted([x_m, x_average])


A = -1
B = 0.5
EPS = 0.0001
DELTA = 0.1
min, iters = quadratic_interpolation()
print("Число итераций: ", iters)
print("Количество вычислений функции: ", call_count)
print("Найденное решение (min): ", min)
print("Значение функции: ", f(min))
